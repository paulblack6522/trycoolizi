/* Coolizi — offer config, click-id capture, geo. Affiliate link assembled at click time. */
(function () {
  "use strict";

  // ============ OFFER LINKS — EDIT HERE TO CHANGE WHERE EACH GEO'S "BUY" BUTTON SENDS TRAFFIC ============
  // To change an offer: edit the "c" (creative / offer id from the network) for a geo below, then commit.
  // It goes LIVE in ~1 minute, no rebuild. Only change "s1" if the network tells you to.
  // Final link = AFF_BASE + "&c=<c>&s1=<s1>".  AFF_BASE = the network + your affiliate id (a=2397).
  var AFF_BASE = "https://bikiraibn.com/?a=2397";
  var OFFERS = {
    //  geo :  { c: "<creative / offer id>",  s1: "<tracking sub-id>" }
    "en": { c: "9578", s1: "try-uk" },   // UK / English  (Coolizi)
    "de": { c: "9553", s1: "try-de" },   // DE / AT / CH  (Coolizi)
    "fr": { c: "9558", s1: "try-fr" },   // FR / BE       (Coolizi)
    "it": { c: "9598", s1: "try-it" },   // Italy         (Coolizi)
    "es": { c: "9587", s1: "try-es" },   // Spain         (Coolizi)
    "nl": { c: "9590", s1: "try-nl" },   // Netherlands   (Coolizi)
    "pt": { c: "9601", s1: "try-pt" },   // Portugal      (Coolizi)
    "el": { c: "9596", s1: "try-gr" }    // Greece        (Coolizi)
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
    var off = (OFFERS && OFFERS[g.code]) || {};   // central OFFERS wins; page-baked value is a safe fallback
    var c = off.c || g.c;
    var s1 = off.s1 || g.s1 || ("try-" + (g.code || "xx"));
    var u = new URL(AFF_BASE);
    if (c) u.searchParams.set("c", c);
    u.searchParams.set("s1", s1);
    // pass any paid click-id into s2 for later reconciliation (ignored harmlessly if unused)
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
