"""Zachte overgangen: zet per sectie blend_top/blend_bottom op basis van de buursecties.
Twee eigen secties naast elkaar lopen naar hun gemengde kleur; naast een Horizon-sectie loopt de eigen sectie
helemaal naar die kleur. Donkere buren (footer) worden overgeslagen. Draai als allerlaatste."""
import json, re, os
load = lambda f: json.load(open(f))
def save(f, d): json.dump(d, open(f, "w"), ensure_ascii=False, indent=2)
SCHEMES = {"scheme-1": "#ffffff", "scheme-2": "#8b6b4a", "scheme-3": "#111111", "scheme-4": "#f1e0d4",
           "scheme-5": "#f6e7de", "scheme-6": None, "scheme-7": None, "": "#ffffff", None: "#ffffff"}
BLENDABLE = {"lovaire-belofte", "lovaire-categories", "lovaire-favorieten", "lovaire-momenten", "lovaire-product-benefits",
             "lovaire-product-cta", "lovaire-product-faq", "lovaire-product-howto", "lovaire-product-reviews",
             "lovaire-product-story", "lovaire-reviews", "lovaire-statement", "lovaire-hero"}
def schema_default(t):
    f = f"sections__{t}.liquid"
    if not os.path.exists(f): return None
    m = re.search(r"{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema", open(f).read(), re.S)
    for x in json.loads(m.group(1))["settings"]:
        if x.get("id") == "background": return x.get("default")
def color(sec):
    st = sec.get("settings", {})
    if sec["type"] == "lovaire-hero": return "#fbf4ef"  # onderkant van het hero-verloop
    if sec["type"] in BLENDABLE: return (st.get("background") or schema_default(sec["type"]) or "#ffffff").lower()
    return SCHEMES.get(st.get("color_scheme"), "#ffffff")
def mix(a, b):
    a, b = a.lstrip("#"), b.lstrip("#")
    return "#" + "".join(f"{(int(a[i:i+2],16)+int(b[i:i+2],16))//2:02x}" for i in (0, 2, 4))
dark = lambda c: c is None or sum(int(c.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) < 200
for f in ["templates__index.json", "templates__product.json", "templates__collection.json", "templates__list-collections.json",
          "templates__page.json", "templates__page.contact.json"]:
    d = load(f); order = d["order"]; S = d["sections"]
    cols = [color(S[k]) for k in order]
    for i, k in enumerate(order):
        sec = S[k]
        if sec["type"] not in BLENDABLE: continue
        st = sec.setdefault("settings", {})
        st.pop("blend_top", None); st.pop("blend_bottom", None)
        for side, j in (("blend_top", i - 1), ("blend_bottom", i + 1)):
            if sec["type"] == "lovaire-hero" and side == "blend_top": continue
            if not 0 <= j < len(order): continue
            n = cols[j]
            if dark(n) or n == cols[i]: continue
            st[side] = mix(cols[i], n) if S[order[j]]["type"] in BLENDABLE else n
    save(f, d)
    print(f, [(k, S[k].get("settings", {}).get("blend_top"), S[k].get("settings", {}).get("blend_bottom")) for k in order if S[k]["type"] in BLENDABLE])
