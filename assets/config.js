/* Coolizi — offer config, click-id capture, geo. Affiliate link assembled at click time. */
(function () {
  "use strict";

  // ============ OFFER ROUTING — EDIT HERE TO CHANGE WHERE EACH GEO'S "BUY" BUTTON SENDS TRAFFIC ============
  // Two rails:
  //   • CoolJet geos (en/de/fr/it/es/nl): buy-intent goes to the on-site CoolJet advertorial (/{geo}/cooljet/).
  //     That page carries the CoolJet Stellar-Yonder/Everflow link (geo tag on sub1, gclid on sub2). Because it
  //     is same-origin, the gclid captured on landing (localStorage "cz_track") is read there — nothing to pass.
  //   • Blitz geos (pt/el): NO CoolJet offer exists for PT/GR, so these stay on Blitz Ads/AiraBreeze
  //     (bikiraibn a=2397). Final link = BLITZ_BASE + "&c=<c>&s1=<s1>" (+ "&s2=<clickid>").  INTL creative = 9538.
  // LIVE in ~1 minute, no rebuild.
  var BLITZ_BASE = "https://bikiraibn.com/?a=2397";
  var OFFERS = {
    "en": { direct: "/en/cooljet/" },     // CoolJet UK  advertorial
    "de": { direct: "/de/cooljet/" },     // CoolJet DE/AT advertorial
    "fr": { direct: "/fr/cooljet/" },     // CoolJet FR  advertorial
    "it": { direct: "/it/cooljet/" },     // CoolJet IT  advertorial
    "es": { direct: "/es/cooljet/" },     // CoolJet ES  advertorial
    "nl": { direct: "/nl/cooljet/" },     // CoolJet NL  advertorial
    "pt": { c: "9538", s1: "intl-pt" },   // Blitz/AiraBreeze — no CoolJet PT
    "el": { c: "9538", s1: "intl-gr" }    // Blitz/AiraBreeze — no CoolJet GR
  };
  // ========================================================================================================
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

  function currentOffer() {
    var g = window.GEO || {};
    return (OFFERS && OFFERS[g.code]) || OFFERS.en || {};      // default to EN/CoolJet if geo unknown
  }
  // Does this geo route straight to an on-site advertorial (no AiraBreeze bridge)?
  function isDirect() { return !!currentOffer().direct; }

  // ---- build the outbound "buy" URL (call at click time) ----
  function buildOfferUrl() {
    var off = currentOffer();
    if (off.direct) return off.direct;                         // on-site CoolJet advertorial (gclid already in cz_track)
    // Blitz / AiraBreeze rail (pt, el)
    var u = new URL(BLITZ_BASE);
    if (off.c) u.searchParams.set("c", off.c);
    u.searchParams.set("s1", off.s1 || ("intl-" + ((window.GEO || {}).code || "xx")));
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

  window.COOLIZI = { buildOfferUrl: buildOfferUrl, getGeo: getGeo, getTrack: getTrack, isDirect: isDirect };
})();
