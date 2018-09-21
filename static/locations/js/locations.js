/*global $*/
// load positions in modal
function loadPositions(l) {
  if ($('.modal-title').html() === 'Update location') {
    var context = {location: l};
    $.get( "/locations/create/positions/", context, function(data) {
      p = JSON.parse(data);
      var positions = {};
      Object.keys(p).map(function(k,t) {
        positions[k] = p[k];
      });
      for (var short_name in positions) {
        var p = short_name.replace(/[0-9]/g, '');
        var verbose_name = positions[short_name];
        var c = '.'+p+'-container';
        var insertion = $('.d-none').children().clone();
        $(insertion).find('.short-name').html(short_name);
        $(insertion).find('.short-name').addClass(p);
        $(insertion).find('.verbose-name').html(verbose_name);
        $(c).append(insertion);
      }
    });
  }
}