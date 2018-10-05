/*global $*/

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


$("document").ready(function(){
    $(".control-panel-item").hover(function(){
      var showing = $(this).find('.list-group.inner').hasClass('show');
      if (!showing) {
        $(this).find('.toggle').children().toggleClass('gradient');
      }
    });
});

$('.toggle').click(function(e) {
  	e.preventDefault();
  
    var $this = $(this);
  
    if ($this.next().hasClass('show')) {
        $this.next().removeClass('show');
        $this.next().slideUp(350);
        $this.children('.gradient').removeClass('gradient');
    } else {
        $this.parent().parent().parent().find('li .inner').removeClass('show');
        $this.parent().parent().parent().find('.gradient').removeClass('gradient');
        $this.parent().parent().parent().find('li .inner').slideUp(350);
        
        $this.next().toggleClass('show');
        $this.children().addClass('gradient');
        $this.next().slideToggle(350);
    }
});


//update to redo muuri layout
$('.location-checkbox').change(function(){
  var target = '#' + $(this).attr('target');
  var check_all = $(this).hasClass('check-all');
  
  if($(this).prop('checked')) {
    $(target).show();
    if (check_all) {
      var locations = $(this).parent().siblings().children().first();
      $(locations).each(function() {
        $(this).prop( "checked", true );
        var target = '#' + $(this).attr('target');
        $(target).show();
      })
    }
    
  } else {
    $(target).hide();
    if (check_all) {
      var locations = $(this).parent().siblings().children().first();
      $(locations).each(function() {
        $(this).prop( "checked", false );
        var target = '#' + $(this).attr('target');
        $(target).hide();
      })
    }
  }
});

$('.highlight-shifts').change(function(){
  var category = $(this).attr('id');
  var shifts = (category === 'scheduled-shifts') ? $('.highlight-employee') : $('.highlight-default');
  $(shifts).each(function () {
    $(this).toggleClass('highlight');
  });
});