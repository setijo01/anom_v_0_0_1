$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip({ boundary: 'window' })
    $('#main_container').hide();

    var words = [
        'Visual Artist.',
        'Graphic Designer.',
        'Software Developer.',
        ], i = 0;
    setInterval(function(){
        $('#job_title').fadeOut(function(){
            $(this).html(words[i=(i+1)%words.length]).fadeIn();
        });
    }, 3000);
    $("#cover_container").click(function() {
        $('#cover_container').fadeOut(1000,'linear');
        $('#main_container').fadeIn(1000,'linear');
    });

    $('.skillbar').each(function(){
		$(this).find('.skillbar-bar').velocity({
			width:$(this).attr('data-percent')
		},4500);
	});

    $('a[href*="#"]')
      // Remove links that don't actually link to anything
      .not('[href="#"]')
      .not('[href="#0"]')
      .click(function(event) {
        // On-page links
        if (
          location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '')
          &&
          location.hostname == this.hostname
        ) {
          // Figure out element to scroll to
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
          // Does a scroll target exist?
          if (target.length) {
            // Only prevent default if animation is actually gonna happen
            event.preventDefault();
            $('html, body').animate({
              scrollTop: target.offset().top
            }, 1000, function() {
              // Callback after animation
              // Must change focus!
              var $target = $(target);
              $target.focus();
              if ($target.is(":focus")) { // Checking if the target was focused
                return false;
              } else {
                $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
                $target.focus(); // Set focus again
              };
            });
          }
        }
      });
    $("form").submit(function(){
        alert("Message is successfully submitted!");
    });
});