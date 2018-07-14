$(document).ready(function() {
    $(".js-example-basic-single").select2({
        placeholder: "Select Employee",
        allowClear: true,
    });
});


// $(".modal").on("hidden.bs.modal", function(){
//     $(".modal-content").html("");
// });

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
  
  var table = '';
  var loadForm = function () {
    var btn = $(this);
    table = '#' + $(this).closest('table').attr('id');
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
            $(table + " tbody").replaceWith(data.html_event_list);
          } else {
            console.log('table is ' + table)
            console.log(data.html_event_list);
            $("#upcoming-events tbody").replaceWith(data.html_event_list);
            
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
  $("#modal-object").on("submit", ".js-object-update-form", saveForm);
  
  // Delete
  $("#upcoming-events").on("click", ".js-delete-object", loadForm);
  $("#previous-events").on("click", ".js-delete-object", loadForm);
  $("#modal-object").on("submit", ".js-object-delete-form", saveForm);

});