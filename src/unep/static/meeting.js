requirejs({
  paths: {
    'jquery.collapse': '++resource++unep/jquery.collapse'
  }
});

require([
  'jquery',
  'jquery.collapse'
], function($) {

  $('#meeting-texts')
    .collapse()
    .on('opened', function(e, section) {
      $(this)
        .find('h2')
        .each(function(i, el) {
          if ($(el).hasClass('open') && el !== section.$summary[0]) {
            section.parent.close(i);
          }
        });
    });

});
