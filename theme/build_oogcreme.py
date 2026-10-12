"""Dr.Melaxin oogcrème: template product.oogcreme in dezelfde opbouw als de andere productpagina's.
Gebruik: python3 build_oogcreme.py <live templates/product.json> <uitvoer product.oogcreme.json>
Teksten per product staan in metavelden (lovaire.benefits, highlight_*, how_to, faq); zie oogcreme_metafields.json."""
import json, sys, copy

src, out = sys.argv[1], sys.argv[2]
raw = open(src).read()
base = json.loads(raw[raw.index("{"):])
main = copy.deepcopy(base["sections"]["main"])

S = {
    "main": main,
    "benefits": {"type": "lovaire-product-benefits", "settings": {
        "eyebrow": "DE ESSENTIALS", "heading": "Alles wat het", "heading_italic": "voor je ogen doet"}},
    "story": {"type": "lovaire-product-story", "settings": {
        "eyebrow": "K-BEAUTY OOGVERZORGING", "heading": "Wakker ogen, ook als je", "heading_italic": "dat niet bent"}},
    "compare": {"type": "lovaire-compare", "settings": {
        "eyebrow": "WAAROM DEZE OOGCRÈME", "heading": "Camouflage én verzorging", "heading_italic": "in één potje",
        "col_1": "Calcium Oogcrème", "col_2": "Concealer", "col_3": "Gewone oogcrème",
        "rows": "Direct zichtbaar resultaat | ja | ja | nee\n"
                "Verzorgt de huid rond je ogen | ja | nee | ja\n"
                "Kruipt niet in fijne lijntjes | ja | nee | ja\n"
                "Eén product, één stap | ja | nee | nee",
        "button": "Bestel je oogcrème", "background": "#fbf8f5"}},
    "howto": {"type": "lovaire-product-howto", "settings": {
        "eyebrow": "ZO GEBRUIK JE HET", "heading": "30 seconden,", "heading_italic": "elke ochtend"}},
    "belofte": copy.deepcopy(base["sections"]["belofte"]),
    "faq": {"type": "lovaire-product-faq", "settings": {"background": "#ffffff"}},
    "cta": {"type": "lovaire-product-cta", "settings": {"eyebrow": "KLAAR VOOR EEN FRISSERE BLIK"}},
}
order = ["main", "benefits", "story", "compare", "howto", "belofte", "faq", "cta"]

# Zachte overgangen, zelfde regels als blend.py
DEFAULT_BG = {"lovaire-product-benefits": "#f8f1ec", "lovaire-product-story": "#ffffff", "lovaire-compare": "#fbf8f5",
              "lovaire-product-howto": "#f4ece4", "lovaire-belofte": "#f6e7de", "lovaire-product-faq": "#f8f1ec",
              "lovaire-product-cta": "#f4ece4"}
HEADER, FOOTER = "#ffffff", "#f6e7de"
def color(sec):
    if sec["type"] in DEFAULT_BG: return (sec["settings"].get("background") or DEFAULT_BG[sec["type"]]).lower()
    return "#ffffff"
def mix(a, b):
    a, b = a.lstrip("#"), b.lstrip("#")
    return "#" + "".join(f"{(int(a[i:i+2],16)+int(b[i:i+2],16))//2:02x}" for i in (0, 2, 4))
cols = [color(S[k]) for k in order]
for i, k in enumerate(order):
    sec = S[k]
    if sec["type"] not in DEFAULT_BG: continue
    st = sec["settings"]; st.pop("blend_top", None); st.pop("blend_bottom", None)
    for side, j in (("blend_top", i - 1), ("blend_bottom", i + 1)):
        n = HEADER if j < 0 else FOOTER if j >= len(order) else cols[j]
        if n == cols[i]: continue
        st[side] = mix(cols[i], n) if 0 <= j < len(order) and S[order[j]]["type"] in DEFAULT_BG else n

json.dump({"sections": S, "order": order}, open(out, "w"), ensure_ascii=False, indent=2)
print([(k, cols[i], S[k]["settings"].get("blend_top"), S[k]["settings"].get("blend_bottom")) for i, k in enumerate(order)])
