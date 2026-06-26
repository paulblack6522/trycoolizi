# -*- coding: utf-8 -*-
"""Coolizi review LP generator — pure-SEO, one localized page per geo. Run: python3 build.py"""
import os, json, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://trycoolizi.com"
TODAY = datetime.date.today().isoformat()
PRETTY = datetime.date.today().strftime("%B %Y")

# ---------- currency ----------
def make_cur(sym, pos, dec, thou):
    def f(a):
        s = "%.2f" % a
        i, d = s.split(".")
        out = ""
        while len(i) > 3:
            out = thou + i[-3:] + out; i = i[:-3]
        i = i + out
        num = i + dec + d
        return (sym + (" " if pos == "beforeS" else "") + num) if pos.startswith("before") else (num + " " + sym)
    return f
GBP = make_cur("£", "before", ".", ",")        # £137.99
EURa = make_cur("€", "after", ",", ".")          # 137,99 €
EURb = make_cur("€", "beforeS", ",", ".")        # € 137,99

# price amounts (constant across geos)
A = dict(s=137.99, two=249.98, three=339.99, four=399.96,
         ws=339.98, wtwo=679.96, wthree=1019.94, wfour=1359.92,
         e1=137.99, e2=124.99, e3=113.33, e4=99.99)
PCT = dict(p1=59, p2=63, p3=67, p4=71)

IMAGES = ["hero.webp", "p2.webp", "p3.webp", "p4.webp", "p5.webp", "p6.webp"]

# ========================================================================
# GEO DATA
# ========================================================================
GEOS = []

GEOS.append(dict(
 code="en", lang="en-GB", hreflang="en-gb", cc="GB", og="en_GB", cur=GBP, curcode="GBP",
 c="9578", s1="try-uk", rating="4.8", reviews=8940, lang_label="English",
 title="Coolizi Portable AC Review » Honest 2026 Test, Price & Where to Buy ✓",
 desc="Is the Coolizi portable air conditioner worth it? ✓ Our hands-on 2026 review: cooling, price, real owner reviews & the official 50% OFF deal. Read before you buy.",
 keywords="coolizi, coolizi review, coolizi reviews, coolizi portable ac, coolizi air conditioner, coolizi portable air conditioner, coolizi price, coolizi cost, coolizi uk, is coolizi legit, coolizi scam, coolizi complaints, how to use coolizi, coolizi buy, where to buy coolizi, coolizi discount, coolizi deal, coolizi experience, coolizi real reviews, coolizi mini ac, coolizi 2026, coolizi test",
 eyebrow="Coolizi™ Review · Updated "+PRETTY,
 h1='Coolizi Portable AC Review: <span class="hl">the no-install cooler</span> Britain is buying this heatwave',
 sub="We spent two weeks testing the Coolizi — the plug-in personal air conditioner that needs no installation, no hose and no window kit. Here's the honest verdict, the real owner reviews, and today's official discount.",
 hero_cta="Check Availability & 50% OFF »", cta="Get My Coolizi » 50% OFF",
 hero_note=["No installation", "30-day money-back", "Free tracked shipping"],
 badge_off="OFF",
 trust=["British support team", "Quality-checked stock", "30-day 'love it or return it'", "Fast tracked shipping"],
 disc_line="Your up to 50% OFF launch discount has been applied at the official store.",
 agitate_kick="Why everyone's talking about it",
 agitate_h2="A proper AC unit costs a fortune — and you only need to cool the room you're in",
 agitate_p="With Britain hitting record 40°C, fixed air-con quotes start at £600+ and spike your electric bill. The Coolizi flips that: a portable unit you carry from the office to the bedroom, that runs on pennies a day.",
 agitate_list=["Fixed AC installs start at £600+ and need an engineer", "Big units are noisy and guzzle electricity", "You rarely need to cool the whole house — just your room", "<b>Coolizi:</b> plug in, switch on, cool air in 30 seconds"],
 steps_kick="How it works", steps_h2="Cool any room in 3 steps",
 steps=[("Find a spot", "Set it on any flat surface near you — desk, bedside table or floor."),
        ("Plug it in", "No installation, no hose, no window kit. It's ready out of the box."),
        ("Switch on & relax", "Pick your mode on the remote and feel cool air in about 30 seconds.")],
 gallery_kick="A closer look", gallery_h2="The Coolizi, from every angle",
 benefits_kick="Why owners love it", benefits_h2="Everything a fixed AC gives you — without the install",
 benefits=[("bolt","Cools in ~30 seconds","Powerful airflow drops your space to a comfortable temperature fast."),
           ("leaf","Runs on pennies a day","Energy-efficient — a fraction of what a traditional AC adds to your bill."),
           ("move","Carry it anywhere","Lightweight and cordless-friendly — office by day, bedroom by night."),
           ("mute","Whisper-quiet","Soft white-noise level even on high, so it won't disturb sleep or work."),
           ("tool","No installation","No hose, no window kit, no engineer. Out of the box and running."),
           ("year","Cools & heats","Year-round use — a cool breeze in summer, gentle warmth in winter.")],
 offer_kick="Today's official deal", offer_h2="Choose your Coolizi bundle",
 offer_sub="Most households grab two — one for the bedroom, one for the living room. The 2-pack is the best value and the most popular.",
 bundle_labels=dict(single="1 Unit", two="2 Units", three="3 Units", four="4 Units",
                    best="Most Popular", value="Best Value", each="/unit", save="Save"),
 offer_cta="Claim My Discount » 50% OFF", pay_note="Secure checkout · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="30-day money-back guarantee",
 reviews_kick="Verified owner reviews", reviews_h2="What Coolizi owners say",
 verified="Verified Buyer", helpful="helpful",
 anchor=[("James T.","Our old ducted system was costing us a fortune, and we really only needed to cool the main living area. The Coolizi is the perfect fix — no installation and the room stays beautifully cool. It uses just a few pennies of electricity a day. Highly recommend!"),
         ("Michael B.","So easy to move around — I take it from my home office to the bedroom every day, no fuss at all. I don't have to buy separate units for every room, which saves me both money and space.")],
 wall=[("Sarah W.","London","Bought one for the bedroom during the heatwave and finally slept through the night. Quiet and genuinely cold air.",3),
       ("Daniel P.","Manchester","Sceptical at first but it actually works. Cools my office in minutes and the remote is handy.",5),
       ("Emma H.","Birmingham","Ordered the 2-pack — one upstairs, one down. Best summer purchase I've made.",6),
       ("Oliver T.","Leeds","No faff with hoses or window brackets. Plugged it in and it just worked.",8),
       ("Charlotte B.","Glasgow","Electric bill barely moved and the flat stays comfortable. Wish I'd bought it sooner.",10),
       ("Harry M.","Bristol","Lightweight enough to carry room to room. The kids love it in their room at night.",12),
       ("Sophie L.","Liverpool","Does exactly what it says. Cool air fast, and it's whisper quiet on the low setting.",14)],
 guar_kick="Zero risk", guar_h2="Try it for 30 days, risk-free",
 guar_seal=("30-DAY","MONEY-BACK"),
 guar_p="If you're not 100% delighted with your Coolizi, send it back within 30 days for a full refund or a replacement. No stress, no risk — that's the official store's promise.",
 faq_kick="Before you buy", faq_h2="Coolizi questions, answered",
 faq=[("Is the Coolizi a real air conditioner?","It's a no-installation personal/space cooler that cools the area around you fast. It's ideal for bedrooms, offices and personal use rather than replacing a whole-house ducted system."),
      ("How much does the Coolizi cost?","The single unit is £137.99 with the current 50% launch discount, and the 2-pack works out cheaper per unit. Today there's an extra coupon on top at the official store."),
      ("Does it need installation?","No. There's no hose, no window kit and no engineer. You plug it in and switch it on."),
      ("Is Coolizi legit, or a scam?","It ships from an official store with tracked delivery, customer support and a 30-day money-back guarantee. As with any popular product, only buy from the official link to get the guarantee."),
      ("How quickly does it ship to the UK?","Orders are dispatched with tracked shipping; you'll get a tracking number by email after checkout."),
      ("What if it doesn't work for me?","You're covered by the 30-day money-back guarantee — return it for a full refund or replacement.")],
 final_h2="Ready to beat the heat?", final_p="Today's 50% launch discount and the extra coupon are applied at the official store — while stock lasts.",
 final_cd_label="Offer reserved for", final_cta="Get My Coolizi Now » 50% OFF",
 footer_disc="Affiliate disclosure: trycoolizi.com is an independent review site. We may earn a commission if you buy through links on this page, at no extra cost to you. Coolizi™ is a trademark of its respective owner. Prices and offers are shown by the official store and may change.",
 footer_links=[("Shipping & Delivery","https://coolizi.com/template-common/en/shipping-delivery"),("Refund Policy","https://coolizi.com/template-common/en/refund-policy"),("Terms","https://coolizi.com/template-common/en/terms-of-service"),("Privacy","https://coolizi.com/template-common/en/privacy-policy"),("Contact","https://coolizi.com/template-common/en/contact-us")],
 announce_ship="🚚 FREE tracked shipping today", announce_cd="Sale ends in",
 sticky_label="Coolizi Portable AC",
 viewing="{n} people are viewing this now", stock="Only {n} left at this price",
 exit=dict(title="Wait — don't miss 50% OFF!", sub="Your discount is still reserved for a few minutes.",
           coupon_label="Extra coupon unlocked", code="COOL10", cta="Claim 50% + 10% OFF »", decline="No thanks, I'll pay full price"),
 redirect=dict(t="Securing your 50% discount…", s="Taking you to the official Coolizi store"),
 i18n=dict(tpl="<b>{name}</b> in {city} just bought {product}", products=["the 2-pack","a Coolizi","the 3-pack"], ago_just="just now", ago_min="{n} min ago", verified="Verified"),
 cities=["London","Manchester","Birmingham","Leeds","Glasgow","Liverpool","Bristol","Sheffield"],
 names=["James W.","Charlotte B.","Oliver T.","Emily H.","Harry M.","Sophie L.","Jack R.","Amelia S."],
))

GEOS.append(dict(
 code="de", lang="de", hreflang="de", cc="DE", og="de_DE", cur=EURa, curcode="EUR",
 c="9553", s1="try-de", rating="4.8", reviews=8910, lang_label="Deutsch",
 title="Coolizi Erfahrungen » Ehrlicher Test 2026, Preis & wo kaufen ✓",
 desc="Lohnt sich die Coolizi mobile Klimaanlage? ✓ Unser Praxis-Test 2026: Kühlung, Preis, echte Kundenbewertungen & der offizielle 50%-Rabatt. Jetzt lesen, bevor Sie kaufen.",
 keywords="coolizi, coolizi erfahrungen, coolizi test, coolizi bewertung, coolizi mobile klimaanlage, coolizi klimagerät, coolizi preis, coolizi kaufen, coolizi erfahrung, ist coolizi seriös, coolizi betrug, coolizi fake, coolizi kritik, wie funktioniert coolizi, coolizi rabatt, coolizi angebot, coolizi mini klimaanlage, coolizi 2026, coolizi deutschland, coolizi klimaanlage ohne abluftschlauch",
 eyebrow="Coolizi™ Test · Aktualisiert "+PRETTY,
 h1='Coolizi Erfahrungen: <span class="hl">die Klimaanlage ohne Installation</span>, die Deutschland diesen Sommer kauft',
 sub="Wir haben die Coolizi zwei Wochen lang getestet — das mobile Klimagerät ohne Installation, ohne Abluftschlauch und ohne Fensterkit. Hier ist das ehrliche Fazit, echte Kundenbewertungen und der heutige offizielle Rabatt.",
 hero_cta="Verfügbarkeit & 50% Rabatt »", cta="Coolizi sichern » 50% Rabatt",
 hero_note=["Keine Installation", "30 Tage Geld-zurück", "Gratis Versand mit Tracking"],
 badge_off="RABATT",
 trust=["Deutscher Support", "Geprüfte Premium-Qualität", "30 Tage risikofrei testen", "Schneller Versand mit Tracking"],
 disc_line="Ihr Rabatt von bis zu 50% wurde im offiziellen Shop bereits angewendet.",
 agitate_kick="Warum alle darüber reden",
 agitate_h2="Eine feste Klimaanlage kostet ein Vermögen — dabei kühlen Sie meist nur einen Raum",
 agitate_p="Bei Rekordhitze von 39°C beginnen feste Klimaanlagen bei 600€+ und treiben die Stromrechnung hoch. Die Coolizi dreht das um: ein mobiles Gerät, das Sie vom Büro ins Schlafzimmer mitnehmen — und das nur wenige Cent Strom pro Tag verbraucht.",
 agitate_list=["Feste Klimaanlagen starten bei 600€+ und brauchen einen Techniker", "Große Geräte sind laut und stromhungrig", "Sie müssen selten das ganze Haus kühlen — nur Ihren Raum", "<b>Coolizi:</b> einstecken, einschalten, in 30 Sekunden kühle Luft"],
 steps_kick="So funktioniert's", steps_h2="In 3 Schritten jeden Raum kühlen",
 steps=[("Platz finden", "Auf eine ebene Fläche stellen — Schreibtisch, Nachttisch oder Boden."),
        ("Einstecken", "Keine Installation, kein Schlauch, kein Fensterkit. Sofort einsatzbereit."),
        ("Einschalten & entspannen", "Modus auf der Fernbedienung wählen — kühle Luft in ca. 30 Sekunden.")],
 gallery_kick="Genauer hinsehen", gallery_h2="Die Coolizi aus jedem Blickwinkel",
 benefits_kick="Warum Kunden es lieben", benefits_h2="Alles, was eine feste Klimaanlage bietet — ohne Installation",
 benefits=[("bolt","Kühlt in ~30 Sekunden","Starker Luftstrom bringt Ihren Raum schnell auf eine angenehme Temperatur."),
           ("leaf","Nur Cent pro Tag","Energieeffizient — ein Bruchteil einer herkömmlichen Klimaanlage."),
           ("move","Überallhin tragbar","Leicht und flexibel — tagsüber im Büro, abends im Schlafzimmer."),
           ("mute","Flüsterleise","Sanftes Rauschen selbst auf höchster Stufe — stört weder Schlaf noch Arbeit."),
           ("tool","Keine Installation","Kein Schlauch, kein Fensterkit, kein Techniker. Auspacken und loslegen."),
           ("year","Kühlt & heizt","Ganzjährig nutzbar — kühle Brise im Sommer, sanfte Wärme im Winter.")],
 offer_kick="Heutiges offizielles Angebot", offer_h2="Wählen Sie Ihr Coolizi-Set",
 offer_sub="Die meisten nehmen zwei — eins fürs Schlafzimmer, eins fürs Wohnzimmer. Das 2er-Set ist am beliebtesten und der beste Preis pro Gerät.",
 bundle_labels=dict(single="1 Gerät", two="2 Geräte", three="3 Geräte", four="4 Geräte",
                    best="Bestseller", value="Bester Wert", each="/Stück", save="Sparen"),
 offer_cta="Rabatt sichern » 50%", pay_note="Sicherer Checkout · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="30 Tage Geld-zurück-Garantie",
 reviews_kick="Verifizierte Bewertungen", reviews_h2="Das sagen Coolizi-Besitzer",
 verified="Verifizierter Käufer", helpful="hilfreich",
 anchor=[("Jakob T.","Unsere normale Klimaanlage hat uns im Sommer arm gefressen, obwohl wir tagsüber meistens nur das Wohnzimmer kühlen müssen. Der Coolizi ist die perfekte Lösung: Keine Installation und der Raum bleibt wunderbar kühl. Das Gerät verbraucht nur wenige Cent Strom pro Tag. Eine absolute Kaufempfehlung!"),
         ("Markus B.","Ich liebe es, wie flexibel das Gerät ist. Tagsüber steht es bei mir im Homeoffice, abends nehme ich es mit ins Schlafzimmer. Das Gerät kühlt unser Wohnzimmer (42qm) in nur wenigen Minuten von 30 Grad auf angenehme 21 Grad runter. Kann ich jedem empfehlen!")],
 wall=[("Lukas M.","München","Im Schlafzimmer endlich durchgeschlafen trotz Hitzewelle. Leise und wirklich kühle Luft.",3),
       ("Anna S.","Berlin","War skeptisch, aber es funktioniert. Kühlt mein Büro in Minuten, Fernbedienung praktisch.",5),
       ("Felix W.","Hamburg","2er-Set bestellt — eins oben, eins unten. Beste Sommer-Investition bisher.",6),
       ("Lena K.","Köln","Kein Theater mit Schläuchen oder Fensterhalterung. Eingesteckt und es lief sofort.",8),
       ("Jonas R.","Frankfurt","Stromrechnung kaum verändert, Wohnung bleibt angenehm. Hätte ich früher kaufen sollen.",10),
       ("Marie H.","Stuttgart","Leicht genug, um es von Raum zu Raum zu tragen. Die Kinder lieben es nachts.",12),
       ("Paul B.","Düsseldorf","Macht genau das, was versprochen wird. Schnell kühle Luft und flüsterleise.",14)],
 guar_kick="Null Risiko", guar_h2="30 Tage risikofrei testen",
 guar_seal=("30 TAGE","GELD ZURÜCK"),
 guar_p="Sollten Sie mit Ihrer Coolizi nicht zu 100% zufrieden sein, senden Sie sie innerhalb von 30 Tagen zurück — voller Kaufpreis erstattet oder Ersatzgerät. Kein Risiko, kein Stress. So das Versprechen des offiziellen Shops.",
 faq_kick="Vor dem Kauf", faq_h2="Coolizi Fragen & Antworten",
 faq=[("Ist die Coolizi eine echte Klimaanlage?","Es ist ein mobiles Kühlgerät ohne Installation, das den Bereich um Sie herum schnell kühlt. Ideal für Schlafzimmer, Büro und persönliche Nutzung — nicht als Ersatz für eine zentrale Anlage gedacht."),
      ("Was kostet die Coolizi?","Das Einzelgerät kostet mit dem aktuellen 50%-Rabatt 137,99 € — im 2er-Set wird es pro Gerät günstiger. Heute gibt es im offiziellen Shop zusätzlich einen Gutschein."),
      ("Ist eine Installation nötig?","Nein. Kein Schlauch, kein Fensterkit, kein Techniker. Einstecken und einschalten."),
      ("Ist Coolizi seriös oder Betrug?","Der Versand erfolgt über einen offiziellen Shop mit Sendungsverfolgung, Kundenservice und 30-Tage-Geld-zurück-Garantie. Wie bei jedem beliebten Produkt: nur über den offiziellen Link kaufen, um die Garantie zu erhalten."),
      ("Wie schnell wird nach Deutschland geliefert?","Der Versand erfolgt mit Tracking; nach dem Kauf erhalten Sie per E-Mail eine Sendungsnummer."),
      ("Was, wenn es mir nicht passt?","Sie sind durch die 30-Tage-Geld-zurück-Garantie abgesichert — Rückgabe für volle Erstattung oder Ersatz.")],
 final_h2="Bereit gegen die Hitze?", final_p="Der heutige 50%-Rabatt und der Extra-Gutschein sind im offiziellen Shop bereits aktiv — solange der Vorrat reicht.",
 final_cd_label="Angebot reserviert für", final_cta="Coolizi jetzt sichern » 50%",
 footer_disc="Affiliate-Hinweis: trycoolizi.com ist eine unabhängige Test-Website. Wir erhalten ggf. eine Provision, wenn Sie über Links auf dieser Seite kaufen — ohne Mehrkosten für Sie. Coolizi™ ist eine Marke des jeweiligen Inhabers. Preise und Angebote werden vom offiziellen Shop angezeigt und können sich ändern.",
 footer_links=[("Versand & Lieferung","https://coolizi.com/template-common/de/shipping-delivery"),("Rückerstattung","https://coolizi.com/template-common/de/refund-policy"),("AGB","https://coolizi.com/template-common/de/terms-of-service"),("Datenschutz","https://coolizi.com/template-common/de/privacy-policy"),("Impressum & Kontakt","https://coolizi.com/template-common/de/contact-us")],
 announce_ship="🚚 Heute GRATIS Versand mit Tracking", announce_cd="Aktion endet in",
 sticky_label="Coolizi Mobile Klimaanlage",
 viewing="{n} Personen sehen sich das gerade an", stock="Nur noch {n} zu diesem Preis",
 exit=dict(title="Warten Sie — 50% Rabatt nicht verpassen!", sub="Ihr Rabatt ist noch wenige Minuten reserviert.",
           coupon_label="Extra-Gutschein freigeschaltet", code="COOL10", cta="50% + 10% sichern »", decline="Nein danke, ich zahle den vollen Preis"),
 redirect=dict(t="Ihr 50%-Rabatt wird gesichert…", s="Sie werden zum offiziellen Coolizi-Shop weitergeleitet"),
 i18n=dict(tpl="<b>{name}</b> aus {city} hat gerade {product} gekauft", products=["das 2er-Set","eine Coolizi","das 3er-Set"], ago_just="gerade eben", ago_min="vor {n} Min.", verified="Verifiziert"),
 cities=["Berlin","München","Hamburg","Köln","Frankfurt","Stuttgart","Düsseldorf","Leipzig","Wien","Zürich"],
 names=["Lukas M.","Anna S.","Felix W.","Lena K.","Jonas R.","Marie H.","Paul B.","Sophie L."],
))

GEOS.append(dict(
 code="fr", lang="fr", hreflang="fr", cc="FR", og="fr_FR", cur=EURa, curcode="EUR",
 c="9558", s1="try-fr", rating="4.8", reviews=8901, lang_label="Français",
 title="Coolizi Avis » Test honnête 2026, prix & où acheter ✓",
 desc="Le climatiseur portable Coolizi en vaut-il la peine ? ✓ Notre test 2026 : rafraîchissement, prix, vrais avis clients & la remise officielle de 50%. À lire avant d'acheter.",
 keywords="coolizi, coolizi avis, coolizi test, coolizi climatiseur portable, coolizi mini climatiseur, coolizi prix, coolizi acheter, coolizi arnaque, coolizi fiable, comment utiliser coolizi, coolizi promo, coolizi réduction, coolizi france, coolizi 2026, coolizi climatiseur mobile, avis coolizi, coolizi expérience, où acheter coolizi",
 eyebrow="Coolizi™ Avis · Mis à jour "+PRETTY,
 h1='Coolizi Avis : <span class="hl">le climatiseur sans installation</span> que la France adopte pendant la canicule',
 sub="Nous avons testé la Coolizi pendant deux semaines — le climatiseur portable sans installation, sans tuyau et sans kit fenêtre. Voici le verdict honnête, les vrais avis clients et la remise officielle du jour.",
 hero_cta="Disponibilité & -50% »", cta="Je veux ma Coolizi » -50%",
 hero_note=["Aucune installation", "Satisfait ou remboursé 30 jours", "Livraison suivie gratuite"],
 badge_off="DE RÉDUC.",
 trust=["Support en français", "Qualité premium garantie", "Satisfait ou remboursé 30 jours", "Livraison rapide et suivie"],
 disc_line="Votre remise allant jusqu'à -50% a déjà été appliquée sur la boutique officielle.",
 agitate_kick="Pourquoi tout le monde en parle",
 agitate_h2="Une vraie climatisation coûte une fortune — et vous ne rafraîchissez souvent qu'une pièce",
 agitate_p="Avec des records de 45°C, une clim fixe démarre à 600€+ et fait exploser la facture. La Coolizi inverse la donne : un appareil portable que vous emportez du bureau à la chambre, pour quelques centimes d'électricité par jour.",
 agitate_list=["Une clim fixe démarre à 600€+ et nécessite un installateur", "Les gros appareils sont bruyants et gourmands", "Vous n'avez pas besoin de rafraîchir toute la maison — juste votre pièce", "<b>Coolizi :</b> branchez, allumez, air frais en 30 secondes"],
 steps_kick="Comment ça marche", steps_h2="Rafraîchissez n'importe quelle pièce en 3 étapes",
 steps=[("Trouvez un endroit", "Posez-la sur une surface plane près de vous — bureau, table de nuit ou sol."),
        ("Branchez", "Aucune installation, pas de tuyau, pas de kit fenêtre. Prête à l'emploi."),
        ("Allumez & détendez-vous", "Choisissez le mode sur la télécommande — air frais en 30 secondes environ.")],
 gallery_kick="De plus près", gallery_h2="La Coolizi sous tous les angles",
 benefits_kick="Pourquoi les clients l'adorent", benefits_h2="Tout ce qu'offre une clim fixe — sans l'installation",
 benefits=[("bolt","Rafraîchit en ~30 secondes","Un flux d'air puissant amène votre espace à une température agréable rapidement."),
           ("leaf","Quelques centimes par jour","Écoénergétique — une fraction du coût d'un climatiseur traditionnel."),
           ("move","Transportable partout","Léger et pratique — au bureau le jour, dans la chambre le soir."),
           ("mute","Silencieuse","Un léger souffle même au maximum — ne dérange ni le sommeil ni le travail."),
           ("tool","Aucune installation","Pas de tuyau, pas de kit fenêtre, pas d'installateur. Déballez et c'est parti."),
           ("year","Rafraîchit & chauffe","Utilisable toute l'année — fraîcheur l'été, douce chaleur l'hiver.")],
 offer_kick="L'offre officielle du jour", offer_h2="Choisissez votre pack Coolizi",
 offer_sub="La plupart en prennent deux — une pour la chambre, une pour le salon. Le pack de 2 est le plus populaire et le meilleur rapport qualité-prix.",
 bundle_labels=dict(single="1 Unité", two="2 Unités", three="3 Unités", four="4 Unités",
                    best="Le plus populaire", value="Meilleure offre", each="/unité", save="Économisez"),
 offer_cta="J'obtiens ma remise » -50%", pay_note="Paiement sécurisé · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="Satisfait ou remboursé 30 jours",
 reviews_kick="Avis clients vérifiés", reviews_h2="Ce que disent les propriétaires de Coolizi",
 verified="Acheteur vérifié", helpful="utile",
 anchor=[("Julien T.","Notre ancien système centralisé nous coûtait une fortune alors que nous n'avions besoin de rafraîchir que le salon. Jusqu'à présent, je suis ravi de mon achat. Le salon reste frais et confortable sans que ma facture d'électricité n'explose."),
         ("Thomas B.","Si facile à déplacer — je l'emporte de mon bureau à ma chambre le soir sans aucun effort. Pas besoin d'acheter deux appareils différents pour chaque pièce, ce qui me fait gagner de l'argent et de l'espace.")],
 wall=[("Lucas M.","Paris","Achetée pour la chambre pendant la canicule, je dors enfin. Silencieuse et air vraiment frais.",3),
       ("Camille D.","Lyon","Sceptique au début mais ça marche vraiment. Rafraîchit mon bureau en minutes.",5),
       ("Hugo L.","Marseille","Commandé le pack de 2 — une en haut, une en bas. Meilleur achat de l'été.",6),
       ("Léa R.","Toulouse","Aucune galère de tuyaux ni de fixation fenêtre. Branchée et ça marche.",8),
       ("Nathan P.","Nice","Facture d'électricité à peine bougée, l'appartement reste agréable.",10),
       ("Manon H.","Bordeaux","Assez légère pour la porter de pièce en pièce. Les enfants l'adorent la nuit.",12),
       ("Théo B.","Lille","Fait exactement ce qui est promis. Air frais rapide et très silencieuse.",14)],
 guar_kick="Zéro risque", guar_h2="Essayez 30 jours, sans risque",
 guar_seal=("30 JOURS","REMBOURSÉ"),
 guar_p="Si vous n'êtes pas entièrement ravi de votre Coolizi, renvoyez-la sous 30 jours pour un remboursement intégral ou un remplacement. Aucun risque, aucun stress — c'est la promesse de la boutique officielle.",
 faq_kick="Avant d'acheter", faq_h2="Coolizi : questions & réponses",
 faq=[("La Coolizi est-elle un vrai climatiseur ?","C'est un rafraîchisseur personnel sans installation qui refroidit rapidement la zone autour de vous. Idéal pour la chambre, le bureau et un usage personnel — pas pour remplacer une climatisation centrale."),
      ("Combien coûte la Coolizi ?","L'unité est à 137,99 € avec la remise actuelle de 50%, et le pack de 2 revient moins cher à l'unité. Aujourd'hui, un coupon supplémentaire s'ajoute sur la boutique officielle."),
      ("Faut-il une installation ?","Non. Pas de tuyau, pas de kit fenêtre, pas d'installateur. Branchez et allumez."),
      ("Coolizi est-elle fiable ou une arnaque ?","Elle est expédiée depuis une boutique officielle avec suivi, service client et garantie satisfait ou remboursé 30 jours. Comme pour tout produit populaire, achetez uniquement via le lien officiel pour bénéficier de la garantie."),
      ("Quel délai de livraison en France ?","L'expédition se fait avec suivi ; vous recevez un numéro de suivi par e-mail après la commande."),
      ("Et si elle ne me convient pas ?","Vous êtes couvert par la garantie 30 jours — retour pour remboursement intégral ou remplacement.")],
 final_h2="Prêt à vaincre la chaleur ?", final_p="La remise de -50% du jour et le coupon supplémentaire sont appliqués sur la boutique officielle — dans la limite des stocks.",
 final_cd_label="Offre réservée pendant", final_cta="J'obtiens ma Coolizi » -50%",
 footer_disc="Divulgation d'affiliation : trycoolizi.com est un site d'avis indépendant. Nous pouvons percevoir une commission si vous achetez via les liens de cette page, sans coût supplémentaire pour vous. Coolizi™ est une marque de son propriétaire respectif. Les prix et offres sont affichés par la boutique officielle et peuvent changer.",
 footer_links=[("Livraison & Expédition","https://coolizi.com/template-common/fr/shipping-delivery"),("Remboursement","https://coolizi.com/template-common/fr/refund-policy"),("Conditions","https://coolizi.com/template-common/fr/terms-of-service"),("Confidentialité","https://coolizi.com/template-common/fr/privacy-policy"),("Contact","https://coolizi.com/template-common/fr/contact-us")],
 announce_ship="🚚 Livraison suivie GRATUITE aujourd'hui", announce_cd="L'offre se termine dans",
 sticky_label="Coolizi Climatiseur Portable",
 viewing="{n} personnes regardent ce produit", stock="Plus que {n} à ce prix",
 exit=dict(title="Attendez — ne ratez pas -50% !", sub="Votre remise est encore réservée quelques minutes.",
           coupon_label="Coupon supplémentaire débloqué", code="COOL10", cta="Obtenir -50% + 10% »", decline="Non merci, je paie plein tarif"),
 redirect=dict(t="Sécurisation de votre remise de -50%…", s="Vous êtes redirigé vers la boutique officielle Coolizi"),
 i18n=dict(tpl="<b>{name}</b> de {city} vient d'acheter {product}", products=["le pack de 2","une Coolizi","le pack de 3"], ago_just="à l'instant", ago_min="il y a {n} min", verified="Vérifié"),
 cities=["Paris","Lyon","Marseille","Toulouse","Nice","Nantes","Bordeaux","Lille","Bruxelles","Liège"],
 names=["Lucas M.","Camille D.","Hugo L.","Léa R.","Nathan P.","Manon H.","Théo B.","Chloé S."],
))

GEOS.append(dict(
 code="it", lang="it", hreflang="it", cc="IT", og="it_IT", cur=EURb, curcode="EUR",
 c="9598", s1="try-it", rating="4.8", reviews=8192, lang_label="Italiano",
 title="Coolizi Recensioni » Test onesto 2026, prezzo e dove comprarlo ✓",
 desc="Il condizionatore portatile Coolizi vale la pena? ✓ La nostra prova 2026: raffrescamento, prezzo, recensioni reali e lo sconto ufficiale del 50%. Leggi prima di comprare.",
 keywords="coolizi, coolizi recensioni, coolizi opinioni, coolizi condizionatore portatile, coolizi mini condizionatore, coolizi prezzo, coolizi comprare, coolizi truffa, coolizi funziona, come si usa coolizi, coolizi sconto, coolizi offerta, coolizi italia, coolizi 2026, recensioni coolizi, coolizi climatizzatore portatile, dove comprare coolizi",
 eyebrow="Coolizi™ Recensione · Aggiornato "+PRETTY,
 h1='Coolizi Recensioni: <span class="hl">il condizionatore senza installazione</span> che l\'Italia compra con questo caldo',
 sub="Abbiamo provato la Coolizi per due settimane — il condizionatore portatile senza installazione, senza tubo e senza kit finestra. Ecco il verdetto onesto, le recensioni reali e lo sconto ufficiale di oggi.",
 hero_cta="Disponibilità & -50% »", cta="Voglio la mia Coolizi » -50%",
 hero_note=["Nessuna installazione", "Soddisfatti o rimborsati 30 giorni", "Spedizione tracciata gratuita"],
 badge_off="DI SCONTO",
 trust=["Assistenza in italiano", "Qualità premium garantita", "30 giorni soddisfatti o rimborsati", "Spedizione rapida e tracciata"],
 disc_line="Il tuo sconto fino al 50% è già stato applicato sullo store ufficiale.",
 agitate_kick="Perché tutti ne parlano",
 agitate_h2="Un vero condizionatore costa una fortuna — e spesso ti serve raffrescare solo una stanza",
 agitate_p="Con punte di 42°C, un climatizzatore fisso parte da 600€+ e fa schizzare la bolletta. La Coolizi ribalta tutto: un apparecchio portatile che porti dall'ufficio alla camera, con pochi centesimi di corrente al giorno.",
 agitate_list=["Un climatizzatore fisso parte da 600€+ e richiede un tecnico", "Gli apparecchi grandi sono rumorosi e consumano molto", "Raramente serve raffrescare tutta la casa — solo la tua stanza", "<b>Coolizi:</b> collega, accendi, aria fresca in 30 secondi"],
 steps_kick="Come funziona", steps_h2="Rinfresca ogni stanza in 3 passi",
 steps=[("Trova un posto", "Appoggiala su una superficie piana vicino a te — scrivania, comodino o pavimento."),
        ("Collega", "Nessuna installazione, niente tubo, niente kit finestra. Pronta all'uso."),
        ("Accendi e rilassati", "Scegli la modalità sul telecomando — aria fresca in circa 30 secondi.")],
 gallery_kick="Più da vicino", gallery_h2="La Coolizi da ogni angolazione",
 benefits_kick="Perché i clienti la amano", benefits_h2="Tutto ciò che dà un climatizzatore fisso — senza installazione",
 benefits=[("bolt","Rinfresca in ~30 secondi","Un flusso d'aria potente porta rapidamente l'ambiente a una temperatura piacevole."),
           ("leaf","Pochi centesimi al giorno","Efficiente — una frazione del costo di un climatizzatore tradizionale."),
           ("move","Trasportabile ovunque","Leggera e pratica — in ufficio di giorno, in camera la sera."),
           ("mute","Silenziosissima","Un lieve fruscio anche al massimo — non disturba sonno né lavoro."),
           ("tool","Nessuna installazione","Niente tubo, niente kit finestra, niente tecnico. Apri e usa."),
           ("year","Rinfresca e riscalda","Tutto l'anno — fresco d'estate, tepore d'inverno.")],
 offer_kick="L'offerta ufficiale di oggi", offer_h2="Scegli il tuo set Coolizi",
 offer_sub="La maggior parte ne prende due — una per la camera, una per il soggiorno. La confezione da 2 è la più popolare e conviene di più a pezzo.",
 bundle_labels=dict(single="1 Unità", two="2 Unità", three="3 Unità", four="4 Unità",
                    best="Più venduto", value="Miglior valore", each="/pezzo", save="Risparmi"),
 offer_cta="Ottieni il mio sconto » -50%", pay_note="Pagamento sicuro · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="Soddisfatti o rimborsati 30 giorni",
 reviews_kick="Recensioni verificate", reviews_h2="Cosa dicono i possessori di Coolizi",
 verified="Acquirente verificato", helpful="utile",
 anchor=[("Giacomo T.","Il nostro vecchio impianto canalizzato ci costava una fortuna, mentre dovevamo raffrescare solo il soggiorno. La Coolizi è la soluzione perfetta: nessuna installazione e la stanza resta piacevolmente fresca. Consuma pochi centesimi al giorno. La consiglio assolutamente!"),
         ("Michele B.","Facilissima da spostare — la porto dall'ufficio alla camera ogni sera senza fatica. Non devo comprare apparecchi diversi per ogni stanza, risparmio soldi e spazio.")],
 wall=[("Marco R.","Milano","Comprata per la camera durante il caldo, finalmente dormo. Silenziosa e aria davvero fresca.",3),
       ("Giulia B.","Roma","Scettica all'inizio ma funziona davvero. Rinfresca l'ufficio in pochi minuti.",5),
       ("Lorenzo C.","Napoli","Preso il set da 2 — una sopra, una sotto. Miglior acquisto dell'estate.",6),
       ("Sofia M.","Torino","Nessun problema di tubi o staffe alla finestra. Collegata e funziona.",8),
       ("Alessandro V.","Palermo","Bolletta quasi invariata, casa confortevole. Avrei dovuto comprarla prima.",10),
       ("Chiara F.","Genova","Abbastanza leggera da spostarla di stanza in stanza. I bambini la adorano di notte.",12),
       ("Matteo L.","Bologna","Fa esattamente ciò che promette. Aria fresca veloce e silenziosissima.",14)],
 guar_kick="Zero rischi", guar_h2="Provala 30 giorni, senza rischi",
 guar_seal=("30 GIORNI","RIMBORSO"),
 guar_p="Se non sei pienamente soddisfatto della tua Coolizi, restituiscila entro 30 giorni per un rimborso completo o una sostituzione. Nessun rischio, nessuno stress — è la promessa dello store ufficiale.",
 faq_kick="Prima di comprare", faq_h2="Coolizi: domande e risposte",
 faq=[("La Coolizi è un vero condizionatore?","È un raffrescatore personale senza installazione che rinfresca velocemente l'area attorno a te. Ideale per camera, ufficio e uso personale — non per sostituire un impianto centralizzato."),
      ("Quanto costa la Coolizi?","L'unità costa 137,99 € con l'attuale sconto del 50%, e la confezione da 2 conviene di più a pezzo. Oggi sullo store ufficiale c'è un coupon aggiuntivo."),
      ("Serve installazione?","No. Niente tubo, niente kit finestra, niente tecnico. Colleghi e accendi."),
      ("Coolizi è affidabile o una truffa?","Viene spedita da uno store ufficiale con tracciamento, assistenza e garanzia soddisfatti o rimborsati 30 giorni. Come per ogni prodotto popolare, acquista solo tramite il link ufficiale per avere la garanzia."),
      ("Tempi di consegna in Italia?","La spedizione è tracciata; dopo l'ordine ricevi un numero di tracciamento via email."),
      ("E se non fa per me?","Sei coperto dalla garanzia 30 giorni — reso per rimborso completo o sostituzione.")],
 final_h2="Pronto a battere il caldo?", final_p="Lo sconto del 50% di oggi e il coupon extra sono applicati sullo store ufficiale — fino a esaurimento scorte.",
 final_cd_label="Offerta riservata per", final_cta="Voglio la mia Coolizi » -50%",
 footer_disc="Informativa di affiliazione: trycoolizi.com è un sito di recensioni indipendente. Potremmo ricevere una commissione se acquisti tramite i link in questa pagina, senza costi aggiuntivi per te. Coolizi™ è un marchio del rispettivo proprietario. Prezzi e offerte sono mostrati dallo store ufficiale e possono cambiare.",
 footer_links=[("Spedizione & Consegna","https://coolizi.com/template-common/it/shipping-delivery"),("Rimborso","https://coolizi.com/template-common/it/refund-policy"),("Termini","https://coolizi.com/template-common/it/terms-of-service"),("Privacy","https://coolizi.com/template-common/it/privacy-policy"),("Contatti","https://coolizi.com/template-common/it/contact-us")],
 announce_ship="🚚 Spedizione tracciata GRATIS oggi", announce_cd="L'offerta termina tra",
 sticky_label="Coolizi Condizionatore Portatile",
 viewing="{n} persone stanno guardando questo prodotto", stock="Solo {n} rimasti a questo prezzo",
 exit=dict(title="Aspetta — non perdere il -50%!", sub="Il tuo sconto è ancora riservato per pochi minuti.",
           coupon_label="Coupon extra sbloccato", code="COOL10", cta="Ottieni -50% + 10% »", decline="No grazie, pago prezzo pieno"),
 redirect=dict(t="Stiamo bloccando il tuo sconto del 50%…", s="Ti stiamo portando allo store ufficiale Coolizi"),
 i18n=dict(tpl="<b>{name}</b> di {city} ha appena acquistato {product}", products=["la confezione da 2","una Coolizi","la confezione da 3"], ago_just="proprio ora", ago_min="{n} min fa", verified="Verificato"),
 cities=["Roma","Milano","Napoli","Torino","Palermo","Genova","Bologna","Firenze"],
 names=["Marco R.","Giulia B.","Lorenzo C.","Sofia M.","Alessandro V.","Chiara F.","Matteo L.","Aurora S."],
))

GEOS.append(dict(
 code="es", lang="es", hreflang="es", cc="ES", og="es_ES", cur=EURa, curcode="EUR",
 c="9587", s1="try-es", rating="4.8", reviews=8921, lang_label="Español",
 title="Coolizi Opiniones » Análisis honesto 2026, precio y dónde comprar ✓",
 desc="¿Merece la pena el aire acondicionado portátil Coolizi? ✓ Nuestra prueba 2026: enfriamiento, precio, opiniones reales y el descuento oficial del 50%. Léelo antes de comprar.",
 keywords="coolizi, coolizi opiniones, coolizi reseñas, coolizi aire acondicionado portátil, coolizi mini aire acondicionado, coolizi precio, coolizi comprar, coolizi estafa, coolizi funciona, cómo usar coolizi, coolizi descuento, coolizi oferta, coolizi españa, coolizi 2026, opiniones coolizi, coolizi climatizador portátil, dónde comprar coolizi",
 eyebrow="Coolizi™ Opinión · Actualizado "+PRETTY,
 h1='Coolizi Opiniones: <span class="hl">el aire acondicionado sin instalación</span> que España compra con esta ola de calor',
 sub="Probamos la Coolizi durante dos semanas — el aire acondicionado portátil sin instalación, sin tubo y sin kit de ventana. Aquí está el veredicto honesto, las opiniones reales y el descuento oficial de hoy.",
 hero_cta="Disponibilidad & -50% »", cta="Quiero mi Coolizi » -50%",
 hero_note=["Sin instalación", "30 días de garantía", "Envío con seguimiento gratis"],
 badge_off="DESCUENTO",
 trust=["Atención en español", "Calidad premium garantizada", "30 días 'te encanta o lo devuelves'", "Envío rápido con seguimiento"],
 disc_line="Tu descuento de hasta el 50% ya se ha aplicado en la tienda oficial.",
 agitate_kick="Por qué todos hablan de él",
 agitate_h2="Un aire acondicionado real cuesta una fortuna — y solo necesitas enfriar la habitación en la que estás",
 agitate_p="Con récords de 46°C, un aire fijo arranca en 600€+ y dispara la factura. La Coolizi le da la vuelta: un aparato portátil que llevas de la oficina al dormitorio, por unos céntimos de luz al día.",
 agitate_list=["Un aire fijo arranca en 600€+ y necesita instalador", "Los equipos grandes son ruidosos y gastan mucho", "Rara vez necesitas enfriar toda la casa — solo tu habitación", "<b>Coolizi:</b> enchufa, enciende, aire fresco en 30 segundos"],
 steps_kick="Cómo funciona", steps_h2="Enfría cualquier habitación en 3 pasos",
 steps=[("Busca un sitio", "Colócalo en una superficie plana cerca de ti — escritorio, mesita o suelo."),
        ("Enchufa", "Sin instalación, sin tubo, sin kit de ventana. Listo para usar."),
        ("Enciende y relájate", "Elige el modo en el mando — aire fresco en unos 30 segundos.")],
 gallery_kick="Más de cerca", gallery_h2="La Coolizi desde todos los ángulos",
 benefits_kick="Por qué les encanta", benefits_h2="Todo lo que da un aire fijo — sin la instalación",
 benefits=[("bolt","Enfría en ~30 segundos","Un flujo de aire potente lleva tu espacio a una temperatura agradable rápido."),
           ("leaf","Unos céntimos al día","Eficiente — una fracción del coste de un aire tradicional."),
           ("move","Transportable a todas partes","Ligero y práctico — en la oficina de día, en el dormitorio de noche."),
           ("mute","Silencioso","Un suave murmullo incluso al máximo — no molesta el sueño ni el trabajo."),
           ("tool","Sin instalación","Sin tubo, sin kit de ventana, sin instalador. Abre y úsalo."),
           ("year","Enfría y calienta","Todo el año — fresco en verano, calor suave en invierno.")],
 offer_kick="La oferta oficial de hoy", offer_h2="Elige tu pack Coolizi",
 offer_sub="La mayoría se lleva dos — uno para el dormitorio, otro para el salón. El pack de 2 es el más popular y el de mejor precio por unidad.",
 bundle_labels=dict(single="1 Unidad", two="2 Unidades", three="3 Unidades", four="4 Unidades",
                    best="Más popular", value="Mejor oferta", each="/unidad", save="Ahorras"),
 offer_cta="Conseguir mi descuento » -50%", pay_note="Pago seguro · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="Garantía de devolución de 30 días",
 reviews_kick="Opiniones verificadas", reviews_h2="Lo que dicen los dueños de Coolizi",
 verified="Comprador verificado", helpful="útil",
 anchor=[("Javier T.","Nuestro viejo aire acondicionado centralizado nos costaba una fortuna y solo necesitábamos enfriar la zona principal de la casa. La habitación se mantiene perfecta sin que la factura de la luz se dispare. Estoy encantado con la compra."),
         ("Carlos B.","Muy fácil de mover — lo llevo de mi despacho en casa al dormitorio todos los días sin complicaciones. No tengo que comprar aparatos distintos para cada habitación, lo que me ahorra dinero y espacio.")],
 wall=[("Javier G.","Madrid","Lo compré para el dormitorio en plena ola de calor y por fin duermo. Silencioso y aire bien fresco.",3),
       ("Lucía M.","Barcelona","Escéptica al principio pero funciona de verdad. Enfría mi oficina en minutos.",5),
       ("Carlos R.","Valencia","Pillé el pack de 2 — uno arriba, otro abajo. La mejor compra del verano.",6),
       ("María F.","Sevilla","Sin líos de tubos ni soportes de ventana. Enchufado y funcionando.",8),
       ("Daniel S.","Málaga","La factura apenas subió y el piso está cómodo. Debí comprarlo antes.",10),
       ("Paula H.","Zaragoza","Ligero para llevarlo de habitación en habitación. A los niños les encanta de noche.",12),
       ("Pablo L.","Bilbao","Hace justo lo que promete. Aire fresco rápido y muy silencioso.",14)],
 guar_kick="Cero riesgo", guar_h2="Pruébalo 30 días, sin riesgo",
 guar_seal=("30 DÍAS","REEMBOLSO"),
 guar_p="Si no estás 100% satisfecho con tu Coolizi, devuélvelo en 30 días para un reembolso completo o un reemplazo. Sin riesgo, sin estrés — es la promesa de la tienda oficial.",
 faq_kick="Antes de comprar", faq_h2="Coolizi: preguntas y respuestas",
 faq=[("¿La Coolizi es un aire acondicionado de verdad?","Es un climatizador personal sin instalación que enfría rápido la zona a tu alrededor. Ideal para dormitorio, oficina y uso personal — no para sustituir un sistema centralizado."),
      ("¿Cuánto cuesta la Coolizi?","La unidad cuesta 137,99 € con el descuento actual del 50%, y el pack de 2 sale más barato por unidad. Hoy hay un cupón adicional en la tienda oficial."),
      ("¿Necesita instalación?","No. Sin tubo, sin kit de ventana, sin instalador. Enchufas y enciendes."),
      ("¿Coolizi es fiable o una estafa?","Se envía desde una tienda oficial con seguimiento, atención al cliente y garantía de 30 días. Como con cualquier producto popular, compra solo por el enlace oficial para tener la garantía."),
      ("¿Cuánto tarda el envío en España?","El envío es con seguimiento; recibirás un número de seguimiento por email tras la compra."),
      ("¿Y si no me convence?","Estás cubierto por la garantía de 30 días — devolución para reembolso completo o reemplazo.")],
 final_h2="¿Listo para vencer el calor?", final_p="El descuento del 50% de hoy y el cupón extra están aplicados en la tienda oficial — hasta agotar existencias.",
 final_cd_label="Oferta reservada durante", final_cta="Quiero mi Coolizi » -50%",
 footer_disc="Aviso de afiliación: trycoolizi.com es un sitio de reseñas independiente. Podemos ganar una comisión si compras a través de los enlaces de esta página, sin coste adicional para ti. Coolizi™ es una marca de su respectivo propietario. Los precios y ofertas los muestra la tienda oficial y pueden cambiar.",
 footer_links=[("Envío y Entrega","https://coolizi.com/template-common/es/shipping-delivery"),("Reembolso","https://coolizi.com/template-common/es/refund-policy"),("Términos","https://coolizi.com/template-common/es/terms-of-service"),("Privacidad","https://coolizi.com/template-common/es/privacy-policy"),("Contacto","https://coolizi.com/template-common/es/contact-us")],
 announce_ship="🚚 Envío con seguimiento GRATIS hoy", announce_cd="La oferta termina en",
 sticky_label="Coolizi Aire Acondicionado Portátil",
 viewing="{n} personas están viendo este producto", stock="Solo quedan {n} a este precio",
 exit=dict(title="¡Espera — no pierdas el -50%!", sub="Tu descuento sigue reservado unos minutos.",
           coupon_label="Cupón extra desbloqueado", code="COOL10", cta="Conseguir -50% + 10% »", decline="No gracias, pago el precio completo"),
 redirect=dict(t="Asegurando tu descuento del 50%…", s="Te llevamos a la tienda oficial de Coolizi"),
 i18n=dict(tpl="<b>{name}</b> de {city} acaba de comprar {product}", products=["el pack de 2","una Coolizi","el pack de 3"], ago_just="ahora mismo", ago_min="hace {n} min", verified="Verificado"),
 cities=["Madrid","Barcelona","Valencia","Sevilla","Málaga","Zaragoza","Bilbao","Murcia"],
 names=["Javier G.","Lucía M.","Carlos R.","María F.","Daniel S.","Paula H.","Pablo L.","Marta C."],
))

GEOS.append(dict(
 code="nl", lang="nl", hreflang="nl", cc="NL", og="nl_NL", cur=EURb, curcode="EUR",
 c="9590", s1="try-nl", rating="4.8", reviews=8119, lang_label="Nederlands",
 title="Coolizi Review » Eerlijke test 2026, prijs & waar te koop ✓",
 desc="Is de Coolizi draagbare airco de moeite waard? ✓ Onze test 2026: koeling, prijs, echte reviews & de officiële 50% korting. Lees dit voordat je koopt.",
 keywords="coolizi, coolizi review, coolizi ervaringen, coolizi draagbare airco, coolizi mini airco, coolizi prijs, coolizi kopen, coolizi oplichting, coolizi werkt, hoe werkt coolizi, coolizi korting, coolizi aanbieding, coolizi nederland, coolizi 2026, coolizi reviews, coolizi mobiele airco, waar coolizi kopen",
 eyebrow="Coolizi™ Review · Bijgewerkt "+PRETTY,
 h1='Coolizi Review: <span class="hl">de airco zonder installatie</span> die Nederland deze hittegolf koopt',
 sub="We testten de Coolizi twee weken lang — de draagbare airco zonder installatie, zonder slang en zonder raamkit. Hier is het eerlijke oordeel, echte reviews en de officiële korting van vandaag.",
 hero_cta="Beschikbaarheid & 50% korting »", cta="Ik wil mijn Coolizi » 50% korting",
 hero_note=["Geen installatie", "30 dagen niet-goed-geld-terug", "Gratis verzending met tracking"],
 badge_off="KORTING",
 trust=["Nederlandstalige support", "Gegarandeerde premium kwaliteit", "30 dagen 'hou ervan of stuur terug'", "Snelle verzending met tracking"],
 disc_line="Je korting tot 50% is al toegepast in de officiële winkel.",
 agitate_kick="Waarom iedereen erover praat",
 agitate_h2="Een echte airco kost een fortuin — en je hoeft meestal maar één kamer te koelen",
 agitate_p="Met recordhitte starten vaste airco's bij €600+ en jagen je energierekening omhoog. De Coolizi draait dat om: een draagbaar apparaat dat je van kantoor naar slaapkamer meeneemt, voor een paar cent stroom per dag.",
 agitate_list=["Vaste airco's starten bij €600+ en vereisen een installateur", "Grote apparaten zijn luid en verbruiken veel", "Je hoeft zelden het hele huis te koelen — alleen je kamer", "<b>Coolizi:</b> insteken, aanzetten, koele lucht in 30 seconden"],
 steps_kick="Hoe het werkt", steps_h2="Koel elke kamer in 3 stappen",
 steps=[("Kies een plek", "Zet hem op een vlakke ondergrond bij je in de buurt — bureau, nachtkastje of vloer."),
        ("Steek in", "Geen installatie, geen slang, geen raamkit. Direct klaar voor gebruik."),
        ("Zet aan & ontspan", "Kies de stand op de afstandsbediening — koele lucht in ongeveer 30 seconden.")],
 gallery_kick="Van dichtbij", gallery_h2="De Coolizi vanuit elke hoek",
 benefits_kick="Waarom klanten er dol op zijn", benefits_h2="Alles wat een vaste airco biedt — zonder de installatie",
 benefits=[("bolt","Koelt in ~30 seconden","Een krachtige luchtstroom brengt je ruimte snel op een aangename temperatuur."),
           ("leaf","Een paar cent per dag","Energiezuinig — een fractie van de kosten van een traditionele airco."),
           ("move","Overal mee naartoe","Licht en handig — overdag op kantoor, 's avonds in de slaapkamer."),
           ("mute","Fluisterstil","Een zacht ruisje zelfs op de hoogste stand — verstoort slaap noch werk."),
           ("tool","Geen installatie","Geen slang, geen raamkit, geen installateur. Uitpakken en gebruiken."),
           ("year","Koelt & verwarmt","Het hele jaar door — koel in de zomer, zachte warmte in de winter.")],
 offer_kick="De officiële aanbieding van vandaag", offer_h2="Kies je Coolizi-set",
 offer_sub="De meesten nemen er twee — één voor de slaapkamer, één voor de woonkamer. De 2-pack is het populairst en het voordeligst per stuk.",
 bundle_labels=dict(single="1 Stuk", two="2 Stuks", three="3 Stuks", four="4 Stuks",
                    best="Populairst", value="Beste deal", each="/stuk", save="Bespaar"),
 offer_cta="Mijn korting claimen » 50%", pay_note="Veilig afrekenen · Visa · Mastercard · iDEAL · PayPal",
 guarantee_mini="30 dagen niet-goed-geld-terug",
 reviews_kick="Geverifieerde reviews", reviews_h2="Wat Coolizi-bezitters zeggen",
 verified="Geverifieerde koper", helpful="nuttig",
 anchor=[("Jasper T.","Ons oude centrale systeem kostte ons een fortuin, terwijl we eigenlijk alleen de woonkamer wilden koelen. De Coolizi is de perfecte oplossing: geen installatie en de kamer blijft heerlijk koel, zonder dat onze energierekening de pan uit rijst."),
         ("Michiel B.","Zo makkelijk te verplaatsen — ik neem hem elke dag mee van mijn werkkamer naar de slaapkamer. Geen gedoe. Ik hoef geen aparte apparaten per kamer te kopen, dat scheelt geld en ruimte.")],
 wall=[("Daan V.","Amsterdam","Gekocht voor de slaapkamer tijdens de hittegolf en ik slaap eindelijk door. Stil en echt koele lucht.",3),
       ("Sanne J.","Rotterdam","Eerst sceptisch maar het werkt echt. Koelt mijn kantoor in minuten.",5),
       ("Bram D.","Den Haag","2-pack besteld — één boven, één beneden. Beste zomeraankoop tot nu toe.",6),
       ("Emma B.","Utrecht","Geen gedoe met slangen of raambeugels. Ingestoken en het werkte.",8),
       ("Thijs K.","Eindhoven","Energierekening nauwelijks gestegen, huis blijft comfortabel. Had hem eerder moeten kopen.",10),
       ("Lotte H.","Groningen","Licht genoeg om van kamer naar kamer te dragen. De kinderen zijn er dol op 's nachts.",12),
       ("Sem P.","Antwerpen","Doet precies wat het belooft. Snel koele lucht en fluisterstil.",14)],
 guar_kick="Geen risico", guar_h2="Probeer het 30 dagen, risicovrij",
 guar_seal=("30 DAGEN","GELD TERUG"),
 guar_p="Ben je niet 100% tevreden met je Coolizi, stuur hem dan binnen 30 dagen terug voor volledige terugbetaling of vervanging. Geen risico, geen stress — dat is de belofte van de officiële winkel.",
 faq_kick="Voor je koopt", faq_h2="Coolizi: vragen & antwoorden",
 faq=[("Is de Coolizi een echte airco?","Het is een draagbare koeler zonder installatie die de ruimte om je heen snel koelt. Ideaal voor slaapkamer, kantoor en persoonlijk gebruik — niet als vervanging van een centraal systeem."),
      ("Wat kost de Coolizi?","Het losse apparaat kost € 137,99 met de huidige 50% korting, en de 2-pack is per stuk voordeliger. Vandaag is er in de officiële winkel een extra kortingscoupon."),
      ("Is installatie nodig?","Nee. Geen slang, geen raamkit, geen installateur. Insteken en aanzetten."),
      ("Is Coolizi betrouwbaar of oplichting?","Hij wordt verzonden vanuit een officiële winkel met tracking, klantenservice en 30 dagen niet-goed-geld-terug. Koop, zoals bij elk populair product, alleen via de officiële link voor de garantie."),
      ("Hoe snel is de levering in Nederland?","Verzending is met tracking; je ontvangt na het bestellen een trackingnummer per e-mail."),
      ("En als het niet bevalt?","Je bent gedekt door de 30-dagen-garantie — retour voor volledige terugbetaling of vervanging.")],
 final_h2="Klaar om de hitte te verslaan?", final_p="De 50% korting van vandaag en de extra coupon staan klaar in de officiële winkel — zolang de voorraad strekt.",
 final_cd_label="Aanbieding gereserveerd voor", final_cta="Ik wil mijn Coolizi » 50%",
 footer_disc="Affiliate-vermelding: trycoolizi.com is een onafhankelijke reviewsite. We kunnen een commissie verdienen als je via links op deze pagina koopt, zonder extra kosten voor jou. Coolizi™ is een handelsmerk van de respectieve eigenaar. Prijzen en aanbiedingen worden door de officiële winkel getoond en kunnen wijzigen.",
 footer_links=[("Verzending & Levering","https://coolizi.com/template-common/nl/shipping-delivery"),("Restitutie","https://coolizi.com/template-common/nl/refund-policy"),("Voorwaarden","https://coolizi.com/template-common/nl/terms-of-service"),("Privacy","https://coolizi.com/template-common/nl/privacy-policy"),("Contact","https://coolizi.com/template-common/nl/contact-us")],
 announce_ship="🚚 GRATIS verzending met tracking vandaag", announce_cd="Aanbieding eindigt over",
 sticky_label="Coolizi Draagbare Airco",
 viewing="{n} mensen bekijken dit nu", stock="Nog maar {n} voor deze prijs",
 exit=dict(title="Wacht — mis 50% korting niet!", sub="Je korting staat nog enkele minuten gereserveerd.",
           coupon_label="Extra coupon vrijgespeeld", code="COOL10", cta="Claim 50% + 10% »", decline="Nee bedankt, ik betaal de volle prijs"),
 redirect=dict(t="Je korting van 50% wordt vastgezet…", s="Je wordt doorgestuurd naar de officiële Coolizi-winkel"),
 i18n=dict(tpl="<b>{name}</b> uit {city} heeft zojuist {product} gekocht", products=["de 2-pack","een Coolizi","de 3-pack"], ago_just="zojuist", ago_min="{n} min geleden", verified="Geverifieerd"),
 cities=["Amsterdam","Rotterdam","Den Haag","Utrecht","Eindhoven","Groningen","Antwerpen","Gent"],
 names=["Daan V.","Sanne J.","Bram D.","Emma B.","Thijs K.","Lotte H.","Sem P.","Tess M."],
))

GEOS.append(dict(
 code="pt", lang="pt-PT", hreflang="pt", cc="PT", og="pt_PT", cur=EURa, curcode="EUR",
 c="9601", s1="try-pt", rating="4.8", reviews=8942, lang_label="Português",
 title="Coolizi Opiniões » Análise honesta 2026, preço e onde comprar ✓",
 desc="O ar condicionado portátil Coolizi vale a pena? ✓ A nossa análise 2026: arrefecimento, preço, opiniões reais e o desconto oficial de 50%. Leia antes de comprar.",
 keywords="coolizi, coolizi opiniões, coolizi análise, coolizi ar condicionado portátil, coolizi mini ar condicionado, coolizi preço, coolizi comprar, coolizi fraude, coolizi funciona, como usar coolizi, coolizi desconto, coolizi promoção, coolizi portugal, coolizi 2026, opiniões coolizi, coolizi climatizador portátil, onde comprar coolizi",
 eyebrow="Coolizi™ Análise · Atualizado "+PRETTY,
 h1='Coolizi Opiniões: <span class="hl">o ar condicionado sem instalação</span> que Portugal compra neste calor',
 sub="Testámos o Coolizi durante duas semanas — o ar condicionado portátil sem instalação, sem tubo e sem kit de janela. Aqui está o veredicto honesto, as opiniões reais e o desconto oficial de hoje.",
 hero_cta="Disponibilidade & -50% »", cta="Quero o meu Coolizi » -50%",
 hero_note=["Sem instalação", "Garantia de 30 dias", "Envio com rastreio grátis"],
 badge_off="DESCONTO",
 trust=["Apoio em português", "Qualidade premium garantida", "30 dias 'adore ou devolva'", "Envio rápido com rastreio"],
 disc_line="O seu desconto até 50% já foi aplicado na loja oficial.",
 agitate_kick="Porque toda a gente fala disto",
 agitate_h2="Um ar condicionado a sério custa uma fortuna — e normalmente só precisa de arrefecer uma divisão",
 agitate_p="Com recordes de 42,7°C, um ar fixo começa nos 600€+ e dispara a fatura. O Coolizi inverte isso: um aparelho portátil que leva do escritório para o quarto, por uns cêntimos de eletricidade por dia.",
 agitate_list=["Um ar fixo começa nos 600€+ e precisa de instalador", "Os aparelhos grandes são ruidosos e gastam muito", "Raramente precisa de arrefecer a casa toda — só a sua divisão", "<b>Coolizi:</b> ligue, acenda, ar fresco em 30 segundos"],
 steps_kick="Como funciona", steps_h2="Refresque qualquer divisão em 3 passos",
 steps=[("Encontre um local", "Coloque numa superfície plana perto de si — secretária, mesa de cabeceira ou chão."),
        ("Ligue à corrente", "Sem instalação, sem tubo, sem kit de janela. Pronto a usar."),
        ("Acenda e relaxe", "Escolha o modo no comando — ar fresco em cerca de 30 segundos.")],
 gallery_kick="Mais de perto", gallery_h2="O Coolizi de todos os ângulos",
 benefits_kick="Porque os clientes adoram", benefits_h2="Tudo o que um ar fixo dá — sem a instalação",
 benefits=[("bolt","Refresca em ~30 segundos","Um fluxo de ar potente leva o seu espaço a uma temperatura agradável depressa."),
           ("leaf","Uns cêntimos por dia","Eficiente — uma fração do custo de um ar condicionado tradicional."),
           ("move","Transportável para todo o lado","Leve e prático — no escritório de dia, no quarto à noite."),
           ("mute","Silenciosíssimo","Um leve ruído mesmo no máximo — não perturba o sono nem o trabalho."),
           ("tool","Sem instalação","Sem tubo, sem kit de janela, sem instalador. Abra e use."),
           ("year","Refresca e aquece","Todo o ano — fresco no verão, calor suave no inverno.")],
 offer_kick="A oferta oficial de hoje", offer_h2="Escolha o seu conjunto Coolizi",
 offer_sub="A maioria leva dois — um para o quarto, outro para a sala. O conjunto de 2 é o mais popular e o melhor preço por unidade.",
 bundle_labels=dict(single="1 Unidade", two="2 Unidades", three="3 Unidades", four="4 Unidades",
                    best="Mais popular", value="Melhor oferta", each="/unidade", save="Poupe"),
 offer_cta="Obter o meu desconto » -50%", pay_note="Pagamento seguro · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="Garantia de devolução de 30 dias",
 reviews_kick="Opiniões verificadas", reviews_h2="O que dizem os donos do Coolizi",
 verified="Comprador verificado", helpful="útil",
 anchor=[("Tiago T.","O nosso antigo sistema central custava-nos uma fortuna, quando só precisávamos de arrefecer a sala. O Coolizi é a solução perfeita: sem instalação e a divisão mantém-se fresca, sem que a conta da luz dispare. Recomendo!"),
         ("Miguel B.","Muito fácil de transportar — levo-o do escritório para o quarto todos os dias sem esforço. Não preciso de comprar aparelhos diferentes para cada divisão, o que me poupa dinheiro e espaço.")],
 wall=[("João S.","Lisboa","Comprei para o quarto durante o calor e finalmente durmo. Silencioso e ar mesmo fresco.",3),
       ("Mariana C.","Porto","Cética no início mas funciona mesmo. Refresca o escritório em minutos.",5),
       ("Tiago F.","Braga","Levei o conjunto de 2 — um em cima, outro em baixo. Melhor compra do verão.",6),
       ("Beatriz A.","Coimbra","Sem complicações de tubos nem suportes de janela. Liguei e funcionou.",8),
       ("Rui P.","Faro","A fatura quase não mexeu e a casa está confortável. Devia ter comprado antes.",10),
       ("Sofia H.","Setúbal","Leve para transportar de divisão em divisão. Os miúdos adoram à noite.",12),
       ("André L.","Aveiro","Faz exatamente o que promete. Ar fresco rápido e silenciosíssimo.",14)],
 guar_kick="Risco zero", guar_h2="Experimente 30 dias, sem risco",
 guar_seal=("30 DIAS","REEMBOLSO"),
 guar_p="Se não ficar 100% satisfeito com o seu Coolizi, devolva-o em 30 dias para reembolso total ou substituição. Sem risco, sem stress — é a promessa da loja oficial.",
 faq_kick="Antes de comprar", faq_h2="Coolizi: perguntas e respostas",
 faq=[("O Coolizi é um ar condicionado a sério?","É um climatizador pessoal sem instalação que arrefece rapidamente a área à sua volta. Ideal para quarto, escritório e uso pessoal — não para substituir um sistema central."),
      ("Quanto custa o Coolizi?","A unidade custa 137,99 € com o desconto atual de 50%, e o conjunto de 2 fica mais barato por unidade. Hoje há um cupão adicional na loja oficial."),
      ("Precisa de instalação?","Não. Sem tubo, sem kit de janela, sem instalador. Liga e acende."),
      ("O Coolizi é fiável ou fraude?","É enviado de uma loja oficial com rastreio, apoio ao cliente e garantia de 30 dias. Como em qualquer produto popular, compre apenas pelo link oficial para ter a garantia."),
      ("Quanto tempo demora a entrega em Portugal?","O envio é com rastreio; recebe um número de rastreio por email após a compra."),
      ("E se não for para mim?","Está coberto pela garantia de 30 dias — devolução para reembolso total ou substituição.")],
 final_h2="Pronto para vencer o calor?", final_p="O desconto de 50% de hoje e o cupão extra estão aplicados na loja oficial — até esgotar o stock.",
 final_cd_label="Oferta reservada por", final_cta="Quero o meu Coolizi » -50%",
 footer_disc="Divulgação de afiliação: trycoolizi.com é um site de análises independente. Podemos receber uma comissão se comprar através dos links nesta página, sem custo adicional para si. Coolizi™ é uma marca do respetivo proprietário. Preços e ofertas são mostrados pela loja oficial e podem mudar.",
 footer_links=[("Envio e Entrega","https://coolizi.com/template-common/pt/shipping-delivery"),("Reembolso","https://coolizi.com/template-common/pt/refund-policy"),("Termos","https://coolizi.com/template-common/pt/terms-of-service"),("Privacidade","https://coolizi.com/template-common/pt/privacy-policy"),("Contacto","https://coolizi.com/template-common/pt/contact-us")],
 announce_ship="🚚 Envio com rastreio GRÁTIS hoje", announce_cd="A oferta termina em",
 sticky_label="Coolizi Ar Condicionado Portátil",
 viewing="{n} pessoas estão a ver este produto", stock="Só restam {n} a este preço",
 exit=dict(title="Espere — não perca os -50%!", sub="O seu desconto está reservado por mais alguns minutos.",
           coupon_label="Cupão extra desbloqueado", code="COOL10", cta="Obter -50% + 10% »", decline="Não obrigado, pago o preço cheio"),
 redirect=dict(t="A garantir o seu desconto de 50%…", s="A levá-lo para a loja oficial Coolizi"),
 i18n=dict(tpl="<b>{name}</b> de {city} acabou de comprar {product}", products=["o conjunto de 2","um Coolizi","o conjunto de 3"], ago_just="agora mesmo", ago_min="há {n} min", verified="Verificado"),
 cities=["Lisboa","Porto","Braga","Coimbra","Faro","Setúbal","Aveiro","Funchal"],
 names=["João S.","Mariana C.","Tiago F.","Beatriz A.","Rui P.","Sofia H.","André L.","Inês M."],
))

GEOS.append(dict(
 code="el", lang="el", hreflang="el", cc="GR", og="el_GR", cur=EURa, curcode="EUR",
 c="9596", s1="try-gr", rating="4.9", reviews=20864, lang_label="Ελληνικά",
 title="Coolizi Κριτικές » Ειλικρινής δοκιμή 2026, τιμή & πού να αγοράσετε ✓",
 desc="Αξίζει το φορητό κλιματιστικό Coolizi; ✓ Η δοκιμή μας 2026: ψύξη, τιμή, πραγματικές κριτικές & η επίσημη έκπτωση 50%. Διαβάστε πριν αγοράσετε.",
 keywords="coolizi, coolizi κριτικές, coolizi αξιολογήσεις, coolizi φορητό κλιματιστικό, coolizi mini κλιματιστικό, coolizi τιμή, coolizi αγορά, coolizi απάτη, coolizi λειτουργεί, πώς λειτουργεί coolizi, coolizi έκπτωση, coolizi προσφορά, coolizi ελλάδα, coolizi 2026, κριτικές coolizi, πού να αγοράσω coolizi",
 eyebrow="Coolizi™ Κριτική · Ενημερώθηκε "+PRETTY,
 h1='Coolizi Κριτικές: <span class="hl">το κλιματιστικό χωρίς εγκατάσταση</span> που αγοράζει η Ελλάδα στον καύσωνα',
 sub="Δοκιμάσαμε το Coolizi για δύο εβδομάδες — το φορητό κλιματιστικό χωρίς εγκατάσταση, χωρίς σωλήνα και χωρίς κιτ παραθύρου. Δείτε την ειλικρινή ετυμηγορία, πραγματικές κριτικές και τη σημερινή επίσημη έκπτωση.",
 hero_cta="Διαθεσιμότητα & -50% »", cta="Θέλω το Coolizi μου » -50%",
 hero_note=["Χωρίς εγκατάσταση", "Εγγύηση 30 ημερών", "Δωρεάν αποστολή με tracking"],
 badge_off="ΕΚΠΤΩΣΗ",
 trust=["Υποστήριξη στα ελληνικά", "Εγγυημένη premium ποιότητα", "30 ημέρες 'το λατρεύεις ή το επιστρέφεις'", "Γρήγορη αποστολή με tracking"],
 disc_line="Η έκπτωσή σας έως 50% έχει ήδη εφαρμοστεί στο επίσημο κατάστημα.",
 agitate_kick="Γιατί μιλάνε όλοι γι' αυτό",
 agitate_h2="Ένα κανονικό κλιματιστικό κοστίζει μια περιουσία — ενώ συνήθως θέλετε να δροσίσετε μόνο ένα δωμάτιο",
 agitate_p="Με ρεκόρ καύσωνα, ένα σταθερό κλιματιστικό ξεκινά από 600€+ και εκτοξεύει τον λογαριασμό. Το Coolizi το αντιστρέφει: μια φορητή συσκευή που μεταφέρετε από το γραφείο στο υπνοδωμάτιο, με λίγα λεπτά ρεύματος την ημέρα.",
 agitate_list=["Ένα σταθερό κλιματιστικό ξεκινά από 600€+ και θέλει τεχνικό", "Οι μεγάλες συσκευές είναι θορυβώδεις και καταναλώνουν πολύ", "Σπάνια χρειάζεται να δροσίσετε όλο το σπίτι — μόνο το δωμάτιό σας", "<b>Coolizi:</b> βάλτε στην πρίζα, ανάψτε, δροσερός αέρας σε 30 δευτερόλεπτα"],
 steps_kick="Πώς λειτουργεί", steps_h2="Δροσίστε κάθε δωμάτιο σε 3 βήματα",
 steps=[("Βρείτε σημείο", "Τοποθετήστε το σε επίπεδη επιφάνεια κοντά σας — γραφείο, κομοδίνο ή πάτωμα."),
        ("Βάλτε στην πρίζα", "Χωρίς εγκατάσταση, χωρίς σωλήνα, χωρίς κιτ παραθύρου. Έτοιμο για χρήση."),
        ("Ανάψτε & χαλαρώστε", "Επιλέξτε λειτουργία στο τηλεχειριστήριο — δροσερός αέρας σε ~30 δευτερόλεπτα.")],
 gallery_kick="Πιο κοντά", gallery_h2="Το Coolizi από κάθε γωνία",
 benefits_kick="Γιατί το λατρεύουν οι πελάτες", benefits_h2="Ό,τι προσφέρει ένα σταθερό κλιματιστικό — χωρίς την εγκατάσταση",
 benefits=[("bolt","Δροσίζει σε ~30 δευτ.","Ισχυρή ροή αέρα φέρνει γρήγορα τον χώρο σε ευχάριστη θερμοκρασία."),
           ("leaf","Λίγα λεπτά την ημέρα","Οικονομικό — ένα κλάσμα του κόστους ενός παραδοσιακού κλιματιστικού."),
           ("move","Μεταφέρεται παντού","Ελαφρύ και πρακτικό — στο γραφείο τη μέρα, στο υπνοδωμάτιο το βράδυ."),
           ("mute","Αθόρυβο","Ένα απαλό βουητό ακόμη και στο μέγιστο — δεν ενοχλεί ύπνο ή εργασία."),
           ("tool","Χωρίς εγκατάσταση","Χωρίς σωλήνα, χωρίς κιτ παραθύρου, χωρίς τεχνικό. Ανοίξτε και χρησιμοποιήστε."),
           ("year","Δροσίζει & ζεσταίνει","Όλο τον χρόνο — δροσιά το καλοκαίρι, απαλή ζέστη τον χειμώνα.")],
 offer_kick="Η σημερινή επίσημη προσφορά", offer_h2="Επιλέξτε το σετ Coolizi σας",
 offer_sub="Οι περισσότεροι παίρνουν δύο — ένα για το υπνοδωμάτιο, ένα για το σαλόνι. Το σετ των 2 είναι το πιο δημοφιλές και η καλύτερη τιμή ανά τεμάχιο.",
 bundle_labels=dict(single="1 Τεμάχιο", two="2 Τεμάχια", three="3 Τεμάχια", four="4 Τεμάχια",
                    best="Πιο δημοφιλές", value="Καλύτερη αξία", each="/τεμ.", save="Κερδίζετε"),
 offer_cta="Θέλω την έκπτωσή μου » -50%", pay_note="Ασφαλής πληρωμή · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="Εγγύηση επιστροφής χρημάτων 30 ημερών",
 reviews_kick="Επαληθευμένες κριτικές", reviews_h2="Τι λένε οι κάτοχοι του Coolizi",
 verified="Επαληθευμένος αγοραστής", helpful="χρήσιμο",
 anchor=[("Δημήτρης Κ.","Το δωμάτιο έπεσε από 28°C σε 19°C μέσα σε 15 λεπτά. Καμία εγκατάσταση, καμία ταλαιπωρία — αξίζει κάθε ευρώ. Επιτέλους δροσιά στην κρεβατοκάμαρα μέσα στον καύσωνα."),
         ("Ελένη Τ.","Ένας τεχνικός μου ζήτησε 3.000€ για κλιματιστικό. Το Coolizi δουλεύει εξίσου καλά για τον χώρο μου, στο ελάχιστο κόστος. Το μεταφέρω εύκολα από δωμάτιο σε δωμάτιο.")],
 wall=[("Μιχάλης Μ.","Πάτρα","Το πήρα για το υπνοδωμάτιο στον καύσωνα και επιτέλους κοιμάμαι. Αθόρυβο και πραγματικά δροσερός αέρας.",3),
       ("Μαρία Ρ.","Θεσσαλονίκη","Αρχικά επιφυλακτική, αλλά δουλεύει στ' αλήθεια. Δροσίζει το γραφείο σε λεπτά.",5),
       ("Γιώργος Χ.","Λάρισα","Πήρα το σετ των 2 — ένα πάνω, ένα κάτω. Η καλύτερη αγορά του καλοκαιριού.",6),
       ("Ελένη Σ.","Ηράκλειο","Καμία ταλαιπωρία με σωλήνες ή βάσεις παραθύρου. Το έβαλα στην πρίζα και δούλεψε.",8),
       ("Γιάννης Μ.","Αθήνα","Ο λογαριασμός ρεύματος ελάχιστα ανέβηκε και το σπίτι είναι άνετο.",10),
       ("Ελένη Β.","Θεσσαλονίκη","Αρκετά ελαφρύ για να το μεταφέρω από δωμάτιο σε δωμάτιο. Τα παιδιά το λατρεύουν το βράδυ.",12),
       ("Δημήτρης Λ.","Αθήνα","Κάνει ακριβώς ό,τι υπόσχεται. Γρήγορα δροσερός αέρας και πολύ αθόρυβο.",14)],
 guar_kick="Μηδέν ρίσκο", guar_h2="Δοκιμάστε το 30 ημέρες, χωρίς ρίσκο",
 guar_seal=("30 ΗΜΕΡΕΣ","ΕΠΙΣΤΡΟΦΗ"),
 guar_p="Αν δεν είστε 100% ικανοποιημένοι με το Coolizi, επιστρέψτε το εντός 30 ημερών για πλήρη επιστροφή χρημάτων ή αντικατάσταση. Χωρίς ρίσκο, χωρίς άγχος — αυτή είναι η υπόσχεση του επίσημου καταστήματος.",
 faq_kick="Πριν αγοράσετε", faq_h2="Coolizi: ερωτήσεις & απαντήσεις",
 faq=[("Είναι το Coolizi πραγματικό κλιματιστικό;","Είναι ένας φορητός δροσιστήρας χωρίς εγκατάσταση που δροσίζει γρήγορα τον χώρο γύρω σας. Ιδανικό για υπνοδωμάτιο, γραφείο και προσωπική χρήση — όχι ως αντικατάσταση κεντρικού συστήματος."),
      ("Πόσο κοστίζει το Coolizi;","Το μεμονωμένο τεμάχιο κοστίζει 137,99 € με την τρέχουσα έκπτωση 50%, και το σετ των 2 βγαίνει φθηνότερο ανά τεμάχιο. Σήμερα υπάρχει επιπλέον κουπόνι στο επίσημο κατάστημα."),
      ("Χρειάζεται εγκατάσταση;","Όχι. Χωρίς σωλήνα, χωρίς κιτ παραθύρου, χωρίς τεχνικό. Το βάζετε στην πρίζα και το ανάβετε."),
      ("Είναι το Coolizi αξιόπιστο ή απάτη;","Αποστέλλεται από επίσημο κατάστημα με tracking, εξυπηρέτηση πελατών και εγγύηση 30 ημερών. Όπως με κάθε δημοφιλές προϊόν, αγοράστε μόνο από τον επίσημο σύνδεσμο για να έχετε την εγγύηση."),
      ("Πόσο γρήγορα είναι η παράδοση στην Ελλάδα;","Η αποστολή γίνεται με tracking· μετά την παραγγελία λαμβάνετε αριθμό παρακολούθησης με email."),
      ("Κι αν δεν μου ταιριάξει;","Καλύπτεστε από την εγγύηση 30 ημερών — επιστροφή για πλήρη αποζημίωση ή αντικατάσταση.")],
 final_h2="Έτοιμοι να νικήσετε τη ζέστη;", final_p="Η σημερινή έκπτωση 50% και το επιπλέον κουπόνι έχουν εφαρμοστεί στο επίσημο κατάστημα — όσο υπάρχει απόθεμα.",
 final_cd_label="Η προσφορά κρατείται για", final_cta="Θέλω το Coolizi μου » -50%",
 footer_disc="Γνωστοποίηση συνεργασίας: το trycoolizi.com είναι ανεξάρτητος ιστότοπος κριτικών. Ενδέχεται να λάβουμε προμήθεια αν αγοράσετε μέσω συνδέσμων αυτής της σελίδας, χωρίς επιπλέον κόστος για εσάς. Το Coolizi™ είναι εμπορικό σήμα του αντίστοιχου κατόχου. Οι τιμές και οι προσφορές εμφανίζονται από το επίσημο κατάστημα και μπορεί να αλλάξουν.",
 footer_links=[("Αποστολή & Παράδοση","https://coolizi.com/template-common/el/shipping-delivery"),("Επιστροφές","https://coolizi.com/template-common/el/refund-policy"),("Όροι","https://coolizi.com/template-common/el/terms-of-service"),("Απόρρητο","https://coolizi.com/template-common/el/privacy-policy"),("Επικοινωνία","https://coolizi.com/template-common/el/contact-us")],
 announce_ship="🚚 ΔΩΡΕΑΝ αποστολή με tracking σήμερα", announce_cd="Η προσφορά λήγει σε",
 sticky_label="Coolizi Φορητό Κλιματιστικό",
 viewing="{n} άτομα βλέπουν αυτό το προϊόν τώρα", stock="Μόνο {n} ακόμη σε αυτή την τιμή",
 exit=dict(title="Περιμένετε — μη χάσετε το -50%!", sub="Η έκπτωσή σας κρατείται για λίγα ακόμη λεπτά.",
           coupon_label="Ξεκλειδώθηκε επιπλέον κουπόνι", code="COOL10", cta="Πάρτε -50% + 10% »", decline="Όχι ευχαριστώ, θα πληρώσω κανονική τιμή"),
 redirect=dict(t="Κατοχυρώνουμε την έκπτωση 50%…", s="Σας μεταφέρουμε στο επίσημο κατάστημα Coolizi"),
 i18n=dict(tpl="<b>{name}</b> από {city} μόλις αγόρασε {product}", products=["το σετ των 2","ένα Coolizi","το σετ των 3"], ago_just="μόλις τώρα", ago_min="πριν {n} λεπτά", verified="Επαληθευμένο"),
 cities=["Αθήνα","Θεσσαλονίκη","Πάτρα","Ηράκλειο","Λάρισα","Βόλος","Ιωάννινα","Χανιά"],
 names=["Γιώργος Κ.","Μαρία Π.","Δημήτρης Ν.","Ελένη Β.","Γιάννης Μ.","Σοφία Λ.","Νίκος Α.","Κατερίνα Σ."],
))

# ========================================================================
# HTML BUILDERS
# ========================================================================
ICONS = {
 "bolt":'<path d="M13 2 4.5 13.5H11l-1 8.5L19.5 10H13z"/>',
 "leaf":'<path d="M5 21c8 0 14-5 14-14 0-1-.2-2-.5-3C10 4 4 9 4 18c0 1 .3 2 1 3z"/><path d="M9 17c2-4 5-6 8-7"/>',
 "move":'<path d="M5 9 2 12l3 3M9 5l3-3 3 3M15 19l-3 3-3-3M19 9l3 3-3 3M2 12h20M12 2v20"/>',
 "mute":'<path d="M11 5 6 9H2v6h4l5 4zM23 9l-6 6M17 9l6 6"/>',
 "tool":'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-2.5z"/>',
 "year":'<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
 "check":'<path d="M20 6 9 17l-5-5"/>',
}
def svg(name, cls=""):
    return '<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (cls, ICONS.get(name, ICONS["check"]))

def stars(n=5):
    return '<span class="s">' + ("★" * int(round(n))) + "</span>"

FEMALE = set("Sarah Emma Charlotte Sophie Amelia Emily Anna Lena Marie Camille Léa Manon Chloé "
             "Giulia Sofia Chiara Aurora Lucía María Paula Marta Sanne Lotte Tess Mariana Beatriz "
             "Inês Ελένη Μαρία Σοφία Κατερίνα".split())
AV_M = ["am%d.webp" % i for i in range(1, 9)]
AV_W = ["aw%d.webp" % i for i in range(1, 9)]
def face_av(name, i):
    first = name.strip().split()[0]
    pool = AV_W if first in FEMALE else AV_M
    return "../assets/img/" + pool[i % len(pool)]

def E(s): return html.escape(s, quote=True)

def build_bundles(g):
    cur, L = g["cur"], g["bundle_labels"]
    rows = [
        (L["single"], cur(A["ws"]), cur(A["s"]),    cur(A["e1"]), PCT["p1"], None),
        (L["two"],    cur(A["wtwo"]),cur(A["two"]),  cur(A["e2"]), PCT["p2"], L["best"]),
        (L["three"],  cur(A["wthree"]),cur(A["three"]),cur(A["e3"]),PCT["p3"],None),
        (L["four"],   cur(A["wfour"]),cur(A["four"]), cur(A["e4"]), PCT["p4"], L["value"]),
    ]
    out = []
    for qty, was, price, each, pct, ribbon in rows:
        best = " best" if ribbon == L["best"] else ""
        rb = ('<span class="ribbon">%s</span>' % E(ribbon)) if ribbon else ""
        out.append(
            '<label class="bundle%s js-cta">%s<span class="qty">%s</span>'
            '<span class="was">%s</span><span class="price">%s</span>'
            '<span class="each">%s%s</span><span class="save">%s -%d%%</span></label>'
            % (best, rb, E(qty), was, price, each, E(L["each"]), E(L["save"]), pct))
    return "\n".join(out)

def build_reviews(g):
    cards = []; idx = 0
    for name, text in g["anchor"]:
        cards.append(
            '<div class="rev-card"><div class="top"><img class="av" src="%s" alt="%s" loading="lazy" width="42" height="42">'
            '<div class="who"><b>%s</b><span>%s</span></div><span class="verified">✔ %s</span></div>'
            '<div class="rs">★★★★★</div><p>%s</p></div>'
            % (face_av(name, idx), E(name), E(name), E(g["verified"]), E(g["verified"]), E(text))); idx += 1
    for name, city, text, days in g["wall"]:
        cards.append(
            '<div class="rev-card"><div class="top"><img class="av" src="%s" alt="%s" loading="lazy" width="42" height="42">'
            '<div class="who"><b>%s</b><span>%s</span></div><span class="verified">✔ %s</span></div>'
            '<div class="rs">★★★★★</div><p>%s</p>'
            '<div class="meta"><span>%s</span></div></div>'
            % (face_av(name, idx), E(name), E(name), E(city), E(g["verified"]), E(text), "%dd" % days)); idx += 1
    return "\n".join(cards)

def build_faq(g):
    out = []
    for q, a in g["faq"]:
        out.append('<div class="faq-item"><div class="faq-q">%s<span class="pm">+</span></div>'
                   '<div class="faq-a"><div>%s</div></div></div>' % (E(q), E(a)))
    return "\n".join(out)

def build_steps(g):
    out = []
    for i, (h, p) in enumerate(g["steps"], 1):
        out.append('<div class="step reveal"><div class="n">%d</div><h3>%s</h3><p>%s</p></div>' % (i, E(h), E(p)))
    return "\n".join(out)

def build_benefits(g):
    out = []
    for ic, h, p in g["benefits"]:
        out.append('<div class="benefit reveal"><div class="ic">%s</div><h3>%s</h3><p>%s</p></div>' % (svg(ic), E(h), E(p)))
    return "\n".join(out)

def build_gallery():
    cells = []
    for i, img in enumerate(IMAGES):
        cells.append('<div class="gi"><img src="../assets/img/%s" alt="Coolizi" loading="lazy" width="500" height="500"></div>' % img)
    return "\n".join(cells)

def build_trust(g):
    return "\n".join('<span>%s %s</span>' % (svg("check"), E(t)) for t in g["trust"])

def build_agitate_list(g):
    return "\n".join('<li><span class="x">✕</span><span>%s</span></li>' % item for item in g["agitate_list"])

def hreflang_links(geos, self_code):
    out = []
    for g in geos:
        out.append('<link rel="alternate" hreflang="%s" href="%s/%s/">' % (g["hreflang"], DOMAIN, g["code"]))
    out.append('<link rel="alternate" hreflang="x-default" href="%s/en/">' % DOMAIN)
    return "\n".join(out)

def jsonld(g):
    price = "%.2f" % A["s"]
    reviews_ld = []
    for name, city, text, days in g["wall"][:5]:
        reviews_ld.append({"@type":"Review","author":{"@type":"Person","name":name},
                           "reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},
                           "reviewBody":text})
    data = [
      {"@context":"https://schema.org","@type":"Product","name":"Coolizi Portable AC",
       "image":["%s/assets/img/%s" % (DOMAIN, IMAGES[0])],
       "description": g["desc"],
       "brand":{"@type":"Brand","name":"Coolizi"},
       "aggregateRating":{"@type":"AggregateRating","ratingValue":g["rating"],"reviewCount":str(g["reviews"]),"bestRating":"5"},
       "review":reviews_ld,
       "offers":{"@type":"AggregateOffer","lowPrice":"%.2f"%A["e4"],"highPrice":price,"priceCurrency":g["curcode"],
                 "offerCount":"4","availability":"https://schema.org/InStock","url":"%s/%s/" % (DOMAIN, g["code"])}},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
         {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in g["faq"]]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
         {"@type":"ListItem","position":1,"name":"Home","item":"%s/%s/" % (DOMAIN, g["code"])},
         {"@type":"ListItem","position":2,"name":"Coolizi Review"}]},
      {"@context":"https://schema.org","@type":"Organization","name":"trycoolizi.com","url":DOMAIN},
    ]
    return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False)

def geo_js(g):
    obj = {"code":g["code"],"cc":g["cc"],"c":g["c"],"s1":g["s1"],
           "thumb":"../assets/img/p2.webp","cities":g["cities"],"names":g["names"],"i18n":g["i18n"]}
    return "document.documentElement.classList.add('js');window.GEO=%s;" % json.dumps(obj, ensure_ascii=False)

# ========================================================================
# PAGE TEMPLATE
# ========================================================================
def render_page(g, geos):
    cur = g["cur"]
    lang_menu = "\n".join('<li><a href="../%s/">%s</a></li>' % (x["code"], E(x["lang_label"])) for x in geos)
    ctx = {
      "LANG": g["lang"], "OG": g["og"], "CODE": g["code"],
      "TITLE": E(g["title"]), "DESC": E(g["desc"]), "KEYWORDS": E(g["keywords"]),
      "CANON": "%s/%s/" % (DOMAIN, g["code"]),
      "HREFLANG": hreflang_links(geos, g["code"]),
      "GEOJS": geo_js(g),
      "OGIMG": "%s/assets/img/%s" % (DOMAIN, IMAGES[0]),
      "ANNOUNCE_SHIP": E(g["announce_ship"]), "ANNOUNCE_CD": E(g["announce_cd"]),
      "LANGMENU": lang_menu, "LANGLABEL": E(g["lang_label"]),
      "EYEBROW": E(g["eyebrow"]), "H1": g["h1"], "SUB": E(g["sub"]),
      "RATING": g["rating"], "REVIEWS": "{:,}".format(g["reviews"]),
      "HEROCTA": E(g["hero_cta"]), "CTA": E(g["cta"]),
      "HERONOTE": "\n".join('<span>%s %s</span>' % (svg("check"), E(n)) for n in g["hero_note"]),
      "BADGEOFF": E(g["badge_off"]),
      "DISCLINE": E(g["disc_line"]),
      "TRUST": build_trust(g),
      "AG_KICK": E(g["agitate_kick"]), "AG_H2": E(g["agitate_h2"]), "AG_P": E(g["agitate_p"]), "AG_LIST": build_agitate_list(g),
      "ST_KICK": E(g["steps_kick"]), "ST_H2": E(g["steps_h2"]), "STEPS": build_steps(g),
      "GA_KICK": E(g["gallery_kick"]), "GA_H2": E(g["gallery_h2"]), "GALLERY": build_gallery(),
      "BE_KICK": E(g["benefits_kick"]), "BE_H2": E(g["benefits_h2"]), "BENEFITS": build_benefits(g),
      "OF_KICK": E(g["offer_kick"]), "OF_H2": E(g["offer_h2"]), "OF_SUB": E(g["offer_sub"]),
      "BUNDLES": build_bundles(g), "OFFERCTA": E(g["offer_cta"]), "PAYNOTE": E(g["pay_note"]), "GUARMINI": E(g["guarantee_mini"]),
      "RV_KICK": E(g["reviews_kick"]), "RV_H2": E(g["reviews_h2"]),
      "REVCARDS": build_reviews(g),
      "GU_KICK": E(g["guar_kick"]), "GU_H2": E(g["guar_h2"]),
      "SEAL1": E(g["guar_seal"][0]), "SEAL2": E(g["guar_seal"][1]), "GU_P": E(g["guar_p"]),
      "FQ_KICK": E(g["faq_kick"]), "FQ_H2": E(g["faq_h2"]), "FAQ": build_faq(g),
      "FN_H2": E(g["final_h2"]), "FN_P": E(g["final_p"]), "FN_CD": E(g["final_cd_label"]), "FN_CTA": E(g["final_cta"]),
      "FOOT_DISC": E(g["footer_disc"]),
      "FOOT_LINKS": " · ".join('<a href="%s" rel="nofollow" target="_blank">%s</a>' % (E(u), E(l)) for l, u in g["footer_links"]),
      "STICKY_LABEL": E(g["sticky_label"]), "PRICE_S": cur(A["s"]), "WAS_S": cur(A["ws"]),
      "VIEWING": E(g["viewing"]).replace("{n}", '<b data-viewers>0</b>'),
      "STOCK": E(g["stock"]).replace("{n}", '<b data-stock>0</b>'),
      "EX_TITLE": E(g["exit"]["title"]), "EX_SUB": E(g["exit"]["sub"]),
      "EX_CLABEL": E(g["exit"]["coupon_label"]), "EX_CODE": E(g["exit"]["code"]),
      "EX_CTA": E(g["exit"]["cta"]), "EX_DECLINE": E(g["exit"]["decline"]),
      "RED_T": E(g["redirect"]["t"]), "RED_S": E(g["redirect"]["s"]),
      "JSONLD": jsonld(g),
      "YEAR": str(datetime.date.today().year),
      "HEROIMG": IMAGES[0],
    }
    html_out = TEMPLATE
    for k, v in ctx.items():
        html_out = html_out.replace("{{%s}}" % k, str(v))
    return html_out

TEMPLATE = r"""<!DOCTYPE html>
<html lang="{{LANG}}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<meta name="keywords" content="{{KEYWORDS}}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{{CANON}}">
{{HREFLANG}}
<meta property="og:type" content="website">
<meta property="og:locale" content="{{OG}}">
<meta property="og:title" content="{{TITLE}}">
<meta property="og:description" content="{{DESC}}">
<meta property="og:image" content="{{OGIMG}}">
<meta property="og:url" content="{{CANON}}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" as="image" href="../assets/img/{{HEROIMG}}">
<link rel="preconnect" href="https://ipinfo.io">
<link rel="stylesheet" href="../assets/styles.css">
<script>{{GEOJS}}</script>
{{JSONLD}}
</head>
<body>
<div class="announce">
  <span>{{ANNOUNCE_SHIP}}</span>
  <span>{{ANNOUNCE_CD}} <b data-cd>15:00</b></span>
</div>

<header class="nav"><div class="wrap">
  <a class="logo" href="#"><span class="dot"></span>Coolizi<small>REVIEW</small></a>
  <div class="lang"><button>🌐 {{LANGLABEL}} ▾</button><ul>{{LANGMENU}}</ul></div>
</div></header>

<!-- HERO -->
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">⭐ {{EYEBROW}}</span>
    <h1>{{H1}}</h1>
    <div class="stars">{{RATING}} ★★★★★ · <b>{{REVIEWS}}</b>&nbsp;reviews</div>
    <p class="sub">{{SUB}}</p>
    <a class="btn pulse js-cta" href="#">{{HEROCTA}} <span class="arw">→</span></a>
    <div class="hero-cta-note">{{HERONOTE}}</div>
  </div>
  <div class="heroimg">
    <div class="badge-off"><b>50%</b>{{BADGEOFF}}</div>
    <img src="../assets/img/{{HEROIMG}}" alt="Coolizi Portable AC" width="560" height="560" fetchpriority="high">
  </div>
</div></section>

<div class="trust"><div class="wrap">{{TRUST}}</div></div>
<div class="announce" style="background:#eafaf1;color:#0a7a4f"><span>✓ {{DISCLINE}}</span></div>

<!-- AGITATE -->
<section class="agitate"><div class="wrap">
  <div class="sec-head reveal"><span class="kick">{{AG_KICK}}</span><h2>{{AG_H2}}</h2></div>
  <div class="row">
    <div class="reveal"><p>{{AG_P}}</p><ul>{{AG_LIST}}</ul></div>
    <div class="card-img reveal"><img src="../assets/img/p3.webp" alt="Coolizi in use" loading="lazy" width="520" height="420"></div>
  </div>
</div></section>

<!-- STEPS -->
<section><div class="wrap">
  <div class="sec-head"><span class="kick">{{ST_KICK}}</span><h2>{{ST_H2}}</h2></div>
  <div class="steps">{{STEPS}}</div>
</div></section>

<!-- GALLERY -->
<section style="background:var(--bg2)"><div class="wrap">
  <div class="sec-head"><span class="kick">{{GA_KICK}}</span><h2>{{GA_H2}}</h2></div>
  <div class="gallery reveal">{{GALLERY}}</div>
</div></section>

<!-- BENEFITS -->
<section><div class="wrap">
  <div class="sec-head"><span class="kick">{{BE_KICK}}</span><h2>{{BE_H2}}</h2></div>
  <div class="benefits">{{BENEFITS}}</div>
</div></section>

<!-- OFFER -->
<section class="offer" id="offer"><div class="wrap">
  <div class="sec-head"><span class="kick">{{OF_KICK}}</span><h2>{{OF_H2}}</h2><p>{{OF_SUB}}</p></div>
  <div class="bundles reveal">{{BUNDLES}}</div>
  <div class="offer-cta">
    <a class="btn pulse js-cta" href="#">{{OFFERCTA}} <span class="arw">→</span></a>
    <div class="pay-row">🔒 {{PAYNOTE}}</div>
    <div class="pay-row">🛡️ {{GUARMINI}} · ⚡ <span>{{STOCK}}</span> · 👀 <span>{{VIEWING}}</span></div>
  </div>
</div></section>

<!-- REVIEWS -->
<section class="reviews"><div class="wrap">
  <div class="sec-head"><span class="kick">{{RV_KICK}}</span><h2>{{RV_H2}}</h2></div>
  <div class="rev-summary">
    <div class="rev-score"><b>{{RATING}}</b><div class="s">★★★★★</div><small>{{REVIEWS}} reviews</small></div>
    <div class="rev-bars">
      <div class="b">5★<span class="track"><i style="width:92%"></i></span></div>
      <div class="b">4★<span class="track"><i style="width:6%"></i></span></div>
      <div class="b">3★<span class="track"><i style="width:1%"></i></span></div>
      <div class="b">2★<span class="track"><i style="width:0.5%"></i></span></div>
      <div class="b">1★<span class="track"><i style="width:0.5%"></i></span></div>
    </div>
  </div>
  <div class="rev-grid">{{REVCARDS}}</div>
</div></section>

<!-- GUARANTEE -->
<section class="guarantee"><div class="wrap">
  <div class="sec-head"><span class="kick">{{GU_KICK}}</span><h2>{{GU_H2}}</h2></div>
  <div class="seal"><b>{{SEAL1}}</b>{{SEAL2}}</div>
  <p>{{GU_P}}</p>
</div></section>

<!-- FAQ -->
<section style="background:var(--bg2)"><div class="wrap">
  <div class="sec-head"><span class="kick">{{FQ_KICK}}</span><h2>{{FQ_H2}}</h2></div>
  <div class="faq-list">{{FAQ}}</div>
</div></section>

<!-- FINAL -->
<section class="final"><div class="wrap">
  <div class="cd">⏳ {{FN_CD}} <b data-cd>15:00</b></div>
  <h2>{{FN_H2}}</h2><p>{{FN_P}}</p>
  <a class="btn js-cta" href="#">{{FN_CTA}} <span class="arw">→</span></a>
</div></section>

<footer><div class="wrap">
  <div class="disc">{{FOOT_DISC}}</div>
  <div class="links">{{FOOT_LINKS}}</div>
  <div class="copy">© {{YEAR}} trycoolizi.com — independent review · Not the official Coolizi store.</div>
</div></footer>

<!-- STICKY BAR -->
<div class="stickybar"><div class="wrap">
  <div class="sb-info"><img src="../assets/img/{{HEROIMG}}" alt=""><div class="sb-txt"><b>{{STICKY_LABEL}}</b><span><s>{{WAS_S}}</s> {{PRICE_S}} · -50%</span></div></div>
  <a class="btn js-cta" href="#">{{CTA}} →</a>
</div></div>

<!-- SOCIAL PROOF TICKER -->
<div id="sp-toast"></div>

<!-- EXIT MODAL -->
<div class="modal-bg" id="exit-modal"><div class="modal">
  <span class="x" data-close-exit>×</span>
  <div class="top"><h3>{{EX_TITLE}}</h3><p>{{EX_SUB}}</p></div>
  <div class="body">
    <img src="../assets/img/{{HEROIMG}}" alt="Coolizi">
    <div class="mcd">⏳ <span data-mcd>15:00</span></div>
    <div class="coupon"><span>{{EX_CLABEL}}</span><b>{{EX_CODE}}</b></div>
    <a class="btn js-cta" href="#">{{EX_CTA}}</a>
    <button class="decline" data-close-exit>{{EX_DECLINE}}</button>
  </div>
</div></div>

<!-- REDIRECT OVERLAY -->
<div id="redirect"><div class="spin"></div><div class="rt">{{RED_T}}</div><div class="rbar"><i></i></div><div class="rs">{{RED_S}}</div></div>

<script src="../assets/config.js"></script>
<script src="../assets/funnel.js"></script>
</body>
</html>
"""

# ========================================================================
# ROOT PICKER / 404 / SITEMAP / ROBOTS / CNAME
# ========================================================================
def render_root(geos):
    links = "\n".join('<a href="%s/">%s %s</a>' % (g["code"], {"en":"🇬🇧","de":"🇩🇪","fr":"🇫🇷","it":"🇮🇹","es":"🇪🇸","nl":"🇳🇱","pt":"🇵🇹","el":"🇬🇷"}[g["code"]], E(g["lang_label"])) for g in geos)
    geomap = {g["cc"]: g["code"] for g in geos}
    extra = {"AT":"de","CH":"de","BE":"fr"}
    geomap.update(extra)
    return """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coolizi Portable AC — Review &amp; Official Deal</title>
<meta name="description" content="Coolizi portable air conditioner review, price and official discount. Choose your language.">
<link rel="canonical" href="%s/en/">
<link rel="stylesheet" href="assets/styles.css">
<script>
var M=%s;
try{var c=(navigator.language||'').slice(0,2).toUpperCase();}catch(e){}
// instant client-side geo redirect (keyless, fast) then fall back to language
fetch('https://ipwho.is/',{cache:'no-store'}).then(function(r){return r.json()}).then(function(d){
  var cc=(d&&d.country_code)||'';var dest=M[cc]||'en';location.replace(dest+'/'+location.search);
}).catch(function(){location.replace('en/'+location.search);});
setTimeout(function(){if(!window.__redir){location.replace('en/'+location.search);}},2500);
</script>
</head><body><div class="picker">
<h1>Coolizi Portable AC</h1>
<p>Choose your country / language</p>
<div class="grid">%s</div>
</div></body></html>""" % (DOMAIN, json.dumps(geomap), links)

def render_404(geos):
    links = " · ".join('<a href="/%s/">%s</a>' % (g["code"], E(g["lang_label"])) for g in geos)
    return """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Not found — Coolizi</title>
<link rel="stylesheet" href="/assets/styles.css"></head><body><div class="picker">
<h1>404</h1><p>Page not found. Pick your language:</p><div style="margin-top:14px">%s</div>
</div></body></html>""" % links

def sitemap(geos):
    urls = ['<url><loc>%s/%s/</loc><lastmod>%s</lastmod><changefreq>daily</changefreq><priority>0.9</priority>'
            '%s</url>' % (DOMAIN, g["code"], TODAY,
            "".join('<xhtml:link rel="alternate" hreflang="%s" href="%s/%s/"/>' % (x["hreflang"], DOMAIN, x["code"]) for x in geos))
            for g in geos]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(urls) + "\n</urlset>\n")

ROBOTS = """User-agent: *
Allow: /

User-agent: GPTBot
Allow: /
User-agent: CCBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: %s/sitemap.xml
""" % DOMAIN

LLMS = """# trycoolizi.com
Independent review of the Coolizi Portable AC (a no-installation personal/space air cooler).
Localized reviews, pricing and the official discount for UK, DE/AT/CH, FR/BE, IT, ES, NL, PT, GR.
> Affiliate disclosure: we may earn a commission on purchases made via our links.
"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full

def main():
    n = 0
    for g in GEOS:
        write("%s/index.html" % g["code"], render_page(g, GEOS)); n += 1
    write("index.html", render_root(GEOS))
    write("404.html", render_404(GEOS))
    write("sitemap.xml", sitemap(GEOS))
    write("robots.txt", ROBOTS)
    write("llms.txt", LLMS)
    write("CNAME", "trycoolizi.com\n")
    write("a7f3c920e84b41d6b5e0c1f8d23a9e74.txt", "a7f3c920e84b41d6b5e0c1f8d23a9e74\n")  # IndexNow key
    print("Built %d geo pages + root + 404 + sitemap + robots + llms + CNAME" % n)
    print("Geos:", ", ".join(g["code"] for g in GEOS))

if __name__ == "__main__":
    main()
