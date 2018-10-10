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

// var boards = itemContainers;

var newestBoard = [];
var childBoards = {};
var createBoards = function (boards = itemContainers.slice(0)) {
    boards.forEach(function (container) {
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
//   .on('dragEnd', function (item, event) {
// //     if (item.getGrid() === grid) {
      
// //       if (grid.getItems().indexOf(item) === 0) {
// //         grid.move(0, 1, {action: 'swap'});
// //       }
// //       grid.hide(0);
// //     }
//   })
  .on('beforeReceive', function (data) {
    var allItems = grid.getItems();
    allItems.forEach(function (item) {
      var el = item.getElement()
      var ch = $(el).children()
      grid.hide(ch);
    });
  })
  .on('send', function (data) {
    var item = data.item;
    if (data.toIndex === 0) {
      var toGrid = data.toGrid 
      toGrid.move(0, 1, {action: 'swap'});
    }
    grid.show(0);
  })
  .on('dragReleaseEnd', function (item, e) {
    if (item.getGrid() === grid) {
      if (grid.getItems().indexOf(item) === 0) {
        grid.move(0, 1, {action: 'swap'});
      }
      grid.hide(0);
    }
    
    
    var elem = item.getElement();
    console.log(elem);
    $(elem).siblings('.highlight-update').removeClass('highlight-default').addClass('highlight-employee');
    
    
    var allItems = grid.getItems();
    var pos = grid.getItems().indexOf(item);
    var l = allItems.length
    var toRemove;
    var elementID
    
    console.log(l, pos)
    if (l === 2 && pos == 0) {
      grid.move(0, 1, {action: 'swap'});
      var firstItem = grid.getItems(0);
      console.log('first item is:')
      console.log(firstItem)
      grid.hide([0])
    //   var firstItem = grid.getItems(0)[0];
    //   grid.hide(firstItem);
    
    
    // } else if (l === 2 && pos == 1) {
      
    //   console.log('correct');
    //   var firstItem = grid.getItems(0);
    //   console.log('first item is:')
    //   console.log(firstItem)
    //   grid.hide([0]);
    // //   var firstItem = grid.getItems(0)[0];
    // //   grid.hide(0);
    // //   grid.hide(1);
        
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
  
  columnGrids.push(grid);
//   childBoards.push(grid);
  
});
};
// var createBoards = function (boards = itemContainers.slice(0)) {
// itemContainers.forEach(function (container) {
//   // Instantiate column grid.
//   var grid = new Muuri(container, {
    
//     items: '.board-item',
//     layoutDuration: 400,
//     layoutEasing: 'ease',
//     dragEnabled: true,
//     dragSort: function () {
//       return columnGrids;
//     },
//     dragStartPredicate: function (item, event) {
//     // // Prevent first item from being dragged. 
//     if (grid.getItems().indexOf(item) === 0) {
//       return false;
//     }
//     return true;
      
//     },
//     //   // For other items use the default drag start predicate.
//     //   return Muuri.ItemDrag.defaultStartPredicate(item, event);
//     // },
//     dragSortInterval: 0,
//     dragContainer: document.body,
//     dragReleaseDuration: 400,
//     dragReleaseEasing: 'ease',
//     layout: function (items, gridWidth, gridHeight) {
//       var layout = {
//           // The layout item slots (left/top coordinates).
//           slots: [],
//           // The layout's total width.
//           width: 0,
//           // The layout's total height.
//           height: 0,
//           // Should Muuri set the grid's width after layout?
//           setWidth: false,
//           // Should Muuri set the grid's height after layout?
//           setHeight: true
//         };
  
//       // Calculate the slots.
//       var item;
//       var m;
//       var x = 0;
//       var y = 0;
//       var z = 0;
//       var w = 0;
//       var h = 0;
//       for (var i = 0; i < items.length; i++) {
//       // for (var i = 0; i < items.length; i++) {
//         item = items[i];
//         y = 0
//         // m = item.getMargin();
//         m = 20;
//         // w = item.getWidth() + m.left + m.right;
//         // w = 10;
//         // w = item.getWidth() - 90;
//         w = item.getWidth() + 90;
//         // h = item.getHeight() + m.top + m.bottom;
//         // if (x === 0) {
//         //   z = 20;
          
//         // } else {
//         //   z += 20;
//         // }
//         x = 40
          
//         layout.slots.push(x, y);
//       }
  
//       // Calculate the layout's total width and height. 
//       // layout.width = w + x;
//       layout.width = 280;
//       layout.height = y + h;
  
//       return layout;
//     }
//   })
//   .on('dragStart', function (item) {
//     item.getElement().style.width = item.getWidth() + 'px';
//     item.getElement().style.height = item.getHeight() + 'px';
//     grid.show(0);
//   })
//   .on('dragEnd', function (item, event) {
//     if (item.getGrid() === grid) {
      
//       if (grid.getItems().indexOf(item) === 0) {
//         grid.move(0, 1, {action: 'swap'});
//       }
//       grid.hide(0);
//     }
//   })
//   .on('beforeReceive', function (data) {
//     var allItems = grid.getItems();
//     allItems.forEach(function (item) {
//       var el = item.getElement()
//       var ch = $(el).children()
//       grid.hide(ch);
//       // grid.hide()
//     });
//   })
//   .on('receive', function (data) {
//     var employeeGrid = columnGrids[103];
//     var toGrid = data.toGrid;
//   })
//   .on('send', function (data) {
//     var item = data.item;
//     if (data.toIndex === 0) {
//       var toGrid = data.toGrid 
//       toGrid.move(0, 1, {action: 'swap'});
//     }
//     grid.show(0);
//   })
//   .on('dragReleaseEnd', function (item, e) {
//     if (item.getGrid() === grid) {
//       if (grid.getItems().indexOf(item) === 0) {
//         grid.move(0, 1, {action: 'swap'});
//       }
//       grid.hide(0);
//     }
//     var toGrid = item.getGrid();
//     var allItems = grid.getItems();
//     var pos = grid.getItems().indexOf(item);
//     var l = allItems.length
//     var toRemove;
//     var elementID
//     if (l === 2 && pos == 0) {
//       grid.move(0, 1, {action: 'swap'});
//     } else if (l >= 3) {
//       if (pos === 0) {
//         grid.move(0, 1, {action: 'swap'});
//         toRemove = 2;
//       } else if (pos === 1) {
//         toRemove = 2;
//       } else if (pos === 2) {
//         grid.move(0, 2, {action: 'swap'});
//         toRemove = 1;
//       }
//       grid.remove(toRemove, {removeElements: true});
//     }
//   });
//   columnGrids.push(grid);
// });
// };


createBoards();
// Instantiate the board grid so we can drag those
// columns around.
var boardContainers = [].slice.call(document.querySelectorAll('.board'));
var parentBoards = {};



boardContainers.forEach(function (board) {
    var name = $(board).attr('id');
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
    parentBoards[name] = boardGrid;
    // if (name != "pills-main-stands") {
    //     boardGrid.hide();
    // }
    // myBoards.push(name);
});

var employeeContainer = [];

var employeeContainers = [].slice.call(document.querySelectorAll('.employee-column-content'));

// var createEmployee = function (boards = employeeContainers.slice(0)) {
// employeeContainers.forEach(function (container) {
//   employees = $('.employee-column-content').children();
//   $.each( employees, function( key, value ) {
//     employeeIndex.push(key);
//   });
//   var employeeGrid = new Muuri('.employee-column-content', {
//     items: '.board-item',
//     layoutDuration: 400,
//     layoutEasing: 'ease',
//     dragEnabled: true,
//     dragSort: function () {
//       return columnGrids;
//     },
//     layout: function (items, gridWidth, gridHeight) {
//     // The layout data object. Muuri will read this data and position the items
//     // based on it.
//     var layout = {
//       // The layout's item slots (left/top coordinates).
//       slots: [],
//       // The layout's total width.
//       width: 0,
//       // The layout's total height.
//       height: 0,
//       // Should Muuri set the grid's width after layout?
//       setWidth: true,
//       // Should Muuri set the grid's height after layout?
//       setHeight: true
//     };

//     // Calculate the slots.
//     var item;
//     var m;
//     var x = 0;
//     var y = 0;
//     var w = 0;
//     var h = 0;
//     for (var i = 0; i < items.length; i++) {
//       item = items[i];
//       x += w;
//       y += h;
//       m = item.getMargin();
//       w = item.getWidth() + m.left + m.right;
//       h = 33 + m.top + m.bottom;
//       layout.slots.push(0, y);
//     }

//     // Calculate the layout's total width and height. 
//     layout.width = x + w;
//     layout.height = y + h;

//     return layout;
//     },
//     dragSortInterval: 0,
//     dragContainer: document.body,
//     dragReleaseDuration: 400,
//     dragReleaseEasing: 'ease',
//   })
//   .on('dragStart', function (item) {
//     item.getElement().style.width = 140 + 'px';
//   })
//   .on('dragReleaseEnd', function (item) {
//     columnGrids.forEach(function (employeeGrid) {
//       employeeGrid.refreshItems();
//     })
//   });
//   columnGrids.push(employeeGrid)
//   employeeContainer.push(employeeGrid)

// });

var employeeContainers = [].slice.call(document.querySelectorAll('.employee-column-content'));
employeeContainers.forEach(function (container) {
  employees = $('.employee-column-content').children();
  $.each( employees, function( key, value ) {
    employeeIndex.push(key);
  });
  var employeeGrid = new Muuri('.employee-column-content', {
    items: '.board-item',
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
      setWidth: false,
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
    layoutDuration: 400,
    layoutEasing: 'ease',
    dragEnabled: true,
    dragSort: function () {
      return columnGrids;
    },
    dragSortInterval: 0,
    dragContainer: document.body,
    dragReleaseDuration: 400,
    dragReleaseEasing: 'ease',
  })
  .on('dragStart', function (item) {
    // item.getElement().style.width = item.getWidth() + 'px';
    // item.getElement().style.height = item.getHeight() + 'px';
    item.getElement().style.width = 140 + 'px';
  })
  .on('dragReleaseEnd', function (item) {
    columnGrids.forEach(function (employeeGrid) {
      employeeGrid.refreshItems();
    })
  });
  columnGrids.push(employeeGrid)
  employeeGrid.refreshItems().layout();

});


$(".add-shift").click(function(){
    
    var board = $(this).parents('.board').attr('id');
    var shiftTemplate = $('.shift-template').clone().removeClass('d-none shift-template').addClass('board-column-content');
    var sequenceNum = Number($(this).attr('value')) + 1;
    
    $(this).attr('value', sequenceNum);
    
    $(this).parents('.board-column').append(shiftTemplate);

    shiftTemplate.find('.board-item-content').html('Extra #'+sequenceNum);
    shiftTemplate.children().first().attr('placeholder', '#'+sequenceNum);
    shiftTemplate.attr('value', sequenceNum);
    
    createBoards(shiftTemplate.toArray());
    parentBoards[board].refreshItems().layout();
    // employeeContainer[0].refreshItems().layout();
    console.log(employeeContainer[0])
    console.log(columnGrids.length)
});

$(".nav-pills .nav-link").click(function(){
    var boardName = $(this).attr('href').slice(1);
    var activeBoard = parentBoards[boardName];
    for (var board in parentBoards) {
        parentBoards[board].hide()
    }
    
    activeBoard.show();
})

for (var i in parentBoards) {
    if (i != "pills-main-stands") {
        parentBoards[i].hide();
    }
    
}
