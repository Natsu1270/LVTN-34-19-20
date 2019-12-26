import "bootstrap/dist/js/bootstrap.bundle.min";
import "owl.carousel";
import "owl.carousel/dist/assets/owl.carousel.css";
import "../../scss/output.scss";

$(document).ready(() => {
	// Fixed header
	function fixedHeader() {
		if ($('.cs-main-header').length) {
			$(window).on('scroll', () => {
				let scroll = $(window).scrollTop();
				if (scroll >= 10) {
					$('#main-header').addClass('cs-header-fixed');
				} else {
					$('#main-header').removeClass('cs-header-fixed');
				}
			})
		}
	}
	fixedHeader();
	// Fixed tab
	function fixedTab() {
		let $tab = $("#cs-course-tab");
		if ($tab.length) {
			let y_post = $tab.offset().top;
			let height = $tab.height();
			$(window).on('scroll', () => {
				let scroll = $(window).scrollTop();
				if (scroll >= y_post + height) {
					$tab.addClass('cs-course-tab__fixed');
				} else {
					$tab.removeClass('cs-course-tab__fixed');
				}
			})
		}

	}

	fixedTab();

	// Owl carousel slider
	$('.owl-carousel').owlCarousel({
		items: 4,
		loop: true,
		autoplay: true,
		animateOut: true,
		animateIn: true,
		margin: 20,
		autoplayHoverPause: true,
		nav: true,
		navText: [
			"<i class='fa fa-caret-left'></i>",
			"<i class='fa fa-caret-right'></i>"
		],
	})

});

