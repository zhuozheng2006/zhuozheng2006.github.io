/* A shuffled portrait sequence; its identical duplicate is presentational only. */
(() => {
  "use strict";

  function initializeBanner() {
    const banner = document.querySelector(".banner");
    if (!banner) return;
    const track = banner.querySelector(".banner__track");
    const group = track?.querySelector(".banner__group");
    if (!track || !group || track.dataset.initialized === "true") return;

    const portraits = Array.from(group.querySelectorAll(":scope > .banner__portrait"));
    if (!portraits.length) return;
    // Fisher–Yates: shuffle once before cloning so the loop seam stays identical.
    for (let i = portraits.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      [portraits[i], portraits[j]] = [portraits[j], portraits[i]];
    }
    group.append(...portraits);

    const duplicate = group.cloneNode(true);
    duplicate.setAttribute("aria-hidden", "true");
    duplicate.setAttribute("inert", "");
    duplicate.removeAttribute("id");
    duplicate.querySelectorAll("[id]").forEach(element => element.removeAttribute("id"));
    duplicate.querySelectorAll("img").forEach(image => { image.alt = ""; });
    track.append(duplicate);
    track.dataset.initialized = "true";

    const viewport = banner.querySelector(".banner__portraits") || banner;
    const deferredImages = Array.from(track.querySelectorAll("img[data-src]"));
    let imageObserver;

    function loadImage(image, priority = "low") {
      const source = image.dataset.src;
      if (!source) return;
      image.decoding = "async";
      image.loading = "eager";
      image.fetchPriority = priority;
      image.src = source;
      image.removeAttribute("data-src");
      imageObserver?.unobserve(image);
    }

    // Start only the visible portraits and two ahead. Fixed panel widths mean
    // this does not need to wait for image downloads or decoding.
    const panelWidth = group.getBoundingClientRect().width / portraits.length || 300;
    const visibleCount = Math.max(1, Math.ceil(viewport.getBoundingClientRect().width / panelWidth));
    portraits.slice(0, visibleCount + 2).forEach((portrait, index) => {
      portrait.querySelectorAll("img[data-src]").forEach(image => {
        loadImage(image, index < visibleCount ? "high" : "low");
      });
    });

    if ("IntersectionObserver" in window) {
      // Observe the actual moving images, relative to the clipped banner.
      // 900px gives roughly 21 seconds of lead time at 42px/s. Observations
      // also update when the viewport is resized or the second group arrives.
      imageObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) loadImage(entry.target);
        });
      }, { root: viewport, rootMargin: "0px 900px", threshold: 0 });
      deferredImages.forEach(image => {
        if (image.dataset.src) imageObserver.observe(image);
      });
    } else {
      // Older browsers keep a complete working sequence without relying on
      // native lazy-loading to notice a CSS transform.
      deferredImages.forEach(image => loadImage(image));
    }

    const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
    function updateMotionPreference() {
      banner.dataset.playing = String(!motionPreference.matches);
    }

    function updateDuration() {
      const distance = group.getBoundingClientRect().width;
      if (distance > 0) track.style.setProperty("--banner-duration", `${distance / 42}s`);
    }

    function updateVisibility() {
      banner.dataset.visible = String(!document.hidden);
    }

    motionPreference.addEventListener("change", updateMotionPreference);
    document.addEventListener("visibilitychange", updateVisibility);

    if ("ResizeObserver" in window) {
      new ResizeObserver(updateDuration).observe(group);
    } else {
      window.addEventListener("resize", updateDuration, { passive: true });
    }

    updateDuration();
    updateVisibility();
    updateMotionPreference();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeBanner, { once: true });
  } else {
    initializeBanner();
  }
})();
