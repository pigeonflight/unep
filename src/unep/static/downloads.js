requirejs({
  paths: {
    'jquery.collapse': '++resource++unep/jquery.collapse',
    'jquery.cookie': '++resource++unep/jquery.cookie',
  }
});

require([
  'jquery',
  'jquery.cookie',
  'jquery.collapse'
], function($) {

  var collapse = new jQueryCollapse($('#meeting-downloads'));

  $('#meeting-downloads').find('input[type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[type="checkbox"]:checked').size());

    });

});
