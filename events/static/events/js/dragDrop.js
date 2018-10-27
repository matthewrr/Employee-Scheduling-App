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
      dragSortInterval: 0,
      dragStartPredicate: function (item, event) {
        return grid.getItems().indexOf(item) === 0 ? false : true;
      },
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
    .on('beforeReceive', function (data) {
      grid.hide();
    })
    .on('receive', function (data) {
      $(grid.getElement).find('.name-input').val('');
    })
    .on('send', function (data) {
      var gridLength = data.fromGrid.getItems().length;
      var idx = data.fromIndex;
      data.fromGrid.show();
      if (gridLength > 2) {
        data.fromGrid.hide(0);
      }
      
      
      var fromGrid = data.fromGrid;
      var el = fromGrid.getElement();
      $(el).find('.employee').addClass('default').removeClass('employee');
      
      
    })
    .on('dragReleaseEnd', function (item, e) {
      var toSend;
      $(item.getElement()).siblings().removeClass('default').addClass('employee');
      $(item.getElement()).children().removeClass('default').addClass('employee');
      var l = grid.getItems().length;
      var pos = grid.getItems().indexOf(item);
      if (pos === 0) grid.move(0, 1, {action: 'swap'});
      if (pos === 2) grid.move(2, 1, {action: 'swap'})
      if (l > 2) {
        var toSend = item.getGrid().getItems(2)[0]
        grid.show(toSend);
        // item.getGrid().getItems(2)[0].show();
        item.getGrid().send(toSend, innerBoards['employeeGrid'], 0);
      }
      // var fromGrid = item.getGrid();
      // console.log(item.fromGrid())
      // console.log(fromGrid.getItems().length)
      if (item.getGrid().length === 1) {
        var el = item.getGrid().getElement();
        $(el).find('.employee').addClass('default').removeClass('employee');
      }
      grid.hide(0);
    })
    columnGrids.push(grid);
    innerBoards[$(container).attr('id')] = grid;
  });
};
createBoards();

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
  if (i != "main-stands") outerBoards[i].hide();
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
$(document).ready(function() {    
  $(".name-input").bind('blur keyup',function(e) {  
    if (e.type === 'blur' || e.keyCode === 13) e.currentTarget.blur();
  });  
});

// Move Item on Textbox Update
$('.board-column').on('blur', '.name-input', function(){
  var $this = $(this);    
  if (!$this.val()) {
    $this.removeClass('box-shadow');
    $this.parent().next().children().show();
  }
  var matchFound = $('#json-datalist').find('option').filter(function () {
    return this.value.toUpperCase() === $this.val().toUpperCase();
  });
  if (matchFound.length) {
    var employeeItem = document.getElementById(matchFound.attr('class'));
    var toGrid = innerBoard($this);
    var fromGrid = innerBoard(employeeItem);
    
    fromGrid.send(employeeItem, toGrid, 1);
    // $(toGrid.getElement()).find('.name-input').val('')
  }
});