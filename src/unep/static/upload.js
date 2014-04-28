require([
  'jquery',
  'dropzone'
], function($, Dropzone) {

  Dropzone.autoDiscover = false;

  function addMessage(type, typeName,  message, closeable) {
    closeable = closeable || false;
    if (closeable) {
      message = '<div>' + message + '</div>' +
          '<a class="notification-close">Close</a>';
    }
    $('#upload-messages').append($('' +
      '<dl class="portalMessage ' + type + '">' +
      '<dt>' + typeName + '</dt>' +
      '<dd>' + message + '</dd>' +
      '</dl>'
    ));
    $('#upload-messages a.notification-close').on('click', function() {
      $('#upload-messages').html('');
    });
  }

  var uploadHtml = $('#upload').html(),
      progress = $('<div><span>Uploading...<span></div>'),
      uploaded = [];

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
        uploaded = [];
        progress.css('width', '0%');
        $('#upload').html(progress).addClass('upload-progress');
        if (self.files.length !== 0) {
            self.processFile(self.files[0]);
        }
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
        $(file.previewElement).html('<div class="dz-feedback">Upload of "' + file.name + '" successful.</div>')

        uploaded.push(JSON.parse(file.xhr.responseText));

        setTimeout(function() {
          self.removeFile(file);
          $('#upload > div').css('width',
              Math.round(uploaded.length * 100 / (uploaded.length + self.files.length)) + '%');
          if (self.files.length !== 0) {
             self.processFile(self.files[0]);
          } else {
            // when last file is uploaded we show all notifications what was
            // uploaded
            $('#upload').html(uploadHtml).removeClass('upload-progress');
            //var message = '';
            //uploaded
            //  .reduce(function(prev, item) {
            //    if (!prev[item.id]){
            //      prev[item.id] = { url: item.url, languages: [ item.language ]};
            //    } else {
            //      prev[item.id].languages.push(item.language);
            //    }
            //    return prev;
            //  }, {})
            //  .forEach(function() {
            //    debugger;
            //  });
            addMessage('info', 'Info',
                       'all files were uploaded!', true);
          }
        }, 300);
      });
    }
  });

});
