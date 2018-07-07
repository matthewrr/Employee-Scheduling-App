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
    var newRow = document.getElementById("new-employee");
    $('#' + myparent).append(newRow)
  });
});


$(document).ready(function() {
  $('.remove-employee').click(function(){
    var target = $(this).attr('id')
    var els = document.getElementsByClassName(target);
    for(var i=0; i<els.length; ++i){
      var s = els[i].style;
      s.display = s.display==='none' ? 'inline-block' : 'none';
    }
  });
});