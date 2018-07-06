// In your Javascript (external .js resource or <script> tag)
$(document).ready(function() {
    $(".js-example-basic-single").select2({
        placeholder: "Select Employee",
        allowClear: true,
    });
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
    $('#' + myparent).append("<div class='row mb-0'><div class='col col-12'><input type='text' class='form-control float-right' placeholder='Stuff here'></div></div>");
  });
});

$(function() {
  $('.remove-employee').click(function(){
    var myparent = $(this).parent().prop('className');
    $('#' + myparent).append("<div class='row mb-0'><div class='col col-12'>Hello!!!</div></div>");
  });
});