/* global tinymce */

document.addEventListener('DOMContentLoaded', function () {
  function waitForTinyMCE(callback) {
    if (typeof tinymce !== 'undefined') {
      callback();
    } else {
      // Wait and try again
      setTimeout(() => waitForTinyMCE(callback), 100);
    }
  }

  waitForTinyMCE(function () {
    tinymce.init({
      selector: 'textarea',
    }).then(editors => {
      console.log('TinyMCE initialized:', editors);
    });
  });
});

