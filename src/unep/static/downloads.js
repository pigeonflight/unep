$(document).ready(function(){   
    
  var collapse = new jQueryCollapse($('#meeting-downloads'));

  $("#meeting-downloads h2 > a").on("click",function(e){
      
        icon = $(this).find('i');
        if (icon.hasClass("fa-chevron-circle-right")) {
            icon.removeClass("fa-chevron-circle-right");
            icon.addClass("fa-chevron-circle-down");
            
        } else {
              icon.removeClass("fa-chevron-circle-down");
              icon.addClass("fa-chevron-circle-right");
        }
      
  });
  $('#meeting-downloads').find('input[type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[type="checkbox"]:checked').size());
        

    });

  $('.meeting-select-disabled input').attr('disabled', 'disabled');

});

