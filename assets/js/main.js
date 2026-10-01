(function () {
  var d = document, root = d.documentElement;
  root.classList.add('js');

  // Sticky header shadow
  var header = d.querySelector('.site-header');
  var onScroll = function () { if (header) header.classList.toggle('scrolled', window.scrollY > 10); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Mobile menu
  var burger = d.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = d.body.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  d.querySelectorAll('.dd-toggle').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentElement, open = li.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  d.querySelectorAll('.menu a').forEach(function (a) {
    a.addEventListener('click', function () { d.body.classList.remove('nav-open'); });
  });

  // Scroll reveal
  var els = d.querySelectorAll('.reveal, .stagger');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Only one FAQ open at a time within a group
  d.querySelectorAll('.faq').forEach(function (group) {
    group.addEventListener('toggle', function (e) {
      if (e.target.open) group.querySelectorAll('details[open]').forEach(function (o) { if (o !== e.target) o.open = false; });
    }, true);
  });

  // Price estimator: maps cubic yards to the published volume price tiers
  var TIERS = [[1, 95, 150], [2, 130, 175], [4, 180, 280], [7.5, 300, 425], [11, 440, 560], [15, 560, 650]];
  var LOADS = ['single item', '1/8 truck', '1/4 truck', '1/2 truck', '3/4 truck', 'full truck'];
  d.querySelectorAll('[data-estimator]').forEach(function (box) {
    var inputs = box.querySelectorAll('input[data-yards]');
    var out = box.querySelector('[data-est-price]'), load = box.querySelector('[data-est-load]');
    var update = function () {
      var yards = 0;
      inputs.forEach(function (i) {
        var n = Math.max(0, Math.min(20, parseInt(i.value, 10) || 0));
        i.value = n; yards += n * parseFloat(i.getAttribute('data-yards'));
      });
      if (!yards) { out.textContent = 'Add items to start'; load.textContent = 'Prices include labor, loading and disposal.'; return; }
      var trucks = Math.floor(yards / 15), rest = yards - trucks * 15, lo = trucks * 560, hi = trucks * 650, label = '';
      if (rest > 0) {
        for (var t = 0; t < TIERS.length; t++) {
          if (rest <= TIERS[t][0]) { lo += TIERS[t][1]; hi += TIERS[t][2]; label = LOADS[t]; break; }
        }
      }
      out.textContent = '$' + lo.toLocaleString() + ' to $' + hi.toLocaleString();
      load.textContent = 'About ' + Math.round(yards * 10) / 10 + ' cubic yards' +
        (trucks ? ' (' + trucks + ' full truck' + (trucks > 1 ? 's' : '') + (label ? ' plus a ' + label : '') + ')' : ' (' + label + ')') + '.';
    };
    box.addEventListener('click', function (e) {
      var b = e.target.closest('.est-step'); if (!b) return;
      var i = b.parentElement.querySelector('input');
      i.value = (parseInt(i.value, 10) || 0) + parseInt(b.getAttribute('data-step'), 10); update();
    });
    box.addEventListener('input', update);
  });

  // Lead tracking: report phone clicks to any analytics tag added later (GA4, GTM)
  d.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="tel:"]'); if (!a) return;
    var data = { event: 'phone_call_click', page: location.pathname, link_text: (a.textContent || '').trim() };
    (window.dataLayer = window.dataLayer || []).push(data);
    if (typeof window.gtag === 'function') window.gtag('event', 'phone_call_click', { page_path: location.pathname });
  });

  // Current year
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
