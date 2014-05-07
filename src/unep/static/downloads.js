$(window).load(function(){   
    
 // var collapse = new jQueryCollapse($('#meeting-downloads'));
 var docscollapse = $('#meeting-downloads').collapse({
 show: function() {
    console.log("hello show"); 
    this.slideDown(100);
  },
  hide: function() {
    this.slideUp(100);
   },
     });

    $(".meeting-downloads-document-link").prepOverlay({
    subtype: 'ajax',
    filter: '#content>*',
    formselector: 'form'
    });
    
  $("#meeting-downloads").on("open", function(e, section) {
  console.log(section, " is open");
});
  $("#meeting-downloads h2 > a").on("click",function(e){
       e.preventDefault();
        icon = $(this).find('i');
        if (icon.hasClass("fa-caret-right")) {
            icon.removeClass("fa-caret-right")
                  .addClass("fa-caret-down");
                  return
        } 
       if (icon.hasClass("fa-caret-down")) {
            icon.removeClass("fa-caret-down")
                  .addClass("fa-caret-right");
                   return
        } 
      /* else {
              icon.removeClass("fa-caret-down")
              .addClass("fa-caret-right");
        }
        */
      
  });
  $('#meeting-downloads').find('input[type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[type="checkbox"]:checked').size());
        

    });

  $('.meeting-select-disabled input').attr('disabled', 'disabled');

});
