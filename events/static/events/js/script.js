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




function loadPositions(l) {
  // var l ='';
  // var l = location;
// $('body').on('click', '.js-update-object', function() { 
  
  // l = $(this).parent().parent().children().first().html();
    
    var context = {location: l};
    console.log(context);
    $.get( "/locations/create/positions/", context, function(data) {
        p = JSON.parse(data);
        var positions = {};
        Object.keys(p).map(function(k,t) {
          positions[k] = p[k]
        });
        console.log('positions:')
        console.log(positions)
        for (var short_name in positions) {
          var p = short_name.replace(/[0-9]/g, '');
          var verbose_name = positions[short_name];
          var c = '.'+p+'-container';
          
          console.log('verbose is: ')
          console.log(verbose_name);
          var insertion = $('.d-none').children().clone();
          
          $(insertion).find('.short-name').html(short_name);
          $(insertion).find('.short-name').attr('class', p)
          $(insertion).find('.verbose-name').html(verbose_name);
          
          $(c).append(insertion);
         
          console.log('hello');
          console.log(insertion)
          console.log('bye')
          
          
          
        }
          
    // });
});
// return $(insertion);
}






$(function() {
  var btn_id = '';
  var table = '';
  var loadForm = function () {
    var btn = $(this);
    console.log(btn);
    table = '#' + $(this).closest('table').attr('id');
    
    
    var l = $(btn).parent().parent().children().first().html();
    
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      
      beforeSend: function () {
        $("#modal-object .modal-content").html("");
        $("#modal-object").modal("show");
      },
      success: function (data) {
        $("#modal-object .modal-content").html(data.html_form);
        // $("#modal-object .modal-content").html(insertion);
        loadPositions(l);
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
          
          if (table != '#undefined') {
            $(table + " tbody").replaceWith(data.html_object_list);
          } else if (btn_id === 'events') {
            $("#upcoming-events tbody").replaceWith(data.html_object_list);
          } else {
            $("#object-table tbody").replaceWith(data.html_object_list);
          }
          $("#modal-object").modal("hide");
        }
        else {
          $("#modal-object .modal-content").html(data.html_form);
        }
      }
    });
    var location = $('#id_location_id').val();
    sendPositions(location);

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

function sendPositions(location) {
  var positions = {};
  
  $('.default-position').each(function() {
    var short_name = $(this).find('.input-group-prepend').children().html();
    var verbose_name = $(this).find('.verbose-name').html();
    if (short_name) {
      positions[short_name] = verbose_name;
      
    }
    console.log(positions);
    
  });
  positions = JSON.stringify(positions)
  context = {positions: positions, location: location}
  $.post( "/locations/create/positions/", context, function(data) {
      console.log('success, good sir!');
  });
  
}







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



function sendPositions(location) {
  var positions = {};
  
  $('.default-position').each(function() {
    var short_name = $(this).find('.input-group-prepend').children().html();
    var verbose_name = $(this).find('.verbose-name').html();
    if (short_name) {
      positions[short_name] = verbose_name;
      
    }
    console.log(positions);
    
  });
  positions = JSON.stringify(positions)
  context = {positions: positions, location: location}
  $.post( "/locations/create/positions/", context, function(data) {
      console.log('success, good sir!');
  });
  
}


$('.modal').on('click', '.add-role-button', function() { 
  var verbose_name = $(this).html();
  var ss = $(this).attr('id');
  var ll = $(this).html();
  
  var short_name = $(this).attr('id');
  
  var added_roles = $('.role-list').children();
  var count = $('.' + short_name).length;
  
  var num = (count += 1)
  
  if (count === 1) {
    short_name = short_name;
  } else if (count === 2) {
    short_name += num
    verbose_name += (' #' + num)
    var first_var = $('.' + ss).first();
    $(first_var).html(ss + '1');
    $(first_var).parent().next().html(ll + ' #1')
  } else {
    short_name += num
    verbose_name += (' #' + num)
  }
  
  var insertion = $('.d-none').children().clone();
  $(insertion).find('.short-name').html(short_name);
  $(insertion).find('.short-name').attr('class', ss)
  $(insertion).find('.verbose-name').html(verbose_name);
  
  var container = ss + '-container'
  
  $('.' + container).append(insertion)
   
});

$('.modal').on('click', '.remove-sub-role', function() {
  var short_id = $(this).prev().prev().children().attr('class');
  var target = $('.'+short_id);
  var verbose_name = $(this).prev().html();
  var v = verbose_name.split(" ").slice(0,-1).join(' ');
  $(this).parent().parent().parent().remove();
  var target = $('.'+short_id);
  if (target.length === 1) {
    target.html(short_id);
    target.parent().next().html(v);
  } else if (target.length > 1) {
    target.each(function(i) {
      $(this).parent().next().html(v+' #'+(i+1));
      $(this).html(short_id+(i+1));
    });
  }
});