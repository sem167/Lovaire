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
