(function () {
  'use strict';

  // ---------------------------------------------------------------
  // Mobile navigation
  // Every [data-menu-toggle] gets a listener — the open button and the
  // close button inside the panel are both toggles. Binding only the
  // first one is what left the old site's close button inert.
  // ---------------------------------------------------------------
  var panel = document.querySelector('[data-menu-panel]');
  var toggles = document.querySelectorAll('[data-menu-toggle]');
  var backdrop = document.querySelector('[data-menu-backdrop]');

  function setMenu(open) {
    if (!panel) return;
    panel.classList.toggle('translate-x-full', !open);
    document.body.classList.toggle('overflow-hidden', open);
    if (backdrop) {
      backdrop.classList.toggle('opacity-0', !open);
      backdrop.classList.toggle('pointer-events-none', !open);
    }
    toggles.forEach(function (btn) {
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  toggles.forEach(function (btn) {
    btn.addEventListener('click', function () {
      setMenu(panel.classList.contains('translate-x-full'));
    });
  });

  if (backdrop) backdrop.addEventListener('click', function () { setMenu(false); });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setMenu(false);
  });

  // Close after tapping a link, and reset when returning to desktop
  document.querySelectorAll('[data-menu-panel] a').forEach(function (a) {
    a.addEventListener('click', function () { setMenu(false); });
  });
  window.addEventListener('resize', function () {
    if (window.innerWidth >= 1024) setMenu(false);
  });

  // ---------------------------------------------------------------
  // Collapsible submenu inside the mobile panel
  // ---------------------------------------------------------------
  document.querySelectorAll('[data-submenu-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var sub = btn.nextElementSibling;
      var open = !sub.classList.contains('hidden');
      sub.classList.toggle('hidden', open);
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      var icon = btn.querySelector('[data-chevron]');
      if (icon) icon.classList.toggle('rotate-180', !open);
    });
  });

  // ---------------------------------------------------------------
  // Header background on scroll
  // ---------------------------------------------------------------
  var header = document.querySelector('[data-header]');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('shadow-lg', window.scrollY > 20);
      header.classList.toggle('bg-brand', window.scrollY > 20);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // ---------------------------------------------------------------
  // Count-up stats, triggered when scrolled into view
  // ---------------------------------------------------------------
  var counters = document.querySelectorAll('[data-count-to]');
  var reduceMotion = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function showFinal() {
    counters.forEach(function (c) {
      c.textContent = c.getAttribute('data-count-to');
    });
  }

  // Without IntersectionObserver (or when motion is reduced) the numbers must
  // still be correct rather than stuck at their "0" placeholder.
  if (!counters.length) {
    /* nothing to do */
  } else if (!('IntersectionObserver' in window) || reduceMotion) {
    showFinal();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        io.unobserve(el);
        var target = parseInt(el.getAttribute('data-count-to'), 10) || 0;
        var started = null;
        var step = function (ts) {
          if (!started) started = ts;
          var progress = Math.min((ts - started) / 1600, 1);
          // ease-out so it decelerates into the final value
          el.textContent = Math.round(target * (1 - Math.pow(1 - progress, 3))).toString();
          if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (c) { io.observe(c); });
  }

  // Stamp the current year in the footer
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();
