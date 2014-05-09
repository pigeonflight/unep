requirejs({
  paths: {
    'jquery.collapse': '++resource++unep/jquery.collapse'
  }
});

require([
  'jquery',
  'jquery.collapse'
], function($) { 
  var collapse = new jQueryCollapse($('#meeting-texts'), { query: '> h2' });
 
     $("#meeting-texts h2").on("click",function(e){
       e.preventDefault();
        clickeditem = $(this);
        icon = clickeditem.find('i');
        if (clickeditem.hasClass("open")) {
            icon.removeClass("fa-caret-down")
                  .addClass("fa-caret-right");
            
        } else {
              icon.removeClass("fa-caret-right")
              .addClass("fa-caret-down");
        }
       
      
  }); 
  $('#meeting-texts h2 > a')
    .on('click', function(e) {
      if ($(this).attr('href').substr(0, 1) === '#') {
       // e.preventDefault();
        var selected = $('#meeting-texts').find($(this).attr('href'));
        collapse.close();
        collapse.open($('#meeting-texts h2').index(selected));
        $(window).scrollTop(selected.offset().top);
      }
      
    });
});
