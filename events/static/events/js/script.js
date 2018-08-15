$(function() {
  $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
});

function myFunction() {
    
  var input, filter, table, tr, td, td2, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    td2 = tr[i].getElementsByTagName("td")[2];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1 || td2.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}

$(function() {
  var btn_id = '';
  var table = '';
  var loadForm = function () {
    var btn = $(this);
    console.log(btn_id);
    console.log("working");
    table = '#' + $(this).closest('table').attr('id');
    console.log(table);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      
      beforeSend: function () {
        console.log("working #1")
        $("#modal-object .modal-content").html("");
        $("#modal-object").modal("show");
      },
      success: function (data) {
        console.log("working #2");
        $("#modal-object .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    console.log('first table is ' + table);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          
          if (table != '#undefined') {
            console.log('table is probably undefined: ' + table)
            $(table + " tbody").replaceWith(data.html_object_list);
          } else if (btn_id === 'events') {
            console.log('table is ' + table)
            console.log(data.html_object_list);
            $("#upcoming-events tbody").replaceWith(data.html_object_list);
          } else {
            $("#object-table tbody").replaceWith(data.html_object_list);
          }
          $("#modal-object").modal("hide");
        }
        else {
          console.log('form not valid');
          $("#modal-object .modal-content").html(data.html_form);
        }
      }
    });
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
  console.log(table_id);
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  if (!table_id) {
    table_id = 'object-table';
  }
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

// Generate Template
var template = {'locations': {}};
$(".generate-template" ).click(function() {
  var template_id = '';
  var title = $('.template-name').val();
  $('.location').each(function() {
    var location = $(this).html();
    var active = $(this).prev().prop('checked');
    template['locations'][location] = active;
  });
  template['title'] = title;
  context = { template: JSON.stringify(template), template_id: template_id, title: title };
  
  var mydata = ''
  $.post( "/schedules/templates/create/generate/", context, function( data ) {
    $('.schedule-cards').html(data);
  });
});



$(".choose-template" ).click(function() {
  var category = $('#template-subcategory').children('option:selected').attr('id');
  $.post( "/schedules/templates/create/modal/", {category: category}, function( data ) {
      $('.modal-body').html(data);
  });
});

$(".update-template" ).click(function() {
  var pk = $('.modal-body').find('.active').attr('id');
  var category = $('#template-subcategory').children('option:selected').attr('id');
  context = {category: category, pk: pk};
  $.post( "/schedules/templates/create/select/", context, function( data ) {
      // $('.modal-body').html(data);
      $('.schedule-cards').html(data);
  });
});


// var template = {'locations': {}};
// $(".generate-template" ).click(function() {
//   var template_id = '';
//   var title = $('.template-name').val();
//   $('.location').each(function() {
//     var location = $(this).html();
//     var active = $(this).prev().prop('checked');
//     template['locations'][location] = active;
//   });
//   template['title'] = title;
//   context = { template: JSON.stringify(template), template_id: template_id, title: title };
  
//   var mydata = ''
//   $.post( "/schedules/templates/create/generate/", context, function( data ) {
//     $('.schedule-cards').html(data);
//   });
// });




// Submit/Update Schedule
var dict = {};
$(".submit-schedule" ).click(function(e) {
  e.preventDefault();
  var template = false;
  var event_id = $('.event-title').attr('id');
  var title = $('.template-name').val()
  if (title) {
    template = true;
  }
  console.log('template is ' + template);
  
  $('.location-body').each(function() {
    var positions = $(this).find('select');
    var scheduled = $(positions).children('option:selected');
    var bar = ($(this).prev().children().children().first().attr('name') === 'bar');
    var active = !$(this).prev().children('label').hasClass('collapsed');
    
    var d = {
      'positions': {},
      'active': active,
      'bar': bar,
      'location':$(this).attr('name'),
    }
    
    $(positions).each(function(i,v){
      var arrive = $(this).next().children().val();
      var position = $(v).children().first().attr('class');
      var person = scheduled[i];
      d['positions'][position] = {
        'arrival_time': arrive,
        'employee': $(person).val()
      }
    })
    dict[$(this).attr('id')] = d;
  });
  
  $.ajax({
     type:"POST",
     url:"/schedules/templates/create/save/",
     dataType: 'json',
     data: { roster: JSON.stringify(dict), event_id: event_id, title: title, template: template, },
     success: function(){
         console.log(dict) 
    }
  });
})


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
$(document).ready(function(){
	$('#managers').on("click", function(){
    var arrival_time = $(this).parent().prev().children().val();
    $('.M').val(arrival_time);
  });
  $('#preps').on("click", function(){
    var arrival_time = $(this).parent().prev().children().val();
    $('.P').val(arrival_time);
  });
  $('#cashiers').on("click", function(){
    var arrival_time = $(this).parent().prev().children().val();
    $('.C').val(arrival_time);
  });
  $('#bartenders').on("click", function(){
    var arrival_time = $(this).parent().prev().children().val();
    $('.B').val(arrival_time);
  });
});

$(".template-header > .save").click(function() {
  $('.template-name').prop('readonly', true);
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
	  new_employee.find('.template-placeholder').attr('placeholder','Extra #' + i);
	  new_employee.find('input').attr('value','');
	  $(card_body).append(new_employee);
	});
});



var template_category = $('#template-category');
var template_subcategory = $( '#template-subcategory' );
var options = template_subcategory.find( 'option' );
    
$(template_category).on('change', function() {
  var val = this.value
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
  

	$(template_subcategory).html(
	  $(options).filter( '[value="' + val + '"]' ) 
	);
}).trigger('change');

$('.company-roles').on('click', '.add-role-button', function() { 
    var new_role = $('.add-role').last().clone();
    $(this).remove()
    $(new_role).find('input').val('');
    $('.company-roles').append(new_role);
});

$('.company-roles').on('click', '.remove-role-button', function() { 
  var myvar = $(this).parent().parent().parent();
  var new_role = $('.add-role');
  $(myvar).remove();
  if (!new_role) {
    $('.role-abbr').next(new_role);
  }
});

$('#save-roles').click(function() {
  var roles = {'roles': {}}
  $('.add-role').each(function() {
    var verbose_name = $(this).find('.role-name').val();
    var short_name = $(this).find('.role-abbr').val();
    roles['roles'][verbose_name] = short_name;
  });
  roles = JSON.stringify(roles)
  
  
  $.post( "/company/roles/", {roles: roles}, function(data) {
    console.log('hello');
  });
  
});
// { roster: JSON.stringify(dict), event_id: event_id, title: title, template: template, },
// context = { template: JSON.stringify(template), template_id: template_id, title: title };

// 'values' : JSON.stringify(values)
