requirejs({
  paths: {
    'jquery.cookie': '++resource++unep/jquery.cookie'
  }
});

require([
  'jquery',
  'jquery.cookie'
], function($) {

  $('#unep-language a').each(function(i, el) {
    $(el).on('click', function(e) {
      e.preventDefault();
      $.cookie('unep-language', $(el).parent().attr('id').substr(-2), { path: '/' });
      window.location.reload();
    });
  });

});
 /* $(document).ready(function(){  

  $('#unep-language a').each(function(i, el) {
    $(el).on('click', function(e) {
      e.preventDefault();
      $.cookie('unep-language', $(el).parent().attr('id').substr(-2), { path: '/' });
      window.location.reload();
                                          });
                                 });

                            });
*/
