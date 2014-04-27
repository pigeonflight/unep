requirejs({
  paths: {
    'jquery.collapse': '++resource++unep/jquery.collapse'
  }
});

require([
  'jquery',
  'jquery.collapse'
], function($) {

  var collapse = new jQueryCollapse($('#meeting-texts'));
  $('#meeting-texts')
    .on('opened', function(e, section) {
      $(this)
        .find('h2')
        .each(function(i, el) {
          if ($(el).hasClass('open') && el !== section.$summary[0]) {
            section.parent.close(i);
          }
        });
    });

  $('#meeting-navigation a')
    .on('click', function(e) {
      if ($(this).attr('href').substr(0, 1) === '#') {
        e.preventDefault();
        var selected = $('#meeting-texts').find($(this).attr('href'));
        collapse.close();
        collapse.open($('#meeting-texts h2').index(selected));
        $(window).scrollTop(selected.offset().top);
      }
    });
});
