$(document).ready(function(){   
    
  var collapse = new jQueryCollapse($('#meeting-downloads'));

  $('#meeting-downloads').find('input[type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[type="checkbox"]:checked').size());

    });

  $('.meeting-select-disabled input').attr('disabled', 'disabled');

});

