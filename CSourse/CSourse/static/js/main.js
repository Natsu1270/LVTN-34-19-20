// Bootstrap JS
import "bootstrap/dist/js/bootstrap.bundle.min";

// Carousel
import "owl.carousel";
import "owl.carousel/dist/assets/owl.carousel.css";

// Fancybox modal
import "@fancyapps/fancybox";
import "@fancyapps/fancybox/dist/jquery.fancybox.css";

// Slicky
import "slick-carousel"
import "slick-carousel/slick/slick.scss";
import "slick-carousel/slick/slick-theme.scss";


// Main style
import "../../scss/output.scss";

$(document).ready(() => {
	const $tab = $("#cs-course-tab");
	const $overview = $("#cs-course-overview");
	const $components = $("#cs-course-components");
	const $instructors = $("#cs-course-tutors");
	const $reviews = $("#cs-course-review");
	const $relates = $("#cs-course-related");
	const tabAddressLink = $(".course-tab__address--link");
	const mainHeader = $('#main-header');
	const loginBtn = $("#login-btn");
	const signupBtn = $("#signup-btn");


	// Function to remove indicator border of tab link
	function resetTabLinked() {
		tabAddressLink.each(function (index) {
			if ($(this).parent().hasClass("course-tab__address--active")) {
				$(this).parent().removeClass("course-tab__address--active");
			}
		});
	}

	// On scroll to tab content -> show indicator border to tab link
	if ($tab.length) {
		const overviewPos = $overview.offset().top;
		const componentsPos = $components.offset().top;
		const instructorsPos = $instructors.offset().top;
		const reviewsPos = $reviews.offset().top;
		const relatesPos = $relates.offset().top;
		$(window).on('scroll', function () {
			let scroll = $(window).scrollTop();
			if (scroll >= overviewPos - 200) {
				resetTabLinked();
				$("#tab-overview").addClass("course-tab__address--active");
			} else {
				resetTabLinked();
			}
			if (scroll >= componentsPos - 200) {
				resetTabLinked();
				$("#tab-components").addClass("course-tab__address--active");
			}
			if (scroll >= instructorsPos - 200) {
				resetTabLinked();
				$("#tab-tutors").addClass("course-tab__address--active");
			}
			if (scroll >= reviewsPos - 200) {
				resetTabLinked();
				$("#tab-review").addClass("course-tab__address--active");
			}
			if (scroll >= relatesPos - 200) {
				resetTabLinked();
				$("#tab-related").addClass("course-tab__address--active");
			}
		})
	}

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
		if ($tab.length) {
			let y_post = $tab.offset().top;
			let height = $tab.height();
			$(window).on('scroll', () => {
				let scroll = $(window).scrollTop();
				if (scroll >= y_post - height) {
					$tab.addClass('section-course-tab__fixed');
					mainHeader.addClass('cs-header-replaced');
					mainHeader.removeClass('cs-header-fixed');
				} else {
					$tab.removeClass('section-course-tab__fixed');
					mainHeader.removeClass('cs-header-replaced');
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
	});

	tabAddressLink.click((e) => {
		e.preventDefault();
		let target = $(e.target.getAttribute('href'));
		if (target.length) {
			e.target.parentElement.classList.add("course-tab__address--active");
			let scrollTo = target.offset().top - 100;
			$('body, html').animate({scrollTop: scrollTo + 'px'}, 500,'linear');
		}
	});

	const switchers = [...document.querySelectorAll('.switcher')];

	switchers.forEach(item => {
		item.addEventListener('click', function() {
			switchers.forEach(item => item.parentElement.classList.remove('is-active'))
			this.parentElement.classList.add('is-active')
		})
	});

	$('[data-fancybox="account"]').fancybox({
	// Options will go here
		hideScrollbar : false,

		afterShow: function( instance, current ) {
		const signUpButton = $("#cs-form-signUp");
		const signInButton = $("#cs-form-signIn");
		const container = $("#cs-form-container");

		signUpButton.on('click', () => {
			container.addClass("right-panel-active")
		});
		signInButton.on('click', () => {
			container.removeClass("right-panel-active");
		});
		},

	});




	$('[data-fancybox="exam1"]').fancybox({
		hideScrollbar: true,
		// afterShow: function (instance, current) {
		// $('.exam_questions__detail').slick({
		// 	slidesToShow : 1,
		// 	slidesToScroll : 1,
		// 	autoplay: false,
		// 	centerMode: true,
		// 	infinite: false,
		// 	variableWidth: true,
		// });
		// }
	});


});

