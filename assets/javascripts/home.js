/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/*
 * home.js — Animations and interactive effects for the Apache Ossie landing page.
 *
 * This script only targets elements with "ossie-" prefixed classes, so it
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
    ".ossie-feature-card, .ossie-involvement-card, .ossie-member-card, " +
    ".ossie-update-card, .ossie-check-item, .ossie-code-block, .ossie-stat, " +
    ".ossie-pitch-card, .ossie-class-card, .ossie-wg-card, .ossie-community-bar"
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
