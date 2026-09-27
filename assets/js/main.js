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

  // Current year
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
