var itemContainers = [].slice.call(document.querySelectorAll('.board-column-content'));
var columnGrids = [];
var boardGrid;
var employeeGrid;

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
    // Prevent first item from being dragged. 
      if (grid.getItems().indexOf(item) === 0) {
        return false;
      }
      // For other items use the default drag start predicate.
      return Muuri.ItemDrag.defaultStartPredicate(item, event);
    },
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
        // x += w;
        x = 50;
        y += h;
        // m = item.getMargin();
        m = 0;
        // w = item.getWidth() + m.left + m.right;
        // w = 10;
        w = item.getWidth()
        h = item.getHeight() + m.top + m.bottom;
        layout.slots.push(x, y);
      }
  
      // Calculate the layout's total width and height. 
      // layout.width = x + w;
      layout.width = 400;
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
  .on('beforeSend', function (data) {
    // console.log(data.item);
    // console.log(data.toIndex);
    // var pos = data.toIndex;
    
  })
  .on('send', function (data) {
    console.log(data.toIndex);
    var pos = data.toIndex;
    if (pos === 0) {
      grid.move(0, 1, {action: 'swap'});
    }
    grid.show(0);
    
    
  })
  .on('beforeReceive', function (data) {
    
    var allItems = grid.getItems();
    allItems.forEach(function (item) {
      el = item.getElement()
      ch = $(el).children()
      grid.hide(ch);
      grid.hide()
    });
    
    
  })
  .on('receive', function (data) {
    var allItems = grid.getItems();
    console.log(data.toIndex);
    var pos = data.toIndex;
    if (pos === 0) {
      grid.move(0, 1, {action: 'swap'});
    }
    
    if (allItems.length === 3) {
      grid.send(1, employeeGrid, -1);
      // grid.remove(1, {removeElements: true});
    }
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

    // get list of invisible items
    var invisible = grid.getItems().filter(function (item) {
      return !item.isVisible();
    });
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
  dragReleaseDuration: 400,
  dragReleaseEasing: 'ease',
});







var employeeContainers = [].slice.call(document.querySelectorAll('.employee-column-content'));

employeeContainers.forEach(function (container) {
  employeeGrid = new Muuri(container, {
      
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
      item.getElement().style.width = item.getWidth() + 'px';
      item.getElement().style.height = item.getHeight() + 'px';
    })
    .on('dragReleaseEnd', function (item) {
      columnGrids.forEach(function (employeeGrid) {
        employeeGrid.refreshItems();
      });
    });
  columnGrids.push(employeeGrid);
});