/*global $*/

$(".generate-template" ).click(function() {
  var template = {'locations': {}};
  var title = $('.template-name').val();
  $('.location').each(function() {
    var location = $(this).attr('id');
    var active = $(this).prev().prop('checked');
    template['locations'][location] = {
      'active': active,
      'bar': '',
      'id': '',
      'location': '',
      'positions': {},
      'scheduled': 0
    };
  });
  template['title'] = title;
  var context = { template:JSON.stringify(template), title:title, new_template: true };
  $.post( "/schedules/templates/create/generate/", context, function( data ) {
    $('.schedule-cards').html(data);
  });
});

$(".choose-template" ).click(function() {
  var category = $('#template-subcategory').children('option:selected').attr('id');
  $.post( "/schedules/templates/create/modal/", {category: category}, function( data ) {
      $('.modal-body').html(data);
  });
  $("#modal-object").modal("hide");
});

$(".update-template" ).click(function() {
  var pk = $('.modal-body').find('.active').attr('id');
  var category = $('#template-subcategory').children('option:selected').attr('id');
  var context = {category: category, pk: pk};
  $.post( "/schedules/templates/create/select/", context, function( data ) {
      $('.schedule-cards').html(data);
  });
  $(".modal").modal("hide");
});