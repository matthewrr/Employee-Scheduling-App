{"filter":false,"title":"company_profile.js","tooltip":"/company_profile/static/company_profile/js/company_profile.js","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":36},"action":"insert","lines":["$(\".colorPickSelector\").colorPick();"],"id":1}],[{"start":{"row":0,"column":36},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":46,"column":3},"action":"insert","lines":["$('.category-header').on('click', '.add-category-button', function() {","    var id = $(this).parent().next().children().first().attr('id');","    var new_category = $('#'+id).find('.add-category').last().clone();","    $('#'+id).children().last().before(new_category);","});","$('.company-categories').on('click', '.delete', function() { ","  var myvar = $(this).parent().parent().parent();","  var new_category = $('.add-category');","  $(myvar).remove();","  if (!new_category) $('.category-abbr').next(new_category);","});","","$('.save-categories').click(function(e) {","  e.preventDefault();","  var categories = {'categories': {}};","  var category_id = $(this).parent().attr('id');","  ","  $(this).parent().children('.add-category').each(function() {","    var color = $(this).find('.colorPickSelector').css('color');","    if (category_id === 'roles') {","      var verbose_name = $(this).find('.category-name').val();","      var short_name = $(this).find('.category-abbr').val();","      categories['categories'][verbose_name] = {","        'color': color,","        'short_name': short_name,","      };","    } else if (category_id == 'location') {","      var category = $(this).find('.category-name').val();","      categories['categories'][category] = {","        'color': color,","      };","    }","  });","  categories = JSON.stringify(categories);","  var context = {","    categories: categories,","    category_id: category_id","  };","  if (category_id === 'roles') {","    $.post( \"/company/roles/\", context);","  } else if (category_id === 'location') {","    $.post( \"/company/location/\", context);","  }","  ","});"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":12},"action":"insert","lines":["/*global $*/"],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":25},"end":{"row":17,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1537553785901,"hash":"ba4428c5bc7e82420024a3bf91225cceb43a3341"}