require([
  'jquery',
  'dropzone'
], function($, Dropzone) {

  Dropzone.autoDiscover = false;

  function addMessage(type, typeName,  message) {
    $('#upload-messages').append($('' +
      '<dl class="portalMessage ' + type + '">' +
      '<dt>' + typeName + '</dt>' +
      '<dd>' + message + '</dd>' +
      '</dl>'
    ));
  }

  var dropzone = new Dropzone("#upload", {
    url: "@@upload",
    addRemoveLinks: true,
    parallelUploads: 1,
    uploadMultiple: false,
    previewsContainer: '#upload-preview',
    clickable: true,
    autoProcessQueue: false,
    init: function() {
      var self = this;

      $('#upload-submit').on('click', function() {
        if (self.files.length !== 0) {
            self.processFile(self.files[0]);
        }
        self.processFile(self);
      });

      $('#upload-cancel').on('click', function() {
        self.removeAllFiles(true);
      });

      self.on("addedfile", function(file) {
        if (file.name.indexOf('.') !== -1 &&
            file.name.split('.').slice(-2)[0].indexOf('-') !== -1 &&
            ['en', 'fr', 'es'].indexOf('assasasa.zip'.split('.').slice(-2)[0].split('-').slice(-1)[0])) {
          if (self.files
              .map(function(f) { return f.name; })
              .filter(function(f) { return f === file.name })
              .length != 1) {
            self.removeFile(file);
          }
        } else {
          addMessage('error', 'Error',
                     'Files need to end with language (-en,-es,-fr) to be able to upload it.');
          self.removeFile(file);
        }
      });

      self.on("complete", function(file) {
        $(file.previewElement).html(
          '<div class="dz-feedback">Upload of "' + file.name + '" successful.</div>')
        setTimeout(function() {
          self.removeFile(file);
          if (self.files.length !== 0) {
              $('#upload-submit').trigger('click');
          }
        }, 300);
      });
    }
  });

});
