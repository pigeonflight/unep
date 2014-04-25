require([
  'jquery',
  'dropzone'
], function($, Dropzone) {

  Dropzone.autoDiscover = false;

  var dropzone = new Dropzone("#unep-upload", {
    url: "@@upload",
    addRemoveLinks: true,
    parallelUploads: 1,
    uploadMultiple: false,
    previewsContainer: '#unep-upload-preview',
    clickable: true,
    autoProcessQueue: false,
    init: function() {
      var self = this;

      $('#unep-upload-submit').on('click', function() {
        if (self.files.length !== 0) {
            self.processFile(self.files[0]);
        }
        self.processFile(self);
      });

      $('#unep-upload-cancel').on('click', function() {
        self.removeAllFiles(true);
      });

      self.on("addedfile", function(file) {
        if (self.files
             .map(function(f) { return f.name; })
             .filter(function(f) { return f === file.name })
             .length != 1) {
          self.removeFile(file);
        }
      });

      self.on("complete", function(file) {
        $(file.previewElement).html(
          '<div class="dz-feedback">Upload of "' + file.name + '" successful.</div>')
        setTimeout(function() {
          self.removeFile(file);
          if (self.files.length !== 0) {
              $('#unep-upload-submit').trigger('click');
          }
        }, 300);
      });
    }
  });

});
