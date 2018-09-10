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
console.log(itemContainers);
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
      var w = 0;
      var h = 0;
      for (var i = 0; i < items.length; i++) {
      // for (var i = 0; i < items.length; i++) {
        item = items[i];
        // x += w;
        x = 50;
        y = 0
        // m = item.getMargin();
        m = 0;
        // w = item.getWidth() + m.left + m.right;
        // w = 10;
        w = item.getWidth();
        h = item.getHeight() + m.top + m.bottom;
        
        layout.slots.push(x, y);
      }
  
      // Calculate the layout's total width and height. 
      layout.width = w + 0;
      // layout.width = 
      layout.height = y + h;
  
      return layout;
    }
  })
  .on('dragStart', function (item) {
    // Let's set fixed widht/height to the dragged item
    // so that it does not stretch unwillingly when
    // it's appended to the document body for the
    // duration of the drag.
    item.getElement().style.width = item.getWidth() + 'px';
    item.getElement().style.height = item.getHeight() + 'px';
    grid.show(0);
  })
  // hide placeholder if name returned to originator
  .on('dragEnd', function (item, event) {
    if (item.getGrid() === grid) {
      
      if (grid.getItems().indexOf(item) === 0) {
        grid.move(0, 1, {action: 'swap'});
      }
      grid.hide(0);
    }
  })
  // hide all items before receiving a new one
  .on('beforeReceive', function (data) {
    var allItems = grid.getItems();
    allItems.forEach(function (item) {
      var el = item.getElement()
      var ch = $(el).children()
      grid.hide(ch);
      // grid.hide()
    });
  })
  .on('receive', function (data) {
    var employeeGrid = columnGrids[103];
    var toGrid = data.toGrid;
    // if (data.fromGrid === employeeGrid && toGrid != employeeGrid) {
    //   grid2Hash[data.item._id] = function (item) {
    //     if (item === data.item) {
    //       var clone = cloneElem(data.item);
    //       data.fromGrid.add(clone, {index: data.fromIndex});
    //       data.fromGrid.hide(clone);
    //     }
    //   };
    // grid.once('dragReleaseStart', grid2Hash[data.item._id]);
    // 
    // }
    })
    
    // console.log('same grid?')
    // console.log(data.fromGrid !== data.toGrid)
    // if (data.fromGrid !== data.toGrid) {
    //   var toGrid = data.toGrid
    //   var fromGrid = data.fromGrid
    //   var idx = data.fromIndex;
    //   var el = data.item.getElement();
    //   console.log('compare');
    //   // fromGrid.add(el, {index: 0})
      
      
      // var clone = cloneElem(data.item.getElement());
      // console.log('the index is: ' + data.fromIndex)
      // data.fromGrid.add(clone, {index: Number(data.fromIndex)});
  // })
  .on('send', function (data) {
    var item = data.item;
    if (data.toIndex === 0) {
      var toGrid = data.toGrid 
      toGrid.move(0, 1, {action: 'swap'});
    }
    grid.show(0);
    
    // grid.on('dragReleaseEnd', function (item) {
    //   console.log('drag release end')
    //   var employeeGrid = columnGrids[103];
    //   console.log(data.fromGrid === employeeGrid)
    //   if (data.fromGrid === employeeGrid) {
    //     var idx = data.fromIndex;
    //     var el = item.getElement();
    //     console.log('el to add:')
    //     console.log(el)
    //     data.fromGrid.add(el, {index: 0})
    //   }
    // });
    // console.log(data.fromGrid)
    // console.log(data.toGrid)
    
    
  })
  // .on('receive', function (data) {
    // var allItems = grid.getItems();
    // var pos = data.toIndex;
    // if (allItems.length === 2) {
    //   if (pos === 0) {
    //     grid.move(0, 1, {action: 'swap'});
    //   }
    // } else if (allItems.length === 3) {
    //   if (pos === 0) {
    //     grid.move(0, 1, {action: 'swap'});
    //     grid.hide(2);
    //   } else if (pos === 2) {
    //     grid.move(0, 2, {action: 'swap'});
    //     grid.hide(1);
    //   }      
      
    // }
    // grid.hide(0);
  // })
  .on('dragReleaseEnd', function (item, e) {

    // item.getElement().style.width = '';
    // item.getElement().style.height = '';
    // if return to same grid
    
    if (item.getGrid() === grid) {
      if (grid.getItems().indexOf(item) === 0) {
        grid.move(0, 1, {action: 'swap'});
      }
      grid.hide(0);
    }
    var toGrid = item.getGrid();
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
  });
  
  columnGrids.push(grid);
});

// Instantiate the board grid so we can drag those
// columns around.
boardGrid = new Muuri('.board', {
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
    dragSortInterval: 0,
    dragContainer: document.body,
    dragReleaseDuration: 400,
    dragReleaseEasing: 'ease',
  })
  .on('dragStart', function (item) {
    // item.getElement().style.width = item.getWidth() + 'px';
    // item.getElement().style.height = item.getHeight() + 'px';
    item.getElement().style.width = 163 + 'px';
  })
  .on('dragReleaseEnd', function (item) {
    columnGrids.forEach(function (employeeGrid) {
      employeeGrid.refreshItems();
    })
  });
  columnGrids.push(employeeGrid)

});