;! function() {

    $('.engage-button').on('click', function(event) {
        $.ajax({
            type: 'GET',
            data: {
                'slug': $(this).data('slug'),
            },
            url: Urls['activities:engage'](),
            success: function(response) {
                console.log(response.message);
            }
        });

    });

}();
