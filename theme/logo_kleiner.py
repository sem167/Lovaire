"""Bouwt config/settings_data.json van het live thema na (identiek aan checksum 3e919dda…) met kleiner logo."""
import json, sys

def scheme(bg, fh, fg, pr, prh, border, pbb, pbt, pbhb, pbhb_border=None, sec="#111111", sec_hover_text="#ffffff", inp_border=None):
    return None  # niet gebruikt

def base(bg, fh, fg, primary, primary_hover, border, btn_bg, btn_text, btn_hover_bg, btn_hover_text, sec_text, sec_hover_bg, sec_hover_text):
    return {"settings": {
        "background": bg, "foreground_heading": fh, "foreground": fg, "primary": primary, "primary_hover": primary_hover,
        "border": border, "shadow": "#00000014",
        "primary_button_background": btn_bg, "primary_button_text": btn_text, "primary_button_border": btn_bg,
        "primary_button_hover_background": btn_hover_bg, "primary_button_hover_text": btn_hover_text,
        "primary_button_hover_border": btn_hover_bg,
        "secondary_button_background": "rgba(0,0,0,0)", "secondary_button_text": sec_text, "secondary_button_border": sec_text,
        "secondary_button_hover_background": sec_hover_bg, "secondary_button_hover_text": sec_hover_text,
        "secondary_button_hover_border": sec_hover_bg,
        "input_background": "#ffffff", "input_text_color": "#111111", "input_border_color": border,
        "input_hover_background": "#ffffff",
        "variant_background_color": "#ffffff", "variant_text_color": "#111111", "variant_border_color": border,
        "variant_hover_background_color": "#f6e7de", "variant_hover_text_color": "#111111",
        "variant_hover_border_color": "#111111",
        "selected_variant_background_color": "#111111", "selected_variant_text_color": "#ffffff",
        "selected_variant_border_color": "#111111", "selected_variant_hover_background_color": "#333333",
        "selected_variant_hover_text_color": "#ffffff", "selected_variant_hover_border_color": "#333333"}}

dark_on_light = dict(btn_bg="#111111", btn_text="#ffffff", btn_hover_bg="#333333", btn_hover_text="#ffffff",
                     sec_text="#111111", sec_hover_bg="#111111", sec_hover_text="#ffffff")
schemes = {
    "scheme-1": base("#ffffff", "#111111", "#5a5a5a", "#8b6b4a", "#111111", "#ddd2c3", **dark_on_light),
    "scheme-2": base("#8b6b4a", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff40", "#ffffff", "#111111", "#111111", "#ffffff", "#ffffff", "#ffffff", "#111111"),
    "scheme-3": base("#111111", "#ffffff", "#e9dfd1cc", "#f1e0d4", "#ffffff", "#ffffff26", "#ffffff", "#111111", "#333333", "#ffffff", "#ffffff", "#ffffff", "#111111"),
    "scheme-4": base("#f1e0d4", "#111111", "#5a5a5a", "#8b6b4a", "#111111", "#11111121", **dark_on_light),
    "scheme-5": base("#f6e7de", "#111111", "#5a5a5a", "#8b6b4a", "#111111", "#11111121", **dark_on_light),
    "scheme-6": base("rgba(0,0,0,0)", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "rgba(0,0,0,0)", "#ffffff", "#111111", "#8b6b4a", "#ffffff", "#ffffff", "#ffffff", "#111111"),
    "scheme-7": base("rgba(0,0,0,0)", "#111111", "#5a5a5a", "#8b6b4a", "#111111", "#ddd2c3", **dark_on_light),
    "scheme-warm-beige": base("#f8f5f0", "#111111", "#5a5a5a", "#111111", "#111111", "#11111126", **dark_on_light),
    "scheme-announcement-black": base("#111111", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff26", "#ffffff", "#111111", "#333333", "#ffffff", "#ffffff", "#ffffff", "#111111"),
}

def build(logo_h, logo_h_mobile):
    return {"current": {
        "logo": "shopify://shop_images/Lovaire.nl.png", "logo_height": logo_h, "logo_height_mobile": logo_h_mobile,
        "type_body_font": "montserrat_n4", "type_subheading_font": "montserrat_n5", "type_heading_font": "montserrat_n4",
        "type_accent_font": "montserrat_n5", "type_size_paragraph": "15", "type_size_h2": "40", "type_font_h3": "heading",
        "type_size_h3": "26", "type_font_h4": "accent", "type_size_h4": "15", "type_letter_spacing_h4": "heading-loose",
        "type_case_h4": "uppercase", "type_size_h5": "16", "type_font_h6": "accent", "type_size_h6": "12",
        "type_line_height_h6": "display-normal", "type_letter_spacing_h6": "heading-loose", "type_case_h6": "uppercase",
        "badge_corner_radius": 4, "badge_sale_color_scheme": "scheme-2", "badge_sold_out_color_scheme": "scheme-4",
        "badge_font_family": "accent", "badge_text_transform": "uppercase", "button_border_radius_primary": 0,
        "secondary_button_border_width": 1, "button_border_radius_secondary": 0, "cart_type": "page",
        "auto_open_cart_drawer": True, "show_accelerated_checkout_buttons": False, "inputs_border_radius": 0,
        "type_preset": "paragraph", "popover_border": "none", "currency_code_enabled_product_pages": False,
        "currency_code_enabled_product_cards": False, "variant_swatch_radius": 40, "variant_button_radius": 40,
        "variant_button_width": "default-width-buttons",
        "sections": {"password-footer": {"type": "password-footer", "settings": {"color_scheme": ""}}},
        "content_for_index": [],
        "blocks": {
            "11532412952436166569": {"type": "shopify://apps/loox-reviews/blocks/loox-inject/5c3b337f-fd14-4df5-b1d6-80ec13e6e28e", "disabled": False, "settings": {}},
            "15557474716127144420": {"type": "shopify://apps/kaching-bundles/blocks/app-embed-block/6c637362-a106-4a32-94ac-94dcfd68cdb8", "disabled": False, "settings": {}},
            "14952540001915115444": {"type": "shopify://apps/upcart-cart-drawer/blocks/app-embed/af3da5fb-f5f7-40ec-8273-41bf50059d4b", "disabled": False, "settings": {}}},
        "color_schemes": schemes}}

if __name__ == "__main__":
    import hashlib
    header = ("/*\n * ------------------------------------------------------------\n * IMPORTANT: The contents of this file are auto-generated.\n *\n"
              " * This file may be updated by the Shopify admin theme editor\n * or related systems. Please exercise caution as any changes\n"
              " * made to this file may be overwritten.\n * ------------------------------------------------------------\n */\n")
    orig = header + json.dumps(build(58, 64), ensure_ascii=False, indent=2) + "\n"
    print("md5 origineel nagebouwd:", hashlib.md5(orig.encode()).hexdigest())
    new = json.dumps(build(int(sys.argv[1]), int(sys.argv[2])), ensure_ascii=False, separators=(",", ":"))
    print(json.dumps({"themeId": "gid://shopify/OnlineStoreTheme/209095164243",
                      "files": [{"filename": "config/settings_data.json", "body": {"type": "TEXT", "value": new}}]}, ensure_ascii=False))
