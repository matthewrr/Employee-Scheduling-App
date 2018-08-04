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
  
  $('.active-location').prop('indeterminate', true)
  
  $('.add-employee').click(function(){
    var myparent = $(this).parent().prop('className');
    var newRow = document.getElementById("new-employee");
    $('#' + myparent).append(newRow)
  });
});

$(function() {
  $('.remove-employee').click(function(){
    var target = $(this).attr('id')
    var els = document.getElementsByClassName(target);
    for(var i=0; i<els.length; ++i){
      var s = els[i].style;
      s.display = s.display==='none' ? 'inline-block' : 'none';
    }
  });
});

// $(".object-edit").on("hidden.bs.modal", function () {
//     $('.modal-body-edit').empty()
// });

// $(".js-create-object").click(function () {
//   var btn = $(this);  // <-- HERE
//   $.ajax({
//     url: btn.attr("data-url"),  // <-- AND HERE
//     type: 'get',
//     dataType: 'json',
//     beforeSend: function () {
//       $("#modal-object").modal("show");
//     },
//     success: function (data) {
//       $("#modal-object .modal-content").html(data.html_form);
//     }
//   });
// });


// $("#modal-object").on("submit", ".js-object-create-form", function () {
//     var form = $(this);
//     $.ajax({
//       url: form.attr("action"),
//       data: form.serialize(),
//       type: form.attr("method"),
//       dataType: 'json',
//       success: function (data) {
//         if (data.form_is_valid) {
//           console.log(data);
//           $(".redbull").parent().html(data.html_event_list);  // <-- Replace the table body
//           $("#modal-object").modal("hide");  // <-- Close the modal
//           $('body').removeClass('modal-open');
//           $('.modal-backdrop').remove();
//           $('.modal').removeData('bs.modal');
//           $('.modal').empty();
//           $('.modal').removeAttr('style');
          
         
//         }
//         else {
//           $("#modal-object .modal-content").html(data.html_form);
//         }
//       }
//     });
//     return false;
//   });

$(function() {
  
});

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
  
  /* Binding */

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





// collect value on change
// $('select').on('change', function() {
//   var employee = this.value;
//   var position = $(this).closest('select').attr('value');
//   var location = $(this).closest('.location-body').attr('id')
//   dict[location] = [position, employee];
// })


$(document).ready(function() {
       $("#test").submit(function(event){
            $.ajax({
                 type:"POST",
                 url:"/edit_favorites/",
                 data: {
                        'video': $('#test').val() // from form
                        },
                 success: function(){
                     $('#message').html("<h2>Contact Form Submitted!</h2>") 
                 }
            });
            return false; //<---- move it here
       });

});

var dict = {};
$(".submit-schedule" ).click(function() {
  var event_id = $('.event-title').attr('id');
  
  $('.location-body').each(function() {
    var location = $(this).attr('id');
    var positions = $(this).find('select');
    var scheduled = $(positions).children('option:selected');
    var posDict = {};
    
    $(positions).each(function(i,v){
      var position = $(v).children().first().attr('class');
      var person = scheduled[i];
      posDict[position] = $(person).val();
    })
    dict[location] = posDict;
  });
  
  
  $.ajax({
     type:"POST",
     url:"/events/update_schedule/",
     data: { schedule: JSON.stringify(dict), event_id: event_id },
     success: function(){
         console.log(dict) 
    }
  });
})




  
$(document).ready(function(){
	$('.toggle-unscheduled').on("click", function(){
      	$('.unscheduled').toggle();
    });
}); 

$(document).ready(function(){
	$('.toggle-scheduled').on("click", function(){
      	$('.scheduled').toggle();
    });
}); 
$(document).ready(function(){
	$('.toggle-inactive-locations').on("click", function(){
	      $('.location-title.collapsed').each(function(){
	        $(this).parent().parent().toggle();
	      });
    });
}); 

$(document).ready(function(){
	$('.toggle-bars').on("click", function(){
	  $('.bar').each(function(){
	    $(this).prop('indeterminate', false);
	    var flag = $(this).is(':checked');
	    $(this).prop('checked', !flag);
	    $(this).parent().parent().parent().toggle();
	      
	    });
	  
	    
	  });
	      
  });

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

