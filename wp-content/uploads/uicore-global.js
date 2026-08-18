/* ================================================================
   uicore-global.js — Replacement for missing UiCore Framework JS
   Handles: mobile menu, smooth scroll, back-to-top, nav scroll
   ================================================================ */
(function() {
    'use strict';

    // Wait for DOM ready
    document.addEventListener('DOMContentLoaded', function() {

        // -------------------------------------------------------
        // 1. MOBILE HAMBURGER MENU TOGGLE
        // -------------------------------------------------------
        var body = document.body;
        var hamBtn = document.querySelector('button.uicore-ham');
        var navWrapper = document.querySelector('.uicore-navigation-wrapper');

        // Add uicore-is-ham class on mobile
        function checkMobile() {
            if (window.innerWidth <= 1024) {
                body.classList.add('uicore-is-ham');
            } else {
                body.classList.remove('uicore-is-ham');
                body.classList.remove('uicore-mobile-nav-show');
                body.classList.remove('uicore-overflow-hidden');
                if (navWrapper) {
                    navWrapper.style.opacity = '';
                    navWrapper.style.pointerEvents = '';
                }
            }
        }
        checkMobile();
        window.addEventListener('resize', checkMobile);

        if (hamBtn) {
            hamBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();

                var isOpen = body.classList.contains('uicore-mobile-nav-show');

                if (isOpen) {
                    // Close menu
                    body.classList.remove('uicore-mobile-nav-show');
                    body.classList.remove('uicore-overflow-hidden');
                    hamBtn.classList.remove('uicore-toggle');
                    if (navWrapper) {
                        navWrapper.style.opacity = '0';
                        navWrapper.style.pointerEvents = 'none';
                    }
                } else {
                    // Open menu
                    body.classList.add('uicore-mobile-nav-show');
                    body.classList.add('uicore-overflow-hidden');
                    hamBtn.classList.add('uicore-toggle');
                    if (navWrapper) {
                        navWrapper.style.opacity = '1';
                        navWrapper.style.pointerEvents = 'all';
                        navWrapper.style.transition = 'opacity 0.3s ease';
                    }

                    // Make menu items visible with animation
                    var menuItems = navWrapper.querySelectorAll('.uicore-menu > .menu-item');
                    menuItems.forEach(function(item, index) {
                        item.classList.add('uicore-visible');
                        item.style.animationDelay = (index * 0.05) + 's';
                    });
                }
            });
        }

        // -------------------------------------------------------
        // 2. MOBILE SUB-MENU TOGGLE (Services dropdown)
        // -------------------------------------------------------
        var subMenuParents = document.querySelectorAll('.uicore-navigation-wrapper .menu-item-has-children > a');
        subMenuParents.forEach(function(link) {
            // Create a clickable arrow area
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 1024) {
                    var parentLi = this.parentElement;
                    var subMenu = parentLi.querySelector('.sub-menu');
                    if (subMenu) {
                        e.preventDefault();
                        if (subMenu.style.display === 'block') {
                            subMenu.style.display = 'none';
                            parentLi.classList.remove('uicore-open');
                        } else {
                            subMenu.style.display = 'block';
                            parentLi.classList.add('uicore-open');
                        }
                    }
                }
            });
        });

        // Close menu when clicking a link (not a parent with submenu)
        var menuLinks = document.querySelectorAll('.uicore-navigation-wrapper .menu-item:not(.menu-item-has-children) > a');
        menuLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 1024 && body.classList.contains('uicore-mobile-nav-show')) {
                    body.classList.remove('uicore-mobile-nav-show');
                    body.classList.remove('uicore-overflow-hidden');
                    if (hamBtn) hamBtn.classList.remove('uicore-toggle');
                    if (navWrapper) {
                        navWrapper.style.opacity = '0';
                        navWrapper.style.pointerEvents = 'none';
                    }
                }
            });
        });

        // -------------------------------------------------------
        // 3. NAVBAR SCROLL EFFECT (add shadow on scroll)
        // -------------------------------------------------------
        var navbar = document.querySelector('#wrapper-navbar');
        var headerWrapper = document.querySelector('.uicore-header-wrapper');

        function handleScroll() {
            if (window.scrollY > 50) {
                body.classList.add('uicore-scrolled');
                if (headerWrapper) headerWrapper.classList.add('uicore-scrolled');
            } else {
                body.classList.remove('uicore-scrolled');
                if (headerWrapper) headerWrapper.classList.remove('uicore-scrolled');
            }
        }
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();

        // -------------------------------------------------------
        // 4. BACK TO TOP BUTTON
        // -------------------------------------------------------
        var backToTop = document.querySelector('#uicore-back-to-top');
        if (backToTop) {
            window.addEventListener('scroll', function() {
                if (window.scrollY > 400) {
                    backToTop.classList.add('uicore-show');
                    backToTop.style.opacity = '1';
                    backToTop.style.visibility = 'visible';
                } else {
                    backToTop.classList.remove('uicore-show');
                    backToTop.style.opacity = '0';
                    backToTop.style.visibility = 'hidden';
                }
            }, { passive: true });

            backToTop.addEventListener('click', function(e) {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        // -------------------------------------------------------
        // 5. ELEMENTOR SECTION STRETCH (for full-width sections)
        // -------------------------------------------------------
        function stretchSections() {
            var sections = document.querySelectorAll('[data-settings*="stretch_section"]');
            sections.forEach(function(section) {
                var windowWidth = window.innerWidth;
                var sectionRect = section.parentElement ? section.parentElement.getBoundingClientRect() : { left: 0, width: windowWidth };
                section.style.width = windowWidth + 'px';
                section.style.marginLeft = -sectionRect.left + 'px';
            });
        }
        stretchSections();
        window.addEventListener('resize', stretchSections);

        // -------------------------------------------------------
        // 6. LAZY-LOAD BACKGROUNDS (remove the no-bg optimization)
        // -------------------------------------------------------
        var lazySections = document.querySelectorAll('.e-con.e-parent');
        lazySections.forEach(function(section) {
            section.classList.add('e-lazyloaded');
        });

        // -------------------------------------------------------
        // 7. PAGE TRANSITION (remove loading overlay if present)
        // -------------------------------------------------------
        var pageTransition = document.querySelector('.uicore-page-transition');
        if (pageTransition) {
            pageTransition.style.opacity = '0';
            setTimeout(function() { pageTransition.style.display = 'none'; }, 500);
        }

        // -------------------------------------------------------
        // 8. ANIMATE ON SCROLL (simple IntersectionObserver)
        // -------------------------------------------------------
        if ('IntersectionObserver' in window) {
            var animObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('uicore-animated');
                        animObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.uicore-animate').forEach(function(el) {
                animObserver.observe(el);
            });
        }

    }); // end DOMContentLoaded
})();
