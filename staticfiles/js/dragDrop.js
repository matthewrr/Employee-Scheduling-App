var itemContainers = [].slice.call(document.querySelectorAll('.board-column-content'));
var columnGrids = [];
var boardGrid;

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
    // dragStartPredicate: function (item, e) {
    // // If this is final event in the drag process, let's prepare the predicate
    // // for the next round (do some resetting/teardown). The default predicate
    // // always needs to be called during the final event if there's a chance it
    // // has been triggered during the drag process because it does some necessary
    // // state resetting.

    // // Prevent first item from being dragged. 
    // /////////////////////////
    //   // if (grid.getItems().indexOf(item) === 0) {
    //   //   return false;
    //   // }
    //   return Muuri.ItemDrag.defaultStartPredicate(item, e);
      
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
        item = items[i];
        // x += w;
        x = 50;
        y += h;
        m = item.getMargin();
        // m = 0;
        // w = item.getWidth() + m.left + m.right;
        w = 10;
        h = item.getHeight() + m.top + m.bottom;
        layout.slots.push(x, y);
      }
  
      // Calculate the layout's total width and height. 
      // layout.width = x + w;
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
  })
  .on('send', function (data) {
    grid.show(0);
    
    
  })
  .on('beforeReceive', function (data) {
    // grid.send(0, '.employees', -1);
    // grid.hide(0);
    // grid.getItems().hide();
    // grid.getItems().filter(function (item) {
    //   item.hide();
    // });
    var allItems = grid.getItems();
    allItems.forEach(function (item) {
      grid.hide(item);
    });
    
    
  })
  .on('receive', function (data) {
    var allItems = grid.getItems();
    
    if (allItems.length === 3) {
      grid.remove(1, {removeElements: true});
    }
    
    
    // allItems.forEach(function (item) {
    //   console.log(allItems.length)
    //   var i = grid.getItems().indexOf(item);
    //   if (i === 1 && allItems.length === 3) {
    //     grid.remove(1, {removeElements: true});
    //     grid.show(2);
    //   }
    //   if (el === 5) {
    //     break;
    //   }
    //   // if (allItems.length === 3) {
    //   //   grid.show(1);
    //   // }
      
    // });
    

  })
  .on('dragReleaseEnd', function (item, e) {
    // Let's remove the fixed width/height from the
    // dragged item now that it is back in a grid
    // column and can freely adjust to it's
    // surroundings.
    // item.getElement().style.width = '';
    // item.getElement().style.height = '';
    // Just in case, let's refresh the dimensions of all items
    // in case dragging the item caused some other items to
    // be different size.
    // console.log('hello!')
    // var count = 0
    // var allItems = grid.getItems();
    // count = allItems.length;
    // console.log('count is:')
    
    // console.log(count)
    
    // get list of invisible items
    var invisible = grid.getItems().filter(function (item) {
      return !item.isVisible();
    });
    
    // make sure it's not the placeholder at index 0
    // var notPlaceholder = invisible.filter(function (item) {
    //   return !item.getPosition(1);
    // });
    // grid.add([item, item]);
    // grid.add(item);
    // var i = grid.getItems().
    // grid.add([item]);
    // grid.on('dragEnd', function (item, event) {
    //   console.log(event);
    //   console.log(item);
    // })
    // console.log(invisible);
    // if (notPlaceholder) {
    //   grid.remove(notPlaceholder, {removeElements: true});
    // }
    // console.log('hidden is')
    // console.log(hidden)
    
    // if (grid.length > 1) {
    //   grid.remove(0, {removeElements: true});
    // }
    
    columnGrids.forEach(function (grid) {
      grid.refreshItems();
    });
  })

  // Add the column grid reference to the column grids
  // array, so we can access it later on.
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
  // dragStartPredicate: {
  //   handle: '.roww'
  // },
  dragReleaseDuration: 400,
  dragReleaseEasing: 'ease',
  // layout: function (items, gridWidth, gridHeight) {
  //     var layout = {
  //         // The layout item slots (left/top coordinates).
  //         slots: [],
  //         // The layout's total width.
  //         width: 0,
  //         // The layout's total height.
  //         height: 0,
  //         // Should Muuri set the grid's width after layout?
  //         setWidth: false,
  //         // Should Muuri set the grid's height after layout?
  //         setHeight: true
  //       };
  
  //     // Calculate the slots.
  //     var item;
  //     var m;
  //     var x = 0;
  //     var y = 0;
  //     var w = 0;
  //     var h = 0;
  //     for (var i = 0; i < items.length; i++) {
  //       item = items[i];
  //       // x += w;
  //       x = 300;
  //       y += h;
  //       m = item.getMargin();
  //       // m = 0;
  //       w = item.getWidth() + m.left + m.right;
  //       // w = 10;
  //       h = item.getHeight() + m.top + m.bottom;
  //       layout.slots.push(x, y);
  //     }
  
  //     // Calculate the layout's total width and height. 
  //     // layout.width = x + w;
  //     layout.height = y + h;
  
  //     return layout;
  //   }
  
});







var employeeContainers = [].slice.call(document.querySelectorAll('.employee-column-content'));
var employeeGrid = [];



employeeContainers.forEach(function (container) {
  var grid = new Muuri(container, {
      
      items: '.employee-item',
      layoutDuration: 400,
      layoutEasing: 'ease',
      dragEnabled: true,
      dragSort: function () {
        return employeeGrid;
      },
      dragSortInterval: 0,
      dragContainer: document.body,
      dragReleaseDuration: 400,
      dragReleaseEasing: 'ease',
    })
    .on('dragStart', function (item) {
      item.getElement().style.width = item.getWidth() + 'px';
      item.getElement().style.height = item.getHeight() + 'px';
    })
    .on('dragReleaseEnd', function (item) {
      employeeGrid.forEach(function (grid) {
        grid.refreshItems();
      });
    });
  employeeGrid.push(grid);
});