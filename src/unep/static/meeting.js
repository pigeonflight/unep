requirejs({
  paths: {
    'jquery.collapse': '++resource++unep/jquery.collapse',
    'moment': '++resource++unep/moment-with-langs.min',
    'jquery.cookie': '++resource++unep/jquery.cookie',
  }
});

require([
  'jquery',
  'jquery.collapse',
  'jquery.cookie',
  'moment'
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
  $(document).ready(function(){ 
  var lang = $.cookie('unep-language');
  if (!lang) lang = 'en';
  momentlang = moment.lang(lang);
    console.log(lang);
  startdate = $('.documentStart').html();
  enddate = $('.documentEnd').html();
      var firstdateformat = {
          fr:"D MMMM YYYY",
          es:"D-MMMM-YYYY",
          en:"D MMMM YYYY"
                            };
  if (moment(startdate).format('MMMM') == moment(enddate).format('MMMM')){
      firstdateformat = {
          fr:"D",
          es:"D",
          en:"D"
                            };
  }
    if (lang == 'fr') {
       $('.documentStart').html(moment(startdate).format(firstdateformat.fr));
       $('.documentEnd').html(moment(enddate).format("D MMMM YYYY")); 
    }
    else if (lang == 'es'){ 
       $('.documentStart').html(moment(startdate).format(firstdateformat.es));
       $('.documentEnd').html(moment(enddate).format("D-MMMM-YYYY")); 
    }
    else {
       $('.documentStart').html(moment(startdate).format(firstdateformat.en));
       $('.documentEnd').html(moment(enddate).format("MMMM D,YYYY"));
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
