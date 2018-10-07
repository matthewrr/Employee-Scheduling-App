var itemContainers = [].slice.call(document.querySelectorAll('.board-column-content'));
var columnGrids = [];
var employeeIndex = [];
var boardGrid;
var employeeGrid;
var employeeCount;
var employees;
var grid2Hash = {};
// Define the column grids so we can drag those
// items around.
itemContainers.forEach(function (container) {
  // Instantiate column grid.
  var grid = new Muuri(container, {
    
    items: '.board-item',
    layoutDuration: 400,
    layoutEasing: 'ease',
    dragEnabled: true,
    dragSort: function () {
      return columnGrids;
    },
    dragStartPredicate: function (item, event) {
    // // Prevent first item from being dragged. 
    if (grid.getItems().indexOf(item) === 0) {
      return false;
    }
    return true;
      
    },
    //   // For other items use the default drag start predicate.
    //   return Muuri.ItemDrag.defaultStartPredicate(item, event);
    // },
    dragSortInterval: 0,
    dragContainer: document.body,
    dragReleaseDuration: 400,
    dragReleaseEasing: 'ease',
    layout: function (items, gridWidth, gridHeight) {
      var layout = {
          // The layout item slots (left/top coordinates).
          slots: [],
          // The layout's total width.
          width: 0,
          // The layout's total height.
          height: 0,
          // Should Muuri set the grid's width after layout?
          setWidth: false,
          // Should Muuri set the grid's height after layout?
          setHeight: true
        };
  
      // Calculate the slots.
      var item;
      var m;
      var x = 0;
      var y = 0;
      var z = 0;
      var w = 0;
      var h = 0;
      for (var i = 0; i < items.length; i++) {
      // for (var i = 0; i < items.length; i++) {
        item = items[i];
        y = 0
        m = 20;
        w = item.getWidth() + 90;
        x = 40
          
        layout.slots.push(x, y);
      }
  
      // Calculate the layout's total width and height. 
      // layout.width = w + x;
      layout.width = 280;
      layout.height = y + h;
      return layout;
    }
  })
  .on('dragStart', function (item) {
    item.getElement().style.width = item.getWidth() + 'px';
    item.getElement().style.height = item.getHeight() + 'px';
    grid.show(0);
  })
  .on('dragEnd', function (item, event) {
    if (item.getGrid() === grid) {
      
      if (grid.getItems().indexOf(item) === 0) {
        grid.move(0, 1, {action: 'swap'});
      }
      grid.hide(0);
    }
  })
  .on('beforeReceive', function (data) {
    var allItems = grid.getItems();
    allItems.forEach(function (item) {
      var el = item.getElement()
      var ch = $(el).children()
      grid.hide(ch);
    });
  })
  .on('receive', function (data) {
    var employeeGrid = columnGrids[103];
    var toGrid = data.toGrid;
  })
  .on('send', function (data) {
    var item = data.item;
    if (data.toIndex === 0) {
      var toGrid = data.toGrid 
      toGrid.move(0, 1, {action: 'swap'});
    }
    grid.show(0);
    
    
    // var fromGrid = data.fromGrid;
    // var fromIndex = data.fromIndex;
    // var item = fromGrid.getItems(0)[0];
    // console.log(fromGrid);
    // console.log(fromGrid.getElement());
    // console.log(item.getElement())
    
    
  })
  .on('dragReleaseEnd', function (item, e) {
    if (item.getGrid() === grid) {
      if (grid.getItems().indexOf(item) === 0) {
        grid.move(0, 1, {action: 'swap'});
      }
      grid.hide(0);
    }
    
    
    var elem = item.getElement();
    $(elem).siblings().removeClass('highlight-default').addClass('highlight-employee');
    
    
    
    
    var allItems = grid.getItems();
    var pos = grid.getItems().indexOf(item);
    var l = allItems.length
    var toRemove;
    var elementID
    if (l === 2 && pos == 0) {
      grid.move(0, 1, {action: 'swap'});
    } else if (l >= 3) {
      if (pos === 0) {
        grid.move(0, 1, {action: 'swap'});
        toRemove = 2;
      } else if (pos === 1) {
        toRemove = 2;
      } else if (pos === 2) {
        grid.move(0, 2, {action: 'swap'});
        toRemove = 1;
      }
      grid.remove(toRemove, {removeElements: true});
    }
  })
  .on('layoutEnd', function (items) {
    // console.log(items);
  });

  columnGrids.push(grid);
  grid.on('click', function (items) {
      console.log('clicked the grid!')
  });
  
});

// Instantiate the board grid so we can drag those
// columns around.
var boardContainers = [].slice.call(document.querySelectorAll('.board'));
var myBoards = {};

boardContainers.forEach(function (board) {
    var name = $(board).attr('id');
    console.log(name);
    boardGrid = new Muuri(board, {
      layoutDuration: 400,
      layoutEasing: 'ease',
      dragEnabled: true,
      dragSortInterval: 0,
      dragStartPredicate: {
        handle: '.board-column-header'
      },
      dragReleaseDuration: 400,
      dragReleaseEasing: 'ease',
    });
    myBoards[name] = boardGrid;
    // myBoards.push(name);
});



var employeeContainers = [].slice.call(document.querySelectorAll('.employee-column-content'));
employeeContainers.forEach(function (container) {
  employees = $('.employee-column-content').children();
  $.each( employees, function( key, value ) {
    employeeIndex.push(key);
  });
  var employeeGrid = new Muuri('.employee-column-content', {
    items: '.board-item',
    layoutDuration: 400,
    layoutEasing: 'ease',
    dragEnabled: true,
    dragSort: function () {
      return columnGrids;
    },
    layout: function (items, gridWidth, gridHeight) {
    // The layout data object. Muuri will read this data and position the items
    // based on it.
    var layout = {
      // The layout's item slots (left/top coordinates).
      slots: [],
      // The layout's total width.
      width: 0,
      // The layout's total height.
      height: 0,
      // Should Muuri set the grid's width after layout?
      setWidth: true,
      // Should Muuri set the grid's height after layout?
      setHeight: true
    };

    // Calculate the slots.
    var item;
    var m;
    var x = 0;
    var y = 0;
    var w = 0;
    var h = 0;
    for (var i = 0; i < items.length; i++) {
      item = items[i];
      x += w;
      y += h;
      m = item.getMargin();
      w = item.getWidth() + m.left + m.right;
      h = 33 + m.top + m.bottom;
      layout.slots.push(0, y);
    }

    // Calculate the layout's total width and height. 
    layout.width = x + w;
    layout.height = y + h;

    return layout;
    },
    dragSortInterval: 0,
    dragContainer: document.body,
    dragReleaseDuration: 400,
    dragReleaseEasing: 'ease',
  })
  .on('dragStart', function (item) {
    item.getElement().style.width = 140 + 'px';
  })
  .on('dragReleaseEnd', function (item) {
    columnGrids.forEach(function (employeeGrid) {
      employeeGrid.refreshItems();
    })
  });
  employeeGrid.refreshItems();
  columnGrids.push(employeeGrid)

});


// $(".add-shift").click(function(){
//   console.log('clicked')
//   var newShift = $('.shift-template').clone().removeClass('shift-template', 'd-none');
//   console.log(newShift)
//   $(this).parent().parent().parent().append(newShift.html());
// });

// console.log(columnGrids)
// console.log(myBoards);

$(".add-shift").click(function(){
    var boardName = $(this).parents('.board').attr('id');
    var board = myBoards[boardName];
    var newShift = $('.shift-template').clone().removeClass('shift-template', 'd-none').html();
    // console.log(newShift);
    // console.log(boardName);
});