/*
 * home.js — Animations and interactive effects for the OSI landing page.
 *
 * This script only targets elements with "osi-" prefixed classes, so it
 * will not interfere with standard MkDocs docs/blog pages.
 */

document.addEventListener("DOMContentLoaded", function () {

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

  var animatedElements = document.querySelectorAll(
    ".osi-feature-card, .osi-involvement-card, .osi-member-card, " +
    ".osi-update-card, .osi-check-item, .osi-code-block, .osi-stat, " +
    ".osi-pitch-card, .osi-class-card, .osi-wg-card, .osi-community-bar"
  );

  animatedElements.forEach(function (el) {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(el);
  });

  document.body.style.opacity = "0";
  setTimeout(function () {
    document.body.style.transition = "opacity 0.5s ease";
    document.body.style.opacity = "1";
  }, 100);

});
