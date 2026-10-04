"""Engelse versie: vervangt alle Nederlandse teksten in de gegenereerde thema-JSON door Engels.
Draai na restyle.py. Klantreviews worden vertaald en als vertaling gemarkeerd."""
import json

EN = {
 "Altijd gratis verzending": "Always free shipping",
 "Elke bestelling met track & trace": "Every order with tracking",
 "Veilig betalen met iDEAL & Klarna": "Secure checkout with iDEAL & Klarna",
 "<p>✦ LOVAIRE VIP ✦</p>": "<p>✦ LOVAIRE VIP ✦</p>",
 "<h2>Word Lovaire VIP</h2>": "<h2>Become a Lovaire VIP</h2>",
 "<p>Als VIP hoor je het als eerste: nieuwe producten, exclusieve acties en beauty tips, rechtstreeks in je inbox.</p>":
   "<p>VIPs hear it first: new products, exclusive offers and beauty tips, straight to your inbox.</p>",
 "Word VIP": "Join now",
 "<p>Gratis aanmelden · Uitschrijven kan altijd</p>": "<p>Free to join · Unsubscribe anytime</p>",
 "<p><strong>Lovaire</strong></p><p>Beauty essentials die jouw natuurlijke schoonheid laten stralen.</p>":
   "<p><strong>Lovaire</strong></p><p>Beauty essentials that let your natural beauty shine.</p>",
 "Informatie": "Information",
 "<p><strong>VEILIG BETALEN</strong></p>": "<p><strong>SECURE PAYMENT</strong></p>",
 "<p>Beveiligde checkout via Shopify. Wij zien en bewaren nooit je betaalgegevens.</p>":
   "<p>Secure checkout powered by Shopify. We never see or store your payment details.</p>",
 "<p><strong>KLANTENSERVICE</strong></p><p>Ma–vr: 09:00–17:00<br/>Za: 10:00–14:00<br/>Zo: gesloten</p><p>lovairesupport@gmail.com</p><p>KVK: 42074062<br/>BTW: NL005474481B21</p>":
   "<p><strong>CUSTOMER SERVICE</strong></p><p>Mon–Fri: 09:00–17:00<br/>Sat: 10:00–14:00<br/>Sun: closed</p><p>lovairesupport@gmail.com</p><p>Chamber of Commerce (KVK): 42074062<br/>VAT: NL005474481B21</p>",
 "Lovaire woordmerk": "Lovaire wordmark",
 "Collectie-kop": "Collection header",
 "<p>LOVAIRE COLLECTIE</p>": "<p>LOVAIRE COLLECTION</p>",
 "Gratis verzending": "Free shipping",
 "Op elke bestelling, zonder minimumbedrag.": "On every order, no minimum spend.",
 "Veilig betalen": "Secure payment",
 "Met iDEAL, Klarna en meer via een beveiligde checkout.": "iDEAL, Klarna and more via a secure checkout.",
 "Track & trace": "Order tracking",
 "Volg je pakketje vanaf het moment van verzending.": "Follow your parcel from the moment it ships.",
 "Persoonlijke service": "Personal service",
 "Ma–vr van 09:00 tot 17:00 staan we voor je klaar.": "We're here for you Mon–Fri, 09:00–17:00.",
 "Lovaire beauty": "Lovaire beauty",
 "<p>Voel je mooi, <em>elke dag</em></p>": "<p>Feel beautiful, <em>every day</em></p>",
 "Make-up, huid- en haarverzorging die je echt gebruikt. Zorgvuldig geselecteerd en altijd gratis verzonden.":
   "Make-up, skin and hair care you'll actually use. Carefully selected and always shipped for free.",
 "Shop nu": "Shop now",
 "Ontdek collecties": "Explore collections",
 "Veilig betalen met iDEAL": "Secure checkout with iDEAL",
 "Met track & trace in je mail": "With tracking sent to your inbox",
 "Ongelofelijk wat dit product doet. Ik ben 50 plus, door dit product zie je mijn rimpels oprecht minder. Heel natuurlijk en de kleur past zich inderdaad aan je eigen huidskleur. Heel erg tevreden.":
   "Incredible what this product does. I'm over 50, and with this product my wrinkles honestly show less. Very natural, and the colour really does adapt to your own skin tone. Very happy.",
 "ECHTE REVIEWS": "REAL REVIEWS",
 "Wat klanten zeggen": "What customers say",
 "Reviews worden na een bestelling verzameld via Loox en ongewijzigd getoond.":
   "Reviews are collected via Loox after purchase. Quotes translated from Dutch.",
 "Veelgestelde vragen": "Frequently asked questions",
 "<h2>Veelgestelde vragen</h2>": "<h2>Frequently asked questions</h2>",
 "Wanneer ontvang ik mijn bestelling?": "When will I receive my order?",
 "<p>Zodra je bestelling is verzonden, ontvang je een e-mail met je track & trace, zodat je precies kunt volgen waar je pakketje is. Alle details vind je in ons <a href=\"/pages/verzendbeleid\">verzendbeleid</a>.</p>":
   "<p>As soon as your order ships, you'll receive an email with your tracking link, so you can follow your parcel every step of the way. You'll find all the details in our <a href=\"/pages/verzendbeleid\">shipping policy</a>.</p>",
 "Wat zijn de verzendkosten?": "How much is shipping?",
 "<p>Niets: bij Lovaire is verzending altijd gratis.</p>": "<p>Nothing: shipping is always free at Lovaire.</p>",
 "Kan ik mijn bestelling retourneren?": "Can I return my order?",
 "<p>Je kunt je bestelling tot 14 dagen na ontvangst retourneren. Voor hygiënische producten, zoals cosmetica en ondergoed, gelden aparte voorwaarden. Lees alles op <a href=\"/pages/bestellingen-en-levering-1\">Ruilen en retourneren</a>.</p>":
   "<p>You can return your order within 14 days of receiving it. Separate conditions apply to hygiene products such as cosmetics and underwear. Read everything on our <a href=\"/pages/bestellingen-en-levering-1\">returns and exchanges</a> page.</p>",
 "Waar worden jullie producten gemaakt?": "Where are your products made?",
 "<p>Onze producten worden zowel lokaal als wereldwijd geproduceerd. We selecteren onze productiepartners zorgvuldig, zodat je kwaliteit krijgt voor een eerlijke prijs.</p>":
   "<p>Our products are made both locally and around the world. We choose our production partners carefully, so you get quality at a fair price.</p>",
 "Ik heb een vraag, hoe bereik ik jullie?": "I have a question, how can I reach you?",
 "<p>Stuur ons een bericht via de <a href=\"/pages/contact\">contactpagina</a>. We reageren op werkdagen tussen 09:00 en 17:00.</p>":
   "<p>Send us a message via our <a href=\"/pages/contact\">contact page</a>. We reply on weekdays between 09:00 and 17:00.</p>",
 "ONZE FAVORIETEN": "OUR FAVOURITES",
 "Shop de favorieten": "Shop the favourites",
 "Bekijk alles": "View all",
 "Alle producten": "All products",
 "ONTDEK": "DISCOVER",
 "Waar ben je naar op zoek?": "What are you looking for?",
 "<p>Make-up, huid en haar. Voor elk moment van <em>jouw dag</em>.</p>": "<p>Make-up, skin and hair. For every moment of <em>your day</em>.</p>",
 "Ochtend": "Morning",
 "Een frisse, stralende start van je dag.": "A fresh, radiant start to your day.",
 "Overdag": "Daytime",
 "Comfortabel en verzorgd de hele dag door.": "Comfortable and polished all day long.",
 "Avond": "Evening",
 "Even tijd voor jezelf.": "A moment just for you.",
 "ELK MOMENT": "EVERY MOMENT",
 "Jouw dag met Lovaire": "Your day with Lovaire",
 "Alle collecties": "All collections",
 "Populair bij Lovaire": "Popular at Lovaire",
 "<p>KLANTENSERVICE</p>": "<p>CUSTOMER SERVICE</p>",
 "<h1>Hoe kunnen we je helpen?</h1>": "<h1>How can we help?</h1>",
 "Contactgegevens": "Contact details",
 "<h3>Openingstijden</h3>": "<h3>Opening hours</h3>",
 "<p>Ma–vr: 09:00–17:00<br/>Za: 10:00–14:00<br/>Zo: gesloten</p>": "<p>Mon–Fri: 09:00–17:00<br/>Sat: 10:00–14:00<br/>Sun: closed</p>",
 "<h3>Bestelling volgen</h3>": "<h3>Track your order</h3>",
 "<p>Gebruik de track &amp; trace-link in je verzendmail.</p>": "<p>Use the tracking link in your shipping confirmation email.</p>",
 "Contactformulier": "Contact form",
 "<h2>Stuur ons een bericht</h2>": "<h2>Send us a message</h2>",
 "Verstuur bericht": "Send message",
 "Hulp nodig": "Need help",
 "<h2>Nog vragen? Wij helpen je graag</h2>": "<h2>Questions? We're happy to help</h2>",
 "<p>Ons team reageert op werkdagen tussen 09:00 en 17:00.</p>": "<p>Our team replies on weekdays between 09:00 and 17:00.</p>",
 "Neem contact op": "Contact us",
 "<p><strong>DE LOVAIRE BELOFTE</strong><br/>✓ Altijd gratis verzending<br/>✓ Veilig betalen met iDEAL of Klarna<br/>✓ Verzonden met track &amp; trace</p>":
   "<p><strong>THE LOVAIRE PROMISE</strong><br/>✓ Always free shipping<br/>✓ Secure checkout with iDEAL or Klarna<br/>✓ Shipped with tracking</p>",
 "Verzending & levering": "Shipping & delivery",
 "<p>Je ontvangt een e-mail met track &amp; trace zodra je bestelling onderweg is. Meer info: <a href=\"/pages/verzendbeleid\">verzendbeleid</a>.</p>":
   "<p>You'll receive an email with a tracking link as soon as your order is on its way. More info: <a href=\"/pages/verzendbeleid\">shipping policy</a>.</p>",
 "Retourneren": "Returns",
 "<p>Je kunt je bestelling tot 14 dagen na ontvangst retourneren. Voor hygiënische producten, zoals cosmetica en ondergoed, gelden aparte voorwaarden: zie <a href=\"/pages/ruilen-en-retourneren\">hygiënische producten</a>. Alle stappen vind je op <a href=\"/pages/bestellingen-en-levering-1\">Ruilen en retourneren</a>.</p>":
   "<p>You can return your order within 14 days of receiving it. Separate conditions apply to hygiene products such as cosmetics and underwear: see <a href=\"/pages/ruilen-en-retourneren\">hygiene products</a>. You'll find every step on our <a href=\"/pages/bestellingen-en-levering-1\">returns and exchanges</a> page.</p>",
 "<p>Je betaalt via de beveiligde checkout van Shopify, met o.a. iDEAL en Klarna. Wij zien en bewaren nooit je betaalgegevens.</p>":
   "<p>You pay through Shopify's secure checkout, with options including iDEAL and Klarna. We never see or store your payment details.</p>",
 "Vragen? Wij helpen je graag": "Questions? We're happy to help",
 "<p>Mail ons via de <a href=\"/pages/contact\">contactpagina</a>. We reageren op werkdagen tussen 09:00 en 17:00.</p>":
   "<p>Email us via our <a href=\"/pages/contact\">contact page</a>. We reply on weekdays between 09:00 and 17:00.</p>",
 "Voordelen": "Benefits",
 "Op elke bestelling": "On every order",
 "Ma–vr 09:00–17:00": "Mon–Fri 09:00–17:00",
 "Aanbevolen": "Recommended",
 "<h2>Misschien vind je dit ook mooi</h2>": "<h2>You may also like</h2>",
}

used = set()
def tr(n):
    if isinstance(n, dict): return {k: tr(v) for k, v in n.items()}
    if isinstance(n, list): return [tr(v) for v in n]
    if isinstance(n, str) and n in EN:
        used.add(n); return EN[n]
    return n

FILES = ["sections__header-group.json", "sections__footer-group.json", "templates__index.json", "templates__product.json",
         "templates__collection.json", "templates__list-collections.json", "templates__page.json", "templates__page.contact.json"]
if __name__ == "__main__":
    for f in FILES:
        json.dump(tr(json.load(open(f))), open(f, "w"), ensure_ascii=False, indent=2)
    # Nieuwe vorm favorieten: kop met cursief accent, ronde knop, geen tab
    for f, head, ital in [("templates__index.json", "Shop the", "favourites"), ("templates__list-collections.json", "Popular at", "Lovaire")]:
        d = json.load(open(f)); st = d["sections"]["favorieten"]["settings"]
        st.pop("tab_label", None)
        st.update({"heading": head, "heading_italic": ital, "button_label": "Shop all", "background": "#f4ece4",
                   "badge_text": "Favourite", "badge_count": 0, "padding_top": 80, "padding_bottom": 80})
        json.dump(d, open(f, "w"), ensure_ascii=False, indent=2)
    unused = set(EN) - used
    print("vertaald:", len(used), "ongebruikt:", len(unused))
    for u in unused: print("  -", u[:70])
