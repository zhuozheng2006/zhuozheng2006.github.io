/* One continuous portrait sequence; its duplicate is presentational only. */
(() => {
  "use strict";

  function initializeBanner() {
    const banner = document.querySelector(".banner");
    if (!banner) return;
    const track = banner.querySelector(".banner__track");
    const group = track?.querySelector(".banner__group");
    const toggle = banner.querySelector(".banner__toggle");
    if (!track || !group || !toggle || track.dataset.initialized === "true") return;
    track.dataset.initialized = "true";

    const duplicate = group.cloneNode(true);
    duplicate.setAttribute("aria-hidden", "true");
    duplicate.setAttribute("inert", "");
    duplicate.removeAttribute("id");
    duplicate.querySelectorAll("[id]").forEach(element => element.removeAttribute("id"));
    duplicate.querySelectorAll("img").forEach(image => { image.alt = ""; });
    track.append(duplicate);

    const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
    let userHasChosen = false;
    let playing = false;

    function setPlaying(next) {
      playing = next;
      banner.dataset.playing = String(playing);
      // The pressed state represents the pause control being engaged.
      toggle.setAttribute("aria-pressed", String(!playing));
      toggle.textContent = playing ? toggle.dataset.pauseLabel : toggle.dataset.playLabel;
    }

    function updateDuration() {
      const distance = group.getBoundingClientRect().width;
      if (distance > 0) track.style.setProperty("--banner-duration", `${distance / 28}s`);
    }

    function updateVisibility() {
      banner.dataset.visible = String(!document.hidden);
    }

    toggle.addEventListener("click", () => {
      userHasChosen = true;
      setPlaying(!playing);
    });
    motionPreference.addEventListener("change", () => {
      if (!userHasChosen) setPlaying(!motionPreference.matches);
    });
    document.addEventListener("visibilitychange", updateVisibility);

    if ("ResizeObserver" in window) {
      new ResizeObserver(updateDuration).observe(group);
    } else {
      window.addEventListener("resize", updateDuration, { passive: true });
    }

    updateDuration();
    updateVisibility();
    setPlaying(!motionPreference.matches);
    toggle.hidden = false;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeBanner, { once: true });
  } else {
    initializeBanner();
  }
})();
