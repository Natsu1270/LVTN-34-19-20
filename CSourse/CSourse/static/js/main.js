import "../../scss/output.scss";
import $ from "jquery";
import "bootstrap/dist/js/bootstrap.bundle.min";

$(document).ready(() => {
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
});

