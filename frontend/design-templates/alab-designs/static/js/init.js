function headerBanner(){
	$(".header-top").height($(window).height()-64);
}
function dupImg(){
	$(".card-org .card-image").each(function(){
		var chever = $(this).find("img")

		$( chever ).clone().appendTo( this );
	})
}
(function($){
  $(function(){
  	headerBanner();
  	dupImg();


    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space



$(window).load(function() {
});

$(window).on('resize', function() {
  	headerBanner();
});