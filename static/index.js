$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault();
        var formData = new FormData($(this)[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                alert('File uploaded and data saved.');
            }
        });
    });
});
