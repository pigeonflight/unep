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
         
$(".meeting-downloads-document-link").prepOverlay({
    subtype: 'ajax',
    filter: '#content>*',
    formselector: 'form',
    noform:'reload'
}); 

var countit = function(){ 
  $('#meeting-downloads-number-of-documents').html(
    $('#meeting-downloads').find('input[name="files"][type="checkbox"]:checked').size()
         );
     console.log("clicky clackety");
                       }

$('#meeting-downloads').find('input[name="all"][type="checkbox"]')
        .on('click', function(){
        section = $(this).attr('rel'); 
        console.log(section);
        // on click 
        if(this.checked) { // check select status
            $('.' + section + ' .meeting-select-active  input[name="files"]').each(function() { // loop through each checkbox
                this.checked = true;  //select all active checkboxes with name "files"               
                   }).promise().done( countit );
             }
              else{
                  
            $('.' + section + ' .meeting-select-active input[name="files"]').each(function() { // loop through each checkbox
                this.checked = false; // deselect all active checkboxes with name "files"                       
                    }).promise().done( countit ); 
                  }
         
        }  
         //,countit  
                    );
    
$("#meeting-downloads h2").on("click",function(e){
       e.preventDefault();
        clickeditem = $(this);
        icon = clickeditem.find('i');
        if (clickeditem.hasClass("jqopen")) {
            icon.removeClass("fa-caret-down")
                  .addClass("fa-caret-right");
            
        } else {
              icon.removeClass("fa-caret-right")
              .addClass("fa-caret-down");
        }
       
      
  }); 
$('#meeting-downloads').find('input[name="all"][type="checkbox"]')
    .on('change', function() {
       
       //
          
       
    });

$('#meeting-downloads').find('input[name="files"][type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[name="files"][type="checkbox"]:checked').size());
        
    });

$('.meeting-select-disabled input').attr('disabled', 'disabled');

}); 