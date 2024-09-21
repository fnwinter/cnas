$(document).ready(function(){
    function handleClick(_path) {
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

    $('.picture').click(function() {
        var path = $(this).data('path');
        handleClick(path);
    });

    $('.folder').click(function() {
        var path = $(this).data('path');
        handleClick(path);
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
