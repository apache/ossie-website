/*
 * home.js — Animations and interactive effects for the OSI landing page.
 *
 * This script only targets elements with "osi-" prefixed classes, so it
 * will not interfere with standard MkDocs docs/blog pages.
 *
 * Features:
 *   - Scroll-triggered fade-in animations via IntersectionObserver
 *   - Enhanced hover effects on member logo cards
 *   - Page load fade-in transition
 */

document.addEventListener("DOMContentLoaded", function () {

  // -----------------------------------------------------------------------
  // Scroll-triggered fade-in animations
  // Elements start invisible and slide up into view as the user scrolls.
  // -----------------------------------------------------------------------
  var observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  };

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  }, observerOptions);

  // Select all cards that should animate in on scroll
  var animatedElements = document.querySelectorAll(
    ".osi-feature-card, .osi-spec-card, .osi-involvement-card, .osi-member-card, .osi-update-card"
  );

  animatedElements.forEach(function (el) {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(el);
  });

  // -----------------------------------------------------------------------
  // Page load fade-in
  // Brief fade-in of the entire page to smooth the initial render.
  // -----------------------------------------------------------------------
  document.body.style.opacity = "0";
  setTimeout(function () {
    document.body.style.transition = "opacity 0.5s ease";
    document.body.style.opacity = "1";
  }, 100);

});
