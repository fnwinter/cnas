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
              console.log(response)
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

});
