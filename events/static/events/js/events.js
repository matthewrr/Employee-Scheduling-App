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

// $('.nav-item a').on('click', function (e) {
//   e.preventDefault()
//   var targetID = $(this).attr('href');
//   console.log(targetID);
//   $(targetID).addClass('show');
  
  
//   // $('#myTab a[href="#profile"]').tab('show')
//   // $(tar).tab('show')
// })

// $('#myTab a[href="#profile"]').tab('show')

// $(function () {
//     function showSlide(n) {
//         $('body').unbind('mousewheel');
//         currSlide += n;
//         currSlide = currSlide <= 0 ? 0 : currSlide >= $slide.length - 1 ? $slide.length - 1 : currSlide;
//         var displacment = window.innerWidth * currSlide;
//         $('.slides').css('transform', 'translateX(-' + displacment + 'px)');
//         setTimeout(function () {
//             $('body').bind('mousewheel', mouseEvent);
//         }, 800);
//         $('.location-categories a.active').removeClass('active');
//         $($('a')[currSlide]).addClass('active');
//     }
//     function mouseEvent(e, delta) {
//         showSlide(delta >= 0 ? 1 : -1);
//         e.preventDefault();
//     }
//     $('.location-categories a').click(function (e) {
//         var newslide = parseInt($(this).attr('href')[1]);
//         var diff = newslide - currSlide - 1;
//         showSlide(diff);
//         e.preventDefault();
//     });
//     $(window).resize(function () {
//         var displacment = window.innerWidth * currSlide;
//         $('.slides').css('transform', 'translateX(-' + displacment + 'px)');
//     });
//     var currSlide = 0;
//     var $slide = $('.slide');
//     $($('.location-categories a')[0]).addClass('active');
//     $('body').bind('mousewheel', mouseEvent);
// });


$("document").ready(function(){
    $(".control-panel-item").hover(function(){
      // var myparent = $(this);
      var showing = $(this).find('.list-group.inner').hasClass('show');
      if (!showing) {
        $(this).find('.toggle').children().toggleClass('gradient');
        // $(this).find('.panel-icon').toggleClass('gradient');
        // $(myparent).find('.toggle').children().toggleClass('gradient');
        
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