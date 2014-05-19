require([
  'jquery',
  'dropzone'
], function($, Dropzone) {

  Dropzone.autoDiscover = false;

  function addMessage(type, typeName,  message) {
    message = '<a href="#" class="notification-close">&times;</a>' +
      '<div>' + message + '</div>';
    $('#upload-messages').append($('' +
      '<dl class="portalMessage ' + type + '">' +
      '<dt>' + typeName + '</dt>' +
      '<dd>' + message + '</dd>' +
      '</dl>'
    ));
    $('#upload-messages a.notification-close').on('click', function() {
      $(this).parents('.portalMessage').remove();
    });
  }
  var I18N = JSON.parse($('#upload').data('i18n')),
      uploadHtml = $('#upload').html(),
      progress = $('<div><span>' + I18N['Uploading ...'] + '<span></div>'),
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
        $('#upload').html(uploadHtml).removeClass('upload-progress');
      });

      self.on("addedfile", function(file) {
        if (file.name.indexOf('.') !== -1 &&
            file.name.split('.').slice(-2)[0].indexOf('-') !== -1 &&
            ['en', 'fr', 'es'].indexOf(file.name.split('.').slice(-2)[0].split('-').slice(-1)[0]) !== -1) {
          if (self.files
              .map(function(f) { return f.name; })
              .filter(function(f) { return f === file.name })
              .length != 1) {
            self.removeFile(file);
          }
        } else {
          addMessage('error', I18N['Error'],
                     '<strong><span class="error">' + file.name + '</span>' +
                      I18N[' does not have a language identifier at the end of it\'s name (-en,-es,-fr). Please rename with a language identifier and attempt to upload again.'] + '</strong>');
          self.removeFile(file);
        }
      });

      self.on("complete", function(file) {
        $(file.previewElement).html(
          '<div class="dz-feedback">' + I18N['Upload successful: '] + file.name + '</div>')

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
            var message = '';
                created = uploaded.reduce(function(prev, item) {
                  if (!prev[item.uid]){
                    prev[item.uid] = {
                      url: item.url,
                      title: item.title,
                      languages: [ item.language ]
                    };
                  } else {
                    prev[item.uid].languages.push(item.language);
                  }
                  return prev;
                }, {});

            Object.keys(created).forEach(function(uid) {
              message += '' +
                '<li>' +
                ' <a href="' + created[uid].url + '" class="uploaded-doc" target="_blank">' +
                '  ' +  created[uid].title +
                ' (' + created[uid].languages.join(',') +')' +
                ' </a>'+
                '</li>';
            });
            if (message !== '') {
              addMessage('info', 'Info',
                '<p>' + I18N['Following documents were created/updated.'] + '</p>' +
                '<p>' + I18N['Click on link to edit their metadata.'] + '</p>' +
                '<ul>' + message + '</ul>', true);
                
          /*      $('a.uploaded-doc').prepOverlay({
    subtype: 'ajax',
    filter: '#content>*',
    formselector: 'form'
    }); */
                overlays = [];
                $('a.uploaded-doc').each(function(index) {
                 var href = $(this).attr('href');
                 overlay = $( this ).prepOverlay({
                    subtype: 'ajax',
                    filter: '#content>*',
                    formselector: 'form',
                    closeselector: 'input#form-buttons-cancel',
                     afterpost: function(data,more){console.log(data,more)},
                     config: {
                         url : index + "|"  + href ,
                        onBeforeLoad : function (e) {
                         console.log(this.getConf().url);
                           return true; }
                         
                            }
                       });
                    overlays.push(overlay);
                     });
                
                
                

            }
          }
        }, 300);
      });
    }
  });

});
