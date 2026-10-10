"""Maximaal drie kleuren in het fashion-thema: wit, zwart en crème (plus transparante varianten daarvan).
- Vaste kleuren in de CSS van de eigen secties worden naar het dichtstbijzijnde paletkleur gezet.
- Kleuren die in de editor zijn opgeslagen (achtergrond, overloop enz.) worden bij het tonen in Liquid omgezet,
  zodat ook bestaande instellingen in de templates binnen het palet vallen.
- config/settings_data.json: alle kleurschema's opnieuw opgebouwd uit de drie kleuren.
Schrijft naar out/ met de echte themapaden. Gebruik: python3 palette3.py"""
import json, os, re

WHITE, BLACK, CREAM = "#ffffff", "#111111", "#f5efe7"
INK = (17, 17, 17)
OUT = "out"

def rgb(h):
    h = h.lstrip("#")
    if len(h) in (3, 4): h = "".join(c * 2 for c in h)
    a = int(h[6:8], 16) / 255 if len(h) == 8 else None
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), a

def bright(c): return (299 * c[0] + 587 * c[1] + 114 * c[2]) / 1000

def fmt(c, a):
    if a is None or a >= 1: return "#%02x%02x%02x" % c
    return "rgba(%d,%d,%d,%s)" % (*c, ("%.2f" % a).rstrip("0").rstrip("."))

def map_color(c, a, prop):
    b = bright(c)
    is_text = prop in ("color", "fill", "stroke", "caret-color", "-webkit-text-stroke", "text-decoration-color")
    is_line = "border" in prop or "outline" in prop or prop in ("column-rule",)
    if c == (255, 255, 255) or b >= 252: return (255, 255, 255), a
    if b < 70: return INK, a
    if is_text:  # gedempte tekst: zwart met transparantie
        return (INK, (a or 1) * (0.65 if b < 200 else 0.45)) if b < 230 else ((245, 239, 231), a)
    if is_line and b < 245:  # lijnen: zachte zwarte lijn
        return INK, (a or 1) * 0.15
    if b < 120: return INK, a
    return (245, 239, 231), a

DECL = re.compile(r"([a-zA-Z-]+)\s*:\s*([^;{}]*)")
COLOR = re.compile(r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+\s*)?\)")

def fix_value(prop, val):
    def rep(m):
        s = m.group(0)
        if s.startswith("#"):
            c, a = rgb(s)
        else:
            n = [float(x) for x in re.findall(r"[\d.]+", s)]
            c, a = tuple(int(x) for x in n[:3]), (n[3] if len(n) > 3 else None)
        c2, a2 = map_color(c, a, prop.lower())
        if a2 == 0: return "rgba(%d,%d,%d,0)" % c2
        return fmt(c2, a2)
    return COLOR.sub(rep, val)

def fix_css(text):
    return DECL.sub(lambda m: m.group(1) + ": " + fix_value(m.group(1), m.group(2)) if COLOR.search(m.group(2)) else m.group(0), text)

def palette_hex(h):
    c, a = rgb(h)
    c2, _ = map_color(c, None, "background")
    return fmt(c2, None)

MAPPER = """{%- comment -%} Palet: wit, zwart, crème {%- endcomment -%}
{%- liquid
VARS
-%}
"""
ONE = """  assign {v} = {src} | append: ''
  if {v} != blank and {v} != 'rgba(0,0,0,0)'
    assign _br = {v} | color_brightness
    if _br >= 252
      assign {v} = '#ffffff'
    elsif _br < 120
      assign {v} = '#111111'
    else
      assign {v} = '#f5efe7'
    endif
  endif"""

def fix_liquid(src, scope="section"):
    m = re.search(r"{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}", src, re.S)
    body, schema_txt = (src[:m.start()], m.group(0)) if m else (src, "")
    schema = json.loads(m.group(1)) if m else {}
    sec_colors = [s["id"] for s in schema.get("settings", []) if s.get("type") == "color"]
    blk_colors = sorted({s["id"] for b in schema.get("blocks", []) for s in b.get("settings", []) if s.get("type") == "color"})
    # CSS-kleuren in de body (niet in Liquid-tags)
    parts = re.split(r"({{.*?}}|{%.*?%})", body, flags=re.S)
    body = "".join(p if p.startswith(("{{", "{%")) else fix_css(p) for p in parts)
    # Restjes (bv. naast een Liquid-variabele of als Liquid-standaardwaarde): dichtstbijzijnde paletkleur
    body = re.sub(r"#[0-9a-fA-F]{6}\b", lambda m: m.group(0) if m.group(0).lower() in (WHITE, BLACK, CREAM) else palette_hex(m.group(0)), body)
    # Opgeslagen kleuren omzetten bij het tonen
    pre = []
    for cid in sec_colors:
        v = "lvc_" + cid
        body = re.sub(r"%s\.settings\.%s\b" % (scope, cid), v, body)
        pre.append(ONE.format(v=v, src=scope + ".settings." + cid))
    if pre:
        body = MAPPER.replace("VARS", "\n".join(pre)) + body
    for cid in blk_colors:  # blokken: binnen de blokcontext
        v = "lvb_" + cid
        if "block.settings." + cid in body:
            first = body.index("block.settings." + cid)
            line_start = body.rfind("\n", 0, first) + 1
            body = re.sub(r"block\.settings\.%s\b" % cid, v, body)
            body = body[:line_start] + "{%- liquid\n" + ONE.format(v=v, src="block.settings." + cid).replace("lvb_" + cid + " = lvb_", "lvb_" + cid + " = block.settings.") + "\n-%}\n" + body[line_start:]
    # Standaardwaarden in het schema
    if m:
        def fix_defaults(o):
            if isinstance(o, dict):
                if o.get("type") == "color" and isinstance(o.get("default"), str) and o["default"].startswith("#"):
                    o["default"] = palette_hex(o["default"])
                for v in o.values(): fix_defaults(v)
            elif isinstance(o, list):
                for v in o: fix_defaults(v)
        fix_defaults(schema)
        schema_txt = "{% schema %}\n" + json.dumps(schema, ensure_ascii=False, indent=2) + "\n{% endschema %}\n"
    return body + schema_txt

def scheme(bg, fg_head, fg, border, inverse=False):
    """Eén kleurschema uit de drie paletkleuren."""
    ink, paper = (WHITE, BLACK) if inverse else (BLACK, WHITE)
    return {
        "background": bg, "foreground_heading": fg_head, "foreground": fg, "primary": ink, "primary_hover": ink,
        "border": border, "shadow": "#11111114",
        "primary_button_background": ink, "primary_button_text": paper, "primary_button_border": ink,
        "primary_button_hover_background": CREAM if inverse else "#111111d9", "primary_button_hover_text": BLACK if inverse else WHITE,
        "primary_button_hover_border": CREAM if inverse else "#111111d9",
        "secondary_button_background": "rgba(0,0,0,0)", "secondary_button_text": ink, "secondary_button_border": ink,
        "secondary_button_hover_background": ink, "secondary_button_hover_text": paper, "secondary_button_hover_border": ink,
        "input_background": WHITE, "input_text_color": BLACK, "input_border_color": border, "input_hover_background": WHITE,
        "variant_background_color": WHITE, "variant_text_color": BLACK, "variant_border_color": "#11111126",
        "variant_hover_background_color": CREAM, "variant_hover_text_color": BLACK, "variant_hover_border_color": BLACK,
        "selected_variant_background_color": BLACK, "selected_variant_text_color": WHITE, "selected_variant_border_color": BLACK,
        "selected_variant_hover_background_color": "#111111d9", "selected_variant_hover_text_color": WHITE,
        "selected_variant_hover_border_color": "#111111d9",
    }

def settings_data(path):
    raw = open(path).read()
    d = json.loads(raw[raw.index("{", raw.index("*/") + 2 if "*/" in raw else 0):])
    light_text = ("#111111", "#111111bf", "#11111126")
    S = {
        "scheme-1": scheme(WHITE, *light_text),
        "scheme-2": scheme(BLACK, WHITE, "#ffffffcc", "#ffffff40", inverse=True),
        "scheme-3": scheme(BLACK, WHITE, "#ffffffcc", "#ffffff26", inverse=True),
        "scheme-4": scheme(CREAM, *light_text),
        "scheme-5": scheme(CREAM, *light_text),
        "scheme-6": scheme("rgba(0,0,0,0)", WHITE, WHITE, "rgba(0,0,0,0)", inverse=True),
        "scheme-7": scheme("rgba(0,0,0,0)", *light_text),
        "scheme-warm-beige": scheme(CREAM, *light_text),
        "scheme-announcement-black": scheme(BLACK, WHITE, WHITE, "#ffffff26", inverse=True),
    }
    for k, v in d["current"]["color_schemes"].items():
        v["settings"] = S.get(k, scheme(WHITE, *light_text))
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n"

if __name__ == "__main__":
    import glob, sys
    os.makedirs(OUT + "/sections", exist_ok=True); os.makedirs(OUT + "/blocks", exist_ok=True)
    os.makedirs(OUT + "/snippets", exist_ok=True); os.makedirs(OUT + "/config", exist_ok=True)
    files = sorted(glob.glob("sections__lvs-*.liquid") + glob.glob("sections__lovaire-*.liquid") + ["blocks__lovaire-product-trust.liquid", "blocks__lovaire-rating.liquid"])
    files = [f for f in files if "reviews" not in f]  # reviews staan uit; theme-versie wijkt af van lokaal
    for f in files:
        out = OUT + "/" + f.replace("__", "/", 1)
        open(out, "w").write(fix_liquid(open(f).read(), "block" if f.startswith("blocks__") else "section"))
        print(out)
    if os.path.exists("fashion__config__settings_data.json"):
        open(OUT + "/config/settings_data.json", "w").write(settings_data("fashion__config__settings_data.json"))
        print(OUT + "/config/settings_data.json")
