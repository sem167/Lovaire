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
