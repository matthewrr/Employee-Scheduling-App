{"filter":false,"title":"dragDrop.js","tooltip":"/staticfiles/js/dragDrop.js","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":275,"column":94},"end":{"row":276,"column":0},"action":"remove","lines":["",""],"id":5071}],[{"start":{"row":275,"column":94},"end":{"row":276,"column":0},"action":"remove","lines":["",""],"id":5072}],[{"start":{"row":248,"column":0},"end":{"row":253,"column":37},"action":"remove","lines":["      ","      // var employeeList = $('.employee-column-content');","      // var el = employeeList.children('#'+toRemove)","      // el.removeClass('muuri-item-hidden')","      // el.addClass('muuri-item-shown')","      // $(el).css('display','block')"],"id":5073},{"start":{"row":247,"column":28},"end":{"row":248,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":246,"column":0},"end":{"row":247,"column":0},"action":"remove","lines":["      // elementID = grid.getItems()[toRemove].getElement().id;",""],"id":5074}],[{"start":{"row":245,"column":0},"end":{"row":246,"column":0},"action":"remove","lines":["      ",""],"id":5075}],[{"start":{"row":184,"column":0},"end":{"row":187,"column":20},"action":"remove","lines":["    // Let's remove the fixed width/height from the","    // dragged item now that it is back in a grid","    // column and can freely adjust to it's","    // surroundings."],"id":5076}],[{"start":{"row":187,"column":0},"end":{"row":194,"column":10},"action":"remove","lines":["    // Just in case, let's refresh the dimensions of all items","    // in case dragging the item caused some other items to","    // be different size.","","    // get list of invisible items","    // var invisible = grid.getItems().filter(function (item) {","    //   return !item.isVisible();","    // });"],"id":5077},{"start":{"row":186,"column":43},"end":{"row":187,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":188,"column":2},"end":{"row":188,"column":4},"action":"remove","lines":["  "],"id":5078},{"start":{"row":188,"column":0},"end":{"row":188,"column":2},"action":"remove","lines":["  "]},{"start":{"row":187,"column":0},"end":{"row":188,"column":0},"action":"remove","lines":["",""]},{"start":{"row":186,"column":43},"end":{"row":187,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":195,"column":0},"end":{"row":204,"column":4},"action":"remove","lines":["    ","    ","    // !!!!!!!","    // console.log(grid !== item.getGrid())","    // if (grid !== item.getGrid()) {","    //   var idx = item.getElement().id;","    //   var el = item.getElement();","    //   grid.add(el, {index: 0})","    // }","    "],"id":5079},{"start":{"row":194,"column":4},"end":{"row":195,"column":0},"action":"remove","lines":["",""]},{"start":{"row":194,"column":2},"end":{"row":194,"column":4},"action":"remove","lines":["  "]},{"start":{"row":194,"column":0},"end":{"row":194,"column":2},"action":"remove","lines":["  "]},{"start":{"row":193,"column":5},"end":{"row":194,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":195,"column":0},"end":{"row":196,"column":0},"action":"remove","lines":["    // if in new grid (use else statement after functioning)",""],"id":5080}],[{"start":{"row":198,"column":0},"end":{"row":200,"column":0},"action":"remove","lines":["    // var employeeGrid = columnGrids[-1];","    // !!!FIGURE OUT HOW TO NAME",""],"id":5081}],[{"start":{"row":202,"column":0},"end":{"row":203,"column":27},"action":"insert","lines":["var pos = grid.getItems().indexOf(item);","    var l = allItems.length"],"id":5082}],[{"start":{"row":202,"column":0},"end":{"row":202,"column":2},"action":"insert","lines":["  "],"id":5083}],[{"start":{"row":202,"column":2},"end":{"row":202,"column":4},"action":"insert","lines":["  "],"id":5084}],[{"start":{"row":194,"column":4},"end":{"row":194,"column":7},"action":"insert","lines":["// "],"id":5085},{"start":{"row":195,"column":4},"end":{"row":195,"column":7},"action":"insert","lines":["// "]},{"start":{"row":196,"column":4},"end":{"row":196,"column":7},"action":"insert","lines":["// "]},{"start":{"row":197,"column":4},"end":{"row":197,"column":7},"action":"insert","lines":["// "]},{"start":{"row":198,"column":4},"end":{"row":198,"column":7},"action":"insert","lines":["// "]},{"start":{"row":199,"column":4},"end":{"row":199,"column":7},"action":"insert","lines":["// "]}],[{"start":{"row":194,"column":4},"end":{"row":194,"column":7},"action":"remove","lines":["// "],"id":5086}],[{"start":{"row":205,"column":17},"end":{"row":206,"column":0},"action":"insert","lines":["",""],"id":5087},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":4},"end":{"row":206,"column":5},"action":"insert","lines":["c"]},{"start":{"row":206,"column":5},"end":{"row":206,"column":6},"action":"insert","lines":["o"]},{"start":{"row":206,"column":6},"end":{"row":206,"column":7},"action":"insert","lines":["n"]},{"start":{"row":206,"column":7},"end":{"row":206,"column":8},"action":"insert","lines":["s"]},{"start":{"row":206,"column":8},"end":{"row":206,"column":9},"action":"insert","lines":["o"]},{"start":{"row":206,"column":9},"end":{"row":206,"column":10},"action":"insert","lines":["l"]},{"start":{"row":206,"column":10},"end":{"row":206,"column":11},"action":"insert","lines":["e"]},{"start":{"row":206,"column":11},"end":{"row":206,"column":12},"action":"insert","lines":["."]},{"start":{"row":206,"column":12},"end":{"row":206,"column":13},"action":"insert","lines":["l"]},{"start":{"row":206,"column":13},"end":{"row":206,"column":14},"action":"insert","lines":["o"]},{"start":{"row":206,"column":14},"end":{"row":206,"column":15},"action":"insert","lines":["g"]}],[{"start":{"row":206,"column":15},"end":{"row":206,"column":17},"action":"insert","lines":["()"],"id":5088}],[{"start":{"row":206,"column":16},"end":{"row":206,"column":17},"action":"insert","lines":["l"],"id":5089}],[{"start":{"row":195,"column":4},"end":{"row":195,"column":7},"action":"remove","lines":["// "],"id":5090}],[{"start":{"row":205,"column":17},"end":{"row":206,"column":0},"action":"insert","lines":["",""],"id":5091},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":4},"end":{"row":206,"column":5},"action":"insert","lines":["c"]},{"start":{"row":206,"column":5},"end":{"row":206,"column":6},"action":"insert","lines":["o"]},{"start":{"row":206,"column":6},"end":{"row":206,"column":7},"action":"insert","lines":["n"]},{"start":{"row":206,"column":7},"end":{"row":206,"column":8},"action":"insert","lines":["s"]},{"start":{"row":206,"column":8},"end":{"row":206,"column":9},"action":"insert","lines":["o"]},{"start":{"row":206,"column":9},"end":{"row":206,"column":10},"action":"insert","lines":["l"]},{"start":{"row":206,"column":10},"end":{"row":206,"column":11},"action":"insert","lines":["e"]},{"start":{"row":206,"column":11},"end":{"row":206,"column":12},"action":"insert","lines":["."]},{"start":{"row":206,"column":12},"end":{"row":206,"column":13},"action":"insert","lines":["l"]},{"start":{"row":206,"column":13},"end":{"row":206,"column":14},"action":"insert","lines":["o"]},{"start":{"row":206,"column":14},"end":{"row":206,"column":15},"action":"insert","lines":["g"]}],[{"start":{"row":206,"column":15},"end":{"row":206,"column":17},"action":"insert","lines":["()"],"id":5092}],[{"start":{"row":206,"column":16},"end":{"row":206,"column":17},"action":"insert","lines":["p"],"id":5093},{"start":{"row":206,"column":17},"end":{"row":206,"column":18},"action":"insert","lines":["o"]},{"start":{"row":206,"column":18},"end":{"row":206,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":221,"column":6},"end":{"row":221,"column":28},"action":"remove","lines":["grid.remove(toRemove);"],"id":5094}],[{"start":{"row":213,"column":21},"end":{"row":214,"column":0},"action":"insert","lines":["",""],"id":5095},{"start":{"row":214,"column":0},"end":{"row":214,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":214,"column":8},"end":{"row":214,"column":30},"action":"insert","lines":["grid.remove(toRemove);"],"id":5096}],[{"start":{"row":216,"column":21},"end":{"row":217,"column":0},"action":"insert","lines":["",""],"id":5097},{"start":{"row":217,"column":0},"end":{"row":217,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":217,"column":8},"end":{"row":217,"column":30},"action":"insert","lines":["grid.remove(toRemove);"],"id":5098}],[{"start":{"row":220,"column":21},"end":{"row":221,"column":0},"action":"insert","lines":["",""],"id":5099},{"start":{"row":221,"column":0},"end":{"row":221,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":221,"column":8},"end":{"row":221,"column":30},"action":"insert","lines":["grid.remove(toRemove);"],"id":5100}],[{"start":{"row":221,"column":30},"end":{"row":221,"column":53},"action":"insert","lines":["{removeElements: true})"],"id":5101}],[{"start":{"row":221,"column":51},"end":{"row":221,"column":52},"action":"remove","lines":["}"],"id":5102}],[{"start":{"row":221,"column":28},"end":{"row":221,"column":29},"action":"insert","lines":[","],"id":5103}],[{"start":{"row":221,"column":29},"end":{"row":221,"column":30},"action":"insert","lines":[" "],"id":5104}],[{"start":{"row":221,"column":30},"end":{"row":221,"column":52},"action":"insert","lines":["{removeElements: true}"],"id":5105}],[{"start":{"row":221,"column":54},"end":{"row":221,"column":76},"action":"remove","lines":["{removeElements: true)"],"id":5106}],[{"start":{"row":221,"column":8},"end":{"row":221,"column":54},"action":"remove","lines":["grid.remove(toRemove, {removeElements: true});"],"id":5107}],[{"start":{"row":224,"column":6},"end":{"row":224,"column":52},"action":"insert","lines":["grid.remove(toRemove, {removeElements: true});"],"id":5108}],[{"start":{"row":217,"column":8},"end":{"row":217,"column":11},"action":"insert","lines":["// "],"id":5109}],[{"start":{"row":214,"column":8},"end":{"row":214,"column":11},"action":"insert","lines":["// "],"id":5110}],[{"start":{"row":214,"column":0},"end":{"row":215,"column":0},"action":"remove","lines":["        // grid.remove(toRemove);",""],"id":5111}],[{"start":{"row":216,"column":0},"end":{"row":217,"column":0},"action":"remove","lines":["        // grid.remove(toRemove);",""],"id":5112}],[{"start":{"row":219,"column":0},"end":{"row":220,"column":8},"action":"remove","lines":["        ","        "],"id":5113},{"start":{"row":218,"column":21},"end":{"row":219,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":206,"column":0},"end":{"row":207,"column":18},"action":"remove","lines":["    console.log(pos)","    console.log(l)"],"id":5114},{"start":{"row":205,"column":17},"end":{"row":206,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":196,"column":0},"end":{"row":200,"column":8},"action":"remove","lines":["    // var pos = grid.getItems().indexOf(item);","    // var l = allItems.length","    // var employeeGrid = columnGrids[103];","    // var employeeItems = employeeGrid.getItems();","        "],"id":5115},{"start":{"row":195,"column":35},"end":{"row":196,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":195,"column":35},"end":{"row":196,"column":0},"action":"remove","lines":["",""],"id":5116}],[{"start":{"row":185,"column":4},"end":{"row":185,"column":7},"action":"remove","lines":["// "],"id":5117},{"start":{"row":186,"column":4},"end":{"row":186,"column":7},"action":"remove","lines":["// "]}],[{"start":{"row":187,"column":29},"end":{"row":188,"column":0},"action":"insert","lines":["",""],"id":5118},{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":188,"column":4},"end":{"row":190,"column":7},"action":"insert","lines":["columnGrids.forEach(function (grid) {","      grid.refreshItems();","    });"],"id":5119}],[{"start":{"row":185,"column":4},"end":{"row":185,"column":7},"action":"insert","lines":["// "],"id":5120},{"start":{"row":186,"column":4},"end":{"row":186,"column":7},"action":"insert","lines":["// "]}],[{"start":{"row":188,"column":4},"end":{"row":190,"column":7},"action":"remove","lines":["columnGrids.forEach(function (grid) {","      grid.refreshItems();","    });"],"id":5121}],[{"start":{"row":215,"column":5},"end":{"row":216,"column":0},"action":"insert","lines":["",""],"id":5122},{"start":{"row":216,"column":0},"end":{"row":216,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":214,"column":5},"end":{"row":215,"column":0},"action":"insert","lines":["",""],"id":5124},{"start":{"row":215,"column":0},"end":{"row":215,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":215,"column":4},"end":{"row":217,"column":7},"action":"insert","lines":["columnGrids.forEach(function (grid) {","      grid.refreshItems();","    });"],"id":5125}],[{"start":{"row":185,"column":4},"end":{"row":185,"column":7},"action":"remove","lines":["// "],"id":5126},{"start":{"row":186,"column":4},"end":{"row":186,"column":7},"action":"remove","lines":["// "]}],[{"start":{"row":185,"column":4},"end":{"row":185,"column":7},"action":"insert","lines":["// "],"id":5127},{"start":{"row":186,"column":4},"end":{"row":186,"column":7},"action":"insert","lines":["// "]}],[{"start":{"row":215,"column":0},"end":{"row":218,"column":0},"action":"remove","lines":["    columnGrids.forEach(function (grid) {","      grid.refreshItems();","    });",""],"id":5129}],[{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"remove","lines":["4"],"id":5130}],[{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"insert","lines":["3"],"id":5131}],[{"start":{"row":73,"column":6},"end":{"row":73,"column":9},"action":"insert","lines":["// "],"id":5132}],[{"start":{"row":73,"column":6},"end":{"row":73,"column":9},"action":"remove","lines":["// "],"id":5133}],[{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"remove","lines":["0"],"id":5134},{"start":{"row":73,"column":22},"end":{"row":73,"column":23},"action":"remove","lines":["0"]},{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"remove","lines":["3"]}],[{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"insert","lines":["2"],"id":5135},{"start":{"row":73,"column":22},"end":{"row":73,"column":23},"action":"insert","lines":["0"]},{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"insert","lines":["$"]}],[{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"remove","lines":["$"],"id":5136}],[{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"insert","lines":["%"],"id":5137}],[{"start":{"row":73,"column":24},"end":{"row":73,"column":25},"action":"remove","lines":[";"],"id":5138}],[{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"remove","lines":["%"],"id":5139},{"start":{"row":73,"column":22},"end":{"row":73,"column":23},"action":"remove","lines":["0"]},{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"remove","lines":["2"]}],[{"start":{"row":72,"column":6},"end":{"row":72,"column":9},"action":"remove","lines":["// "],"id":5140}],[{"start":{"row":73,"column":6},"end":{"row":73,"column":9},"action":"insert","lines":["// "],"id":5141}],[{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"remove","lines":["w"],"id":5142},{"start":{"row":72,"column":24},"end":{"row":72,"column":25},"action":"remove","lines":[" "]},{"start":{"row":72,"column":23},"end":{"row":72,"column":24},"action":"remove","lines":["+"]},{"start":{"row":72,"column":22},"end":{"row":72,"column":23},"action":"remove","lines":[" "]}],[{"start":{"row":72,"column":21},"end":{"row":72,"column":22},"action":"remove","lines":["x"],"id":5143}],[{"start":{"row":72,"column":21},"end":{"row":72,"column":22},"action":"insert","lines":["0"],"id":5144}],[{"start":{"row":72,"column":21},"end":{"row":72,"column":22},"action":"remove","lines":["0"],"id":5145}],[{"start":{"row":72,"column":21},"end":{"row":72,"column":22},"action":"insert","lines":["w"],"id":5146}],[{"start":{"row":72,"column":22},"end":{"row":72,"column":23},"action":"insert","lines":[" "],"id":5147},{"start":{"row":72,"column":23},"end":{"row":72,"column":24},"action":"insert","lines":["-"]}],[{"start":{"row":72,"column":24},"end":{"row":72,"column":25},"action":"insert","lines":[" "],"id":5148},{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"insert","lines":["x"]}],[{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"remove","lines":["x"],"id":5149},{"start":{"row":72,"column":24},"end":{"row":72,"column":25},"action":"remove","lines":[" "]},{"start":{"row":72,"column":23},"end":{"row":72,"column":24},"action":"remove","lines":["-"]}],[{"start":{"row":72,"column":23},"end":{"row":72,"column":24},"action":"insert","lines":["+"],"id":5150}],[{"start":{"row":72,"column":24},"end":{"row":72,"column":25},"action":"insert","lines":[" "],"id":5151},{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"insert","lines":["0"]}],[{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"remove","lines":["e"],"id":5157},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"remove","lines":["u"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"remove","lines":["r"]},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"remove","lines":["t"]}],[{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["f"],"id":5158},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["a"]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["l"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["s"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":256,"column":4},"end":{"row":256,"column":7},"action":"insert","lines":["// "],"id":5162},{"start":{"row":257,"column":4},"end":{"row":257,"column":7},"action":"insert","lines":["// "]}],[{"start":{"row":257,"column":64},"end":{"row":258,"column":0},"action":"insert","lines":["",""],"id":5164},{"start":{"row":258,"column":0},"end":{"row":258,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":258,"column":4},"end":{"row":258,"column":59},"action":"insert","lines":["item.getElement().style.width = item.getWidth() + 'px';"],"id":5165}],[{"start":{"row":258,"column":36},"end":{"row":258,"column":58},"action":"remove","lines":["item.getWidth() + 'px'"],"id":5166},{"start":{"row":258,"column":36},"end":{"row":258,"column":37},"action":"insert","lines":["1"]},{"start":{"row":258,"column":37},"end":{"row":258,"column":38},"action":"insert","lines":["6"]},{"start":{"row":258,"column":38},"end":{"row":258,"column":39},"action":"insert","lines":["3"]},{"start":{"row":258,"column":39},"end":{"row":258,"column":40},"action":"insert","lines":["p"]},{"start":{"row":258,"column":40},"end":{"row":258,"column":41},"action":"insert","lines":["x"]}],[{"start":{"row":258,"column":40},"end":{"row":258,"column":41},"action":"remove","lines":["x"],"id":5167},{"start":{"row":258,"column":39},"end":{"row":258,"column":40},"action":"remove","lines":["p"]}],[{"start":{"row":258,"column":39},"end":{"row":258,"column":40},"action":"insert","lines":[" "],"id":5168},{"start":{"row":258,"column":40},"end":{"row":258,"column":41},"action":"insert","lines":["+"]}],[{"start":{"row":258,"column":41},"end":{"row":258,"column":42},"action":"insert","lines":[" "],"id":5169}],[{"start":{"row":258,"column":42},"end":{"row":258,"column":44},"action":"insert","lines":["''"],"id":5170}],[{"start":{"row":258,"column":43},"end":{"row":258,"column":44},"action":"insert","lines":["p"],"id":5171},{"start":{"row":258,"column":44},"end":{"row":258,"column":45},"action":"insert","lines":["x"]}],[{"start":{"row":84,"column":4},"end":{"row":84,"column":7},"action":"remove","lines":["// "],"id":5172},{"start":{"row":85,"column":4},"end":{"row":85,"column":7},"action":"remove","lines":["// "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":7},"action":"remove","lines":["// "],"id":5173},{"start":{"row":25,"column":4},"end":{"row":25,"column":7},"action":"remove","lines":["// "]},{"start":{"row":26,"column":4},"end":{"row":26,"column":7},"action":"remove","lines":["// "]}],[{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":[","],"id":5174}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"remove","lines":["  "],"id":5175},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"remove","lines":["  "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"remove","lines":["  "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":7},"action":"remove","lines":["// "],"id":5176}],[{"start":{"row":26,"column":4},"end":{"row":28,"column":4},"action":"insert","lines":["","      ","    "],"id":5177}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["}"],"id":5178}],[{"start":{"row":26,"column":5},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":5179},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["r"]},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["e"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["t"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["u"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["r"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":[" "],"id":5180},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["t"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["r"]},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["u"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["e"]},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["l"]}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"remove","lines":["l"],"id":5181}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":[";"],"id":5182}]]},"ace":{"folds":[],"scrolltop":189.5,"scrollleft":0,"selection":{"start":{"row":16,"column":17},"end":{"row":16,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1536602305934,"hash":"1ff9cbdf96631a341eb6088c6228a49d0afd1779"}