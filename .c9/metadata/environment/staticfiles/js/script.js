{"filter":false,"title":"script.js","tooltip":"/staticfiles/js/script.js","ace":{"folds":[],"scrolltop":3602.5,"scrollleft":0,"selection":{"start":{"row":266,"column":4},"end":{"row":266,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":81,"state":"start","mode":"ace/mode/javascript"}},"hash":"60ed747d2c4d04d5cc90586e3058d30f6e2f03d8","undoManager":{"mark":30,"position":30,"stack":[[{"start":{"row":258,"column":0},"end":{"row":279,"column":4},"action":"remove","lines":["// Control Panel Toggles","$(document).ready(function(){","\t$('.toggle-unscheduled').on(\"click\", function(){","    $('.unscheduled').toggle();","  });","  $('.toggle-scheduled').on(\"click\", function(){","    $('.scheduled').toggle();","  });","  $('.toggle-inactive-locations').on(\"click\", function(){","\t  $('.location-title.collapsed').each(function(){","\t    $(this).parent().parent().toggle();","\t  });","  });","  $('.toggle-bars').on(\"click\", function(){","\t  $('.bar').each(function(){","\t    var flag = $(this).is(':checked');","\t    $(this).prop('indeterminate', false);","\t    $(this).prop('checked', !flag);","\t    $(this).parent().parent().parent().toggle();","    });","  });","}); "],"id":505},{"start":{"row":257,"column":0},"end":{"row":258,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":256,"column":3},"end":{"row":257,"column":0},"action":"remove","lines":["",""],"id":506}],[{"start":{"row":258,"column":0},"end":{"row":267,"column":3},"action":"remove","lines":["// Control Panel Arrival Times","$('.update-role').on(\"click\", function(){","  var target = $(this).attr('id')[0].toUpperCase();","  var arrival_time = $(this).parent().prev().children().val();","  $('.'+target).val(arrival_time);","});","","$(\".template-header > .edit\").click(function() {","  $('.template-name').prop('readonly', false);","});"],"id":507},{"start":{"row":257,"column":0},"end":{"row":258,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":508},{"start":{"row":2,"column":97},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":36},"action":"remove","lines":["$(\".colorPickSelector\").colorPick();"],"id":509}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["// Navbar: set active link",""],"id":510}],[{"start":{"row":9,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["","  // $(\".check-all\").click(function(){","  //     $('input:checkbox').not(this).prop('checked', this.checked);","  // });","  "],"id":511},{"start":{"row":8,"column":5},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":5},"end":{"row":9,"column":2},"action":"remove","lines":["","  "],"id":512}],[{"start":{"row":34,"column":0},"end":{"row":56,"column":1},"action":"remove","lines":["// Location App: load positions","function loadPositions(l) {","  if ($('.modal-title').html() === 'Update location') {","    var context = {location: l};","    $.get( \"/locations/create/positions/\", context, function(data) {","      p = JSON.parse(data);","      var positions = {};","      Object.keys(p).map(function(k,t) {","        positions[k] = p[k];","      });","      for (var short_name in positions) {","        var p = short_name.replace(/[0-9]/g, '');","        var verbose_name = positions[short_name];","        var c = '.'+p+'-container';","        var insertion = $('.d-none').children().clone();","        $(insertion).find('.short-name').html(short_name);","        $(insertion).find('.short-name').addClass(p);","        $(insertion).find('.verbose-name').html(verbose_name);","        $(c).append(insertion);","      }","    });","  }","}"],"id":513}],[{"start":{"row":133,"column":0},"end":{"row":134,"column":0},"action":"remove","lines":["// {'locations': {'10': {'active': False},",""],"id":514}],[{"start":{"row":227,"column":0},"end":{"row":267,"column":3},"action":"remove","lines":["// Add/Remove Employees","$(function() {","  $('.schedule-cards').on('click', '.remove-employee', function(event) { ","\t  var shift = $(this).parent().next().find('.arrival-time');","\t  $(this).toggleClass('rotate');","\t  $(shift).each(function() {","\t    var delete_button = $(this).next();","\t    $(delete_button).toggleClass('display-flex');","\t    $(this).toggle();","      $(this).prev().toggleClass('red-border');","      $(this).prev().prev().children().toggleClass('red-border-background');","\t  });","\t});","\t$('.schedule-cards').on('click', '.remove-button', function(event) { ","\t  $(this).parent().parent().parent().remove();","  });","  $('.schedule-cards').on('click', '.add-employee', function(event) { ","\t  var card_body = $(this).parent().next();","\t  var new_position = $(card_body).children().last().find('span').html();","\t  var prefix = new_position.split('')[0];","\t  var i = Number(new_position.split('')[1]);","\t  ","\t  if (prefix !== 'E') {","\t    new_position = 'E1';","\t    i = 1;","\t  } else {","\t    i += 1;","\t    new_position = 'E'+i;","\t  }","\t  ","\t  var new_employee = $(card_body).children().first().clone();","\t  new_employee.find('input').attr('value','');","\t  new_employee.find('option').first().html('Extra #' + i);","\t  new_employee.find('option').first().attr('value','Extra #' + i);","\t  new_employee.find('option').first().attr('class',new_position);","\t  new_employee.find('span').html(new_position);","\t  new_employee.find('.template-placeholder').attr('placeholder','Extra #' + i);","\t  new_employee.find('.verbose-name').html('Extra #' + i);","\t  $(card_body).append(new_employee);","\t});","});"],"id":515}],[{"start":{"row":226,"column":0},"end":{"row":227,"column":0},"action":"remove","lines":["",""],"id":516},{"start":{"row":225,"column":0},"end":{"row":226,"column":0},"action":"remove","lines":["",""]},{"start":{"row":224,"column":3},"end":{"row":225,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":248,"column":0},"end":{"row":249,"column":0},"action":"remove","lines":["  console.log('hello');",""],"id":517}],[{"start":{"row":247,"column":0},"end":{"row":291,"column":3},"action":"remove","lines":["$('.category-header').on('click', '.add-category-button', function() {","    var id = $(this).parent().next().children().first().attr('id');","    var new_category = $('#'+id).find('.add-category').last().clone();","    $('#'+id).children().last().before(new_category);","});","$('.company-categories').on('click', '.delete', function() { ","  var myvar = $(this).parent().parent().parent();","  var new_category = $('.add-category');","  $(myvar).remove();","  if (!new_category) $('.category-abbr').next(new_category);","});","","$('.save-categories').click(function(e) {","  e.preventDefault();","  var categories = {'categories': {}};","  var category_id = $(this).parent().attr('id');","  ","  $(this).parent().children('.add-category').each(function() {","    var color = $(this).find('.colorPickSelector').css('color');","    if (category_id === 'roles') {","      var verbose_name = $(this).find('.category-name').val();","      var short_name = $(this).find('.category-abbr').val();","      categories['categories'][verbose_name] = {","        'color': color,","        'short_name': short_name,","      };","    } else if (category_id == 'location') {","      var category = $(this).find('.category-name').val();","      categories['categories'][category] = {","        'color': color,","      };","    }","  });","  categories = JSON.stringify(categories);","  var context = {","    categories: categories,","    category_id: category_id","  };","  if (category_id === 'roles') {","    $.post( \"/company/roles/\", context);","  } else if (category_id === 'location') {","    $.post( \"/company/location/\", context);","  }","  ","});"],"id":518}],[{"start":{"row":246,"column":0},"end":{"row":247,"column":0},"action":"remove","lines":["",""],"id":519},{"start":{"row":245,"column":0},"end":{"row":246,"column":0},"action":"remove","lines":["",""]},{"start":{"row":244,"column":0},"end":{"row":245,"column":0},"action":"remove","lines":["",""]},{"start":{"row":243,"column":0},"end":{"row":244,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":246,"column":0},"end":{"row":247,"column":0},"action":"remove","lines":["",""],"id":520},{"start":{"row":245,"column":0},"end":{"row":246,"column":0},"action":"remove","lines":["",""]},{"start":{"row":244,"column":0},"end":{"row":245,"column":0},"action":"remove","lines":["",""]},{"start":{"row":243,"column":0},"end":{"row":244,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":269,"column":0},"end":{"row":273,"column":6},"action":"remove","lines":["  // var count = $('.' + short_name).length;","  // count = 0;","  // $('.' + short_name).each(function(){","//     count += 1;","// });"],"id":521},{"start":{"row":268,"column":60},"end":{"row":269,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["  ",""],"id":522}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["  ",""],"id":523}],[{"start":{"row":4,"column":0},"end":{"row":30,"column":3},"action":"remove","lines":["$(document).ready(function () {","  $(\".check-all\").click(function(){","      $(this).parent().siblings().find('input:checkbox').not(this).prop('checked', this.checked);","  });","  $(\".location-checkbox:input[type=checkbox]\").each(function () {","      var location = $(this).parent().parent().prev();","      $(this).change(function() {","         $(this).change(updateCount(location));","      });","  });","","  updateCount(l = false);","","  function updateCount (l = false) {","    if (!l) {","      var locationCategories = $('.location-category');","      $(locationCategories).each(function() {","        var count = $(this).next().find(\".check-one:input[type=checkbox]:checked\").length;","        ","        $(this).find(\".active-count\").text(count);","      });","    } else {","      var count = $(l).next().find(\".check-one:input[type=checkbox]:checked\").length;","      $(l).find(\".active-count\").text(count);","    }","  }","});"],"id":524}],[{"start":{"row":3,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["","","","",""],"id":525},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"remove","lines":["    ",""],"id":526}],[{"start":{"row":98,"column":1},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":527}],[{"start":{"row":100,"column":0},"end":{"row":139,"column":3},"action":"remove","lines":["// Generate Template","$(\".generate-template\" ).click(function() {","  var template = {'locations': {}};","  var title = $('.template-name').val();","  $('.location').each(function() {","    var location = $(this).attr('id');","    var active = $(this).prev().prop('checked');","    template['locations'][location] = {","      'active': active,","      'bar': '',","      'id': '',","      'location': '',","      'positions': {},","      'scheduled': 0","    };","  });","  template['title'] = title;","  var context = { template:JSON.stringify(template), title:title, new_template: true };","  $.post( \"/schedules/templates/create/generate/\", context, function( data ) {","    $('.schedule-cards').html(data);","  });","});","","$(\".choose-template\" ).click(function() {","  var category = $('#template-subcategory').children('option:selected').attr('id');","  $.post( \"/schedules/templates/create/modal/\", {category: category}, function( data ) {","      $('.modal-body').html(data);","  });","  $(\"#modal-object\").modal(\"hide\");","});","","$(\".update-template\" ).click(function() {","  var pk = $('.modal-body').find('.active').attr('id');","  var category = $('#template-subcategory').children('option:selected').attr('id');","  var context = {category: category, pk: pk};","  $.post( \"/schedules/templates/create/select/\", context, function( data ) {","      $('.schedule-cards').html(data);","  });","  $(\".modal\").modal(\"hide\");","});"],"id":528}],[{"start":{"row":144,"column":0},"end":{"row":145,"column":0},"action":"remove","lines":["      // if (verbose_name) d['positions'][position]['verbose_name'] = verbose_name;",""],"id":529}],[{"start":{"row":153,"column":0},"end":{"row":155,"column":52},"action":"remove","lines":["var template_category = $('#template-category');","var template_subcategory = $( '#template-subcategory' );","var options = template_subcategory.find( 'option' );"],"id":530}],[{"start":{"row":154,"column":46},"end":{"row":155,"column":0},"action":"insert","lines":["",""],"id":531},{"start":{"row":155,"column":0},"end":{"row":155,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":155,"column":2},"end":{"row":157,"column":52},"action":"insert","lines":["var template_category = $('#template-category');","var template_subcategory = $( '#template-subcategory' );","var options = template_subcategory.find( 'option' );"],"id":532}],[{"start":{"row":156,"column":0},"end":{"row":156,"column":2},"action":"insert","lines":["  "],"id":533},{"start":{"row":157,"column":0},"end":{"row":157,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":154,"column":2},"end":{"row":154,"column":19},"action":"remove","lines":["template_category"],"id":534},{"start":{"row":154,"column":2},"end":{"row":154,"column":22},"action":"insert","lines":["'#template-category'"]}],[{"start":{"row":155,"column":0},"end":{"row":156,"column":0},"action":"remove","lines":["  var template_category = $('#template-category');",""],"id":535}]]},"timestamp":1537555526242}