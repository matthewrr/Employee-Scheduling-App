/*global $*/
$(function() {$('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');});

// CRUD Objects
$(function() {
  var location = ($('.title') === 'location');
  var loadForm = function () {
    $.ajax({
      url: $(this).attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-object .modal-content").html("");
        $("#modal-object").modal("show");
      },
      success: function (data) {
        $("#modal-object .modal-content").html(data.html_form);
        if (location) loadPositions($(this).parent().parent().children().first().html());
      }
    });
  };
  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          var table = '#' + $(this).closest('table').attr('id');
          $(table + " tbody").replaceWith(data.html_object_list);
          $("#modal-object").modal("hide");
        } else {
          $("#modal-object .modal-content").html(data.html_form);
        }
      }
    });
    
    if (location) sendPositions($('#id_location_id').val());
    
    var loc_id = $('#id_location_id');
    if (loc_id && !location) sendPositions($('#id_location_id').val());
    
    return false;
  };
  // Create
  $(".js-create-object").click(loadForm);
  $("#modal-object").on("submit", ".js-object-create-form", saveForm);
  // Update
  $("#upcoming-events").on("click", ".js-update-object", loadForm);
  $("#previous-events").on("click", ".js-update-object", loadForm);
  $("#object-table").on("click", ".js-update-object", loadForm);
  $("#modal-object").on("submit", ".js-object-update-form", saveForm);
  // Delete
  $("#upcoming-events").on("click", ".js-delete-object", loadForm);
  $("#previous-events").on("click", ".js-delete-object", loadForm);
  $("#object-table").on("click", ".js-delete-object", loadForm);
  $("#modal-object").on("submit", ".js-object-delete-form", saveForm);
});

// Sort Columns
function sortTable(n,table_id) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  if (!table_id) table_id = 'object-table';
  table = document.getElementById(table_id);
  switching = true;
  dir = "asc"; 
  while (switching) {
    switching = false;
    rows = table.getElementsByTagName("TR");
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++; 
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}



// Submit/Update Schedule
var dict = {};
$('.roster-body').on('click', '.submit-schedule', function(e) { 
  e.preventDefault();
  var event_id = $('.event-title').attr('id');
  var title = $('.template-name').val();
  var pk = $('.template-name').attr('id');
  var template = title ? true : false;
  $('.location-body').each(function() {
    var positions = $(this).find('select');
    var scheduled = $(positions).children('option:selected');
    var bar = ($(this).prev().children().children().first().attr('name') === 'bar');
    var active = !$(this).prev().children('label').hasClass('collapsed');
    var id = $(this).attr('id');
    var d = {
      'positions': {},
      'active': active,
      'bar': bar,
      'location':$(this).attr('name'),
      'id': id,
    };
    $(positions).each(function(i,v){
      var arrive = $(this).next().children().val();
      var position = $(v).children('.default-position').attr('value');
      var person = scheduled[i];
      var employee = '';
      var verbose_name = '';
      verbose_name = $(this).find('.default-position').html();
      console.log(position)
      var attr = $(person).attr('default')
      if (typeof attr !== typeof undefined && attr !== false) {
        employee = '';
        // verbose_name = $(v).children().first().html();
      } else {
        
        employee = $(person).val();
      }
      d['positions'][position] = {
        'arrival_time': arrive,
        'employee': employee,
        'verbose_name': verbose_name
      };
    });
    id = $(this).attr('id');
    dict[id] = d;
    
  });
  var context = {roster:JSON.stringify(dict), event_id:event_id, title:title, template:template, pk:pk };
  $.post("/schedules/templates/create/save/", context);
});


$(template_category).on('change', function() {
  var template_category = $('#template-category');
  var template_subcategory = $( '#template-subcategory' );
  var options = template_subcategory.find( 'option' );
  var val = this.value;
  if (val === '2' || val === '3') {
    $(template_subcategory).removeAttr('disabled');
    $('.choose-template').removeAttr('disabled');
  } else if (val === '0') {
    $('.choose-template').attr('disabled','disabled');
    $(template_subcategory).attr('disabled','disabled');
  } else {
    $('.choose-template').removeAttr('disabled');
    $(template_subcategory).attr('disabled','disabled');
  }
	$(template_subcategory).html($(options).filter( '[value="'+val+'"]') );
}).trigger('change');

function sendPositions(location_id) {
  var positions = {};
  $('.default-position').each(function() {
    var short_name = $(this).find('.input-group-prepend').children().html();
    var verbose_name = $(this).find('.verbose-name').html();
    if (short_name) positions[short_name] = verbose_name;
  });
  positions = JSON.stringify(positions);
  console.log(positions);
  var category = $('.category-select option:selected').text();
  
  var context = {positions: positions, location_id: location_id, category: category};
  $.post("/locations/create/positions/", context);
}

$('.modal').on('click', '.add-role-button', function() { 
  
  var insertion = $('.d-none').children().clone();
  var short = $(insertion).find('.short-name');
  var short_name = $(this).attr('id');
  var verbose_name = $(this).html();
  short.addClass(short_name);
  short.attr('value', short_name);
  
  var count = $('.role-list').find('.' + short_name).length;
  var num = (count += 1);
  var container = short_name + '-container';
  if (count === 2) {
    var first_var = $('.' + short_name).first();
    $(first_var).html(short_name + '1');
    short_name += num;
    $(first_var).parent().next().html(verbose_name + ' #1');
    verbose_name += (' #' + num);
  } else if (count > 2) {
    short_name += num;
    verbose_name += (' #' + num);
  }
  short.html(short_name);
  $(insertion).find('.verbose-name').html(verbose_name);
  $(insertion).find('.verbose-name').attr('placeholder', verbose_name);
  $('.' + container).append(insertion);
  
});

$('.modal').on('click', '.remove-sub-role', function() {
  var short_id = $(this).parent().parent().prev().prev().children().attr('value');
  var verbose_name = $(this).parent().parent().prev().attr('placeholder');
  var v = verbose_name.split(" ").slice(0,-1).join(' ');
  if (v.length === 0) v = verbose_name
  $(this).parent().parent().parent().parent().parent().remove();
  var target = $('.'+short_id);
  if (target.length === 1) {
    target.html(short_id);
    var content = v ? v.slice(0) : v.slice(verbose_name);
    target.parent().next().html(content);
  } else if (target.length > 1) {
    target.each(function(i) {
      var content = v ? (v+' #'+(i+1)) : (verbose_name+' #'+(i+1));
      $(this).parent().next().html(content);
      $(this).html(short_id+(i+1));
    });
  }
});

$('.roster-body').on('click', '.submit-template', function(e) { 
  e.preventDefault();
  var event_id = $('.event-title').attr('id');
  var title = $('.template-name').val();
  var pk = $('.template-name').attr('id');
  var template = true;
  $('.location-body').each(function() {
    var positions = $(this).children();
    var bar = ($(this).prev().children().children().first().attr('name') === 'bar');
    var active = !$(this).prev().children('label').hasClass('collapsed');
    var id = $(this).attr('id');
    var d = {
      'positions': {},
      'active': active,
      'bar': bar,
      'location':$(this).attr('name'),
      'id': id,
    };
    $(positions).each(function(){
      var position = $(this).find('.short-name').html();
      var verbose_name = $(this).find('.verbose-name').html();
      d['positions'][position] = {
        'arrival_time': '',
        'employee': '',
        'verbose_name': verbose_name
      };
    });
    id = $(this).attr('id');
    dict[id] = d;
  });
  var context = {roster:JSON.stringify(dict), event_id:event_id, title:title, template:template, pk:pk };
  $.post("/schedules/templates/create/save/", context);
});