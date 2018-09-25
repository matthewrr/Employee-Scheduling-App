{"filter":false,"title":"events.js","tooltip":"/events/static/events/js/events.js","undoManager":{"mark":78,"position":78,"stack":[[{"start":{"row":0,"column":0},"end":{"row":26,"column":3},"action":"insert","lines":["$(document).ready(function () {","  $(\".check-all\").click(function(){","      $(this).parent().siblings().find('input:checkbox').not(this).prop('checked', this.checked);","  });","  $(\".location-checkbox:input[type=checkbox]\").each(function () {","      var location = $(this).parent().parent().prev();","      $(this).change(function() {","         $(this).change(updateCount(location));","      });","  });","","  updateCount(l = false);","","  function updateCount (l = false) {","    if (!l) {","      var locationCategories = $('.location-category');","      $(locationCategories).each(function() {","        var count = $(this).next().find(\".check-one:input[type=checkbox]:checked\").length;","        ","        $(this).find(\".active-count\").text(count);","      });","    } else {","      var count = $(l).next().find(\".check-one:input[type=checkbox]:checked\").length;","      $(l).find(\".active-count\").text(count);","    }","  }","});"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["/"],"id":3},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["/"]}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["C"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["o"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["n"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["t"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["r"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["o"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[" "],"id":5},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["P"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["a"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["n"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["e"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":12},"action":"insert","lines":["/*global $*/"],"id":7}],[{"start":{"row":1,"column":16},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":8}],[{"start":{"row":0,"column":12},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":29,"column":3},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["",""]},{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""]},{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":33,"column":0},"end":{"row":65,"column":0},"action":"insert","lines":["$(function () {","    function showSlide(n) {","        $('body').unbind('mousewheel');","        currSlide += n;","        currSlide = currSlide <= 0 ? 0 : currSlide >= $slide.length - 1 ? $slide.length - 1 : currSlide;","        var displacment = window.innerWidth * currSlide;","        $('.slides').css('transform', 'translateX(-' + displacment + 'px)');","        setTimeout(function () {","            $('body').bind('mousewheel', mouseEvent);","        }, 800);","        $('nav a.active').removeClass('active');","        $($('a')[currSlide]).addClass('active');","    }","    function mouseEvent(e, delta) {","        showSlide(delta >= 0 ? 1 : -1);","        e.preventDefault();","    }","    $('nav a').click(function (e) {","        var newslide = parseInt($(this).attr('href')[1]);","        var diff = newslide - currSlide - 1;","        showSlide(diff);","        e.preventDefault();","    });","    $(window).resize(function () {","        var displacment = window.innerWidth * currSlide;","        $('.slides').css('transform', 'translateX(-' + displacment + 'px)');","    });","    var currSlide = 0;","    var $slide = $('.slide');","    $($('nav a')[0]).addClass('active');","    $('body').bind('mousewheel', mouseEvent);","});",""],"id":11}],[{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"remove","lines":["v"],"id":12},{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"remove","lines":["a"]},{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"remove","lines":["n"]}],[{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["."],"id":13},{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["l"]},{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["o"]},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["c"]},{"start":{"row":43,"column":15},"end":{"row":43,"column":16},"action":"insert","lines":["a"]},{"start":{"row":43,"column":16},"end":{"row":43,"column":17},"action":"insert","lines":["t"]},{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":["i"]},{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":["o"]},{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["-"],"id":14},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["c"]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["a"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["t"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["e"]},{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"insert","lines":["g"]},{"start":{"row":43,"column":26},"end":{"row":43,"column":27},"action":"insert","lines":["o"]},{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"insert","lines":["r"]},{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["i"]},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["e"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":50,"column":9},"end":{"row":50,"column":10},"action":"remove","lines":["v"],"id":15},{"start":{"row":50,"column":8},"end":{"row":50,"column":9},"action":"remove","lines":["a"]},{"start":{"row":50,"column":7},"end":{"row":50,"column":8},"action":"remove","lines":["n"]}],[{"start":{"row":50,"column":7},"end":{"row":50,"column":8},"action":"insert","lines":["."],"id":16},{"start":{"row":50,"column":8},"end":{"row":50,"column":9},"action":"insert","lines":["l"]},{"start":{"row":50,"column":9},"end":{"row":50,"column":10},"action":"insert","lines":["o"]},{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"insert","lines":["c"]},{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"insert","lines":["a"]},{"start":{"row":50,"column":12},"end":{"row":50,"column":13},"action":"insert","lines":["t"]},{"start":{"row":50,"column":13},"end":{"row":50,"column":14},"action":"insert","lines":["i"]},{"start":{"row":50,"column":14},"end":{"row":50,"column":15},"action":"insert","lines":["o"]},{"start":{"row":50,"column":15},"end":{"row":50,"column":16},"action":"insert","lines":["n"]},{"start":{"row":50,"column":16},"end":{"row":50,"column":17},"action":"insert","lines":["-"]},{"start":{"row":50,"column":17},"end":{"row":50,"column":18},"action":"insert","lines":["c"]},{"start":{"row":50,"column":18},"end":{"row":50,"column":19},"action":"insert","lines":["a"]},{"start":{"row":50,"column":19},"end":{"row":50,"column":20},"action":"insert","lines":["t"]},{"start":{"row":50,"column":20},"end":{"row":50,"column":21},"action":"insert","lines":["e"]},{"start":{"row":50,"column":21},"end":{"row":50,"column":22},"action":"insert","lines":["g"]},{"start":{"row":50,"column":22},"end":{"row":50,"column":23},"action":"insert","lines":["o"]},{"start":{"row":50,"column":23},"end":{"row":50,"column":24},"action":"insert","lines":["r"]},{"start":{"row":50,"column":24},"end":{"row":50,"column":25},"action":"insert","lines":["i"]}],[{"start":{"row":50,"column":25},"end":{"row":50,"column":26},"action":"insert","lines":["e"],"id":17},{"start":{"row":50,"column":26},"end":{"row":50,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"remove","lines":["v"],"id":18},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"remove","lines":["a"]},{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"remove","lines":["n"]}],[{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"insert","lines":["."],"id":19},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"insert","lines":["l"]},{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"insert","lines":["o"]},{"start":{"row":62,"column":12},"end":{"row":62,"column":13},"action":"insert","lines":["c"]},{"start":{"row":62,"column":13},"end":{"row":62,"column":14},"action":"insert","lines":["a"]},{"start":{"row":62,"column":14},"end":{"row":62,"column":15},"action":"insert","lines":["t"]},{"start":{"row":62,"column":15},"end":{"row":62,"column":16},"action":"insert","lines":["i"]},{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"insert","lines":["o"]},{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"insert","lines":["n"]},{"start":{"row":62,"column":18},"end":{"row":62,"column":19},"action":"insert","lines":["-"]},{"start":{"row":62,"column":19},"end":{"row":62,"column":20},"action":"insert","lines":["c"]},{"start":{"row":62,"column":20},"end":{"row":62,"column":21},"action":"insert","lines":["a"]},{"start":{"row":62,"column":21},"end":{"row":62,"column":22},"action":"insert","lines":["t"]},{"start":{"row":62,"column":22},"end":{"row":62,"column":23},"action":"insert","lines":["e"]},{"start":{"row":62,"column":23},"end":{"row":62,"column":24},"action":"insert","lines":["g"]},{"start":{"row":62,"column":24},"end":{"row":62,"column":25},"action":"insert","lines":["o"]},{"start":{"row":62,"column":25},"end":{"row":62,"column":26},"action":"insert","lines":["r"]}],[{"start":{"row":62,"column":26},"end":{"row":62,"column":27},"action":"insert","lines":["i"],"id":20},{"start":{"row":62,"column":27},"end":{"row":62,"column":28},"action":"insert","lines":["e"]},{"start":{"row":62,"column":28},"end":{"row":62,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":3},"action":"insert","lines":["// "],"id":21},{"start":{"row":34,"column":0},"end":{"row":34,"column":3},"action":"insert","lines":["// "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":3},"action":"insert","lines":["// "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":3},"action":"insert","lines":["// "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":3},"action":"insert","lines":["// "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":3},"action":"insert","lines":["// "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":3},"action":"insert","lines":["// "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":3},"action":"insert","lines":["// "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":3},"action":"insert","lines":["// "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":3},"action":"insert","lines":["// "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":3},"action":"insert","lines":["// "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":3},"action":"insert","lines":["// "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":3},"action":"insert","lines":["// "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":3},"action":"insert","lines":["// "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":3},"action":"insert","lines":["// "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":3},"action":"insert","lines":["// "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":3},"action":"insert","lines":["// "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":3},"action":"insert","lines":["// "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":3},"action":"insert","lines":["// "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":3},"action":"insert","lines":["// "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":3},"action":"insert","lines":["// "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":3},"action":"insert","lines":["// "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":3},"action":"insert","lines":["// "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":3},"action":"insert","lines":["// "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":3},"action":"insert","lines":["// "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":3},"action":"insert","lines":["// "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":3},"action":"insert","lines":["// "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":3},"action":"insert","lines":["// "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":3},"action":"insert","lines":["// "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":3},"action":"insert","lines":["// "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":3},"action":"insert","lines":["// "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":3},"action":"insert","lines":["// "]}],[{"start":{"row":31,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["$('#myTab a').on('click', function (e) {","  e.preventDefault()","  $(this).tab('show')","})"],"id":22}],[{"start":{"row":34,"column":2},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":42},"action":"insert","lines":["$('#myTab a[href=\"#profile\"]').tab('show')"],"id":24}],[{"start":{"row":31,"column":3},"end":{"row":31,"column":9},"action":"remove","lines":["#myTab"],"id":25},{"start":{"row":31,"column":3},"end":{"row":31,"column":4},"action":"insert","lines":["."]},{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["n"]},{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"insert","lines":["a"]},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"insert","lines":["v"]},{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":["-"]},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["l"]},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["i"]},{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["n"]},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["k"]}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"remove","lines":["k"],"id":26},{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"remove","lines":["n"]},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"remove","lines":["i"]},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"remove","lines":["l"]}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["i"],"id":27},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["t"]},{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["e"]},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["m"]}],[{"start":{"row":32,"column":20},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["  "]},{"start":{"row":33,"column":2},"end":{"row":34,"column":0},"action":"insert","lines":["",""]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"insert","lines":["$"],"id":29}],[{"start":{"row":33,"column":3},"end":{"row":33,"column":5},"action":"insert","lines":["()"],"id":30}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["t"],"id":31},{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"insert","lines":["h"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["i"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["."],"id":32}],[{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["a"],"id":33},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["t"]},{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["t"]},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":33,"column":14},"end":{"row":33,"column":16},"action":"insert","lines":["()"],"id":34}],[{"start":{"row":33,"column":15},"end":{"row":33,"column":17},"action":"insert","lines":["''"],"id":35}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":["h"],"id":36},{"start":{"row":33,"column":17},"end":{"row":33,"column":18},"action":"insert","lines":["r"]},{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"insert","lines":["e"]},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"insert","lines":["f"]}],[{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"insert","lines":[";"],"id":37}],[{"start":{"row":33,"column":23},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"insert","lines":["v"],"id":39},{"start":{"row":33,"column":3},"end":{"row":33,"column":4},"action":"insert","lines":["a"]},{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["r"]}],[{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"insert","lines":[" "],"id":40},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["t"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["a"]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["r"]},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"remove","lines":["g"],"id":41}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":[" "],"id":42},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"remove","lines":["this"],"id":44},{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"insert","lines":["t"]},{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["a"]},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":3},"action":"insert","lines":["// "],"id":45}],[{"start":{"row":36,"column":2},"end":{"row":36,"column":5},"action":"insert","lines":["// "],"id":47}],[{"start":{"row":35,"column":2},"end":{"row":35,"column":44},"action":"insert","lines":["$('#myTab a[href=\"#profile\"]').tab('show')"],"id":48}],[{"start":{"row":33,"column":33},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"remove","lines":["r"],"id":50},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"remove","lines":["a"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"remove","lines":["t"]}],[{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["c"],"id":51},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["l"]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["i"]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"remove","lines":["i"],"id":52},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"remove","lines":["l"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"remove","lines":["c"]}],[{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["c"],"id":53},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["l"]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["i"]},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["k"]},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["e"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["r"]}],[{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"remove","lines":["r"],"id":54},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"remove","lines":["e"]},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"remove","lines":["k"]}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["c"],"id":55},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["k"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["e"]},{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["d"]},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["L"]},{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"insert","lines":["i"]},{"start":{"row":33,"column":15},"end":{"row":33,"column":16},"action":"insert","lines":["n"]},{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":["k"]}],[{"start":{"row":33,"column":6},"end":{"row":33,"column":17},"action":"remove","lines":["clickedLink"],"id":56},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["t"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["a"]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["r"]},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["g"]},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["e"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["I"],"id":57},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["D"]}],[{"start":{"row":33,"column":38},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"insert","lines":["$"],"id":59}],[{"start":{"row":34,"column":3},"end":{"row":34,"column":5},"action":"insert","lines":["()"],"id":60}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["t"],"id":61},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["a"]},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["r"]},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["g"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["e"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["t"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["I"]},{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["d"]}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"remove","lines":["d"],"id":62}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["D"],"id":63}],[{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["."],"id":64},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["c"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["l"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["a"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["s"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":21},"action":"insert","lines":["()"],"id":65}],[{"start":{"row":34,"column":20},"end":{"row":34,"column":22},"action":"insert","lines":["''"],"id":66}],[{"start":{"row":34,"column":20},"end":{"row":34,"column":22},"action":"remove","lines":["''"],"id":67},{"start":{"row":34,"column":19},"end":{"row":34,"column":21},"action":"remove","lines":["()"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"remove","lines":["s"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"remove","lines":["s"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"remove","lines":["a"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"remove","lines":["l"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"remove","lines":["c"]}],[{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["a"],"id":68},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["d"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["d"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["C"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["l"]},{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["a"]},{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["s"]},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":34,"column":22},"end":{"row":34,"column":24},"action":"insert","lines":["()"],"id":69}],[{"start":{"row":34,"column":23},"end":{"row":34,"column":25},"action":"insert","lines":["''"],"id":70}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["s"],"id":71},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["h"]},{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"insert","lines":["o"]},{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"insert","lines":["w"]}],[{"start":{"row":34,"column":30},"end":{"row":34,"column":31},"action":"insert","lines":[";"],"id":72}],[{"start":{"row":37,"column":2},"end":{"row":37,"column":5},"action":"insert","lines":["// "],"id":73}],[{"start":{"row":33,"column":38},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":74},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["  "]},{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"insert","lines":["c"]},{"start":{"row":34,"column":3},"end":{"row":34,"column":4},"action":"insert","lines":["o"]},{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["n"]},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["s"]},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["o"]},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["l"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["e"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["."]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["l"]},{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["o"]},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["i"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"remove","lines":["g"],"id":75},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"remove","lines":["i"]}],[{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["g"],"id":76}],[{"start":{"row":34,"column":13},"end":{"row":34,"column":15},"action":"insert","lines":["()"],"id":77}],[{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["t"],"id":78},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["a"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["r"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["g"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["e"]},{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["t"]},{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["I"]},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["D"]}],[{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":[";"],"id":79}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":3},"action":"insert","lines":["// "],"id":80},{"start":{"row":32,"column":0},"end":{"row":32,"column":3},"action":"insert","lines":["// "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":3},"action":"insert","lines":["// "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":3},"action":"insert","lines":["// "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":3},"action":"insert","lines":["// "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":3},"action":"insert","lines":["// "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":3},"action":"insert","lines":["// "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":3},"action":"insert","lines":["// "]}]]},"ace":{"folds":[],"scrolltop":433.5,"scrollleft":0,"selection":{"start":{"row":40,"column":5},"end":{"row":40,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/javascript"}},"timestamp":1537897607461,"hash":"bd87d6b16a264cba5138a113afcd04b87e414994"}