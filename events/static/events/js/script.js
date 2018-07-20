// $(document).ready(function() {
//     $(".js-example-basic-single").select2({
//         placeholder: "Select Employee",
//         allowClear: true,
//     });
// });


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


// $(function() {
//   var myvar = $("#201-P-MG").val();
//   console.log(myvar + 'hello!');
//   var employee = document.getElementById("201-P-MG");
//   employee.options[employee.options.selectedIndex].selected = true;
// });
var dict = {};

$('select').on('change', function() {
  var employee = this.value;
  var position = $(this).closest('select').attr('value');
  var location = $(this).closest('.location-body').attr('id')
  dict[location] = [position, employee];
})