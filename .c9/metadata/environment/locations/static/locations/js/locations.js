{"filter":false,"title":"locations.js","tooltip":"/locations/static/locations/js/locations.js","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["// Location App: load positions","function loadPositions(l) {","  if ($('.modal-title').html() === 'Update location') {","    var context = {location: l};","    $.get( \"/locations/create/positions/\", context, function(data) {","      p = JSON.parse(data);","      var positions = {};","      Object.keys(p).map(function(k,t) {","        positions[k] = p[k];","      });","      for (var short_name in positions) {","        var p = short_name.replace(/[0-9]/g, '');","        var verbose_name = positions[short_name];","        var c = '.'+p+'-container';","        var insertion = $('.d-none').children().clone();","        $(insertion).find('.short-name').html(short_name);","        $(insertion).find('.short-name').addClass(p);","        $(insertion).find('.verbose-name').html(verbose_name);","        $(c).append(insertion);","      }","    });","  }","}"],"id":1}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":17},"action":"remove","lines":["Location App: "],"id":2}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["i"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["m"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["o"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["d"]},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["a"]},{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":12},"action":"insert","lines":["/*global $*/"],"id":6}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":12},"end":{"row":0,"column":12},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1537553778632,"hash":"794af2cecc67d25f2c7cda5524c1755e8c338525"}