/* Coolizi — offer config, click-id capture, geo. Affiliate link assembled at click time. */
(function () {
  "use strict";

  // ============ OFFER LINKS — EDIT HERE TO CHANGE WHERE EACH GEO'S "BUY" BUTTON SENDS TRAFFIC ============
  // NETWORK: Influx (Everflow). To change an offer: paste the new "url" (the offer's tracking link from
  // Influx) for a geo below, then commit. LIVE in ~1 minute, no rebuild. Keep "s1" (our geo tracking tag).
  // Final link = <url> + "?sub1=<s1>" (+ "&sub2=<clickid>" if a paid click-id is present).
  var OFFERS = {
    //  geo :  { url: "<Influx/Everflow tracking link>",            s1: "<tracking sub-id>" }
    "en": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D6NGN16/", s1: "try-uk" },  // UK / Ireland
    "de": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D6JB1RC/", s1: "try-de" },  // DE / AT / CH
    "fr": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D6M3R8K/", s1: "try-fr" },  // FR / BE
    "it": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D726T5F/", s1: "try-it" },  // Italy
    "es": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D73KPW2/", s1: "try-es" },  // Spain
    "nl": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D6W26XL/", s1: "try-nl" },  // Netherlands
    "pt": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D6ZRZDS/", s1: "try-pt" },  // Portugal
    "el": { url: "https://www.abjdoi4kjd.com/27DJQ2C/D6XF3N7/", s1: "try-gr" }   // Greece
  };
  // ======================================================================================================
  var IPINFO_TOKEN = "fcc8c88c9a040a"; // geo provider for the social-proof ticker (ipwho.is is the fallback)

  // ---- capture inbound click-ids ONCE (first-touch) ----
  var TRACK_KEYS = ["gclid", "fbclid", "ttclid", "msclkid", "utm_source", "utm_campaign", "utm_medium", "s1", "s2"];
  function captureClickIds() {
    try {
      var q = new URLSearchParams(location.search);
      var store = JSON.parse(localStorage.getItem("cz_track") || "{}");
      TRACK_KEYS.forEach(function (k) { var v = q.get(k); if (v && !store[k]) store[k] = v; });
      if (!store._ts) store._ts = Date.now();
      if (!store._lp) store._lp = location.pathname;
      localStorage.setItem("cz_track", JSON.stringify(store));
    } catch (e) {}
  }
  captureClickIds();

  function getTrack() { try { return JSON.parse(localStorage.getItem("cz_track") || "{}"); } catch (e) { return {}; } }

  // ---- build the outbound affiliate URL (call at click time) ----
  function buildOfferUrl() {
    var g = window.GEO || {};
    var off = (OFFERS && OFFERS[g.code]) || OFFERS.en || {};   // default to EN if geo unknown
    var s1 = off.s1 || ("try-" + (g.code || "xx"));
    var u = new URL(off.url || "https://www.abjdoi4kjd.com/27DJQ2C/D6NGN16/");
    u.searchParams.set("sub1", s1);                            // our geo tracking tag -> Everflow sub1
    // pass any paid click-id into sub2 for later reconciliation
    var t = getTrack();
    var clickid = t.gclid || t.fbclid || t.ttclid || t.msclkid;
    if (clickid) u.searchParams.set("sub2", clickid);
    return u.toString();
  }

  // ---- visitor geo for the social-proof ticker (ipinfo -> ipwho.is -> page default) ----
  function getGeo() {
    return new Promise(function (resolve) {
      try {
        var cached = JSON.parse(localStorage.getItem("cz_geo") || "null");
        if (cached && cached.cc) return resolve(cached);
      } catch (e) {}

      var def = { cc: (window.GEO && window.GEO.cc) || "DE", city: null };
      var done = false;
      function finish(geo) {
        if (done) return; done = true;
        try { localStorage.setItem("cz_geo", JSON.stringify(geo)); } catch (e) {}
        resolve(geo);
      }
      // hard timeout so the ticker never blocks
      var timer = setTimeout(function () { finish(def); }, 3000);

      function tryIpinfo() {
        fetch("https://ipinfo.io/json?token=" + IPINFO_TOKEN, { cache: "no-store" })
          .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
          .then(function (d) {
            if (d && d.country) { clearTimeout(timer); finish({ cc: d.country, city: d.city || null }); }
            else tryIpwho();
          })
          .catch(tryIpwho);
      }
      function tryIpwho() {
        fetch("https://ipwho.is/", { cache: "no-store" })
          .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
          .then(function (d) {
            clearTimeout(timer);
            finish({ cc: (d && d.country_code) || def.cc, city: (d && d.city) || null });
          })
          .catch(function () { clearTimeout(timer); finish(def); });
      }
      tryIpinfo();
    });
  }

  window.COOLIZI = { buildOfferUrl: buildOfferUrl, getGeo: getGeo, getTrack: getTrack };
})();
