function headerBanner(){
	$(".header-top").height($(window).height()-64);
  $(".parallax.doc").height($(document).height());
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

    $('select').material_select();
  }); // end of document ready
})(jQuery); // end of jQuery name space



$(window).load(function() {
});

$(window).on('resize', function() {
  	headerBanner();
});