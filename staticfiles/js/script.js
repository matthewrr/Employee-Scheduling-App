/*global $*/
// Navbar: set active link
$(function() {$('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');});

// Location App: load positions
function loadPositions(l) {
  if ($('.modal-title').html() === 'Update location') {
    var context = {location: l};
    $.get( "/locations/create/positions/", context, function(data) {
      p = JSON.parse(data);
      var positions = {};
      Object.keys(p).map(function(k,t) {
        positions[k] = p[k];
      });
      for (var short_name in positions) {
        var p = short_name.replace(/[0-9]/g, '');
        var verbose_name = positions[short_name];
        var c = '.'+p+'-container';
        var insertion = $('.d-none').children().clone();
        $(insertion).find('.short-name').html(short_name);
        $(insertion).find('.short-name').addClass(p);
        $(insertion).find('.verbose-name').html(verbose_name);
        $(c).append(insertion);
      }
    });
  }
}

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
// {'locations': {'10': {'active': False},
// Generate Template
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

// Submit/Update Schedule
var dict = {};
$('.roster-body').on('click', '.submit-schedule', function(e) { 
  e.preventDefault();
  var event_id = $('.event-title').attr('id');
  var title = $('.template-name').val();
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
      var position = $(v).children().first().attr('class');
      var person = scheduled[i];
      var employee = '';
      // var employee = ($(person).val() === $(person).attr('.class'));
      var attr = $(person).attr('default')
      if (typeof attr !== typeof undefined && attr !== false) {
        employee = '';
      } else {
        
        employee = $(person).val();
      }
      console.log(employee);
      d['positions'][position] = {
        'arrival_time': arrive,
        'employee': employee
      };
    });
    id = $(this).attr('id');
    dict[id] = d;
  });
  var context = {roster:JSON.stringify(dict), event_id:event_id, title:title, template:template };
  $.post("/schedules/templates/create/save/", context);
});

// Control Panel Toggles
$(document).ready(function(){
	$('.toggle-unscheduled').on("click", function(){
    $('.unscheduled').toggle();
  });
  $('.toggle-scheduled').on("click", function(){
    $('.scheduled').toggle();
  });
  $('.toggle-inactive-locations').on("click", function(){
	  $('.location-title.collapsed').each(function(){
	    $(this).parent().parent().toggle();
	  });
  });
  $('.toggle-bars').on("click", function(){
	  $('.bar').each(function(){
	    var flag = $(this).is(':checked');
	    $(this).prop('indeterminate', false);
	    $(this).prop('checked', !flag);
	    $(this).parent().parent().parent().toggle();
    });
  });
}); 

// Control Panel Arrival Times
$('.update-role').on("click", function(){
  var target = $(this).attr('id')[0].toUpperCase();
  var arrival_time = $(this).parent().prev().children().val();
  $('.'+target).val(arrival_time);
});

$(".template-header > .edit").click(function() {
  $('.template-name').prop('readonly', false);
});

// Add/Remove Employees
$(function() {
  $('.schedule-cards').on('click', '.remove-employee', function(event) { 
	  var shift = $(this).parent().next().find('.arrival-time');
	  $(this).toggleClass('rotate');
	  $(shift).each(function() {
	    var delete_button = $(this).next();
	    $(delete_button).toggleClass('display-flex');
	    $(this).toggle();
      $(this).prev().toggleClass('red-border');
      $(this).prev().prev().children().toggleClass('red-border-background');
	  });
	});
	$('.schedule-cards').on('click', '.remove-button', function(event) { 
	  $(this).parent().parent().parent().remove();
  });
  $('.schedule-cards').on('click', '.add-employee', function(event) { 
	  var card_body = $(this).parent().next();
	  var new_position = $(card_body).children().last().find('span').html();
	  var prefix = new_position.split('')[0];
	  var i = Number(new_position.split('')[1]);
	  if (prefix !== 'E') {
	    new_position = 'E1';
	    i = 1;
	  } else {
	    i += 1;
	    new_position = 'E' + i;
	  }
	  var new_employee = $(card_body).children().first().clone();
	  new_employee.find('span').html(new_position);
	  new_employee.find('option').first().html('Extra #' + i);
	  new_employee.find('option').first().attr('value','Extra #' + i);
	  new_employee.find('option').first().attr('class',new_position);
	  new_employee.find('.template-placeholder').attr('placeholder','Extra #' + i);
	  new_employee.find('input').attr('value','');
	  $(card_body).append(new_employee);
	});
});

var template_category = $('#template-category');
var template_subcategory = $( '#template-subcategory' );
var options = template_subcategory.find( 'option' );
$(template_category).on('change', function() {
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

$('.company-roles').on('click', '.add-role-button', function() { 
    var new_role = $('.add-role').last().clone();
    $(this).remove();
    $(new_role).find('input').val('');
    $('.company-roles').append(new_role);
});
$('.company-roles').on('click', '.remove-role-button', function() { 
  var myvar = $(this).parent().parent().parent();
  var new_role = $('.add-role');
  $(myvar).remove();
  if (!new_role) $('.role-abbr').next(new_role);
});

$('#save-roles').click(function() {
  var roles = {'roles': {}};
  $('.add-role').each(function() {
    var verbose_name = $(this).find('.role-name').val();
    var short_name = $(this).find('.role-abbr').val();
    roles['roles'][verbose_name] = short_name;
  });
  roles = JSON.stringify(roles);
  $.post( "/company/roles/", {roles: roles});
});

function sendPositions(location) {
  var positions = {};
  $('.default-position').each(function() {
    var short_name = $(this).find('.input-group-prepend').children().html();
    var verbose_name = $(this).find('.verbose-name').html();
    if (short_name) positions[short_name] = verbose_name;
  });
  positions = JSON.stringify(positions);
  var context = {positions: positions, location: location};
  $.post("/locations/create/positions/", context);
}

$('.modal').on('click', '.add-role-button', function() { 
  var verbose_name = $(this).html();
  var ss = $(this).attr('id');
  var ll = $(this).html();
  var short_name = $(this).attr('id');
  var count = $('.' + short_name).length;
  var num = (count += 1);
  var container = ss + '-container';
  if (count === 1) {
    short_name = short_name;
  } else if (count === 2) {
    short_name += num;
    verbose_name += (' #' + num);
    var first_var = $('.' + ss).first();
    $(first_var).html(ss + '1');
    $(first_var).parent().next().html(ll + ' #1');
  } else {
    short_name += num;
    verbose_name += (' #' + num);
  }
  var insertion = $('.d-none').children().clone();
  var short = $(insertion).find('.short-name');
  short.html(short_name);
  short.addClass(ss);
  short.attr('value', ss);
  $(insertion).find('.verbose-name').html(verbose_name);
  $(insertion).find('.verbose-name').attr('placeholder', verbose_name);
  $('.' + container).append(insertion);
});

$('.modal').on('click', '.remove-sub-role', function() {
  var short_id = $(this).parent().parent().prev().prev().children().attr('value');
  var verbose_name = $(this).parent().parent().prev().attr('placeholder');
  var v = verbose_name.split(" ").slice(0,-1).join(' ');
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