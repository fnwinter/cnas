$(document).ready(function(){
    function handleFolder(_path) {
        var data = {
          "path": _path
        };

        $.ajax({
            url: '/gallery',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
              document.body.innerHTML = response
              window.location.reload();
            },
            error: function(xhr, status, error) {
              console.log(error)
            }
        });
    }

    function showModal(_path) {
        $('.modal').addClass('is-active');
        var rel_path = $('#rel_path').data('path');
        $('#full_image').attr('src',
          "/gallery_file/"+rel_path+"/"+_path);
    };

    function hideModal() {
        $('.modal').removeClass('is-active');
    }

    $('.picture').click(function() {
        var path = $(this).data('path');
        showModal(path);
    });

    $('.modal-close').click(function() {
        hideModal();
    });

    $('.folder').click(function() {
        var path = $(this).data('path');
        handleFolder(path);
    });

    $('.hoverArea').hover(
      function() {
          const targetDiv = $(this).data('target');
          $('#' + targetDiv).stop(true, true).fadeIn(500);
      },
      function() {
          const targetDiv = $(this).data('target');
          $('#' + targetDiv).stop(true, true).fadeOut(500);
      }
    );
});
