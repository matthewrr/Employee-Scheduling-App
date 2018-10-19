/*global $, Muuri*/
var boardContainers = [].slice.call(document.querySelectorAll('.board'));
var itemContainers = [].slice.call(document.querySelectorAll('.board-column-content'));
var columnGrids = [];

// Helper Functions
var innerBoards = {};
var outerBoards = {};
var innerBoard = function(el) {
  return innerBoards[$(el).parents('.board-name').attr('id')];
};

// Create Inner Boards
var createBoards = function (boards = itemContainers.slice(0)) {
  boards.forEach(function (container) {
    var grid = new Muuri(container, {
      items: '.board-item',
      layoutDuration: 400,
      layoutEasing: 'ease',
      dragEnabled: true,
      dragSort: function () {return columnGrids;},
      dragSortInterval: 20,
      dragStartPredicate: function (item, event) {
        return grid.getItems().indexOf(item) === 0 ? false : true;
      },
      // dragSortPredicate: function (item, e) {
      // return Muuri.ItemDrag.defaultSortPredicate(item, {
      //   threshold: 50,
      //   action: 'move',
      //   index: 1
      //   });
      // },
      dragContainer: document.body,
      dragReleaseDuration: 400,
      dragReleaseEasing: 'ease',
      layout: function (items, gridWidth, gridHeight) {
        var layout = {
          slots: [],
          width: 0,
          height: 0,
          setWidth: false,
          setHeight: true
        };
        var item, m, x, y, z, w, h;
        y = z = w = h = 0;
        m = 20;
        x = 40;
        for (var i = 0; i < items.length; i++) {
          item = items[i];
          w = item.getWidth() + 90;
          layout.slots.push(x, y);
        }
        layout.width = 280;
        layout.height = y + h;
        return layout;
      }
    })


    .on('dragStart', function (item, event) {
      var g = item.getGrid();
      var l = g.getItems().length;
      if (l <= 2) {
        g.show(0)
      } else {
        g.show(1)
      }
    })
    // .on('beforeSend', function (data) {
    //   var l = grid.getItems().length;
    //   if (l <= 2) {
    //     grid.show(0)
    //   } else {
    //     grid.show(1)
    //   }
    // })
    // .on('send', function (data) {
    //   var l = grid.getItems().length;
    //   if (l <= 2) {
    //     grid.show(0)
    //   } else {
    //     grid.show(1)
    //   }
    // })
    // .on('layoutStart', function (items) {
    //   console.log('before receive')
    //   // var g = data.toGrid;
    //   // grid.hide(-1);
    //   // g.hide(-1);
    //   // set ease style similar to Muuri items. jquery only allows 'slide' and 'linear'.
    //   // $(grid.getElement()).find('.input-container').hide(600);
    // })
    .on('beforeReceive', function (data) {
      grid.hide();
    })
    .on('beforeSend', function (data) {
      
      var gridLength = data.fromGrid.getItems().length;
      if (gridLength === 2) {
        grid.show(0);
      } else if (gridLength === 3) {
        grid.show(1);
      } else {
        console.log('Unexpected Grid Length')
      }
      
      
      var myItem = data.item;
      var fromGrid = data.fromGrid;
      // fromGrid.show();
      
      
      // var idx = grid.getItems().length - 2;
      // // console.log('item', i[-2])
      // console.log('item', grid.getItems([idx]))
      // var i = grid.getItems([idx])
      // i.show()
      // console.log('i is', i)
      // // grid.getItems([idx]).show();
      // grid.show([idx]);
      // grid.show()[]
    })
    
    // .on('receive', function (data) {
    //   $(data.fromGrid.getElement()).find('.name-input').val('');
    // })\
    .on('dragReleaseEnd', function (item, e) {
      console.log('drag release end')
      $(item.getElement()).siblings('.highlight-update').removeClass('highlight-default').addClass('highlight-employee');
      var l = grid.getItems().length;
      var pos = grid.getItems().indexOf(item);
      if (pos === 0) grid.move(0, 1, {action: 'swap'});
      if (pos === 2) grid.move(2, 1, {action: 'swap'})
      
      if (l > 2) item.getGrid().send(item.getGrid().getItems(2)[0], innerBoards['employeeGrid'], 0);
      grid.hide(0);
    })
    // .on('layoutEnd', function (items) {
    //   $(grid.getElement()).find('.name-input').val('');
      // $(data.fromGrid.getElement()).find('.name-input').val('');
      // $(grid.getElement()).find('.input-container').hide();
    // });
    columnGrids.push(grid);
    innerBoards[$(container).attr('id')] = grid;
  });
};
createBoards();
console.log('hi')

// Create Outer Boards
boardContainers.forEach(function (board) {
  var grid = new Muuri(board, {
    layoutDuration: 400,
    layoutEasing: 'ease',
    dragEnabled: true,
    dragSortInterval: 0,
    dragStartPredicate: {handle: '.board-column-header'},
    dragReleaseDuration: 400,
    dragReleaseEasing: 'ease',
  });
  outerBoards[$(board).attr('id')] = grid;
});

// Create Employee Board
var employeeContainers = [].slice.call(document.querySelectorAll('.employee-column-content'));
employeeContainers.forEach(function (container) {
  var employeeGrid = new Muuri('.employee-column-content', {
    items: '.board-item',
    layout: function (items, gridWidth, gridHeight) {
      var layout = {
        slots: [],
        width: 0,
        height: 0,
        setWidth: false,
        setHeight: true
      };
      var item, m, x, y, w, h;
      x = y = w = h = 0;
      for (var i = 0; i < items.length; i++) {
        x += w;
        y += h;
        item = items[i];
        m = item.getMargin();
        h = 33 + m.top + m.bottom;
        w = item.getWidth() + m.left + m.right;
        layout.slots.push(0, y);
      }
      layout.width = x + w;
      layout.height = y + h;
      return layout;
    },
    layoutDuration: 400,
    layoutEasing: 'ease',
    dragEnabled: true,
    dragSort: function () {return columnGrids;},
    dragSortInterval: 0,
    dragSortPredicate: function (item, e) {
      return Muuri.ItemDrag.defaultSortPredicate(item, {
        threshold: 50,
        action: 'move',
        index: 1
      });
    },
    dragContainer: document.body,
    dragReleaseDuration: 400,
    dragReleaseEasing: 'ease',
  })
  .on('dragReleaseEnd', function (item) {
    columnGrids.forEach(function (employeeGrid) {
      employeeGrid.refreshItems();
    });
  });
  columnGrids.push(employeeGrid);
  innerBoards['employeeGrid'] = employeeGrid;
});

// BOARD ACTIONS //
// Hide Boards on Load
for (var i in outerBoards) {
  if (i != "pills-main-stands") outerBoards[i].hide();
}

// Hide Background Board Items on Category Selection
$(".nav-pills .nav-link").click(function(){
    var boardName = $(this).attr('href').slice(1);
    for (var board in outerBoards) {if (board != boardName) outerBoards[board].hide()}
    outerBoards[boardName].show();
});

// TEXTBOX ACTIONS //
// Add Shift
$(".add-shift").click(function(){
  var $this = $(this);
  var board = $this.parents('.board').attr('id');
  var sequenceNum = Number($this.attr('value')) + 1;
  var shiftTemplate = $('.shift-template').clone().removeClass('d-none shift-template').addClass('board-column-content');

  $this.attr('value', sequenceNum);
  $this.parents('.board-column').append(shiftTemplate);
  shiftTemplate.find('.board-item-content').html('Extra #'+sequenceNum);
  shiftTemplate.children().first().attr('placeholder', '#'+sequenceNum);
  shiftTemplate.attr('value', sequenceNum);
  createBoards(shiftTemplate.toArray());
  outerBoards[board].refreshItems().layout();
});

// Textbox Behavior
$('.board-column').on('click', '.board-item', function(){
    // var target = $(this).parents('.board-column-content').find('.name-input');
    // target.blur();
    var textbox = $(this).parents('.board-column-content').find('.input-container');
    textbox.addClass('box-shadow');
    textbox.show();
    textbox.children().focus();
    
   
    $(this).hide();
});

// Blur employee name input on 'Enter'
// $(document).ready(function() {    
//   $(".name-input").bind('blur keyup',function(e) {  
//     if (e.type === 'blur' || e.keyCode === 13) e.currentTarget.blur();
//   });  
// });

// Move Item on Textbox Update
// $('.board-column').on('blur', '.name-input', function(){
//   var $this = $(this);    
//   if (!$this.val()) {
//     $this.removeClass('box-shadow');
//     $this.parent().next().children().show();
//   }
//   var matchFound = $('#json-datalist').find('option').filter(function () {
//     return this.value.toUpperCase() === $this.val().toUpperCase();
//   });
//   if (matchFound.length) {
//     var employeeItem = document.getElementById(matchFound.attr('class'));
//     var toGrid = innerBoard($this);
//     var fromGrid = innerBoard(employeeItem);
//     fromGrid.send(employeeItem, toGrid, 1);
//   }
// });