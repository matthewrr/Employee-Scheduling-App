$(document).ready(function() {
    $(".js-example-basic-single").select2({
        placeholder: "Select Employee",
        allowClear: true,
    });
});

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

$('#editEvent').on('shown.bs.modal', function () {
  $('#editEventInput').trigger('focus')
})


$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})


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


$(document).ready(function(){
  
  var pk = '';
  
  $('.edit-object').click(function(){
    pk = $(this).attr('id');
    var test = $('body');
    $(test).attr('id','hello');
    
    console.log('this is the edit-object function');
    console.log('pk is...');
    console.log(pk);
    console.log('-----------');
    
    $.ajax({
      url: '/events/edit/' + pk + '/',
      type: "GET",
      data: pk,
      success: function(data) {
        $('.modal-body-edit').append(data)
      }});
    
    var thing = $('.edit-submit').attr('id',pk)
      
      
  });


  $('.edit-submit').click(function(){

    console.log('this is the edit-submit function');
    console.log('pk is...');
    console.log(pk);
    console.log('-----------');
    
    $.ajax({
      url: '/events/edit/' + pk + '/',
      type: "POST",
      data: pk,
    });
  });
    
});

$(".object-edit").on("hidden.bs.modal", function () {
    $('.modal-body-edit').empty()
});



$(".js-create-event").click(function () {
  var btn = $(this);  // <-- HERE
  $.ajax({
    url: btn.attr("data-url"),  // <-- AND HERE
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#modal-event").modal("show");
    },
    success: function (data) {
      $("#modal-event .modal-content").html(data.html_form);
    }
  });
});

// $(function () {

//   $(".js-create-event").click(function () {
    
//     $.ajax({
//       url: '/events/myevents/create/',
//       type: 'get',
//       dataType: 'json',
//       beforeSend: function () {
//         $("#modal-event").modal("show");
//       },
//       success: function (data) {
//         $("#modal-event .modal-content").html(data.html_form);
//       }
//     });
    
//   });

// });

// $("#modal-event").on("submit", ".js-event-create-form", function () {
//     var form = $(this);
//     $.ajax({
//       url: form.attr("action"),
//       data: form.serialize(),
//       type: form.attr("method"),
//       dataType: 'json',
//       success: function (data) {
//         if (data.form_is_valid) {
//           alert("Event created!");  // <-- This is just a placeholder for now for testing
//         }
//         else {
//           $("#modal-event .modal-content").html(data.html_form);
//         }
//       }
//     });
//     return false;
//   });

$("#modal-event").on("submit", ".js-event-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#event-table tbody").html(data.html_event_list);  // <-- Replace the table body
          $("#modal-event").modal("hide");  // <-- Close the modal
        }
        else {
          $("#modal-event .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-event").modal("show");
      },
      success: function (data) {
        $("#modal-event .modal-content").html(data.html_form);
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
          $("#event-table tbody").html(data.html_event_list);
          $("#modal-event").modal("hide");
        }
        else {
          $("#modal-event .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create event
  $(".js-create-event").click(loadForm);
  $("#modal-event").on("submit", ".js-event-create-form", saveForm);

  // Update event
  $("#event-table").on("click", ".js-update-event", loadForm);
  $("#modal-event").on("submit", ".js-event-update-form", saveForm);

});