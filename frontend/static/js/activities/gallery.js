;!function () {
    function onInstagramAuthClicked(event) {
        var url = 'https://api.instagram.com/oauth/authorize?' + [
            'client_id=' + INSTAGRAM.clientId,
            'redirect_uri=' + encodeURIComponent(INSTAGRAM.redirectUrl),
            'response_type=code'
        ].join('&');
        
        window.open(url, null, 'left=0,top=0');
    };
    
    !function initialize() {
        $('#authenticateBtn').click(onInstagramAuthClicked);
    }();
}();
