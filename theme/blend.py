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
# Header en footer zonder lijnen; footer in zachte blush zodat de pagina erin kan overlopen
hg = load("sections__header-group.json")
for k, sec in hg["sections"].items():
    st = sec.setdefault("settings", {})
    if sec["type"] == "header-announcements": st["color_scheme"] = "scheme-1"
    if sec["type"] == "header": st["divider_width"] = 0; st["border_width"] = 0
save("sections__header-group.json", hg)
fg = load("sections__footer-group.json")
for k, sec in fg["sections"].items():
    st = sec.setdefault("settings", {})
    st["color_scheme"] = "scheme-5"
    if "divider_thickness" in st: st["divider_thickness"] = 0
save("sections__footer-group.json", fg)
HEADER = "#ffffff"
FOOTER = SCHEMES["scheme-5"]

for f in ["templates__index.json", "templates__product.json", "templates__collection.json", "templates__list-collections.json",
          "templates__page.json", "templates__page.contact.json"]:
    d = load(f); S = d["sections"]
    for k in [k for k in S if k.startswith("fade_")]: S.pop(k)
    order = [k for k in d["order"] if not k.startswith("fade_")]
    # Twee niet-mengbare buren (of header/footer) met verschillende kleur: zet er een overloop-sectie tussen
    cols0 = [color(S[k]) for k in order]
    seq = [("_header", HEADER, False)] + [(k, c, S[k]["type"] in BLENDABLE) for k, c in zip(order, cols0)] + [("_footer", FOOTER, False)]
    new = []
    for (ka, ca, ba), (kb, cb, bb) in zip(seq, seq[1:]):
        if ka != "_header": new.append(ka)
        if not ba and not bb and ca != cb and not dark(ca) and not dark(cb):
            fk = f"fade_{len(new)}"
            S[fk] = {"type": "lovaire-fade", "settings": {"from": ca, "to": cb, "height": 70 if ka == "_header" else 120}}
            new.append(fk)
    d["order"] = order = new
    cols = [S[k]["settings"]["to"] if S[k]["type"] == "lovaire-fade" else color(S[k]) for k in order]
    for i, k in enumerate(order):
        sec = S[k]
        if sec["type"] not in BLENDABLE: continue
        st = sec.setdefault("settings", {})
        st.pop("blend_top", None); st.pop("blend_bottom", None)
        for side, j in (("blend_top", i - 1), ("blend_bottom", i + 1)):
            if j < 0: n = HEADER
            elif j >= len(order): n = FOOTER
            else: n = cols[j]
            if dark(n) or n == cols[i]: continue
            st[side] = mix(cols[i], n) if 0 <= j < len(order) and S[order[j]]["type"] in BLENDABLE else n
    for sec in S.values():
        for b in sec.get("blocks", {}).values():
            if b.get("type") == "accordion" and f == "templates__index.json": b["settings"]["dividers"] = False
    save(f, d)
    print(f, order)
    print(f, [(k, S[k].get("settings", {}).get("blend_top"), S[k].get("settings", {}).get("blend_bottom")) for k in order if S[k]["type"] in BLENDABLE])
