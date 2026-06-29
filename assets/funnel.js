/* Coolizi — funnel behaviour: reveal anim, countdown, FOMO, ticker, exit-intent, redirect. */
(function () {
  "use strict";
  var G = window.GEO || {};
  var I = G.i18n || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var rnd = function (a) { return a[Math.floor(Math.random() * a.length)]; };

  /* ---------- subtle reveal-on-scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); }
  // backstop: never leave content hidden if the observer misses (non-scrolling sessions, bots)
  setTimeout(function () { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); }, 4000);

  /* ---------- evergreen countdown ---------- */
  var WINDOW = 15 * 60 * 1000;
  function cdEnd() {
    var e = +localStorage.getItem("cz_cd_end");
    if (!e || e < Date.now()) { e = Date.now() + WINDOW; localStorage.setItem("cz_cd_end", e); }
    return e;
  }
  var END = cdEnd();
  function tickCd() {
    var left = Math.max(0, END - Date.now());
    var m = Math.floor(left / 60000), s = Math.floor((left % 60000) / 1000);
    var txt = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
    $$("[data-cd]").forEach(function (el) { el.textContent = txt; });
    $$("[data-mcd]").forEach(function (el) { el.textContent = txt; });
    if (left <= 0) { END = Date.now() + WINDOW; localStorage.setItem("cz_cd_end", END); }
  }
  tickCd(); setInterval(tickCd, 1000);

  /* ---------- low stock + viewers ---------- */
  var stock = +localStorage.getItem("cz_stock") || (6 + Math.floor(Math.random() * 8));
  function paintStock() { $$("[data-stock]").forEach(function (e) { e.textContent = stock; }); }
  paintStock();
  setInterval(function () { if (stock > 2 && Math.random() < 0.16) { stock--; localStorage.setItem("cz_stock", stock); paintStock(); } }, 11000);

  /* ---------- low-stock alert bar (above footer) ---------- */
  var stock2 = +localStorage.getItem("cz_stock2") || (38 + Math.floor(Math.random() * 9)); // ~38-46
  function paintStock2() {
    $$("[data-stock2]").forEach(function (e) { e.textContent = stock2; });
    var pct = Math.max(6, Math.min(22, stock2 / 3)); // always reads "low" (~13-15%)
    $$("[data-stockbar]").forEach(function (e) { e.style.width = pct + "%"; });
  }
  paintStock2();
  setInterval(function () { if (stock2 > 7 && Math.random() < 0.22) { stock2--; localStorage.setItem("cz_stock2", stock2); paintStock2(); } }, 9000);

  var viewers = 14 + Math.floor(Math.random() * 33);
  function paintViewers() { $$("[data-viewers]").forEach(function (e) { e.textContent = viewers; }); }
  paintViewers();
  setInterval(function () { viewers += (Math.random() < 0.5 ? -1 : 2); if (viewers < 8) viewers = 8; paintViewers(); }, 4200);

  /* ---------- sticky buy bar ---------- */
  var bar = $(".stickybar");
  if (bar) addEventListener("scroll", function () {
    bar.classList.toggle("show", scrollY > innerHeight * 0.6);
  }, { passive: true });

  /* ---------- language dropdown ---------- */
  var lang = $(".lang");
  if (lang) {
    $(".lang button").addEventListener("click", function (e) { e.stopPropagation(); lang.classList.toggle("open"); });
    document.addEventListener("click", function () { lang.classList.remove("open"); });
  }

  /* ---------- FAQ accordion ---------- */
  $$(".faq-item").forEach(function (it) {
    $(".faq-q", it).addEventListener("click", function () {
      var open = it.classList.toggle("open");
      var a = $(".faq-a", it);
      a.style.maxHeight = open ? a.scrollHeight + "px" : 0;
    });
  });

  /* ---------- bridge (Coolizi sold out -> AiraBreeze) + redirect overlay ---------- */
  var redirecting = false;
  var bridge = $("#bridge");
  function showBridge() {
    if (redirecting) return;
    if (!bridge) { goOffer(); return; }                              // no bridge in DOM -> straight to offer
    bridge.classList.add("show");
  }
  function hideBridge() { if (bridge) bridge.classList.remove("show"); }
  function goOffer() {
    if (redirecting) return; redirecting = true;
    if (bridge) bridge.classList.remove("show");                     // never stack popups over the redirect
    var ov = $("#redirect"); if (ov) ov.classList.add("show");
    var url = (window.COOLIZI && window.COOLIZI.buildOfferUrl && window.COOLIZI.buildOfferUrl()) || "https://bikiraibn.com/?a=2397";
    var nav = function () { try { window.location.href = url; } catch (e) { try { window.location.assign(url); } catch (e2) {} } };
    setTimeout(nav, 650);                                            // quick hand-off
    setTimeout(function () { if (!document.hidden) nav(); }, 3500);  // hard fallback if the first navigation didn't take
  }
  document.addEventListener("click", function (e) {
    if (e.target.closest(".js-go")) { e.preventDefault(); goOffer(); return; }      // bridge CTA -> AiraBreeze
    if (e.target.closest(".js-bx")) { e.preventDefault(); hideBridge(); return; }   // bridge dismiss (× / decline)
    var t = e.target.closest(".js-cta"); if (!t) return;
    e.preventDefault(); showBridge();                                              // any buy intent -> bridge first
  });

  /* ---------- auto-advance to the offer after engagement (bot-safe) ---------- */
  // Never fires for crawlers/automation (protects SEO) or before a real interaction.
  if (!navigator.webdriver) {
    var armed = false;
    var arm = function () {
      if (armed) return; armed = true;
      setTimeout(function () { if (!document.hidden && !redirecting) showBridge(); }, 30000);
    };
    ["scroll", "mousemove", "touchstart", "keydown", "pointerdown"].forEach(function (ev) {
      addEventListener(ev, arm, { once: true, passive: true });
    });
  }

  /* ---------- social-proof ticker ---------- */
  var toast = $("#sp-toast");
  if (toast && window.COOLIZI) {
    window.COOLIZI.getGeo().then(function (geo) {
      var cities = G.cities || ["Berlin"];
      var names = G.names || ["Alex M."];
      var products = I.products || ["2× Coolizi"];
      var tpl = I.tpl || "<b>{name}</b> in {city} just bought {product}";
      var count = 0;

      function agoText(min) {
        if (min <= 1) return I.ago_just || "just now";
        return (I.ago_min || "{n} min ago").replace("{n}", min);
      }
      function build() {
        // show the visitor's detected city ~40% of the time, else a random local city
        var city = (geo.city && Math.random() < 0.4) ? geo.city : rnd(cities);
        var line = tpl.replace("{name}", "<b>" + rnd(names) + "</b>").replace("{city}", city).replace("{product}", rnd(products));
        var min = 1 + Math.floor(Math.random() * 27);
        return '<img src="' + (G.thumb || "") + '" alt="">' +
               '<div class="sp-b">' + line + '<span class="sp-ago">✔ ' + (I.verified || "Verified") + " · " + agoText(min) + "</span></div>" +
               '<span class="sp-x" aria-label="close">×</span>';
      }
      function show() {
        if (count++ >= 14) return;
        if (!document.hidden) {
          toast.innerHTML = build();
          toast.classList.add("show");
          $(".sp-x", toast).addEventListener("click", function () { toast.classList.remove("show"); });
          setTimeout(function () { toast.classList.remove("show"); }, 5200);
        }
        setTimeout(show, 8500 + Math.random() * 12000);
      }
      setTimeout(show, 5200);
    });
  }

  /* ---------- exit-intent + back-button trap -> bridge (no backdrop escape) ---------- */
  function showExit() {
    if (!bridge || redirecting) return;
    if (sessionStorage.getItem("cz_exit")) return;
    sessionStorage.setItem("cz_exit", "1");
    showBridge();
  }
  if (bridge) {
    // desktop: cursor leaves toward the top
    document.addEventListener("mouseout", function (e) {
      if (e.clientY <= 0 && !e.relatedTarget) showExit();
    });
    // mobile + desktop: back-button trap (one extra push to re-capture)
    try {
      history.pushState(null, "", location.href);
      addEventListener("popstate", function () {
        if (!sessionStorage.getItem("cz_exit")) { showExit(); history.pushState(null, "", location.href); }
      });
    } catch (e) {}
    // dismiss only via × / decline (handled in the click delegator) — NO backdrop close, keep them on the deal
  }
})();
