"use strict";

(function($) {
    // if ($(window).width() < 993) {
        $('.dropdown-submenu a.dropdown-toggle').on("click", function(e) {
            $(this).next('ul').toggle();
            e.stopPropagation();
            e.preventDefault();
        });
    // }
}(window.jQuery));