requirejs({
  paths: {
    'jquery.collapse': '++resource++unep/jquery.collapse',
    'jszip': '++resource++unep/jszip',
    'jszip.utils': '++resource++unep/jszip.utils',
    'jquery.cookie': '++resource++unep/jquery.cookie',
    'filesaver': '++resource++unep/FileSaver'
  }
});

require([
  'jquery',
  'jszip',
  'jszip.utils',
  'filesaver',
  'jquery.cookie',
  'jquery.collapse'
], function($, JSZip, JSZipUtils) {

  function downloadFile(url, filename, zip) {
    var deferred = $.Deferred();

    JSZipUtils.getBinaryContent(url, function (err, data) {
      if (err) {
        deferred.reject(err);
      } else {
        zip.file(filename, data, { binary: true });
        deferred.resolve(data);
      }
    });

    return deferred;
  }

  var collapse = new jQueryCollapse($('#meeting-downloads'));

  $('#meeting-downloads').find('input[type="checkbox"]')
    .on('change', function() {
      $('#meeting-downloads-number-of-documents').html(
        $('#meeting-downloads').find('input[type="checkbox"]:checked').size());

    });

    $('#meeting-downloads-button').on('click', function(e) {
      e.preventDefault();

      var zip = new JSZip(),
          deferreds = [];

      $('#meeting-downloads').find('input[type="checkbox"]:checked')
        .each(function(i, el) {
          deferreds.push(downloadFile(
            $(el).attr('value'),
            $(el).attr('name'),
            zip
          ));
        });

      $.when.apply($, deferreds)
        .done(function () {
          var blob = zip.generate({type:"blob"});

          saveAs(blob, 'unep.zip');

          // TODO: showMessage("done !");
        })
        .fail(function (err) {
          // TODO: showError(err);
        });

    });


});
