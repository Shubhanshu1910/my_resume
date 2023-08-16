// static/js/custom.js

document.addEventListener('DOMContentLoaded', function() {
    var navbarToggler = document.querySelector('.navbar-toggler');
    
    navbarToggler.addEventListener('click', function() {
        // Toggle the aria-expanded attribute
        var isExpanded = navbarToggler.getAttribute('aria-expanded') === 'true';
        navbarToggler.setAttribute('aria-expanded', !isExpanded);
    });
});
