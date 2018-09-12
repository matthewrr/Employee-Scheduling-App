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
          setWidth: true,
          // Should Muuri set the grid's height after layout?
          setHeight: true
        };
  
      // Calculate the slots.
      var item;
      var m;
      var x = 0;
      var y = 0;
      z = 0;
      var w = 0;
      var h = 0;
      for (var i = 0; i < items.length; i++) {
      // for (var i = 0; i < items.length; i++) {
        item = items[i];
        x = 50;
        y = 0
        // m = item.getMargin();
        m = 0;
        // w = item.getWidth() + m.left + m.right;
        // w = 10;
        w = item.getWidth() - 70;
        // h = item.getHeight() + m.top + m.bottom;
        if (x === 0) {
          z = 20;
          
        } else {
          z += 20;
        }
        x = 50
          
        layout.slots.push(x, y);
      }
  
      // Calculate the layout's total width and height. 
      // layout.width = w + x;
      layout.width = w * 4;
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
      // grid.hide()
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
  })
  .on('dragReleaseEnd', function (item, e) {
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
  layout: function (items, gridWidth, gridHeight) {
    // The layout data object. Muuri will read this data and position the items
    // based on it.
    
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
    var z = 0;
    var w = 0;
    var h = 0;
    var rowHeights = [];
    var columns = 4;
    var colObjs = 0;
    var colHeight = 0;
    var count = 0
    for (var i = 0; i < items.length; i++) {
      
      
      
      // y += h;
      // y = 0
      // w = item.getWidth() + m.left + m.right;
      // h = item.getHeight() + m.top + m.bottom;
      
      item = items[i];
      m = item.getMargin();
      w = item.getWidth();
      h = item.getHeight() + m.top + m.bottom;
      
      
      var column = count % 4;
      if (column === 0) {
        
        console.log('column is 0')
        
        var maxHeight = Math.max(...rowHeights.slice(-4));
        var currentHeight = rowHeights
        const arrSum = arr => arr.reduce((a,b) => a + b, 0)
        var heightArr = rowHeights.slice(colObjs*-1);
        for (var height in heightArr) {
          colHeight += Number(height);
          console.log(heightArr)
          console.log(colHeight);
          
          if (h < maxHeight) {
            colObjs += 1;
            y = maxHeight;
            x = x
            
          } else {
            colObjs = 1
            
            y = maxHeight
            x = (w/5)*i
            
          }
          console.log('colobjs is: ' + colObjs)
        }
      }
      rowHeights.push(h)
  
      // x = (w/5)*i
      layout.slots.push(x, y);
      colHeight = 0
      // x += ;
    }
    // Calculate the layout's total width and height. 
    // layout.width = x + w;
    // layout.width = (layout.slots[2] - layout.slots[1]) * 4;
    layout.width = 16 + '%'
    layout.height = y + h;

    return layout;
  }
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




var rowObjCounter = 0;

for (obj in objs) {
  var checkNewRow = rowObjCounter % 4 === 0;
  if (checkNewRow) {
    var objHeight = ;
    var currentRowHeight = ;
    var maxRowHeight = ;
    if (currentRowHeight + objHeight < maxRowHeight) {
      x += 0
      y = currentRowHeight;

    } else {
      x = 0
      y = maxRowHeight;
    }
  }
}

var desiredCols = 4;
var maxRowObj = ;
var numOfRowColumns = ;
var rowColHeights = []

var itemHeight = ;
var maxRowHeight = ;


if (numOfRowColumns === desiredCols) {
  if (itemHeight + rowColHeights[-1] > maxRowHeight) {
    // start new row
  } else {
    // append to 
  }
}


New Row?column
If current item + current row column height > max row height
X = 0
Y = max row height
 Row columns at 0
Row column height = item height
Same Row
If current item + current row column height <= max row height
X = most recent x
Y = most reent row column height
Row column height += current item height
Row columns unchanged

Else (you’ll start a new column)...
Row columns += 1
X = most recent x in list + item width
Y = most recent y
rowcolumnheight  = item height
