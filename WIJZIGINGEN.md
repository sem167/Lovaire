# Opschoonactie Lovaire-winkel — 1 oktober 2026

Originele teksten staan in `backup/2026-10-01-origineel.json`.

## Producten
| Oud | Nieuw | Type | Extra |
|---|---|---|---|
| LashLift Waterproof Mascara | LashLift Waterproof Mascara | Mascara | URL `duo-stick-cream-bronzer-brush` → `lashlift-waterproof-mascara` (oude URL redirect automatisch) |
| lovaire - Support Bh | Support BH | BH | |
| Self tanner - tanning lotion | Self Tan Mousse | Zelfbruiner | |
| Zelfkleurende Foundation SPF15 | Zelfkleurende Foundation SPF15 | Foundation | |
| spray & massage borstel | Spray & Massage Haarborstel | Haarborstel | ook in Haarverzorging |
| Lovaire HairBoost Shampoo | HairBoost Shampoo | Shampoo | verplaatst van Huidverzorging naar Haarverzorging |

Voor alle producten:
- Beschrijvingen hebben nu dezelfde opbouw (intro → "Waarom je hem gaat willen" → gebruik/FAQ) en zijn opgeschoond (geen lege alinea's, losse streepjes of alles-vet meer).
- SEO-titel, meta-beschrijving en tags zijn ingevuld.

## Collecties
- `Make Up` → **Make-up**, `Huid Producten` → **Huidverzorging** (URL's ongewijzigd)
- Nieuwe collectie **Haarverzorging**
- Alle collecties hebben nu een beschrijving en SEO-tekst

## Menu's
- Hoofdmenu → Collecties: Make-up, Huidverzorging, Haarverzorging, Beauty Tools, Shapewear
- Informatiemenu: titels netjes met hoofdletters, logischere volgorde

## Nog te doen (handmatig)
- **Algemene voorwaarden** linkt naar de contactpagina: er bestaat nog geen voorwaardenpagina. Maak die aan via Instellingen → Beleid.
- **Volg je bestelling** linkt naar de contactpagina.
- Voorraad staat op 0 of negatief (mascara −12, shampoo −4, foundation −2). Als je via dropshipping verkoopt, zet voorraadtracking uit. Doe je dat niet, dan klopt de voorraad niet.
- De Self Tan Mousse heeft maar 1 foto, de borstel 2. Voeg meer beelden toe.
- Afbeeldingsnamen zoals `WhatsApp_Image_...` / `ChatGPT_Image_...`: geef ze alt-teksten.

# Nieuw thema "Lovaire – Nieuw design" — 1 oktober 2026

Kopie van het live Dwell-thema (ID 208207184211), **niet gepubliceerd**.
Voorbeeld: https://lovaire.nl/?preview_theme_id=208207184211

Bronbestanden: `theme/build.py` genereert de vier aangepaste themabestanden in `theme/`.

- **Stijl:** zacht & vrouwelijk. Crème `#fbf7f4`, blush `#f6e9e6`, nude `#efe4da`, oudroze `#b9818a`, cacao `#3b2a26`.
- **Lettertypes:** Playfair Display (koppen), Jost (tekst). Knoppen afgerond.
- **Header:** vaste header, zoeken rechts, cacaokleurige aankondigingsbalk.
- **Homepage:** hero met twee knoppen → voordelen → bestsellers (alle 6 producten) → "Shop per categorie" (5 collecties, incl. Haarverzorging) → "Over Lovaire" → reviews → veelgestelde vragen.
- **Footer:** nieuwsbriefblok, kolommen Shop / Informatie / Klantenservice, "Powered by Shopify" uit, lege social-links verwijderd.
- App-embeds (Loox, Kaching Bundles, Upcart) blijven actief.

## Update: vertrouwen & productpagina (1 oktober 2026)
- Eén universele productpagina voor alle producten (`theme/build_product.py`), ook gekopieerd naar de sjablonen `support-bh-2`, `tanning-oil`, `foundation` en `kam`. Alleen in het nieuwe thema; het live thema is ongewijzigd.
  - Opbouw: foto's met miniaturen → titel → prijs (incl. termijnen/btw-info) → varianten als knoppen → winkelwagen + snelle checkout → blush-blok met garanties → beschrijving → uitklapblokken Verzending, Retourneren, Veilig betalen, Vragen.
  - Daaronder de voordelenbalk en "Misschien vind je dit ook mooi".
  - De oude productspecifieke blokken met claims als "Duizenden vrouwen…" en de shampoo-content die ook op de mascara stond, zijn verwijderd.
- Homepage: nieuw blok "Zorgeloos bestellen" (3 stappen: bestel veilig → wij verzenden → niet tevreden).

## Update: alle pagina's in nieuwe stijl (1 oktober 2026)
`theme/build_pages.py`:
- **Collectiepagina's:** nude kopblok met titel + collectiebeschrijving, horizontale filters, afgeronde productkaarten, voordelenbalk onderaan.
- **Alle collecties:** Nederlandse kop ("Alle collecties" i.p.v. "Collections"), kapot kleurenschema gerepareerd, voordelenbalk.
- **Gewone pagina's** (Over ons, verzend- en retourbeleid…): sierlijke kop + blok "Nog vragen? Wij helpen je graag".
- **Contactpagina:** "Hoe kunnen we je helpen?", drie infoblokken (e-mail, openingstijden, bestelling volgen), formulier met knop "Verstuur bericht" i.p.v. "Submit".

## Update: eerlijke beloftes + algemene voorwaarden (1 oktober 2026)
**Tegenstrijdigheid gevonden:** de live site belooft "30 dagen geld terug", maar de eigen pagina's zeggen 14 dagen (retourkosten voor de klant) en geen retour op hygiënische producten (cosmetica, huidverzorging, ondergoed).
In het nieuwe thema staan nu alleen beloftes die op de eigen beleidspagina's staan:
- Aankondigingsbalk: "Altijd gratis verzending" en "Levering in 5–12 werkdagen met track & trace".
- Voordelenbalk: Gratis verzending / Veilig betalen / Persoonlijke service.
- Productpagina, veelgestelde vragen en bestelstappen: 14 dagen bedenktijd, met verwijzing naar het hygiënebeleid.

**Algemene voorwaarden:** concept-pagina `/pages/algemene-voorwaarden` aangemaakt (NIET gepubliceerd). Gebaseerd op de eigen bedrijfsgegevens en beleidspagina's, met het wettelijke herroepingsrecht (14 dagen; uitzondering voor verzegelde hygiëneproducten die na levering zijn geopend). Laten nakijken voor publicatie.

**Let op:** het hygiënebeleid ("geen retour zodra verzonden") is strenger dan de wet toestaat. De uitzondering geldt alleen voor geopende, verzegelde producten.

## Update: beige & zwart (1 oktober 2026)
Op verzoek volledig omgezet naar een strak beige-zwart ontwerp:
- Palet: beige `#f5f0e8` / `#ede4d8` / `#e6d9c7` / `#d8c8b4`, zwart `#111111`, grijs `#3a3a3a`, wit.
- Koppen: Josefin Sans; tekst: Jost.
- Alle hoeken recht (knoppen, foto's, kaarten, badges, invoervelden).
- Zwarte aankondigingsbalk en footer; homepage-hero gecentreerd met kop in hoofdletters.

## Update: extra wow voor de vrouwelijke doelgroep (1 oktober 2026)
- Bewegende tekstband (zwart/beige) direct onder de hero: "Jouw glow ✦ Selfcare ✦ Altijd gratis verzending ✦ Voel je mooi".
- Spotlight-blok: LashLift Waterproof Mascara groot uitgelicht op beige ("Wimpers die de hele dag blijven stralen").
- Warmere teksten: "Jouw nieuwe favorieten", "Voor elke vrouw die zich mooi wil voelen", "Geliefd door onze klanten".
- Homepage-volgorde: hero → tekstband → voordelen → favorieten → categorieën → spotlight → zorgeloos bestellen → over Lovaire → reviews → FAQ.

## Update: betaal-iconen & luxe afwerking (1 oktober 2026)
- Betaal-iconen (automatisch de in Shopify actieve betaalmethodes) direct onder de bestelknop op alle productpagina's.
- Footer: nieuwe kolom "Veilig betalen" met betaal-iconen en uitleg over de beveiligde checkout.
- Aankondigingsbalk: derde bericht "Veilig betalen met iDEAL & Klarna".

## Update: nieuwe hoofdpagina-foto (1 oktober 2026)
- Hero: productfoto's van LashLift Mascara + Zelfkleurende Foundation naast elkaar (desktop), mascara op mobiel. Vervangt de WhatsApp-foto.
- iDEAL kan niet via de API worden aangezet: Instellingen → Betalingen. Zolang iDEAL uit staat, kloppen de iDEAL-teksten in het thema niet.

## Update: sfeerfoto + Lovaire VIP (1 oktober 2026)
- Nieuwe hero-sfeerfoto: "Woman Holding A Makeup Product" door Ron Lach (Pexels, foto 8128684, gratis commercieel te gebruiken), opgeslagen als `lovaire-hero-vrouw-make-up.jpg`. Desktop: naast de mascara-productfoto; mobiel: alleen de sfeerfoto.
- Nieuwsbrief vervangen door zwart "Lovaire VIP"-blok dat naadloos overloopt in de zwarte footer (knop "Word VIP").

## Update: strakke hero-foto (1 oktober 2026)
- Twee foto's naast elkaar vervangen door één brede, strakke foto: "Minimalist Skincare Product Flat Lay" (Pexels 34939732) → `lovaire-hero-breed-2.jpg`.
- Mobiel: staande foto uit dezelfde neutrale serie (Pexels 34939759) → `lovaire-hero-strak.jpg`.
- Ongebruikte foto's (vrouw met make-up, "Variety of Makeup Products") verwijderd uit Bestanden.

## Update: meer Lovaire-branding (1 oktober 2026)
- Hero: groot LOVAIRE-woordmerk (jumbo-tekst met onthul-animatie) boven "Jouw glow, elke dag".
- Footer: reusachtig LOVAIRE-woordmerk over de volle breedte onderaan elke pagina.
- Tekstband begint met "LOVAIRE ✦"; koppen "De Lovaire favorieten", "Shop Lovaire", "Lovaire spotlight", "Zorgeloos bestellen bij Lovaire", "Waarom klanten van Lovaire houden"; "Lovaire collectie" op collectiepagina's; "De Lovaire belofte" op productpagina's.

## Update: Lyvelle-stijl (1 oktober 2026)
Alleen de stijl van de voorbeeldsite is overgenomen, niet het logo of de teksten.
- Wit met zachte blush/perzik secties, Montserrat-koppen en kleine taupe hoofdletter-labels ("ONTDEK", "ONZE BELOFTE").
- Zwarte rechthoekige knoppen ("Shop nu →"), blush aankondigingsbalk.
- Hero links uitgelijnd op blush: "Beauty essentials voor jouw glow, elke dag".
- Collectieblok "Waar ben je naar op zoek?" en leveringsblok "Zorgeloos shoppen bij Lovaire".
- Afgeronde productkaarten. Bewust GEEN nep-uitverkoopbadges en GEEN "30 dagen garantie" (Lovaire hanteert 14 dagen).
- Producttemplate ook gekopieerd naar product.support-bh-2/tanning-oil/foundation/kam.
- Homepage-opbouw zoals het voorbeeld: hero → voordelen → "ONZE FAVORIETEN" (nieuwe sectie `lovaire-favorieten`: afgeronde productkaarten, 3 kolommen, zwarte "Shop alles →"-knop) → "ONTDEK" categorie-rondjes → "ONZE BELOFTE" → verhaal → reviews → FAQ. Tekstband en spotlight verwijderd voor een rustiger geheel.

## Update: spectaculaire hero (1 oktober 2026)
- Nieuwe eigen sectie `lovaire-hero`: tekst links op blush, grote sfeerfoto rechts (op mobiel bovenaan).
- Foto: "A Portrait of a Woman in a White Robe Holding a Dropper Bottle" (Pexels 11179593, gratis commercieel bruikbaar) → `lovaire-hero-glow.jpg`.
- Animaties: tekst schuift gefaseerd omhoog, foto zoomt langzaam in, zwevend glas-label "Altijd gratis verzending", draaiend embleem "LOVAIRE · BEAUTY · ESSENTIALS". Uit bij 'beperkte beweging'.
- Kop "Voel je mooi, *elke dag*" met cursief accent; twee knoppen; vinkjes Gratis verzending / iDEAL / Persoonlijke service.
- Alles aanpasbaar in de thema-editor (foto, focus, teksten, kleuren, hoogte).

## Update: echte reviews en geen levertijd in de etalage (1 oktober 2026)
- Oude homepage-testimonials (Laura, Yvonne, Fleur, Luna, Esther; herkomst niet controleerbaar) vervangen door nieuwe sectie `lovaire-reviews` met alleen echte Loox-reviews, letterlijk overgenomen, met productlink en het echte Loox-gemiddelde (5,0 uit 3 reviews).
- Productkaarten tonen de echte Loox-sterren en het aantal reviews (alleen als er reviews zijn).
- Levertijd (5–12 werkdagen) weggehaald uit aankondigingsbalk, homepage, FAQ en productpagina's; vervangen door "track & trace". Staat nog wel op de verzendbeleidpagina (wettelijk verplicht). Geen "snelle levering" beloofd, omdat 5–12 werkdagen dat niet is.

## Update: strakker en professioneler (1 oktober 2026)
- Nieuwe sectie `lovaire-belofte`: 4 witte kaarten met lijn-iconen (gratis verzending, veilig betalen, track & trace, persoonlijke service) en de echte betaaliconen. Vervangt de genummerde stappen en de losse voordelenbalk onder de hero (dubbel met de vinkjes in de hero).
- Homepage: hero → favorieten → categorieën → belofte → over Lovaire → reviews → FAQ, met gelijkmatige witruimte (72–88 px).
- Productpagina's: nieuw blok `lovaire-rating` onder de titel met de echte Loox-score en het aantal reviews (verborgen als een product nog geen reviews heeft); klikt door naar de Loox-reviews.
- Verzoek om 100 reviews te verzinnen niet uitgevoerd: nep-reviews zijn verboden (Omnibus-richtlijn / ACM).

## Update: mobiele Lyvelle-stijl overal (1 oktober 2026)
Op basis van 4 mobiele screenshots van lyvelle.nl (alleen vormgeving overgenomen, geen teksten/logo/beloftes).
- Nieuwe secties: `lovaire-categories` (rondjes met gestippelde gouden rand, scrollbaar op mobiel), `lovaire-statement` (groot merkstatement met animerende gouden lijn), `lovaire-momenten` (tabs Ochtend/Overdag/Avond met producten en winkelwagenknop), snippet `lovaire-buy` (direct in winkelwagen of "Kies opties").
- `lovaire-favorieten`: blush achtergrond, tab "Alle producten", swipe-carrousel met bolletjes op mobiel, volle zwarte "In winkelwagen"-knop per product.
- `lovaire-belofte`: extra weergave "Compacte lijst" (2×2 met ronde iconen en scheidingslijnen), direct onder de hero.
- Hero: op mobiel eerst tekst, dan foto; volle knop met gouden rand.
- Homepage: hero → voordelen → categorieën → favorieten → statement → momenten → reviews → FAQ.
- Collectiepagina's: blush kop met categorie-rondjes als navigatie, vierkante productfoto's, compacte voordelen met betaaliconen. "Alle collecties"-pagina vernieuwd.
- Niet overgenomen: "30 dagen garantie" (Lovaire: 14 dagen) en de verwachte leverdatum (op verzoek levertijd niet tonen).

## Update: hele store in het Engels + nieuwe favorieten (4 oktober 2026)
Backup van alle Nederlandse teksten (producten, collecties, pagina's, menu's): `backup/2026-10-04-nl-voor-engels.json`.
- Thema: alle teksten Engels via `theme/translate_en.py` (draai na restyle.py); knoppen "Add to cart / Choose options / Sold out", "From", reviewlabels. Klantreview vertaald en gemarkeerd als "Quotes translated from Dutch".
- Producten: titels, beschrijvingen, producttype en SEO in het Engels (Support BH → Support Bra, Zelfkleurende Foundation → Colour-Adapting Foundation, Haarborstel → Hair Brush). BH-opties: Colour (Black/White/Bronze/Beige) en Cup size; kleurlabels aangepast in de gekoppelde kleur-metaobjecten.
- Collecties: Huidverzorging → Skincare, Haarverzorging → Hair care, plus beschrijvingen en SEO.
- Pagina's: About us, Orders & delivery, Returns & exchanges, Hygiene products policy, Shipping policy, Privacy policy en (nog ongepubliceerd) Terms & conditions; inhoud getrouw vertaald. Handles/URL's ongewijzigd.
- Menu's: Main menu, Information, Footer menu en klantaccountmenu in het Engels.
- Niet aangepast: Shopify-privacybeleid onder Instellingen → Beleid (opnieuw genereren in het Engels), en de winkeltaal (nl) — kan alleen in de admin.
- "Shop the favourites" opnieuw ontworpen: latte-achtergrond, boogvormige foto's, verspringende kolommen, N° 01-nummering, tweede foto bij hover, ronde "+"-knop om direct toe te voegen.

## Update: telefoonweergave verbeterd (4 oktober 2026)
Gecontroleerd met een lokale weergave van de eigen secties op 390 px breed (Chromium-screenshots).
- Hero: compactere tekst, foto in boogvorm, tweede knop als tekstlink, vinkjes gecentreerd op één regel waar het past, embleem kleiner.
- Voordelenblok: op mobiel icoon boven de tekst, gecentreerd in een 2×2-raster met scheidingslijnen (geen smalle tekstkolommen meer).
- Categorieën: op mobiel 3 + 2 gecentreerd i.p.v. afgesneden scrollrij.
- Reviewscore: netjes gecentreerd als het over twee regels gaat.
- Het nieuwe thema is inmiddels gepubliceerd (live), dus deze wijzigingen staan in een kopie: "Lovaire – Nieuw design (mobiel verbeterd)" (208376430931).

## Update: productpagina's vernieuwd + geen snelle checkoutknoppen (4 oktober 2026)
Alles in het concept-thema "Lovaire – Nieuw design (mobiel verbeterd)" (208376430931); `theme/product_page.py` draaien na translate_en.py.
- Snelle checkoutknoppen (Shop Pay, Apple Pay, PayPal enz.) weg: eigen versie van `blocks/accelerated-checkout.liquid` die niets toont, plus `show_accelerated_checkout_buttons` uit voor de themawinkelwagen. De Upcart-winkelwagen heeft een eigen instelling hiervoor (in de Upcart-app uitzetten).
- Nieuw blok `lovaire-product-trust` onder de knop: voorraadregel, kaart "Secure checkout" met de echte betaaliconen en 4 voordeeltegels (gratis verzending, track & trace, veilig betalen, persoonlijke service).
- Langere productpagina: `lovaire-product-story` (foto's in boogvorm met uitleg), `lovaire-product-howto` (genummerde stappen), `lovaire-product-reviews` (Loox), belofte-kaarten en "You may also like" (huidige product wordt overgeslagen).
- Teksten per product staan in metavelden (`lovaire.highlight_1/2_title`, `_text`, `how_to`) en zijn gebaseerd op de eigen productbeschrijvingen; aanpasbaar in de admin bij het product.
- "Shop the favourites" toont nooit het product waar je op dat moment naar kijkt.

## Update: productpagina's langer en meer gericht op kopen (4 oktober 2026)
In concept-thema 208376430931.
- Volgorde: product → "Everything it does for you" (voordelenlijst) → uitleg met foto's (nu 3 blokken) → gebruik → reviews → belofte → FAQ → afsluitend koopblok.
- "You may also like" verwijderd: geen links meer naar andere producten op de productpagina.
- Vaste koopbalk onderin (foto, naam, prijs, knop) zodra de gewone knop uit beeld is; vervangt de sticky balk van Horizon. Bij producten met opties (BH) scrolt de knop naar maat/kleur als er nog niets gekozen is.
- Afsluitend koopblok met echte Loox-score, prijs, knop en "Free shipping · 14-day returns · Secure checkout".
- Voorraad: "Only X left in stock" met balkje toont alleen het échte aantal, en alleen als Shopify de voorraad bijhoudt (staat nu uit bij alle producten, dus nu wordt gewoon "In stock" getoond). Geen verzonnen aantallen (misleidende schaarste is verboden).
- Uitlegblok zonder eigen productfoto krijgt een sierblok i.p.v. dezelfde foto nogmaals.
- Nieuwe metavelden per product: `lovaire.benefits`, `lovaire.faq` (vraag :: antwoord) en `lovaire.highlight_3_title/_text`, gebaseerd op de eigen productbeschrijvingen.

## Update: Engelse productafbeeldingen (4 oktober 2026)
- 14 nieuwe afbeeldingen (map `fotos/`) in Lovaire-stijl, toegevoegd achter de bestaande foto's: mascara 3 (voordelen, gebruik, studio – met vrijstaande packshot), Support Bra 2, Self Tan Mousse 3, Foundation 2, Haarborstel 2, Shampoo 2. Teksten alleen uit de eigen productbeschrijvingen.
- Bestaande foto's niet verwijderd: welke Nederlandse tekst bevatten kon niet worden gecontroleerd (cdn.shopify.com geblokkeerd in de werkomgeving).

## Update: reviews (voorlopig) niet tonen (5 oktober 2026)
In nieuw concept-thema "Lovaire – zonder reviews" (208439312723), kopie van het live thema. `theme/hide_reviews.py` draaien na product_page.py.
- Homepage: reviewsectie weg. Productpagina: reviewsectie en sterren onder de titel weg.
- Sterren in productkaarten ("Shop the favourites") en score in het koopblok uit via nieuwe instelling "Reviewsterren tonen" / "Reviewscore tonen" (standaard uit) – later met één vinkje weer aan te zetten.
- Loox zelf en de bestaande echte reviews zijn niet verwijderd.

## Update: zachte overgangen tussen secties (5 oktober 2026)
In concept-thema "Lovaire – zonder reviews" (208439312723).
- Nieuwe snippet `lovaire-bg`: elke eigen sectie loopt boven en onder met een verloop over in de kleur van de buursectie (geen harde kleurgrens meer). Hero loopt onderaan zacht over.
- `theme/blend.py` (draai als allerlaatste) rekent per pagina de overloopkleuren uit; tussen twee eigen secties wordt de mengkleur gebruikt. De zwarte footer wordt bewust niet gemengd.
- Scheidingslijnen in het voordelenblok vervagen nu naar de randen; de harde lijnen boven en onder dat blok zijn weg.
- Pipeline: build.py → build_product.py → build_pages.py → restyle.py → translate_en.py → product_page.py → hide_reviews.py → blend.py
- Aanvulling: menu zonder rand-/scheidingslijn, aankondigingsbalk wit (zelfde kleur als menu), hero loopt bovenaan zacht over vanuit het witte menu.
- Footer van zwart naar zachte blush (scheme-5) zonder scheidingslijn; de pagina loopt er met een verloop in over.
- Nieuwe sectie `lovaire-fade`: blend.py zet die automatisch tussen twee Horizon-secties met verschillende kleur (ook richting header/footer), op alle pagina's.
- FAQ op de homepage zonder lijntjes tussen de vragen.

## Update: oogcrème-pagina in Lyvelle-stijl (12 oktober 2026)
In nieuw concept-thema "Lovaire – oogcrème Lyvelle-stijl" (209002824019), kopie van het live thema "Lovaire – Nederlands (oogcrème vernieuwd)". Alleen het sjabloon `product.oogcreme` is aangepast.
- Nieuw blok `lovaire-pdp-intro` (`theme/blocks__lovaire-pdp-intro.liquid`): ondertitel "Oogcrème | Korean Dark Spot Formula" en drie omrande voordeel-balkjes met emoji direct onder de titel. Alle teksten zijn aan te passen in de thema-editor.
- Hetzelfde blok maakt de titel vet en groot, de prijs groot en de winkelwagenknop groot en groen (#6ab04c), met het winkelwagen-icoon. De kleur is in te stellen en de stijl met één vinkje uit te zetten.
- Het LOVAIRE-label boven de titel is weg.
- Balkjes alleen met claims uit de eigen productinfo ("camoufleert donkere kringen", "calcium, niacinamide & collageen"). "Wallen verdwijnen" is niet overgenomen: de crème camoufleert, ze laat wallen niet verdwijnen.
- Niet overgenomen: "Excellent | 100+ reviews" (zoveel reviews zijn er niet, en reviews staan uit).
- "1+1 gratis / 2+2 gratis" moet je instellen in Kaching Bundles (app is actief). Dan rekent de korting in de winkelwagen ook echt goed.
- Script: `theme/oogcreme_lyvelle.py` (werkt op `theme/templates__product.oogcreme.json`).

## Update: twee video's op de oogcrème-pagina (12 oktober 2026)
"Lovaire – oogcrème Lyvelle-stijl" (209002824019) is inmiddels live. Daarom staan deze wijzigingen in een nieuwe kopie: "Lovaire – oogcrème + video's" (209003086163).
- Nieuwe sectie `lovaire-video-duo` (`theme/sections__lovaire-video-duo.liquid`): vette kop en twee staande video's (9:16) naast elkaar, ook op mobiel. De video's spelen automatisch, zonder geluid en herhalend.
- Op de oogcrème-pagina staat de sectie direct onder het koopblok, met de kop "Zie de Calcium Oogcrème zelf in actie 💕".
- De video's kies je in de thema-editor uit Inhoud → Bestanden. Zonder gekozen video's blijft de sectie onzichtbaar voor bezoekers.
- Script: `theme/oogcreme_videos.py`.
- Video 1 en 2 ingesteld op de twee geüploade video's (7629350726313053471 en 7647742984905166093, beide 720×1280, ±1 minuut).

## Update: kortere producttitel oogcrème (13 oktober 2026)
- Producttitel "Dr.Melaxin Calcium Dark Spot Cover Oogcrème 15g" → "Calcium Dark Spot Oogcrème" (past beter op een telefoon). De URL blijft hetzelfde. SEO-titel ("Dr.Melaxin getinte oogcrème …"), merk (Dr.Melaxin), beschrijving en foto's zijn ongewijzigd.

## Update: kleiner logo (13 oktober 2026)
In concept-thema "Lovaire – kleiner logo" (209095164243), een kopie van het live thema "Lovaire – oogcrème + video's". Shopify zit aan het maximum van 20 thema's, dus de ongebruikte kopie "video's met geluidsknop" is hiervoor hergebruikt en hernoemd.
- Logohoogte op desktop 58 → 44 px, op mobiel 64 → 32 px (eerst 48, op verzoek nog kleiner) (`config/settings_data.json`, verder ongewijzigd).
- Script: `theme/logo_kleiner.py` (bouwt settings_data na; `python3 theme/logo_kleiner.py 44 32`).

## Update: winkelwagen duidelijk Nederlands (13 oktober 2026)
In hetzelfde concept-thema, nu "Lovaire – kleiner logo + winkelwagen NL" (209095164243).
- `locales/nl.json` (`theme/locales__nl.json`): "Verzendkosten worden berekend bij de checkout" vervangen door "Altijd gratis verzending" (overal). Fout "1 artikel verwijderd" bij toevoegen → "1 artikel toegevoegd aan je winkelwagen". "Afrekenen" → "Veilig afrekenen", "Geschat totaal" → "Totaal", "Speciale instructies" → "Opmerking bij je bestelling", "Doorgaan met winkelen" → "Verder winkelen", "Recent beoordeeld" → "Recent bekeken", "Uitverkoop" → "Aanbieding", "Inclusief btw." bij prijzen, en duidelijkere foutmeldingen.
- `templates/cart.json`: titel "Je winkelwagen", vertrouwensblok onder het totaal (veilig betalen, gratis verzending met track & trace, contact) en kop "Maak je routine compleet" boven de aanbevelingen.
- Let op: de Upcart-app (winkelwagen-schuif) heeft eigen teksten. Die pas je aan in de Upcart-app.
- Script: `theme/winkelwagen_nl.py`.

## Update: zwarte aankondigingsbalk + belangrijkste voordeel onder de titel (13 oktober 2026)
Zelfde concept-thema (209095164243), nu "Lovaire – concept 13 okt".
- Aankondigingsbalk op alle pagina's zwart met witte tekst (`scheme-announcement-black`). Script: `theme/aankondiging_zwart.py`.
- Oogcrème: de ondertitel onder de titel is nu het belangrijkste voordeel: "Camoufleert donkere kringen direct – voor een frissere, uitgeruste blik" (donkerder en iets vetter). Balkje 2 is daarom "Oogcrème én concealer in één" geworden, zodat er niets dubbel staat.

## Update: 30 dagen retour, 24/7 klantenservice, video's hoger (13 oktober 2026)
Op verzoek: **30 dagen retour op ongeopende producten** (geopende hygiëneproducten blijven uitgesloten) en **24/7 Nederlandse klantenservice**.
- Concept-thema "Lovaire – concept 13 okt" (209095164243), 16 bestanden: alle productpagina's (uitklapblok Retourneren/Vragen, belofte-kaart "24/7 klantenservice"), homepage (hero-vinkje, FAQ, belofte), collectiepagina's, contactpagina ("Openingstijden: 24/7 bereikbaar"), standaard paginasjabloon, footer (KLANTENSERVICE), vertrouwensblok onder de knop ("24/7 klantenservice – Nederlands, dag en nacht"), koopblok-voordeel "30 dagen retour" en de FAQ-standaardtekst. Script: `theme/retour30_service247.py`.
- Oogcrème: de video's staan direct onder het koopblok (ruimte 48+40 px → 8+8 px).
- Pagina's (direct live, geen thema): "Ruilen & retourneren" (30 dagen, ongeopend), "Ruil- & retourbeleid — Hygiëneproducten" (ongeopend en verzegeld = 30 dagen retour, geopend niet; was "geen retour zodra verzonden"), "Over ons" (24/7 in plaats van 6 dagen per week) en het concept "Algemene voorwaarden" (art. 6: 30 dagen retour naast de wettelijke 14 dagen bedenktijd).
- Let op: 24/7 is een belofte. Zorg dat er ook 's nachts en in het weekend iemand (of een chat) reageert.
- Oogcrème: uitklapkopjes compacter (12 px boven/onder, 13 px letter) via `lovaire-pdp-intro`. Geen extra ruimte meer onder het productblok, zodat de video's direct volgen.
- Oogcrème: nieuwe sectie `lovaire-tekst-foto` direct na de video's: kop "Eén laagje, direct verschil", korte uitleg en de echte voor-en-na-foto (`6-voor-direct.jpg`) met onderschrift "Resultaten kunnen per persoon verschillen". Voorbeeldsite lovelia.dk was vanuit de werkomgeving niet bereikbaar.
- Dubbeling weg: `lovaire-product-story` heeft een nieuwe instelling "Begin bij punt" (standaard 1). Op de oogcrème-pagina staat die op 2, omdat punt 1 (zelfde kop en 2e productfoto) nu direct na de video's staat. Onderschrift van de voor-en-na-foto is gecorrigeerd naar "Illustratie – …", want de foto zelf is een illustratie.

## Update: oogcrème-pagina opgebouwd zoals lovelia.dk (13 oktober 2026)
Op basis van screenshots van de concurrent (alleen de opbouw, eigen teksten en foto's). In concept-thema "Lovaire – concept 13 okt".
- Na de video's volgen vijf verhaalblokken (`lovaire-tekst-foto`: vette gecentreerde kop, korte tekst met vette accenten, foto over de volle breedte op mobiel):
  1. "Zie je er moe uit, ook als je goed hebt geslapen?" + voor-en-na-illustratie (zonder onderschrift; "Illustratie" staat in de foto zelf)
  2. "Waarom een gewone oogcrème vaak niet genoeg is" + textuurfoto
  3. "Wat deze oogcrème anders maakt" + packshot
  4. "Zo gebruik je het" (3 stappen) + eigen foto `oogcreme-oog-druppels.jpg` (aangeleverd door de eigenaar)
  5. "Zie er weer uit zoals je je voelt"
- Daarna FAQ en het afsluitende koopblok. Verwijderd van deze pagina: voordelenlijst, productverhaal, vergelijkingstabel, losse gebruik-sectie en belofte-kaarten (dubbel met de nieuwe blokken en het vertrouwensblok onder de knop).
- Niet overgenomen van de concurrent: "zonder te camoufleren" (onze crème camoufleert juist), "Populair bij 8.500+ vrouwen", "morgen verzonden", nep-doorgestreepte prijzen en reviews die er (nog) niet zijn.
- Script: `theme/oogcreme_verhaal.py`.

## 13 okt – "Inclusief btw" weg bij de prijs (oogcrème)
- templates/product.oogcreme.json: prijsblok `show_tax_info` → false.
- Het concept-thema is inmiddels gepubliceerd (live); schrijven naar het live thema kan niet via de API.
  Daarom kopie gemaakt: "Lovaire – zonder btw-regel" (209111023955) met deze wijziging. Gebruiker publiceert.

## 13 okt – Winkelwagen-lade in Lovelia-stijl
Kopie-thema "Lovaire – nieuwe winkelwagen" (209125638483), gemaakt van het live thema "zonder btw-regel".
Bestanden in `theme/live/` (live versies + wijzigingen via `theme/winkelwagen_lovelia.py`):
- settings_data: `cart_type` page → drawer (winkelwagen schuift open i.p.v. aparte pagina).
- header-actions: kop "Je winkelwagen" gecentreerd met grijs kruisje, groene balk "Gratis verzending! (incl. Track & Trace)",
  "🔒 30 dagen retourrecht" boven de knop, betaal-icoontjes eronder, totaalregel verborgen (staat in de knop).
- cart-summary: knop "Veilig afrekenen • €totaal" (donker).
- cart-products: "(Je bespaart €…)" in het groen per product, rand om aantal-kiezer.
Bewust niet overgenomen: "geld-terug-garantie" (ons beleid = 30 dagen retour, ongeopend), "50.000+ tevreden klanten"
en "Bestelling gereserveerd voor 10 minuten" (niet waar → misleidend volgens ACM).
