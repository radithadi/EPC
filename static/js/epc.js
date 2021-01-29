$(document).ready(function () {
    setTimeout(function () {
        if ($('.alert').is(':visible')) {
            $('.alert').fadeOut('slow');
        }
    }, 3000)
});