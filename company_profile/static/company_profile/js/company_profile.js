/*global $*/
$(".colorPickSelector").colorPick();

$('.category-header').on('click', '.add-category-button', function() {
    var id = $(this).parent().next().children().first().attr('id');
    var new_category = $('#'+id).find('.add-category').last().clone();
    $('#'+id).children().last().before(new_category);
});
$('.company-categories').on('click', '.delete', function() { 
  var myvar = $(this).parent().parent().parent();
  var new_category = $('.add-category');
  $(myvar).remove();
  if (!new_category) $('.category-abbr').next(new_category);
});

$('.save-categories').click(function(e) {
  e.preventDefault();
  var categories = {'categories': {}};
  var category_id = $(this).parent().attr('id');
  
  $(this).parent().children('.add-category').each(function() {
    var color = $(this).find('.colorPickSelector').css('color');
    if (category_id === 'roles') {
      var verbose_name = $(this).find('.category-name').val();
      var short_name = $(this).find('.category-abbr').val();
      categories['categories'][verbose_name] = {
        'color': color,
        'short_name': short_name,
      };
    } else if (category_id == 'location') {
      var category = $(this).find('.category-name').val();
      categories['categories'][category] = {
        'color': color,
      };
    }
  });
  categories = JSON.stringify(categories);
  var context = {
    categories: categories,
    category_id: category_id
  };
  if (category_id === 'roles') {
    $.post( "/company/roles/", context);
  } else if (category_id === 'location') {
    $.post( "/company/location/", context);
  }
  
});