;! function() {

    $('#join-organization-button').on('click', function(event) {
        $.ajax({
            type: 'GET',
            url: "/organization/join/"+$(this).data('organization')+"/",
            success: function(response) {
                if (response.message=='SUCCESS') {
                    console.log('SUCCESS!');
                    // add modal to display successful adding here
                }
            },
            error: function(response) {
                console.log('ERROR!');
                // add modal to display error here
            }
        });

    });

}();
