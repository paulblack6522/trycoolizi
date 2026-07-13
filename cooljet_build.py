#!/usr/bin/env python3
# CoolJet advertorial generator -> /{geo}/cooljet/index.html for 6 geos (en/de/fr/it/es/nl).
# Advertorial, disclosure at FOOT. Sample-style (red ticker, heat map, myths, before/after photo,
# 6 reasons, comparison, verdict, bundle picker, exit-intent popup). Honest: NO fabricated review
# counts, NO fake named testimonials, NO fake ticking countdown, NO invented stock numbers.
# CTA -> CoolJet (Stellar Yonder/Everflow ZZ2GX): geo tag on sub1, gclid on sub2.
import os
OUT = os.path.dirname(os.path.abspath(__file__))
EF = "https://www.slmw4qtrk.com/ZZ2GX/{code}/"

STYLE = """
  :root{--ink:#16181d;--muted:#5b636e;--line:#e7e9ee;--bg:#fff;--soft:#f6f8fa;--brand:#0a84c9;--brand-d:#0769a3;--red:#d90429;--red-d:#a80320;--orange:#ff5a00;--green:#00a651;--green-d:#0b8a47;--amber:#e0a100;--shadow:0 12px 34px rgba(20,30,45,.12);--serif:Georgia,"Times New Roman",serif;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  *{box-sizing:border-box}html,body{margin:0;padding:0}
  body{font-family:var(--sans);color:var(--ink);background:var(--soft);line-height:1.62;-webkit-font-smoothing:antialiased}
  img{max-width:100%;height:auto;display:block}a{color:var(--brand-d)}
  .ic{width:1em;height:1em;display:inline-block;vertical-align:-.14em;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
  .ticker{background:var(--red);color:#fff;overflow:hidden;white-space:nowrap;font-weight:800;font-size:12.5px;letter-spacing:.04em}
  .ticker .run{display:flex;width:max-content;animation:tick 30s linear infinite}
  .ticker .seg{padding:8px 0;flex:0 0 auto}
  @keyframes tick{from{transform:translateX(0)}to{transform:translateX(-50%)}}
  .mast{background:var(--bg);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:30}
  .mast .in{max-width:720px;margin:0 auto;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;gap:12px}
  .logo{font-family:var(--serif);font-weight:700;font-size:20px}.logo .b{color:var(--brand-d)}
  .mast .date{font-size:12px;color:var(--muted);text-align:right;line-height:1.35}
  .wrap{max-width:720px;margin:0 auto;padding:0 18px}
  article{background:var(--bg);margin:16px auto;border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--shadow)}
  .pad{padding:24px 22px}@media(max-width:560px){.pad{padding:18px 15px}}
  .kick{display:inline-flex;align-items:center;gap:7px;background:#fdecec;color:var(--red);font-weight:800;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;padding:6px 11px;border-radius:6px}
  .lv{width:8px;height:8px;border-radius:50%;background:currentColor;animation:blink 1.05s infinite}@keyframes blink{50%{opacity:.2}}
  h1{font-family:var(--serif);font-weight:700;font-size:34px;line-height:1.14;margin:13px 0 10px;letter-spacing:-.015em}@media(max-width:560px){h1{font-size:26px}}
  h1 .hl{background:linear-gradient(180deg,transparent 62%,#ffe08a 62%);padding:0 2px}
  .stand{font-size:18.5px;color:#333b45;margin:0 0 16px}
  .byline{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-size:13px;color:var(--muted);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:11px 0;margin-bottom:18px}
  .byline .spon{background:#eef4f9;color:var(--brand-d);font-weight:700;padding:3px 8px;border-radius:5px;font-size:11.5px}.byline .dot{color:#c4cad2}
  article p{font-size:17px;margin:0 0 15px}
  h2{font-family:var(--serif);font-size:24px;margin:30px 0 12px;letter-spacing:-.01em;display:flex;align-items:center;gap:9px}
  h2 .em{font-size:26px;line-height:1}
  .lead::first-letter{font-family:var(--serif);float:left;font-size:58px;line-height:.8;padding:6px 10px 0 0;color:var(--red);font-weight:700}
  .hero{position:relative;background:radial-gradient(120% 130% at 50% 0,#e9f7ff,#f3fbff 55%,#fff);border:1px solid #e0f0f8;border-radius:14px;padding:14px;text-align:center;overflow:hidden}
  .hero .cjlogo{position:relative;z-index:3;height:26px;width:auto;margin:2px auto 6px}
  .hero .prod{position:relative;z-index:2;margin:0 auto;max-height:340px;width:auto;filter:drop-shadow(0 16px 24px rgba(10,90,140,.22));animation:rise .9s ease both}
  @keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
  .flake{position:absolute;z-index:1;color:#bfe4f5;opacity:.7;animation:floaty linear infinite}
  @keyframes floaty{0%{transform:translateY(-6px) rotate(0)}50%{transform:translateY(10px) rotate(180deg)}100%{transform:translateY(-6px) rotate(360deg)}}
  .badgeR{position:absolute;z-index:3;top:12px;left:12px;background:var(--red);color:#fff;font-weight:800;font-size:11.5px;padding:6px 11px;border-radius:20px;box-shadow:0 4px 12px rgba(217,4,41,.4)}
  .badgeR::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;background:#fff;margin-right:6px;vertical-align:1px;animation:blink 1.05s infinite}
  figcaption{font-size:12.5px;color:var(--muted);text-align:center;margin-top:8px;font-style:italic}
  .heat{display:flex;gap:12px;align-items:center;background:linear-gradient(90deg,#fff2ee,#fff8f5);border:1px solid #ffd6c4;border-left:4px solid var(--orange);border-radius:10px;padding:14px 16px;margin:18px 0;font-weight:600}
  .heat .t{font-size:30px;line-height:1}
  .lifeimg{border-radius:14px;overflow:hidden;border:1px solid var(--line);margin:16px 0}.lifeimg img{width:100%;display:block}
  .lifecap{font-size:12.5px;color:var(--muted);font-style:italic;text-align:center;margin:8px 0 0}
  .heatmap{border:2px solid var(--red);border-radius:14px;overflow:hidden;margin:18px 0}
  .hm-head{background:var(--red);color:#fff;font-weight:800;font-size:13.5px;padding:9px 14px;display:flex;align-items:center;gap:8px;letter-spacing:.03em}
  .hm-map{position:relative;height:300px;background:linear-gradient(135deg,#ffd24d,#ff7a1a 55%,#d90429)}
  .hm-map .isle{position:absolute;fill:rgba(255,255,255,.14);stroke:rgba(255,255,255,.45);stroke-width:2}
  .pin{position:absolute;transform:translate(-50%,-50%);background:rgba(255,255,255,.94);color:#a80320;font-weight:800;font-size:11px;padding:3px 7px;border-radius:20px;white-space:nowrap;box-shadow:0 2px 6px rgba(0,0,0,.28)}
  .pin b{font-size:12.5px}.pin.hot{background:#fff;color:var(--red);font-size:12px}
  .pin.hot::after{content:"";position:absolute;inset:-5px;border:2px solid #fff;border-radius:22px;opacity:.7;animation:ping 1.7s infinite}
  @keyframes ping{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.7);opacity:0}}
  .hm-foot{background:#1a1a2e;color:#c9d0da;font-size:11px;padding:6px 14px;display:flex;justify-content:space-between}
  .myth{display:flex;gap:12px;align-items:flex-start;border:1px solid var(--line);border-radius:12px;padding:13px 15px;margin-bottom:10px;background:#fff}
  .myth .x{flex:0 0 24px;width:24px;height:24px;color:var(--red)}.myth b{display:block;margin-bottom:3px}
  .myth .fix{color:var(--green-d);font-weight:600;font-size:14.5px;display:flex;gap:6px;align-items:flex-start;margin-top:6px}
  .myth .fix .c{flex:0 0 18px;width:18px;height:18px;color:var(--green)}
  .note{background:#fffdf5;border:1px solid #f0e4bd;border-left:4px solid var(--amber);border-radius:10px;padding:16px 18px;margin:20px 0}.note b{display:block;margin-bottom:4px}
  .chips{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:16px 0}
  @media(max-width:560px){.chips{grid-template-columns:repeat(2,1fr)}}
  .chip{background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:12px 8px;text-align:center}
  .chip img{width:38px;height:38px;margin:0 auto 6px}.chip span{font-size:12.5px;font-weight:700;color:#333b45}
  .reasons{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:14px 0}
  @media(max-width:560px){.reasons{grid-template-columns:1fr}}
  .reason{display:flex;gap:11px;align-items:flex-start;background:#f2fbf6;border:1px solid #cdeddb;border-radius:12px;padding:13px 14px}
  .reason .c{flex:0 0 26px;width:26px;height:26px;color:var(--green)}.reason h4{margin:0 0 3px;font-size:15px}.reason p{margin:0;font-size:13.5px;color:var(--muted)}
  .cmp{width:100%;border-collapse:collapse;margin:14px 0;font-size:15px;border:1px solid var(--line);border-radius:12px;overflow:hidden}
  .cmp th,.cmp td{padding:11px 10px;text-align:center;border-bottom:1px solid var(--line);vertical-align:middle}
  .cmp thead th{background:#1a1a2e;color:#fff;font-size:12.5px;text-transform:uppercase;letter-spacing:.03em}
  .cmp thead th.cj{background:var(--brand)}
  .cmp td:first-child,.cmp th:first-child{text-align:left;font-weight:600;color:#333b45}
  .cmp .cjcol{background:#f5fbff;font-weight:700}.cmp tbody tr:last-child td{border-bottom:none}
  .cmp .c{width:20px;height:20px;color:var(--green)}.cmp .x{width:20px;height:20px;color:var(--red)}
  @media(max-width:560px){.cmp,.cmp th,.cmp td{font-size:12.5px;padding:9px 6px}}
  .verdict{border:1px solid var(--line);border-radius:16px;padding:20px;margin:22px 0;text-align:center;background:linear-gradient(180deg,#fffdf6,#fff)}
  .verdict .score{font-size:46px;font-weight:800;line-height:1}.verdict .stars{color:#f5a623;font-size:26px;letter-spacing:2px;margin:4px 0}.verdict .who{font-size:13px;color:var(--muted)}
  .vtwo{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px;text-align:left}@media(max-width:520px){.vtwo{grid-template-columns:1fr}}
  .vcol{border:1px solid var(--line);border-radius:12px;padding:13px 15px}.vcol h4{margin:0 0 7px;font-size:14px}
  .vcol ul{margin:0;padding-left:0;list-style:none;font-size:14px}.vcol li{display:flex;gap:7px;margin-bottom:6px;align-items:flex-start}
  .vcol .mk{flex:0 0 17px;width:17px;height:17px;margin-top:2px}.vgood h4{color:var(--green-d)}.vgood .mk{color:var(--green)}.vwarn h4{color:var(--orange)}.vwarn .mk{color:var(--orange)}
  .deal{border:2px solid var(--brand);border-radius:16px;padding:20px;margin:24px 0;background:linear-gradient(180deg,#f7fdff,#fff)}
  .deal .dhead{text-align:center;margin-bottom:14px}.deal .dhead .badge{display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:12px;letter-spacing:.04em;padding:5px 12px;border-radius:20px;text-transform:uppercase}
  .bundles{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0 12px}
  .bundle{position:relative;border:2px solid var(--line);border-radius:12px;padding:16px 8px 12px;text-align:center;cursor:pointer;background:#fff;transition:border-color .15s,box-shadow .15s}
  .bundle:hover{border-color:#bfe0f2}.bundle.sel{border-color:var(--brand);box-shadow:0 6px 18px rgba(10,132,201,.18)}
  .bundle .rib{position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:var(--green);color:#fff;font-size:10.5px;font-weight:800;padding:3px 9px;border-radius:10px;white-space:nowrap;text-transform:uppercase}
  .bundle .q{font-weight:800;font-size:14.5px}.bundle .pu{font-size:21px;font-weight:800;margin:5px 0 0}.bundle .pu small{font-size:12px;font-weight:600;color:var(--muted)}.bundle .sv{font-size:11.5px;color:var(--green-d);font-weight:800;margin-top:3px}
  .price{display:flex;align-items:baseline;justify-content:center;gap:10px;margin:6px 0 2px}.price .now{font-size:34px;font-weight:800}.price .was{font-size:18px;color:var(--muted);text-decoration:line-through}
  .price .off{background:#fdecec;color:var(--red);font-weight:800;font-size:13px;padding:3px 9px;border-radius:6px}
  .seal{display:flex;align-items:center;justify-content:center;gap:12px;margin:12px 0;font-size:13px;color:#333b45}.seal img{width:64px;height:auto}
  .cta{display:block;width:100%;max-width:440px;margin:14px auto 4px;background:linear-gradient(180deg,#12b257,var(--green-d));color:#fff;text-align:center;text-decoration:none;font-weight:800;font-size:19px;padding:17px 20px;border-radius:12px;box-shadow:0 10px 22px rgba(16,150,80,.32);animation:cpulse 2.1s ease-in-out infinite}
  @keyframes cpulse{0%,100%{transform:scale(1)}50%{transform:scale(1.02)}}.cta:hover{filter:brightness(1.05)}.cta .arw{margin-left:6px}.cta.mini{max-width:360px;font-size:16px;padding:13px}
  .trustrow{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;font-size:12.5px;color:var(--muted);margin-top:10px}.trustrow span{display:inline-flex;gap:5px;align-items:center}.trustrow .c{width:15px;height:15px;color:var(--green)}
  details{border:1px solid var(--line);border-radius:10px;padding:2px 14px;margin-bottom:10px;background:#fff}
  summary{font-weight:700;padding:12px 0;cursor:pointer;font-size:15.5px;list-style:none}summary::-webkit-details-marker{display:none}
  summary::after{content:"+";float:right;color:var(--brand-d);font-weight:800}details[open] summary::after{content:"\\2013"}details p{font-size:15px;margin:0 0 12px}
  .imagine{background:linear-gradient(180deg,#eef7fd,#fff);border:1px solid #d6ebf7;border-radius:14px;padding:18px 20px;margin:22px 0;font-size:16.5px;font-style:italic;color:#26303a}
  .urg{margin:24px 0 6px;border-radius:16px;overflow:hidden;border:2px solid var(--red)}
  .urg .top{background:repeating-linear-gradient(45deg,var(--red),var(--red) 14px,var(--red-d) 14px,var(--red-d) 28px);color:#fff;padding:11px 16px;font-weight:800;letter-spacing:.03em;font-size:14px;display:flex;align-items:center;gap:9px}
  .urg .body{padding:20px;background:linear-gradient(180deg,#fff6f6,#fff)}.urg h3{margin:0 0 8px;font-size:22px;font-family:var(--serif)}.urg p{font-size:15.5px;margin:0 0 14px}
  .urg .pill{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--red);color:var(--red);font-weight:800;font-size:14px;padding:8px 14px;border-radius:999px;margin-bottom:14px}
  .foot{max-width:720px;margin:8px auto 30px;padding:18px;color:var(--muted);font-size:12.5px;text-align:center;line-height:1.7}
  .foot a{color:var(--muted);text-decoration:underline;margin:0 6px}.foot .aff{background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin-bottom:14px;text-align:left}
  .sticky{position:fixed;left:0;right:0;bottom:0;background:rgba(255,255,255,.97);backdrop-filter:blur(8px);border-top:1px solid var(--line);padding:9px 14px;display:none;z-index:40;box-shadow:0 -6px 20px rgba(0,0,0,.07)}
  .sticky .row{max-width:720px;margin:0 auto;display:flex;align-items:center;gap:12px}.sticky .p{font-weight:800;font-size:15px;white-space:nowrap}.sticky .p small{display:block;font-weight:600;color:var(--muted);font-size:11px;text-decoration:line-through}
  .sticky .cta{margin:0;flex:1;padding:13px;font-size:16px;animation:none}
  @media(max-width:720px){.sticky{display:block}body{padding-bottom:76px}}
  .ep-bg{position:fixed;inset:0;background:rgba(0,0,0,.7);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);z-index:60;display:none;align-items:center;justify-content:center;padding:18px}
  .ep-bg.show{display:flex}
  .ep{position:relative;background:linear-gradient(140deg,#e60b2e,#a80320 85%);color:#fff;border-radius:18px;max-width:450px;width:100%;padding:30px 26px 20px;text-align:center;box-shadow:0 24px 70px rgba(120,0,12,.55),0 0 0 4px rgba(255,255,255,.06);animation:epin .42s cubic-bezier(.2,1.25,.4,1) both}
  @keyframes epin{from{transform:scale(.8);opacity:0}to{transform:scale(1);opacity:1}}
  .ep .epclose{position:absolute;top:12px;right:14px;border:none;background:rgba(255,255,255,.16);color:#fff;width:30px;height:30px;border-radius:50%;font-size:18px;cursor:pointer;line-height:1}
  .ep .eic{font-size:48px;line-height:1;filter:drop-shadow(0 3px 6px rgba(0,0,0,.25))}
  .ep .eptitle{font-family:var(--serif);font-weight:800;font-size:25px;line-height:1.24;margin:8px 0}
  .ep .eptext{font-size:16px;opacity:.94;line-height:1.55;margin:0 0 16px}.ep .eptext strong{color:#ffe08a}
  .ep .epcta{display:block;width:100%;background:#fff;color:var(--red);text-decoration:none;font-weight:800;font-size:18.5px;padding:16px 20px;border-radius:14px;box-shadow:0 8px 20px rgba(0,0,0,.28);transition:transform .18s ease;animation:eppulse 1.9s ease-in-out infinite}
  @keyframes eppulse{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
  .ep .epcta:hover{transform:scale(1.04)}
  .ep .epno{display:block;width:100%;margin-top:12px;background:none;border:none;color:rgba(255,255,255,.72);font-size:13px;text-decoration:underline;cursor:pointer}
  .reveal{opacity:0;transform:translateY(16px);transition:opacity .55s ease,transform .55s ease}.reveal.in{opacity:1;transform:none}
  @media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}.cta,.flake,.lv,.badgeR::before{animation:none}}
"""

SPRITE = """<svg style="display:none" aria-hidden="true">
  <symbol id="i-check" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.4 2.4 4.6-4.8"/></symbol>
  <symbol id="i-x" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m9 9 6 6M15 9l-6 6"/></symbol>
  <symbol id="i-alert" viewBox="0 0 24 24"><path d="M12 3 2 20h20L12 3Z"/><path d="M12 9v5M12 17h.01"/></symbol>
  <symbol id="i-snow" viewBox="0 0 24 24"><path d="M12 2v20M4 6l16 12M20 6 4 18"/></symbol>
</svg>"""

ISLE = '<svg class="isle" width="100%" height="100%" viewBox="0 0 300 300" preserveAspectRatio="xMidYMid meet" aria-hidden="true"><path class="isle" d="M150 22c10 6 6 20 14 26s18 4 20 16-14 16-10 28 16 10 14 24-18 8-22 22-2 26-16 34-24-2-34-14-6-24-18-30-22-4-24-18 14-16 12-30-10-22 0-32 20-2 28-14 14-30 24-36 24 8 22-6Z"/></svg>'
CHIP_ICONS = ["f-cooling.png", "f-switch.png", "f-quiet.png", "f-energy.png"]


def flakes():
    p = [(7,16,20,7,0),(22,9,14,9,.5),(80,12,16,8,.3),(90,24,12,10,.8)]
    return "".join(f'<span class="flake" style="left:{l}%;top:{t}%;width:{s}px;height:{s}px;animation-duration:{d}s;animation-delay:{dl}s"><svg class="ic"><use href="#i-snow"/></svg></span>' for l,t,s,d,dl in p)

def mark(v):
    return '<svg class="ic c"><use href="#i-check"/></svg>' if v=="c" else ('<svg class="ic x"><use href="#i-x"/></svg>' if v=="x" else "—")

def page(g):
    ef = EF.format(code=g["ef"])
    ticker = "".join(f'<div class="seg"{"" if i==0 else " aria-hidden=\"true\""}>{g["ticker"]}</div>' for i in range(2))
    pins = "".join(f'<div class="pin{" hot" if hot else ""}" style="left:{x}%;top:{y}%">{n} <b>{t}°</b></div>' for n,t,x,y,hot in g["cities"])
    myths = "".join(f'<div class="myth reveal"><svg class="ic x"><use href="#i-x"/></svg><div><b>{c}</b>{tr}<div class="fix"><svg class="ic c"><use href="#i-check"/></svg><span>{fx}</span></div></div></div>' for c,tr,fx in g["myths"])
    chips = "".join(f'<div class="chip"><img src="/assets/img/cj/{CHIP_ICONS[i]}" alt=""><span>{lbl}</span></div>' for i,lbl in enumerate(g["chips"]))
    reasons = "".join(f'<div class="reason reveal"><svg class="ic c"><use href="#i-check"/></svg><div><h4>{t}</h4><p>{d}</p></div></div>' for t,d in g["reasons"])
    rows = "".join(f'<tr><td>{f}</td><td>{mark(a)}</td><td>{mark(b)}</td><td class="cjcol">{mark(c)}</td></tr>' for f,a,b,c in g["cmp_rows"])
    vg = "".join(f'<li><svg class="ic mk"><use href="#i-check"/></svg>{x}</li>' for x in g["vgood"])
    vw = "".join(f'<li><svg class="ic mk"><use href="#i-alert"/></svg>{x}</li>' for x in g["vwarn"])
    bundles = "".join(f'<div class="bundle{" sel" if rib else ""}" data-b>{f"<span class=\"rib\">{rib}</span>" if rib else ""}<span class="q">{q}</span><div class="pu">{g["cur"]}{pu}<small>{g["per"]}</small></div><div class="sv">{sv}</div></div>' for q,pu,sv,rib in g["bundles"])
    faq = "\n  ".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q,a in g["faq"])
    return f"""<!DOCTYPE html>
<html lang="{g['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, follow">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#d90429">
<title>{g['title']}</title>
<meta name="description" content="{g['desc']}">
<link rel="canonical" href="https://trycoolizi.com/{g['code']}/cooljet/">
<style>{STYLE}</style>
</head>
<body>
{SPRITE}
<div class="ticker"><div class="run">{ticker}</div></div>
<header class="mast"><div class="in"><div class="logo">The <span class="b">Cooling</span> Report</div><div class="date">{g['desk']}<br>{g['updated']}</div></div></header>
<div class="wrap">
<article><div class="pad">
  <span class="kick"><span class="lv"></span>{g['kick']}</span>
  <h1>{g['h1']}</h1>
  <p class="stand">{g['stand']}</p>
  <div class="byline"><span class="spon">{g['spon']}</span><span>{g['by']}</span><span class="dot">•</span><span>{g['read']}</span></div>
  <figure>
    <div class="hero">{flakes()}<span class="badgeR">{g['fast']}</span><img class="cjlogo" src="/assets/img/cj/logo-dark.png" alt="CoolJet" width="130" height="26"><img class="prod" src="/assets/img/cooljet.png" alt="CoolJet {g['prod']}" width="330" height="383" fetchpriority="high"></div>
    <figcaption>{g['figcap']}</figcaption>
  </figure>
  <p class="lead">{g['lead']}</p>
  <div class="heat"><span class="t">🔥</span><div>{g['heat']}</div></div>
  <div class="heatmap reveal">
    <div class="hm-head"><svg class="ic"><use href="#i-alert"/></svg> {g['hm_head']}</div>
    <div class="hm-map">{ISLE}{pins}</div>
    <div class="hm-foot"><span>{g['hm_foot_l']}</span><span>{g['hm_foot_r']}</span></div>
  </div>
  <p>{g['p_ac']}</p>
  <figure class="lifeimg reveal"><img src="/assets/img/cj/heat-lady.webp" alt="{g['lady_alt']}" width="900" height="600" loading="lazy"></figure>
  <p class="lifecap reveal">{g['lady_cap']}</p>

  <h2 class="reveal"><span class="em">🚫</span> {g['h2_myths']}</h2>
  {myths}
  <a class="cta mini reveal" href="#deal" data-scroll>{g['see_deal']} <span class="arw">→</span></a>

  <h2 class="reveal"><span class="em">🧊</span> {g['h2_what']}</h2>
  <div class="note reveal"><b>{g['what_b']}</b>{g['what']}</div>
  <div class="chips reveal">{chips}</div>

  <h2 class="reveal"><span class="em">🌡️</span> {g['h2_ba']}</h2>
  <figure class="lifeimg reveal"><img src="/assets/img/cj/beforeafter.webp" alt="{g['ba_alt']}" width="900" height="503" loading="lazy"></figure>
  <p class="lifecap reveal">{g['ba_cap']}</p>

  <h2 class="reveal"><span class="em">✅</span> {g['h2_reasons']}</h2>
  <div class="reasons">{reasons}</div>

  <h2 class="reveal"><span class="em">⚔️</span> {g['h2_cmp']}</h2>
  <table class="cmp reveal"><thead><tr><th></th><th>{g['col_fan']}</th><th>{g['col_ac']}</th><th class="cj">CoolJet</th></tr></thead><tbody>{rows}</tbody></table>
  <p class="reveal" style="font-size:14.5px;color:var(--muted)">{g['cmp_after']}</p>

  <div class="verdict reveal">
    <div class="stars">★★★★☆</div><div class="score">4 / 5</div><div class="who">{g['who']}</div>
    <div class="vtwo"><div class="vcol vgood"><h4>{g['vgood_h']}</h4><ul>{vg}</ul></div><div class="vcol vwarn"><h4>{g['vwarn_h']}</h4><ul>{vw}</ul></div></div>
  </div>

  <h2 id="deal" class="reveal"><span class="em">🎁</span> {g['h2_deal']}</h2>
  <div class="deal reveal">
    <div class="dhead"><span class="badge">{g['deal_badge']}</span><div class="price"><span class="now">{g['cur']}{g['now']}</span><span class="was">{g['cur']}{g['was']}</span><span class="off">{g['off']}</span></div></div>
    <div class="bundles">{bundles}</div>
    <div class="seal"><img src="/assets/img/cj/30day.png" alt="{g['seal_alt']}"><span>{g['seal']}</span></div>
    <a class="cta" href="{ef}" data-cta rel="nofollow sponsored noopener" target="_blank">{g['cta']} <span class="arw">→</span></a>
    <div class="trustrow"><span><svg class="ic c"><use href="#i-check"/></svg>{g['t1']}</span><span><svg class="ic c"><use href="#i-check"/></svg>{g['t2']}</span><span><svg class="ic c"><use href="#i-check"/></svg>{g['t3']}</span></div>
  </div>
  <p class="reveal" style="font-size:13.5px;color:var(--muted);text-align:center">{g['price_note']}</p>

  <h2 class="reveal"><span class="em">❓</span> {g['h2_faq']}</h2>
  {faq}

  <div class="imagine reveal">{g['imagine']}</div>

  <div class="urg reveal">
    <div class="top"><span class="lv"></span>🔥 {g['urg_top']}</div>
    <div class="body"><h3>{g['urg_h']}</h3><div class="pill"><span class="lv"></span>{g['urg_pill']}</div><p>{g['urg_p']}</p>
      <a class="cta" href="{ef}" data-cta rel="nofollow sponsored noopener" target="_blank">{g['urg_cta']} <span class="arw">→</span></a></div>
  </div>
</div></article>
</div>

<div class="foot">
  <div class="aff">{g['aff']}</div>
  <a href="/{g['code']}/privacy/">{g['f_priv']}</a> · <a href="/{g['code']}/terms/">{g['f_terms']}</a> · <a href="/{g['code']}/disclosure/">{g['f_disc']}</a> · <a href="/{g['code']}/contact/">{g['f_contact']}</a>
  <div style="margin-top:10px">{g['copyright']}</div>
</div>

<div class="sticky"><div class="row"><div class="p">{g['cur']}{g['now']} <small>{g['cur']}{g['was']}</small></div><a class="cta" href="{ef}" data-cta rel="nofollow sponsored noopener" target="_blank">{g['sticky_cta']}</a></div></div>

<div class="ep-bg" id="exitpop" role="dialog" aria-modal="true" aria-label="{g['ep_title']}">
  <div class="ep">
    <button class="epclose" data-epclose aria-label="Close">×</button>
    <div class="eic">🚨</div>
    <h3 class="eptitle">{g['ep_title']}</h3>
    <p class="eptext">{g['ep_text']}</p>
    <a class="epcta" href="{ef}" data-cta rel="nofollow sponsored noopener" target="_blank">🔥 {g['ep_cta']} →</a>
    <button class="epno" data-epclose>{g['ep_no']}</button>
  </div>
</div>

<script>
(function(){{"use strict";
  var GEO_TAG="{g['tag']}", BASE="{ef}";
  var KEYS=["gclid","fbclid","ttclid","msclkid","utm_source","utm_campaign","utm_medium"];
  var store={{}}; try{{store=JSON.parse(localStorage.getItem("cz_track")||"{{}}");}}catch(e){{}}
  try{{var q=new URLSearchParams(location.search);KEYS.forEach(function(k){{var v=q.get(k);if(v&&!store[k])store[k]=v;}});if(!store._ts)store._ts=Date.now();localStorage.setItem("cz_track",JSON.stringify(store));}}catch(e){{}}
  function offerUrl(){{var id=store.gclid||store.fbclid||store.ttclid||store.msclkid||"";var u;try{{u=new URL(BASE);}}catch(e){{return BASE;}}u.searchParams.set("sub1",GEO_TAG);if(id)u.searchParams.set("sub2",id);return u.toString();}}
  var url=offerUrl();[].forEach.call(document.querySelectorAll("[data-cta]"),function(a){{a.href=url;}});
  [].forEach.call(document.querySelectorAll("[data-b]"),function(b){{b.addEventListener("click",function(){{[].forEach.call(document.querySelectorAll("[data-b]"),function(x){{x.classList.remove("sel");}});b.classList.add("sel");}});}});
  [].forEach.call(document.querySelectorAll("[data-scroll]"),function(a){{a.addEventListener("click",function(e){{var t=document.getElementById("deal");if(t){{e.preventDefault();t.scrollIntoView({{behavior:"smooth"}});}}}});}});
  // exit-intent popup, once per session
  var ep=document.getElementById("exitpop"),shown=false;
  function showEp(){{if(shown||sessionStorage.getItem("cj_ep"))return;shown=true;sessionStorage.setItem("cj_ep","1");ep.classList.add("show");}}
  function hideEp(){{ep.classList.remove("show");}}
  if(ep){{
    [].forEach.call(ep.querySelectorAll("[data-epclose]"),function(b){{b.addEventListener("click",hideEp);}});
    ep.addEventListener("click",function(e){{if(e.target===ep)hideEp();}});
    document.addEventListener("mouseout",function(e){{if(e.clientY<=0&&!e.relatedTarget)showEp();}});
    try{{history.pushState(null,"",location.href);addEventListener("popstate",function(){{if(!sessionStorage.getItem("cj_ep")){{showEp();history.pushState(null,"",location.href);}}}});}}catch(e){{}}
    setTimeout(function(){{showEp();}},45000);
  }}
  // scroll-reveal (robust: never leaves content hidden)
  var rev=[].slice.call(document.querySelectorAll(".reveal"));function reveal(el){{el.classList.add("in");}}
  try{{
    if("IntersectionObserver" in window){{
      var io=new IntersectionObserver(function(es){{es.forEach(function(en){{if(en.isIntersecting){{reveal(en.target);io.unobserve(en.target);}}}});}},{{threshold:0,rootMargin:"0px 0px -6% 0px"}});
      rev.forEach(function(el){{io.observe(el);}});
      var sweep=function(){{rev.forEach(function(el){{if(el.getBoundingClientRect().top<(window.innerHeight||800))reveal(el);}});}};
      addEventListener("load",sweep);addEventListener("scroll",sweep,{{passive:true}});sweep();
    }} else {{ rev.forEach(reveal); }}
  }}catch(e){{ rev.forEach(reveal); }}
}})();
</script>
</body>
</html>"""


# ---- shared bundle/comparison shapes; per-geo prices differ only by currency symbol/format ----
def bundles_eur(): return [("1×",'89,95',"-50%",""),("2×",'79,95',"-55%","Beliebt"),("3×",'59,95',"-67%","")]

GEOS = {
 "en": dict(
  code="en",lang="en",ef="HTL1R5",tag="cj-uk",cur="£",now="89.95",was="179.90",off="50% OFF",per="/unit",
  title="UK Heatwave: The £89 Cooler Selling Out Across Britain This Week",
  desc="As Britain bakes, a compact evaporative cooler is flying off the shelves. What the CoolJet does, what it costs, why buyers are switching from Coolizi — plus today's 50%-off deal.",
  desk="Consumer Desk",updated="Updated 13 July 2026",
  ticker="🔴 HEATWAVE ALERT&nbsp;&nbsp;·&nbsp;&nbsp;UK TEMPERATURES CLIMBING AGAIN THIS WEEK&nbsp;&nbsp;·&nbsp;&nbsp;COMPACT COOLERS SELLING FAST&nbsp;&nbsp;·&nbsp;&nbsp;50% OFF WHILE STOCK LASTS&nbsp;&nbsp;·&nbsp;&nbsp;BEAT THE HEAT — SHOP TODAY&nbsp;&nbsp;·&nbsp;&nbsp;",
  kick="Heatwave alert · selling fast",
  h1='UK Heatwave: The £89 Cooler That\'s <span class="hl">Selling Out Across Britain</span> — Here\'s Why Everyone\'s Switching',
  stand="Fans just push hot air around. Fixed air-con costs thousands. So Britain has found a third option — and this week it's disappearing from warehouses faster than sellers can restock.",
  spon="Sponsored feature",by="By the Cooling Report Reviews Desk",read="4 min read",
  fast="Selling fast this heatwave",prod="portable evaporative air cooler",
  figcap="The CoolJet — a palm-sized evaporative cooler that chills and mists the air right around you.",
  lead="If you've lain awake even one night this summer with the fan roaring and the room still stifling, you already know the ugly truth: an ordinary fan does nothing but shove hot air from one side of the room to the other. It never lowers the temperature — not by a single degree.",
  heat="It's already hit <strong>38°C in London this month</strong> — and forecasters say the next spike will be hotter. Millions are trying to sleep in bedrooms that simply won't cool down.",
  hm_head="EXTREME HEAT WARNING — UK, this week",hm_foot_l="Cooling Report · UK heat outlook",hm_foot_r="Updated this week",
  cities=[("Glasgow",30,30,14,False),("Edinburgh",31,44,19,False),("Newcastle",32,55,30,False),("Manchester",34,46,43,False),("Birmingham",36,49,56,False),("Cardiff",35,33,68,False),("Bristol",37,44,69,False),("London",39,64,70,True)],
  p_ac="The obvious fix — a proper wall-mounted air conditioner — runs <strong>£2,000 to £5,000</strong> installed, plus a fatter electricity bill every time you switch it on. That's a brutal price for the handful of genuinely sweltering weeks Britain actually gets. So most people just suffer. Until now.",
  lady_alt="A woman lying awake in bed, too hot to sleep during the heatwave",
  lady_cap="Sound familiar? When the bedroom won't cool down, no amount of tossing and turning helps.",
  h2_myths="5 myths about cooling fans",
  myths=[('"A fan cools the room."',"It doesn't. A fan moves air; it can't lower the actual temperature.","An evaporative cooler chills and mists the air before it reaches you."),
         ('"You have to cool the whole room to feel better."',"You don't — you only need to cool the air around <em>you</em>.","Point-cooling your desk or bed is cheaper and works in minutes."),
         ('"Only a £2,000 AC unit actually cools."',"For a whole house, sure. For one person? Overkill.","A £89 personal cooler handles the metre that matters."),
         ('"Portable coolers are all noisy."',"Old ones were. This one has a genuine quiet night mode.","Low hum + soft light — you can sleep right next to it."),
         ('"They cost a fortune to run."',"Not this class. It sips power over USB.","Pennies a night, not the pounds a compressor AC burns.")],
  see_deal="See today's 50% deal",
  h2_what="So what exactly is the CoolJet?",
  what_b="Straight talk: it's an evaporative cooler, not an air-conditioner.",
  what=" You fill a small tank and a fan draws air across the damp filter, so the air reaching you is cooler and lightly misted. It's built for <strong>personal, close-range cooling</strong> — a desk, a bed, a pushchair, a tent — not for refrigerating a whole room. Anyone claiming a £90 gadget replaces central air-con is lying to you. Within its real job, though, it's genuinely good.",
  chips=["Cool &amp; mist","4 speeds","Quiet night mode","Low power / USB"],
  h2_ba="Before vs after",ba_alt="Before: a hot, restless bedroom. After: a cool bedroom with a personal cooler running",
  ba_cap="Left, another sweaty, sleepless night. Right, cooled and misted air right where you sleep.",
  h2_reasons="6 reasons people are switching",
  reasons=[("Cool where you actually are","Desk, bed, sofa — it follows you room to room."),("A fraction of AC's cost","£89 today vs thousands to install a fixed unit."),("Ultrasonic mist","A fine cool mist for a sharper chill on dry, hot days."),("Sleep-friendly","Quiet mode + soft night light you can nod off next to."),("Set-and-forget timer","Switches off on its own — no waking to fiddle with it."),("Pennies to run","USB-powered — plug, laptop or power bank.")],
  h2_cmp="CoolJet vs the alternatives",col_fan="Ordinary fan",col_ac="Fixed AC",
  cmp_rows=[("Actually cools the air","x","c","c"),("Affordable","c","x","c"),("No installation","c","x","c"),("Portable room-to-room","-","x","c"),("Cheap to run","c","x","c")],
  cmp_after="And versus <strong>Coolizi</strong> — the cooler a lot of readers found first — CoolJet is the same type of product but checks out cleanly in <strong>£ GBP</strong>, ships to the <strong>UK</strong> with tracking, and states a <strong>30-day money-back</strong> window. Those are exactly the things that tripped Coolizi buyers up, which is why our links go to CoolJet.",
  who="— The Cooling Report editorial verdict",vgood_h="Where it shines",vwarn_h="Manage expectations",
  vgood=["Fast, personal cooling that goes where you go","Mist + 4 speeds + quiet night mode","Localised £ checkout, 30-day returns stated"],
  vwarn=["Cools <em>you</em>, not a whole room","Refill and occasionally clean the tank","Works best within about a metre"],
  h2_deal="Choose your deal — 50% off today",deal_badge="Summer heatwave price — live now",
  bundles=[("1× CoolJet","89.95","Save 50%",""),("2× CoolJet","79.95","Save 55%","Most popular"),("3× CoolJet","59.95","Save 67%","")],
  seal_alt="30-day money-back guarantee",seal="30-day money-back guarantee · tracked UK delivery · secure checkout",
  cta="Check price &amp; availability",t1="Secure checkout",t2="30-day money-back",t3="Tracked shipping",
  price_note="Prices, bundles and stock are set by the retailer and can change during a heatwave — the button always shows the current offer.",
  h2_faq="Straight answers to common questions",
  faq=[("Will this actually cool my bedroom?","It cools the air around <em>you</em> — perfect aimed at a desk chair or the head of a bed. It will not chill an entire room like a compressor AC, and we won't pretend otherwise. For personal, close-range relief in a heatwave, it's exactly the tool."),
       ("How much is it and can I send it back?","A single unit is £89.95 right now (down from £179.90), and the per-unit price drops on 2- and 3-packs. The retailer states a 30-day money-back window — confirm the exact terms on the checkout page."),
       ("Is delivery to the UK sorted?","Yes — the CoolJet checkout is set up for tracked UK delivery, with prices shown in pounds."),
       ("Why not just buy Coolizi?","Same type of product — but we point to CoolJet because its checkout is localised in £, it ships to the UK, and it states a 30-day money-back window. Those are precisely the things that tripped up Coolizi buyers.")],
  imagine="Imagine tonight: the room still warm, but a cool, softly-misted breeze right on your face — and you actually fall asleep. That's the whole point of a personal cooler. Not the whole house. Just you, comfortable, for the price of a takeaway.",
  urg_top="WHY WE'D BUY NOW, NOT LATER",urg_h="The 50% price is a heatwave promotion — not the norm",urg_pill="50% off · while the summer promo lasts",
  urg_p="Compact coolers like this routinely sell out mid-heatwave, and the £89.95 you see today is a limited-time launch discount off the £179.90 list price — not a permanent one. Once the promotion ends or this batch clears, it's back to full price and a wait for restock. If you want one working on your desk this week, the sensible move is to lock in the discounted price now, while it's live.",
  urg_cta="Claim my CoolJet at 50% off",
  ep_title="Wait — don't lose the 50% price",
  ep_text="Your <strong>50% heatwave discount</strong> is still live — <strong>£89.95</strong> instead of £179.90. Once the summer promotion ends, it's back to full price. Grab it before you go.",
  ep_cta="Get CoolJet at 50% off",ep_no="No thanks, I'll pay full price later",
  aff="<strong>Advertising disclosure.</strong> This is a sponsored advertorial, not independent editorial. We receive a commission if you purchase through the links on this page, at no additional cost to you. Product claims, pricing and availability are set by the retailer and were accurate at the time of writing. Evaporative coolers provide personal, localised cooling and are not a substitute for a refrigerant air-conditioning system.",
  f_priv="Privacy",f_terms="Terms",f_disc="Affiliate Disclosure",f_contact="Contact",
  copyright="© 2026 The Cooling Report. All product names are trademarks of their respective owners.",
  sticky_cta="Get 50% off →"),
}

# ---- de/fr/it/es/nl are built by cloning EN's structure and swapping the localized strings ----
_L = {
 "de": dict(ef="HS752J",tag="cj-de",cur="€",now="89,95",was="179,90",off="50% RABATT",per="/Stk.",
  title="Hitzewelle: Der 89-€-Kühler, der gerade überall ausverkauft ist",
  desc="Während Deutschland schwitzt, geht ein kompakter Verdunstungskühler weg wie warme Semmeln. Was der CoolJet kann, was er kostet, warum Käufer von Coolizi umsteigen — plus 50%-Deal.",
  desk="Verbraucher-Ressort",updated="Aktualisiert 13. Juli 2026",
  ticker="🔴 HITZEWELLEN-ALARM&nbsp;&nbsp;·&nbsp;&nbsp;TEMPERATUREN STEIGEN DIESE WOCHE WEITER&nbsp;&nbsp;·&nbsp;&nbsp;KOMPAKTE KÜHLER STARK GEFRAGT&nbsp;&nbsp;·&nbsp;&nbsp;50% RABATT SOLANGE VORRAT REICHT&nbsp;&nbsp;·&nbsp;&nbsp;JETZT DER HITZE ENTKOMMEN&nbsp;&nbsp;·&nbsp;&nbsp;",
  kick="Hitzewellen-Alarm · stark gefragt",
  h1='Hitzewelle: Der 89-€-Kühler, der gerade <span class="hl">überall ausverkauft</span> ist — und warum alle umsteigen',
  stand="Ventilatoren schieben nur warme Luft herum. Eine feste Klimaanlage kostet Tausende. Deutschland hat eine dritte Option gefunden — und diese Woche ist sie schneller vergriffen, als Händler nachlegen können.",
  spon="Gesponserter Beitrag",by="Von der Cooling-Report-Redaktion",read="4 Min. Lesezeit",
  fast="In dieser Hitzewelle stark gefragt",prod="tragbarer Verdunstungskühler",
  figcap="Der CoolJet — ein handtellergroßer Verdunstungskühler, der die Luft direkt um Sie herum kühlt und befeuchtet.",
  lead="Wenn Sie diesen Sommer auch nur eine Nacht wach lagen, während der Ventilator dröhnte und das Zimmer trotzdem stickig blieb, kennen Sie die unbequeme Wahrheit: Ein normaler Ventilator schiebt die warme Luft nur von einer Ecke in die andere. Er senkt die Temperatur nicht — kein einziges Grad.",
  heat="Es waren diesen Monat schon <strong>38°C</strong> — und die nächste Spitze wird laut Prognosen noch heißer. Millionen versuchen, in Schlafzimmern zu schlafen, die einfach nicht abkühlen.",
  hm_head="EXTREME HITZEWARNUNG — Deutschland, diese Woche",hm_foot_l="Cooling Report · Hitze-Ausblick",hm_foot_r="Diese Woche aktualisiert",
  cities=[("Hamburg",33,42,15,False),("Berlin",36,62,24,False),("Köln",35,30,45,False),("Frankfurt",37,42,52,False),("Dresden",35,64,44,False),("Stuttgart",36,44,66,False),("Wien",36,72,72,False),("München",39,52,80,True)],
  p_ac="Die naheliegende Lösung — eine fest montierte Klimaanlage — kostet installiert <strong>2.000 bis 5.000 Euro</strong>, plus höhere Stromrechnung bei jedem Einschalten. Ein brutaler Preis für die paar wirklich glühenden Wochen. Also leiden die meisten einfach. Bis jetzt.",
  lady_alt="Eine Frau liegt wach im Bett, zu heiß zum Schlafen während der Hitzewelle",
  lady_cap="Kommt Ihnen bekannt vor? Wenn das Schlafzimmer nicht abkühlt, hilft kein Hin- und Herwälzen.",
  h2_myths="5 Mythen über Ventilatoren",
  myths=[('„Ein Ventilator kühlt den Raum."',"Tut er nicht. Er bewegt Luft, senkt aber nicht die Temperatur.","Ein Verdunstungskühler kühlt und befeuchtet die Luft, bevor sie Sie erreicht."),
         ('„Man muss den ganzen Raum kühlen."',"Nein — es reicht, die Luft um <em>Sie</em> herum zu kühlen.","Punktkühlung am Schreibtisch oder Bett ist günstiger und wirkt in Minuten."),
         ('„Nur eine 2.000-€-Klimaanlage kühlt wirklich."',"Für ein ganzes Haus, ja. Für eine Person? Übertrieben.","Ein 89-€-Kühler schafft den einen Meter, der zählt."),
         ('„Tragbare Kühler sind alle laut."',"Alte schon. Dieser hat einen echten leisen Nachtmodus.","Leises Summen + sanftes Licht — Sie schlafen direkt daneben."),
         ('„Der Betrieb kostet ein Vermögen."',"Nicht diese Klasse. Er läuft sparsam über USB.","Centbeträge pro Nacht statt Euro wie bei einer Klimaanlage.")],
  see_deal="Zum 50%-Deal",
  h2_what="Was ist der CoolJet eigentlich?",
  what_b="Klartext: Es ist ein Verdunstungskühler, keine Klimaanlage.",
  what=" Sie füllen einen kleinen Tank, ein Ventilator zieht Luft über den feuchten Filter — die Luft, die ankommt, ist kühler und leicht befeuchtet. Er ist für die <strong>persönliche Nahkühlung</strong> gemacht — Schreibtisch, Bett, Kinderwagen, Zelt — nicht für einen ganzen Raum. Wer sagt, ein 90-€-Gerät ersetze eine Klimaanlage, lügt. In seinem echten Job ist er aber richtig gut.",
  chips=["Kühlen &amp; Nebel","4 Stufen","Leiser Nachtmodus","Sparsam / USB"],
  h2_ba="Vorher vs. nachher",ba_alt="Vorher: heißes Schlafzimmer. Nachher: kühles Schlafzimmer mit Kühler.",
  ba_cap="Links: wieder eine verschwitzte, schlaflose Nacht. Rechts: gekühlte, vernebelte Luft dort, wo Sie schlafen.",
  h2_reasons="6 Gründe für den Umstieg",
  reasons=[("Kühlung dort, wo Sie sind","Schreibtisch, Bett, Sofa — er wandert mit."),("Ein Bruchteil der Klima-Kosten","89 € heute statt Tausende für eine feste Anlage."),("Ultraschall-Nebel","Feiner, kühler Sprühnebel für mehr Kühle an trockenen Tagen."),("Schlaffreundlich","Leise-Modus + sanftes Nachtlicht direkt daneben."),("Timer","Schaltet von allein ab — kein nächtliches Aufstehen."),("Sparsam","USB-Betrieb — Netzteil, Laptop oder Powerbank.")],
  h2_cmp="CoolJet vs. die Alternativen",col_fan="Ventilator",col_ac="Feste Klima",
  cmp_after="Und gegenüber <strong>Coolizi</strong> — dem Kühler, den viele zuerst fanden — ist der CoolJet dieselbe Produktklasse, rechnet aber sauber in <strong>Euro</strong> ab, liefert nach <strong>DE &amp; Österreich</strong> mit Tracking und nennt eine <strong>30-Tage-Geld-zurück</strong>-Frist. Genau daran haperte es bei Coolizi — deshalb führen unsere Links zum CoolJet.",
  who="— Redaktionelles Urteil des Cooling Report",vgood_h="Das kann er",vwarn_h="Realistisch bleiben",
  vgood=["Schnelle persönliche Kühlung, die mitkommt","Nebel + 4 Stufen + leiser Nachtmodus","Lokalisierte €-Kasse, 30 Tage Rückgabe angegeben"],
  vwarn=["Kühlt <em>Sie</em>, nicht den ganzen Raum","Tank nachfüllen und ab und zu reinigen","Wirkt am besten bis etwa einen Meter"],
  h2_deal="Wählen Sie Ihren Deal — 50% heute",deal_badge="Sommer-Hitzepreis — jetzt aktiv",
  seal_alt="30 Tage Geld-zurück-Garantie",seal="30 Tage Geld-zurück · Lieferung mit Tracking · sichere Kasse",
  cta="Preis &amp; Verfügbarkeit prüfen",t1="Sichere Kasse",t2="30 Tage Geld-zurück",t3="Versand mit Tracking",
  price_note="Preise, Bundles und Bestände legt der Händler fest und können sich während einer Hitzewelle ändern — der Button zeigt immer das aktuelle Angebot.",
  h2_faq="Klare Antworten auf häufige Fragen",
  faq=[("Kühlt das wirklich mein Schlafzimmer?","Es kühlt die Luft um <em>Sie</em> herum — perfekt auf Stuhl oder Kopfende gerichtet. Einen ganzen Raum kühlt es nicht wie eine Kompressor-Klimaanlage, und das behaupten wir nicht. Für persönliche Nahkühlung in der Hitze ist es genau richtig."),
       ("Was kostet er und kann ich ihn zurückgeben?","Ein Einzelgerät kostet aktuell 89,95 € (statt 179,90 €), im Mehrfachkauf sinkt der Stückpreis. Der Händler nennt 30 Tage Geld-zurück — Details an der Kasse."),
       ("Ist die Lieferung nach DE/Österreich geregelt?","Ja — die CoolJet-Kasse ist auf Lieferung mit Tracking eingestellt, Preise in Euro."),
       ("Warum nicht einfach Coolizi?","Gleiche Produktklasse — aber wir verlinken den CoolJet, weil die Kasse in Euro ist, er nach DE/Österreich liefert und 30 Tage Rückgabe nennt. Genau daran haperte es bei Coolizi.")],
  imagine="Stellen Sie sich heute Nacht vor: das Zimmer noch warm, aber eine kühle, sanft vernebelte Brise direkt im Gesicht — und Sie schlafen tatsächlich ein. Genau dafür ist ein Personal-Kühler da. Nicht fürs ganze Haus. Nur für Sie.",
  urg_top="WARUM JETZT, NICHT SPÄTER",urg_h="Der 50%-Preis ist eine Hitzewellen-Aktion — nicht der Normalpreis",urg_pill="50% Rabatt · solange die Sommer-Aktion läuft",
  urg_p="Kompakte Kühler wie dieser sind mitten in der Hitzewelle regelmäßig ausverkauft, und die 89,95 € heute sind ein befristeter Einführungsrabatt auf den Listenpreis von 179,90 € — nicht dauerhaft. Endet die Aktion oder ist die Charge weg, gilt wieder der volle Preis plus Wartezeit. Wenn er diese Woche auf Ihrem Schreibtisch stehen soll, sichern Sie sich den reduzierten Preis jetzt.",
  urg_cta="CoolJet mit 50% Rabatt sichern",
  ep_title="Warten Sie — der 50%-Preis wäre weg",
  ep_text="Ihr <strong>50%-Hitzerabatt</strong> ist noch aktiv — <strong>89,95 €</strong> statt 179,90 €. Wenn die Sommer-Aktion endet, gilt wieder der volle Preis. Sichern Sie ihn, bevor Sie gehen.",
  ep_cta="CoolJet mit 50% sichern",ep_no="Nein danke, später den vollen Preis zahlen",
  aff="<strong>Werbehinweis.</strong> Dies ist eine gesponserte Anzeige (Advertorial), keine unabhängige Redaktion. Wir erhalten eine Provision, wenn Sie über die Links auf dieser Seite kaufen — ohne Mehrkosten für Sie. Produktangaben, Preise und Verfügbarkeit legt der Händler fest und waren zum Zeitpunkt der Erstellung korrekt. Verdunstungskühler kühlen persönlich und punktuell und ersetzen keine Kompressor-Klimaanlage.",
  f_priv="Datenschutz",f_terms="AGB",f_disc="Affiliate-Hinweis",f_contact="Kontakt",
  copyright="© 2026 The Cooling Report. Alle Produktnamen sind Marken der jeweiligen Eigentümer.",
  sticky_cta="50% sichern →"),

 "fr": dict(ef="HZCR8C",tag="cj-fr",cur="€",now="89,95",was="179,90",off="-50%",per="/u.",
  title="Canicule : le rafraîchisseur à 89 € en rupture partout en France",
  desc="Pendant que la France suffoque, un rafraîchisseur évaporatif compact s'arrache. Ce que fait le CoolJet, son prix, pourquoi on quitte Coolizi — et l'offre -50%.",
  desk="Rubrique Conso",updated="Mis à jour le 13 juillet 2026",
  ticker="🔴 ALERTE CANICULE&nbsp;&nbsp;·&nbsp;&nbsp;LES TEMPÉRATURES REMONTENT CETTE SEMAINE&nbsp;&nbsp;·&nbsp;&nbsp;LES RAFRAÎCHISSEURS S'ARRACHENT&nbsp;&nbsp;·&nbsp;&nbsp;-50% DANS LA LIMITE DES STOCKS&nbsp;&nbsp;·&nbsp;&nbsp;ÉCHAPPEZ À LA CHALEUR&nbsp;&nbsp;·&nbsp;&nbsp;",
  kick="Alerte canicule · s'arrache",
  h1='Canicule : le rafraîchisseur à 89 € <span class="hl">en rupture partout en France</span> — et pourquoi tout le monde s\'y met',
  stand="Un ventilateur ne fait que brasser l'air chaud. Une vraie clim coûte des milliers d'euros. La France a trouvé une troisième voie — et cette semaine, elle part plus vite que les vendeurs ne réapprovisionnent.",
  spon="Contenu sponsorisé",by="Par la rédaction du Cooling Report",read="4 min de lecture",
  fast="Très demandé pendant la canicule",prod="rafraîchisseur d'air portable",
  figcap="Le CoolJet — un rafraîchisseur évaporatif de la taille d'une main qui rafraîchit et humidifie l'air autour de vous.",
  lead="Si vous avez passé une seule nuit cet été éveillé, ventilateur à fond et pièce toujours étouffante, vous connaissez la vérité qui dérange : un ventilateur ordinaire ne fait que déplacer l'air chaud d'un côté à l'autre. Il ne baisse pas la température — pas d'un seul degré.",
  heat="On a déjà relevé <strong>38°C ce mois-ci</strong> — et le prochain pic sera plus chaud selon les prévisions. Des millions de gens tentent de dormir dans des chambres qui ne refroidissent pas.",
  hm_head="ALERTE CHALEUR EXTRÊME — France, cette semaine",hm_foot_l="Cooling Report · prévision chaleur",hm_foot_r="Mis à jour cette semaine",
  cities=[("Lille",34,50,16,False),("Paris",38,52,30,False),("Strasbourg",36,70,34,False),("Nantes",35,34,48,False),("Lyon",37,62,55,False),("Bordeaux",36,34,66,False),("Toulouse",37,46,72,False),("Marseille",40,64,74,True)],
  p_ac="La solution évidente — un vrai climatiseur mural — coûte de <strong>2 000 à 5 000 €</strong> posé, plus une facture d'électricité qui gonfle à chaque usage. Un prix brutal pour les quelques semaines vraiment torrides. Alors la plupart des gens serrent les dents. Jusqu'ici.",
  lady_alt="Une femme éveillée dans son lit, trop chaud pour dormir pendant la canicule",
  lady_cap="Ça vous parle ? Quand la chambre ne refroidit pas, se retourner ne change rien.",
  h2_myths="5 idées reçues sur les ventilateurs",
  myths=[('« Un ventilateur rafraîchit la pièce. »',"Non. Il déplace l'air, il ne baisse pas la température.","Un rafraîchisseur évaporatif rafraîchit et brumise l'air avant qu'il ne vous atteigne."),
         ('« Il faut rafraîchir toute la pièce. »',"Non — il suffit de rafraîchir l'air autour de <em>vous</em>.","Cibler votre bureau ou votre lit coûte moins cher et agit en minutes."),
         ('« Seule une clim à 2 000 € rafraîchit. »',"Pour une maison, oui. Pour une personne ? Excessif.","Un rafraîchisseur à 89 € gère le mètre qui compte."),
         ('« Les rafraîchisseurs portables sont bruyants. »',"Les anciens, oui. Celui-ci a un vrai mode nuit silencieux.","Ronron discret + veilleuse — vous dormez juste à côté."),
         ('« Ça coûte une fortune en électricité. »',"Pas cette catégorie. Il consomme peu, en USB.","Quelques centimes la nuit, pas les euros d'une clim.")],
  see_deal="Voir l'offre -50%",
  h2_what="Alors, c'est quoi exactement le CoolJet ?",
  what_b="Soyons clairs : c'est un rafraîchisseur par évaporation, pas un climatiseur.",
  what=" Vous remplissez un petit réservoir, un ventilateur fait passer l'air sur le filtre humide : l'air qui vous parvient est plus frais et légèrement brumisé. Il est conçu pour un <strong>rafraîchissement personnel de proximité</strong> — bureau, lit, poussette, tente — pas pour une pièce entière. Quiconque dit qu'un gadget à 90 € remplace une clim vous ment. Mais dans son vrai rôle, il est vraiment bon.",
  chips=["Frais &amp; brume","4 vitesses","Mode nuit silencieux","Basse conso / USB"],
  h2_ba="Avant vs après",ba_alt="Avant : chambre chaude. Après : chambre fraîche avec un rafraîchisseur.",
  ba_cap="À gauche, une nuit moite et blanche de plus. À droite, un air frais et brumisé là où vous dormez.",
  h2_reasons="6 raisons de passer au CoolJet",
  reasons=[("Frais là où vous êtes","Bureau, lit, canapé — il vous suit de pièce en pièce."),("Une fraction du prix d'une clim","89 € aujourd'hui contre des milliers pour une pose fixe."),("Brume ultrasonique","Une fine brume fraîche pour un froid plus net les jours secs."),("Bon pour dormir","Mode silencieux + veilleuse douce juste à côté."),("Minuteur","S'éteint tout seul — pas de réveil nocturne."),("Économique","Alimentation USB — prise, ordinateur ou batterie.")],
  h2_cmp="CoolJet vs les alternatives",col_fan="Ventilateur",col_ac="Clim fixe",
  cmp_after="Et face à <strong>Coolizi</strong> — le rafraîchisseur trouvé en premier par beaucoup — le CoolJet est le même type de produit mais paie proprement en <strong>euros</strong>, livre en <strong>France</strong> avec suivi et indique un <strong>retour 30 jours</strong>. C'est exactement ce qui a coincé chez Coolizi — d'où nos liens vers CoolJet.",
  who="— Avis de la rédaction du Cooling Report",vgood_h="Ses points forts",vwarn_h="Restez réaliste",
  vgood=["Rafraîchissement personnel qui vous suit","Brume + 4 vitesses + mode nuit silencieux","Paiement localisé en €, retour 30 jours indiqué"],
  vwarn=["Vous rafraîchit <em>vous</em>, pas toute la pièce","Remplir et nettoyer le réservoir de temps en temps","Efficace jusqu'à environ un mètre"],
  h2_deal="Choisissez votre offre — -50% aujourd'hui",deal_badge="Prix canicule d'été — en cours",
  seal_alt="Garantie satisfait ou remboursé 30 jours",seal="30 jours satisfait ou remboursé · livraison suivie · paiement sécurisé",
  cta="Vérifier le prix &amp; le stock",t1="Paiement sécurisé",t2="30 jours remboursé",t3="Livraison suivie",
  price_note="Les prix, lots et stocks sont fixés par le vendeur et peuvent changer pendant une canicule — le bouton affiche toujours l'offre en cours.",
  h2_faq="Des réponses claires aux questions fréquentes",
  faq=[("Est-ce que ça rafraîchit vraiment ma chambre ?","Ça rafraîchit l'air autour de <em>vous</em> — parfait dirigé vers la chaise ou la tête du lit. Ça ne climatise pas une pièce entière comme un appareil à compresseur, et on ne prétend pas le contraire. Pour un soulagement personnel de proximité en canicule, c'est exactement l'outil."),
       ("Combien coûte-t-il et puis-je le renvoyer ?","L'unité est à 89,95 € (au lieu de 179,90 €), avec un prix à l'unité plus bas en lot. Le vendeur indique 30 jours satisfait ou remboursé — conditions au paiement."),
       ("La livraison en France est-elle gérée ?","Oui — le paiement CoolJet est configuré pour une livraison suivie en France, prix en euros."),
       ("Pourquoi pas simplement Coolizi ?","Même type de produit — mais nous orientons vers CoolJet car il paie en €, livre en France et indique 30 jours de retour. C'est précisément ce qui a coincé chez Coolizi.")],
  imagine="Imaginez ce soir : la pièce encore chaude, mais une brise fraîche et légèrement brumisée sur votre visage — et vous vous endormez vraiment. C'est tout l'intérêt d'un rafraîchisseur personnel. Pas toute la maison. Juste vous.",
  urg_top="POURQUOI MAINTENANT, PAS PLUS TARD",urg_h="Le prix -50% est une promo de canicule — pas le prix habituel",urg_pill="-50% · tant que dure la promo d'été",
  urg_p="Les rafraîchisseurs compacts comme celui-ci sont régulièrement en rupture en pleine canicule, et les 89,95 € affichés aujourd'hui sont une remise de lancement limitée sur le prix catalogue de 179,90 € — pas définitive. Quand la promo se termine ou que le lot est écoulé, on repasse au plein tarif avec un délai. Si vous le voulez sur votre bureau cette semaine, verrouillez le prix réduit maintenant.",
  urg_cta="Je prends le CoolJet à -50%",
  ep_title="Attendez — vous alliez perdre le -50%",
  ep_text="Votre <strong>remise canicule de 50%</strong> est encore active — <strong>89,95 €</strong> au lieu de 179,90 €. Quand la promo d'été se termine, on repasse au plein tarif. Profitez-en avant de partir.",
  ep_cta="Prendre le CoolJet à -50%",ep_no="Non merci, je paierai plein tarif plus tard",
  aff="<strong>Divulgation publicitaire.</strong> Ceci est une publi-information sponsorisée, pas un contenu éditorial indépendant. Nous percevons une commission si vous achetez via les liens de cette page, sans coût supplémentaire pour vous. Les caractéristiques, prix et disponibilités sont fixés par le vendeur et étaient exacts à la rédaction. Les rafraîchisseurs par évaporation offrent un rafraîchissement personnel et localisé et ne remplacent pas une climatisation à compresseur.",
  f_priv="Confidentialité",f_terms="CGU",f_disc="Divulgation d'affiliation",f_contact="Contact",
  copyright="© 2026 The Cooling Report. Tous les noms de produits sont des marques de leurs propriétaires respectifs.",
  sticky_cta="Profiter du -50% →"),

 "it": dict(ef="J4JFG6",tag="cj-it",cur="€",now="89,95",was="179,90",off="-50%",per="/u.",
  title="Ondata di caldo: il raffrescatore da 89 € esaurito ovunque in Italia",
  desc="Mentre l'Italia soffoca, un raffrescatore evaporativo compatto va a ruba. Cosa fa il CoolJet, quanto costa, perché si lascia Coolizi — e l'offerta -50%.",
  desk="Sezione Consumatori",updated="Aggiornato 13 luglio 2026",
  ticker="🔴 ALLERTA CALDO&nbsp;&nbsp;·&nbsp;&nbsp;TEMPERATURE IN RISALITA QUESTA SETTIMANA&nbsp;&nbsp;·&nbsp;&nbsp;RAFFRESCATORI A RUBA&nbsp;&nbsp;·&nbsp;&nbsp;-50% FINO A ESAURIMENTO&nbsp;&nbsp;·&nbsp;&nbsp;BATTI IL CALDO OGGI&nbsp;&nbsp;·&nbsp;&nbsp;",
  kick="Allerta caldo · va a ruba",
  h1='Ondata di caldo: il raffrescatore da 89 € <span class="hl">esaurito ovunque in Italia</span> — ed ecco perché tutti passano a questo',
  stand="Il ventilatore sposta solo aria calda. Un vero condizionatore costa migliaia di euro. L'Italia ha trovato una terza via — e questa settimana sparisce più in fretta di quanto i venditori riescano a rifornire.",
  spon="Contenuto sponsorizzato",by="A cura della redazione del Cooling Report",read="4 min di lettura",
  fast="Molto richiesto in questa ondata di caldo",prod="raffrescatore d'aria portatile",
  figcap="Il CoolJet — un raffrescatore evaporativo grande come una mano che rinfresca e umidifica l'aria intorno a te.",
  lead="Se hai passato anche una sola notte quest'estate sveglio, con il ventilatore a palla e la stanza comunque soffocante, conosci la verità scomoda: un normale ventilatore non fa che spostare l'aria calda da una parte all'altra. Non abbassa la temperatura — nemmeno di un grado.",
  heat="Si sono già toccati <strong>38°C questo mese</strong> — e il prossimo picco sarà più caldo secondo le previsioni. Milioni provano a dormire in camere che non si raffreddano.",
  hm_head="ALLERTA CALDO ESTREMO — Italia, questa settimana",hm_foot_l="Cooling Report · previsione caldo",hm_foot_r="Aggiornato questa settimana",
  cities=[("Milano",36,44,16,False),("Torino",35,32,20,False),("Venezia",35,56,22,False),("Bologna",37,48,36,False),("Firenze",38,46,48,False),("Roma",39,48,64,True),("Napoli",38,56,72,False),("Bari",37,70,74,False)],
  p_ac="La soluzione ovvia — un vero condizionatore a parete — costa dai <strong>2.000 ai 5.000 euro</strong> installato, più una bolletta più salata a ogni accensione. Un prezzo brutale per le poche settimane davvero roventi. Così la maggior parte stringe i denti. Fino a ora.",
  lady_alt="Una donna sveglia a letto, troppo caldo per dormire durante l'ondata di caldo",
  lady_cap="Ti suona familiare? Quando la camera non si raffredda, rigirarsi non serve a nulla.",
  h2_myths="5 falsi miti sui ventilatori",
  myths=[('«Il ventilatore rinfresca la stanza.»',"No. Sposta l'aria, ma non abbassa la temperatura.","Un raffrescatore evaporativo rinfresca e nebulizza l'aria prima che ti raggiunga."),
         ('«Bisogna rinfrescare tutta la stanza.»',"No — basta rinfrescare l'aria intorno a <em>te</em>.","Rinfrescare scrivania o letto costa meno e agisce in pochi minuti."),
         ('«Solo un condizionatore da 2.000 € rinfresca.»',"Per una casa, sì. Per una persona? Eccessivo.","Un raffrescatore da 89 € copre il metro che conta."),
         ('«I raffrescatori portatili sono rumorosi.»',"Quelli vecchi. Questo ha una vera modalità notte silenziosa.","Ronzio basso + luce soffusa — ci dormi accanto."),
         ('«Consumano un patrimonio.»',"Non questa categoria. Consuma poco, via USB.","Centesimi a notte, non gli euro di un condizionatore.")],
  see_deal="Vedi l'offerta -50%",
  h2_what="Ma cos'è esattamente il CoolJet?",
  what_b="Parliamo chiaro: è un raffrescatore evaporativo, non un condizionatore.",
  what=" Riempi un piccolo serbatoio, una ventola spinge l'aria attraverso il filtro umido: l'aria che ti arriva è più fresca e leggermente nebulizzata. È pensato per il <strong>raffrescamento personale ravvicinato</strong> — scrivania, letto, passeggino, tenda — non per un'intera stanza. Chi dice che un aggeggio da 90 € sostituisce un condizionatore ti sta mentendo. Ma nel suo vero compito è davvero valido.",
  chips=["Fresco &amp; nebbia","4 velocità","Modalità notte silenziosa","Bassi consumi / USB"],
  h2_ba="Prima vs dopo",ba_alt="Prima: camera calda. Dopo: camera fresca con un raffrescatore.",
  ba_cap="A sinistra, l'ennesima notte sudata e insonne. A destra, aria fresca e nebulizzata dove dormi.",
  h2_reasons="6 motivi per passare al CoolJet",
  reasons=[("Fresco dove sei davvero","Scrivania, letto, divano — ti segue di stanza in stanza."),("Una frazione del costo di un condizionatore","89 € oggi contro migliaia per un impianto fisso."),("Nebbia a ultrasuoni","Una fine nebbia fresca per un freddo più deciso nei giorni secchi."),("Adatto al sonno","Modalità silenziosa + luce notturna soffusa accanto."),("Timer","Si spegne da solo — niente risvegli notturni."),("Economico","Alimentazione USB — presa, portatile o power bank.")],
  h2_cmp="CoolJet vs le alternative",col_fan="Ventilatore",col_ac="Condizionatore fisso",
  cmp_after="E rispetto a <strong>Coolizi</strong> — il raffrescatore che molti hanno trovato per primo — il CoolJet è lo stesso tipo di prodotto ma paga correttamente in <strong>euro</strong>, spedisce in <strong>Italia</strong> con tracciamento e indica un <strong>reso 30 giorni</strong>. Proprio ciò che con Coolizi non ha funzionato — per questo i nostri link portano al CoolJet.",
  who="— Giudizio della redazione del Cooling Report",vgood_h="Dove eccelle",vwarn_h="Aspettative realistiche",
  vgood=["Raffrescamento personale che ti segue","Nebbia + 4 velocità + modalità notte silenziosa","Checkout localizzato in €, reso 30 giorni indicato"],
  vwarn=["Rinfresca <em>te</em>, non l'intera stanza","Riempire e pulire ogni tanto il serbatoio","Rende al meglio entro circa un metro"],
  h2_deal="Scegli la tua offerta — -50% oggi",deal_badge="Prezzo estivo caldo — attivo ora",
  seal_alt="Garanzia soddisfatti o rimborsati 30 giorni",seal="30 giorni soddisfatti o rimborsati · spedizione tracciata · pagamento sicuro",
  cta="Verifica prezzo &amp; disponibilità",t1="Pagamento sicuro",t2="30 giorni rimborso",t3="Spedizione tracciata",
  price_note="Prezzi, pacchetti e disponibilità sono decisi dal venditore e possono cambiare durante un'ondata di caldo — il pulsante mostra sempre l'offerta attuale.",
  h2_faq="Risposte chiare alle domande frequenti",
  faq=[("Rinfresca davvero la mia camera?","Rinfresca l'aria intorno a <em>te</em> — perfetto puntato sulla sedia o sulla testata. Non raffredda un'intera stanza come un apparecchio a compressore, e non lo raccontiamo. Per un sollievo personale ravvicinato in piena ondata di caldo è lo strumento giusto."),
       ("Quanto costa e posso restituirlo?","L'unità singola costa 89,95 € (invece di 179,90 €), con prezzo unitario più basso sui pacchetti. Il venditore indica 30 giorni soddisfatti o rimborsati — condizioni al checkout."),
       ("La consegna in Italia è gestita?","Sì — il checkout CoolJet è impostato per la consegna tracciata in Italia, prezzi in euro."),
       ("Perché non comprare semplicemente Coolizi?","Stesso tipo di prodotto — ma indirizziamo al CoolJet perché paga in €, spedisce in Italia e indica 30 giorni di reso. Proprio ciò che con Coolizi non ha funzionato.")],
  imagine="Immagina stanotte: la stanza ancora calda, ma una brezza fresca e leggermente nebulizzata sul viso — e ti addormenti davvero. È tutto qui il senso di un raffrescatore personale. Non l'intera casa. Solo tu.",
  urg_top="PERCHÉ ORA, NON DOPO",urg_h="Il prezzo -50% è una promo da ondata di caldo — non il prezzo normale",urg_pill="-50% · finché dura la promo estiva",
  urg_p="I raffrescatori compatti come questo vanno regolarmente esauriti in piena ondata di caldo, e gli 89,95 € di oggi sono uno sconto di lancio a tempo sul prezzo di listino di 179,90 € — non permanente. Quando la promo finisce o il lotto si esaurisce, si torna al prezzo pieno con attesa. Se lo vuoi sulla scrivania questa settimana, blocca ora il prezzo scontato.",
  urg_cta="Prendo il CoolJet a -50%",
  ep_title="Aspetta — stavi per perdere il -50%",
  ep_text="Il tuo <strong>sconto caldo del 50%</strong> è ancora attivo — <strong>89,95 €</strong> invece di 179,90 €. Quando la promo estiva finisce, si torna al prezzo pieno. Prendilo prima di uscire.",
  ep_cta="Prendi il CoolJet a -50%",ep_no="No grazie, pagherò il prezzo pieno più tardi",
  aff="<strong>Informativa pubblicitaria.</strong> Questo è un pubbliredazionale sponsorizzato, non un contenuto editoriale indipendente. Riceviamo una commissione se acquisti tramite i link in questa pagina, senza costi aggiuntivi per te. Caratteristiche, prezzi e disponibilità sono decisi dal venditore ed erano corretti al momento della stesura. I raffrescatori evaporativi offrono un raffrescamento personale e localizzato e non sostituiscono un condizionatore a compressore.",
  f_priv="Privacy",f_terms="Termini",f_disc="Informativa affiliazione",f_contact="Contatti",
  copyright="© 2026 The Cooling Report. Tutti i nomi dei prodotti sono marchi dei rispettivi proprietari.",
  sticky_cta="Ottieni il -50% →"),

 "es": dict(ef="J5XB6R",tag="cj-es",cur="€",now="89,95",was="179,90",off="-50%",per="/u.",
  title="Ola de calor: el climatizador de 89 € agotado en toda España",
  desc="Mientras España se asa, un climatizador evaporativo compacto vuela de las estanterías. Qué hace el CoolJet, cuánto cuesta, por qué se deja Coolizi — y la oferta -50%.",
  desk="Sección Consumo",updated="Actualizado 13 julio 2026",
  ticker="🔴 ALERTA POR CALOR&nbsp;&nbsp;·&nbsp;&nbsp;LAS TEMPERATURAS SUBEN ESTA SEMANA&nbsp;&nbsp;·&nbsp;&nbsp;LOS CLIMATIZADORES VUELAN&nbsp;&nbsp;·&nbsp;&nbsp;-50% HASTA AGOTAR EXISTENCIAS&nbsp;&nbsp;·&nbsp;&nbsp;VENCE AL CALOR HOY&nbsp;&nbsp;·&nbsp;&nbsp;",
  kick="Alerta por calor · se agota",
  h1='Ola de calor: el climatizador de 89 € <span class="hl">agotado en toda España</span> — y por qué todos se pasan a él',
  stand="Un ventilador solo mueve aire caliente. Un aire acondicionado de verdad cuesta miles. España ha encontrado una tercera vía — y esta semana se agota más rápido de lo que los vendedores reponen.",
  spon="Contenido patrocinado",by="Por la redacción de Cooling Report",read="4 min de lectura",
  fast="Muy demandado en esta ola de calor",prod="climatizador de aire portátil",
  figcap="El CoolJet — un climatizador evaporativo del tamaño de una mano que refresca y humidifica el aire a tu alrededor.",
  lead="Si has pasado una sola noche este verano en vela, con el ventilador a tope y la habitación igual de asfixiante, ya conoces la verdad incómoda: un ventilador normal solo mueve el aire caliente de un lado a otro. No baja la temperatura — ni un grado.",
  heat="Ya se han alcanzado <strong>38°C este mes</strong> — y el próximo pico será más caluroso según las previsiones. Millones intentan dormir en habitaciones que no se enfrían.",
  hm_head="AVISO POR CALOR EXTREMO — España, esta semana",hm_foot_l="Cooling Report · previsión de calor",hm_foot_r="Actualizado esta semana",
  cities=[("Bilbao",33,40,16,False),("Zaragoza",38,54,28,False),("Barcelona",36,70,30,False),("Madrid",40,48,44,True),("Valencia",38,64,52,False),("Sevilla",42,34,68,False),("Málaga",39,44,74,False),("Murcia",39,60,66,False)],
  p_ac="La solución obvia — un aire acondicionado de pared de verdad — cuesta entre <strong>2.000 y 5.000 €</strong> instalado, más una factura más alta cada vez que lo enciendes. Un precio brutal para las pocas semanas realmente abrasadoras. Así que la mayoría aprieta los dientes. Hasta ahora.",
  lady_alt="Una mujer despierta en la cama, con demasiado calor para dormir durante la ola de calor",
  lady_cap="¿Te suena? Cuando la habitación no se enfría, dar vueltas no sirve de nada.",
  h2_myths="5 mitos sobre los ventiladores",
  myths=[('«Un ventilador enfría la habitación.»',"No. Mueve el aire, pero no baja la temperatura.","Un climatizador evaporativo enfría y nebuliza el aire antes de que te llegue."),
         ('«Hay que enfriar toda la habitación.»',"No — basta con enfriar el aire a <em>tu</em> alrededor.","Enfriar tu escritorio o cama cuesta menos y actúa en minutos."),
         ('«Solo un aire de 2.000 € enfría de verdad.»',"Para una casa, sí. ¿Para una persona? Excesivo.","Un climatizador de 89 € cubre el metro que importa."),
         ('«Los climatizadores portátiles son ruidosos.»',"Los antiguos, sí. Este tiene un modo noche silencioso de verdad.","Zumbido bajo + luz suave — duermes justo al lado."),
         ('«Gastan una fortuna en luz.»',"No esta categoría. Consume poco, por USB.","Céntimos por noche, no los euros de un aire acondicionado.")],
  see_deal="Ver la oferta -50%",
  h2_what="Entonces, ¿qué es exactamente el CoolJet?",
  what_b="Claro y directo: es un climatizador evaporativo, no un aire acondicionado.",
  what=" Llenas un pequeño depósito y un ventilador pasa el aire por el filtro húmedo: el aire que te llega es más fresco y ligeramente nebulizado. Está pensado para <strong>refrescar de forma personal y cercana</strong> — escritorio, cama, carrito, tienda — no para una habitación entera. Quien diga que un aparato de 90 € sustituye a un aire acondicionado, miente. Pero en su función real es realmente bueno.",
  chips=["Fresco &amp; niebla","4 velocidades","Modo noche silencioso","Bajo consumo / USB"],
  h2_ba="Antes vs después",ba_alt="Antes: habitación calurosa. Después: habitación fresca con un climatizador.",
  ba_cap="A la izquierda, otra noche sudorosa y en vela. A la derecha, aire fresco y nebulizado donde duermes.",
  h2_reasons="6 razones para pasarse al CoolJet",
  reasons=[("Fresco donde estás de verdad","Escritorio, cama, sofá — te sigue de habitación en habitación."),("Una fracción del coste de un aire","89 € hoy frente a miles por una instalación fija."),("Niebla ultrasónica","Una fina niebla fresca para un frío más marcado en días secos."),("Bueno para dormir","Modo silencioso + luz nocturna suave al lado."),("Temporizador","Se apaga solo — sin despertarte de noche."),("Económico","Alimentación USB — enchufe, portátil o batería.")],
  h2_cmp="CoolJet vs las alternativas",col_fan="Ventilador",col_ac="Aire fijo",
  cmp_after="Y frente a <strong>Coolizi</strong> — el climatizador que muchos encontraron primero — el CoolJet es el mismo tipo de producto pero cobra correctamente en <strong>euros</strong>, envía a <strong>España</strong> con seguimiento e indica una <strong>devolución de 30 días</strong>. Justo lo que falló con Coolizi — por eso nuestros enlaces van a CoolJet.",
  who="— Valoración editorial de Cooling Report",vgood_h="En qué destaca",vwarn_h="Expectativas realistas",
  vgood=["Refresco personal que te acompaña","Niebla + 4 velocidades + modo noche silencioso","Pago localizado en €, 30 días de devolución indicados"],
  vwarn=["Te refresca <em>a ti</em>, no toda la habitación","Rellenar y limpiar de vez en cuando el depósito","Rinde mejor hasta un metro aprox."],
  h2_deal="Elige tu oferta — -50% hoy",deal_badge="Precio de ola de calor — activo ahora",
  seal_alt="Garantía de devolución de 30 días",seal="30 días de devolución · envío con seguimiento · pago seguro",
  cta="Ver precio &amp; disponibilidad",t1="Pago seguro",t2="30 días de devolución",t3="Envío con seguimiento",
  price_note="Los precios, packs y stock los fija el vendedor y pueden cambiar durante una ola de calor — el botón muestra siempre la oferta actual.",
  h2_faq="Respuestas claras a las preguntas frecuentes",
  faq=[("¿De verdad enfría mi habitación?","Enfría el aire a <em>tu</em> alrededor — perfecto apuntado a la silla o al cabecero. No enfría una habitación entera como un equipo con compresor, y no lo pintamos de otra forma. Para alivio personal y cercano en plena ola de calor es la herramienta justa."),
       ("¿Cuánto cuesta y puedo devolverlo?","La unidad cuesta 89,95 € (antes 179,90 €), con precio por unidad más bajo en packs. El vendedor indica 30 días de devolución — condiciones al pagar."),
       ("¿El envío a España está resuelto?","Sí — el pago de CoolJet está configurado para envío con seguimiento a España, precios en euros."),
       ("¿Por qué no comprar Coolizi sin más?","Mismo tipo de producto — pero recomendamos CoolJet porque cobra en €, envía a España e indica 30 días de devolución. Justo lo que falló con Coolizi.")],
  imagine="Imagina esta noche: la habitación aún cálida, pero una brisa fresca y ligeramente nebulizada en la cara — y por fin te duermes. De eso va un climatizador personal. No de toda la casa. Solo de ti.",
  urg_top="POR QUÉ AHORA, NO DESPUÉS",urg_h="El precio -50% es una promo de ola de calor — no el precio habitual",urg_pill="-50% · mientras dure la promo de verano",
  urg_p="Los climatizadores compactos como este se agotan con frecuencia en plena ola de calor, y los 89,95 € de hoy son un descuento de lanzamiento por tiempo limitado sobre el precio de lista de 179,90 € — no permanente. Cuando acaba la promo o se agota el lote, se vuelve al precio completo y a esperar. Si lo quieres en tu escritorio esta semana, asegura ahora el precio rebajado.",
  urg_cta="Quiero el CoolJet al -50%",
  ep_title="Espera — ibas a perder el -50%",
  ep_text="Tu <strong>descuento por calor del 50%</strong> sigue activo — <strong>89,95 €</strong> en vez de 179,90 €. Cuando acabe la promo de verano, se vuelve al precio completo. Aprovéchalo antes de irte.",
  ep_cta="Conseguir el CoolJet al -50%",ep_no="No gracias, pagaré el precio completo más tarde",
  aff="<strong>Aviso publicitario.</strong> Esto es un publirreportaje patrocinado, no contenido editorial independiente. Recibimos una comisión si compras a través de los enlaces de esta página, sin coste adicional para ti. Las características, precios y disponibilidad los fija el vendedor y eran correctos al redactar. Los climatizadores evaporativos ofrecen refresco personal y localizado y no sustituyen a un aire acondicionado con compresor.",
  f_priv="Privacidad",f_terms="Términos",f_disc="Aviso de afiliación",f_contact="Contacto",
  copyright="© 2026 The Cooling Report. Todos los nombres de producto son marcas de sus respectivos propietarios.",
  sticky_cta="Consigue el -50% →"),

 "nl": dict(ef="J1QMZZ",tag="cj-nl",cur="€",now="89,95",was="179,90",off="-50%",per="/st.",
  title="Hittegolf: de koeler van 89 € die overal in Nederland uitverkocht is",
  desc="Terwijl Nederland smelt, vliegt een compacte verdampingskoeler de schappen uit. Wat de CoolJet doet, wat hij kost, waarom mensen Coolizi laten staan — en de 50%-deal.",
  desk="Consumentenredactie",updated="Bijgewerkt 13 juli 2026",
  ticker="🔴 HITTEGOLF-ALARM&nbsp;&nbsp;·&nbsp;&nbsp;TEMPERATUREN LOPEN DEZE WEEK WEER OP&nbsp;&nbsp;·&nbsp;&nbsp;COMPACTE KOELERS RAKEN SNEL UITVERKOCHT&nbsp;&nbsp;·&nbsp;&nbsp;-50% ZOLANG DE VOORRAAD STREKT&nbsp;&nbsp;·&nbsp;&nbsp;VERSLA DE HITTE VANDAAG&nbsp;&nbsp;·&nbsp;&nbsp;",
  kick="Hittegolf-alarm · snel uitverkocht",
  h1='Hittegolf: de koeler van 89 € die <span class="hl">overal uitverkocht raakt</span> — en waarom iedereen overstapt',
  stand="Een ventilator verplaatst alleen warme lucht. Een echte airco kost duizenden euro's. Nederland heeft een derde optie gevonden — en deze week is hij sneller weg dan verkopers kunnen bijvullen.",
  spon="Gesponsord artikel",by="Door de redactie van Cooling Report",read="4 min leestijd",
  fast="Populair tijdens deze hittegolf",prod="draagbare luchtkoeler",
  figcap="De CoolJet — een verdampingskoeler ter grootte van een hand die de lucht om je heen koelt en bevochtigt.",
  lead="Als je deze zomer ook maar één nacht wakker lag met de ventilator op vol vermogen en de kamer nog steeds benauwd, ken je de ongemakkelijke waarheid: een gewone ventilator verplaatst alleen warme lucht van de ene kant naar de andere. Hij verlaagt de temperatuur niet — geen enkele graad.",
  heat="Het werd deze maand al <strong>38°C</strong> — en de volgende piek wordt volgens de weersverwachting nog heter. Miljoenen proberen te slapen in slaapkamers die simpelweg niet afkoelen.",
  hm_head="EXTREME HITTEWAARSCHUWING — Nederland, deze week",hm_foot_l="Cooling Report · hitte-verwachting",hm_foot_r="Deze week bijgewerkt",
  cities=[("Groningen",32,64,16,False),("Leeuwarden",32,50,18,False),("Zwolle",34,58,34,False),("Amsterdam",34,40,38,False),("Den Haag",33,30,48,False),("Utrecht",35,48,48,False),("Eindhoven",36,52,66,False),("Maastricht",37,56,80,True)],
  p_ac="De voor de hand liggende oplossing — een echte wandairco — kost geïnstalleerd <strong>2.000 tot 5.000 euro</strong>, plus een hogere energierekening bij elk gebruik. Een keiharde prijs voor de paar echt snikhete weken. Dus zweten de meesten het maar uit. Tot nu.",
  lady_alt="Een vrouw ligt wakker in bed, te warm om te slapen tijdens de hittegolf",
  lady_cap="Herkenbaar? Als de slaapkamer niet afkoelt, helpt draaien en woelen niets.",
  h2_myths="5 mythes over ventilatoren",
  myths=[('„Een ventilator koelt de kamer."',"Niet waar. Hij verplaatst lucht, maar verlaagt de temperatuur niet.","Een verdampingskoeler koelt en vernevelt de lucht voordat die je bereikt."),
         ('„Je moet de hele kamer koelen."',"Nee — je hoeft alleen de lucht om <em>jou</em> heen te koelen.","Gericht koelen op je bureau of bed is goedkoper en werkt in minuten."),
         ('„Alleen een airco van 2.000 € koelt echt."',"Voor een heel huis, ja. Voor één persoon? Overdreven.","Een koeler van 89 € dekt de meter die telt."),
         ('„Draagbare koelers zijn allemaal luidruchtig."',"Oude wel. Deze heeft een echte stille nachtstand.","Laag gezoem + zacht licht — je slaapt er vlak naast."),
         ('„Ze kosten een vermogen aan stroom."',"Deze klasse niet. Hij verbruikt weinig, via USB.","Centen per nacht, niet de euro's van een airco.")],
  see_deal="Bekijk de -50% deal",
  h2_what="Wat is de CoolJet nu precies?",
  what_b="Eerlijk: het is een verdampingskoeler, geen airco.",
  what=" Je vult een klein reservoir en een ventilator trekt lucht langs het vochtige filter: de lucht die bij je aankomt is koeler en licht verneveld. Hij is gemaakt voor <strong>persoonlijke koeling dichtbij</strong> — bureau, bed, kinderwagen, tent — niet voor een hele kamer. Wie zegt dat een apparaat van 90 € een airco vervangt, liegt. Maar in zijn echte taak is hij echt goed.",
  chips=["Koelen &amp; nevel","4 standen","Stille nachtstand","Zuinig / USB"],
  h2_ba="Voor vs na",ba_alt="Voor: warme slaapkamer. Na: koele slaapkamer met een koeler.",
  ba_cap="Links, weer een zweterige, slapeloze nacht. Rechts, gekoelde en vernevelde lucht waar je slaapt.",
  h2_reasons="6 redenen om over te stappen",
  reasons=[("Koel waar je echt bent","Bureau, bed, bank — hij gaat met je mee."),("Een fractie van de airco-kosten","89 € vandaag versus duizenden voor een vaste installatie."),("Ultrasone nevel","Een fijne koele nevel voor scherpere kou op droge dagen."),("Fijn om te slapen","Stille stand + zacht nachtlampje ernaast."),("Timer","Schakelt vanzelf uit — 's nachts niet wakker worden."),("Zuinig","USB-gevoed — stopcontact, laptop of powerbank.")],
  h2_cmp="CoolJet vs de alternatieven",col_fan="Ventilator",col_ac="Vaste airco",
  cmp_after="En vergeleken met <strong>Coolizi</strong> — de koeler die velen eerst vonden — is de CoolJet hetzelfde soort product, maar rekent netjes af in <strong>euro's</strong>, levert naar <strong>Nederland</strong> met track &amp; trace en vermeldt <strong>30 dagen retour</strong>. Precies waar het bij Coolizi misging — daarom gaan onze links naar CoolJet.",
  who="— Redactioneel oordeel van Cooling Report",vgood_h="Waar hij uitblinkt",vwarn_h="Houd verwachtingen reëel",
  vgood=["Snelle persoonlijke koeling die met je meegaat","Nevel + 4 standen + stille nachtstand","Gelokaliseerde €-checkout, 30 dagen retour vermeld"],
  vwarn=["Koelt <em>jou</em>, niet een hele kamer","Reservoir bijvullen en af en toe schoonmaken","Werkt het best tot ongeveer een meter"],
  h2_deal="Kies je deal — vandaag -50%",deal_badge="Hittegolf-zomerprijs — nu actief",
  seal_alt="30 dagen niet-goed-geld-terug garantie",seal="30 dagen geld terug · verzending met track &amp; trace · veilig afrekenen",
  cta="Bekijk prijs &amp; voorraad",t1="Veilig afrekenen",t2="30 dagen geld terug",t3="Verzending met tracking",
  price_note="Prijzen, bundels en voorraad worden bepaald door de verkoper en kunnen tijdens een hittegolf veranderen — de knop toont altijd de actuele aanbieding.",
  h2_faq="Duidelijke antwoorden op veelgestelde vragen",
  faq=[("Koelt dit echt mijn slaapkamer?","Het koelt de lucht om <em>jou</em> heen — perfect gericht op de bureaustoel of het hoofdeinde. Het koelt geen hele kamer zoals een compressor-apparaat, en dat doen we ook niet alsof. Voor persoonlijke verkoeling dichtbij tijdens een hittegolf is het precies het juiste."),
       ("Wat kost hij en kan ik hem terugsturen?","Een losse unit kost nu €89,95 (was €179,90), met lagere stukprijs bij meerdere. De verkoper vermeldt 30 dagen retour — voorwaarden bij het afrekenen."),
       ("Is bezorging in Nederland geregeld?","Ja — de CoolJet-checkout is ingesteld op bezorging met tracking in Nederland, prijzen in euro's."),
       ("Waarom niet gewoon Coolizi?","Zelfde soort product — maar we verwijzen naar CoolJet omdat hij in € afrekent, naar Nederland levert en 30 dagen retour vermeldt. Precies waar het bij Coolizi misging.")],
  imagine="Stel je vanavond voor: de kamer nog warm, maar een koele, zacht vernevelde bries recht op je gezicht — en je valt echt in slaap. Daar draait een persoonlijke koeler om. Niet het hele huis. Alleen jij.",
  urg_top="WAAROM NU, NIET LATER",urg_h="De -50%-prijs is een hittegolf-actie — niet de normale prijs",urg_pill="-50% · zolang de zomeractie loopt",
  urg_p="Compacte koelers als deze raken tijdens een hittegolf regelmatig uitverkocht, en de €89,95 van vandaag is een tijdelijke introductiekorting op de adviesprijs van €179,90 — niet blijvend. Als de actie stopt of deze partij op is, geldt weer de volle prijs plus wachttijd. Wil je hem deze week op je bureau, zet dan nu de kortingsprijs vast.",
  urg_cta="Ik wil de CoolJet met -50%",
  ep_title="Wacht — je zou de -50% mislopen",
  ep_text="Je <strong>hittegolfkorting van 50%</strong> is nog actief — <strong>€89,95</strong> in plaats van €179,90. Als de zomeractie stopt, geldt weer de volle prijs. Pak hem voordat je weggaat.",
  ep_cta="CoolJet met -50% pakken",ep_no="Nee bedankt, ik betaal later de volle prijs",
  aff="<strong>Advertentie-informatie.</strong> Dit is een gesponsord advertorial, geen onafhankelijke redactie. We ontvangen een commissie als je via de links op deze pagina koopt, zonder extra kosten voor jou. Productclaims, prijzen en beschikbaarheid worden bepaald door de verkoper en waren correct op het moment van schrijven. Verdampingskoelers bieden persoonlijke, gerichte koeling en vervangen geen airco met compressor.",
  f_priv="Privacy",f_terms="Voorwaarden",f_disc="Affiliate-informatie",f_contact="Contact",
  copyright="© 2026 The Cooling Report. Alle productnamen zijn handelsmerken van hun respectieve eigenaren.",
  sticky_cta="Pak de -50% →"),
}

# clone the fixed structural bits (bundles/comparison rows) into each localized geo
for code, d in _L.items():
    d["code"] = code; d["lang"] = code
    d["cmp_rows"] = GEOS["en"]["cmp_rows"]
    # localized bundle "Most popular" ribbon + Save labels
    save = {"de":("Sparen 50%","Sparen 55%","Sparen 67%","Beliebt"),
            "fr":("-50%","-55%","-67%","Le + choisi"),
            "it":("Risparmia 50%","Risparmia 55%","Risparmia 67%","Il più scelto"),
            "es":("Ahorra 50%","Ahorra 55%","Ahorra 67%","El más elegido"),
            "nl":("Bespaar 50%","Bespaar 55%","Bespaar 67%","Populairst")}[code]
    d["bundles"] = [("1× CoolJet","89,95",save[0],""),("2× CoolJet","79,95",save[1],save[3]),("3× CoolJet","59,95",save[2],"")]
    GEOS[code] = d


def main():
    for code, g in GEOS.items():
        dd = os.path.join(OUT, code, "cooljet")
        os.makedirs(dd, exist_ok=True)
        with open(os.path.join(dd, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(g))
        print("wrote", os.path.join(code, "cooljet", "index.html"))

if __name__ == "__main__":
    main()
