$(document).ready(function(){   
    
   var collapse = new jQueryCollapse($('#meeting-downloads'));
         
    $(".meeting-downloads-document-link").prepOverlay({
    subtype: 'ajax',
    filter: '#content>*',
    formselector: 'form',
    noform:'reload'
    });
    
  $("#meeting-downloads").on("open", function(e, section) {
  console.log(section, " is open");
});
 
  $("#meeting-downloads h2").on("click",function(e){
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
  $('#meeting-downloads').find('input[type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[type="checkbox"]:checked').size());
        

    });

  $('.meeting-select-disabled input').attr('disabled', 'disabled');

});