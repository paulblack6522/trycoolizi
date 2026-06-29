/* Coolizi — offer config, click-id capture, geo. Affiliate link assembled at click time. */
(function () {
  "use strict";

  // ============ OFFER LINKS — EDIT HERE TO CHANGE WHERE EACH GEO'S "BUY" BUTTON SENDS TRAFFIC ============
  // NETWORK: Blitz Ads (bikiraibn, affiliate a=2397) → AiraBreeze. To change an offer: edit the "c"
  // (creative id) for a geo, then commit. LIVE in ~1 minute, no rebuild. Keep "s1" (our geo tracking tag).
  // Final link = AFF_BASE + "&c=<c>&s1=<s1>" (+ "&s2=<clickid>" for paid).   DACH creative = 9540, INTL = 9538.
  var AFF_BASE = "https://bikiraibn.com/?a=2397";
  var OFFERS = {
    //  geo :  { c: "<creative id>",  s1: "<tracking tag>" }
    "en": { c: "9538", s1: "intl-uk" },   // INTL → UK / Ireland
    "de": { c: "9540", s1: "try-de"  },   // DACH → DE / AT / CH
    "fr": { c: "9538", s1: "intl-fr" },   // INTL → FR / BE
    "it": { c: "9538", s1: "intl-it" },   // INTL → Italy
    "es": { c: "9538", s1: "intl-es" },   // INTL → Spain
    "nl": { c: "9538", s1: "intl-nl" },   // INTL → Netherlands
    "pt": { c: "9538", s1: "intl-pt" },   // INTL → Portugal
    "el": { c: "9538", s1: "intl-gr" }    // INTL → Greece
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
    var off = (OFFERS && OFFERS[g.code]) || OFFERS.en || {};   // default to INTL/EN if geo unknown
    var c = off.c;
    var s1 = off.s1 || ("intl-" + (g.code || "xx"));
    var u = new URL(AFF_BASE);
    if (c) u.searchParams.set("c", c);
    u.searchParams.set("s1", s1);
    // pass any paid click-id into s2 for later reconciliation
    var t = getTrack();
    var clickid = t.gclid || t.fbclid || t.ttclid || t.msclkid;
    if (clickid) u.searchParams.set("s2", clickid);
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
