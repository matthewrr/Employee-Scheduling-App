/*global $*/

$('#main-stands').addClass('show active');

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
      var locationCategories = $('.loc-category');
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
    var $header = $(this);
    var $content = $header.next();
    if ($content.hasClass('show')) {
        $content.removeClass('show');
        $content.slideUp(350);
        $header.children('.gradient').removeClass('gradient');
    } else {
        var $cp = $('#cp');
        $cp.find('li .inner').removeClass('show').slideUp(350);
        $cp.find('.gradient').removeClass('gradient');
        
        $content.toggleClass('show');
        $header.children().addClass('gradient');
        $content.slideToggle(350);
    }
});

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

// Highlight scheduled/unscheduled shifts
$('.highlight-shifts').change(function(){
  var category = $(this).attr('id');
  var shifts = (category === 'scheduled-shifts') ? $('.employee') : $('.default');
  $(shifts).each(function () {$(this).toggleClass('highlight');});
  $('.board-item').removeClass('highlight');
});

// Update arrival time by job title
$(".btn-arrival").click(function(){
  var category = $(".display-select option:selected").attr('id');
  var targets = $('.'+category);
  var time = $('.input-arrival').val();
  targets.val(time);
  $('.input-arrival').val('');
});

// Get list of employees for autocomplete
var dataList = $('#json-datalist');
$.post( "/employees/list/", function( employeeList ) {
  for (var employee in employeeList) {
    var option = document.createElement('option');
    option.value = employeeList[employee]['name'];
    option.classList.add(employeeList[employee]['id']);
    dataList.append(option);
  }
});