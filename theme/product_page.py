"""Langere, rijkere productpagina's: vertrouwensblok onder de knop, productverhaal, gebruik, reviews, belofte en
een afsluitend koopblok met vaste koopbalk (geen links naar andere producten). Draai als laatste (na translate_en.py)."""
import json
load = lambda f: json.load(open(f))
def save(f, d): json.dump(d, open(f, "w"), ensure_ascii=False, indent=2)

prod = load("templates__product.json")
S = prod["sections"]
det = S["main"]["blocks"]["product-details"]
for k in ("payicons", "trust"):
    det["blocks"].pop(k, None)
det["blocks"]["lovaire_trust"] = {"type": "lovaire-product-trust", "settings": {}, "blocks": {}}
order = [k for k in det["block_order"] if k not in ("payicons", "trust", "lovaire_trust")]
order.insert(order.index("buy") + 1, "lovaire_trust")
det["block_order"] = order

idx = load("templates__index.json")
belofte = json.loads(json.dumps(idx["sections"]["belofte"]))
belofte["settings"].update({"layout": "cards", "eyebrow": "OUR PROMISE", "heading": "Worry-free shopping at Lovaire",
                            "show_payment": False, "background": "#f6e7de", "padding_top": 72, "padding_bottom": 72})
S.pop("usps", None); S.pop("recommendations", None)
S["story"] = {"type": "lovaire-product-story", "settings": {}}
S["howto"] = {"type": "lovaire-product-howto", "settings": {}}
S["reviews"] = {"type": "lovaire-product-reviews", "settings": {}}
S["belofte"] = belofte
# Geen 'You may also like' meer: bezoekers blijven bij dit product
S.pop("more", None)
S["benefits"] = {"type": "lovaire-product-benefits", "settings": {}}
S["faq"] = {"type": "lovaire-product-faq", "settings": {"background": "#ffffff"}}
S["cta"] = {"type": "lovaire-product-cta", "settings": {}}
# Eigen koopbalk (in lovaire-product-cta) vervangt die van Horizon
S["main"]["settings"]["enable_sticky_add_to_cart"] = False
prod["order"] = ["main", "benefits", "story", "howto", "reviews", "belofte", "faq", "cta"]
save("templates__product.json", prod)

st = load("config__settings_data.json")
st["current"]["show_accelerated_checkout_buttons"] = False
save("config__settings_data.json", st)
print("productpagina", prod["order"])
