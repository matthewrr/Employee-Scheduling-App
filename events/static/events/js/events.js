/*global $*/

// Control Panel
$(document).ready(function () {
  $(".check-all").click(function(){
      $(this).parent().siblings().find('input:checkbox').not(this).prop('checked', this.checked);
  });
  $(".location-checkbox:input[type=checkbox]").each(function () {
      var location = $(this).parent().parent().prev();
      $(this).change(function() {
         $(this).change(updateCount(location));
      });
  });

  updateCount(l = false);

  function updateCount (l = false) {
    if (!l) {
      var locationCategories = $('.location-category');
      $(locationCategories).each(function() {
        var count = $(this).next().find(".check-one:input[type=checkbox]:checked").length;
        
        $(this).find(".active-count").text(count);
      });
    } else {
      var count = $(l).next().find(".check-one:input[type=checkbox]:checked").length;
      $(l).find(".active-count").text(count);
    }
  }
});