"""Aankondigingsbalk zwart met witte tekst (scheme-announcement-black: #111111 / #ffffff), op alle pagina's."""
import json
def ann(text, link):
    return {"type": "_announcement", "settings": {"text": text, "link": link, "font": "var(--font-accent--family)",
            "font_size": "0.75rem", "letter_spacing": "loose", "case": "uppercase"}, "blocks": {}}
hg = {"type": "header", "name": "Header", "sections": {
  "header_announcements_pbXTDf": {"type": "header-announcements", "name": "t:names.announcement_bar",
    "blocks": {"a1": ann("Altijd gratis verzending", "shopify://pages/bestellingen-en-levering"),
               "a2": ann("Elke bestelling met tracking", "shopify://pages/verzendbeleid"),
               "a3": ann("Veilig afrekenen met iDEAL & Klarna", "")},
    "block_order": ["a1", "a2", "a3"],
    "settings": {"speed": 5, "section_width": "full-width", "color_scheme": "scheme-announcement-black",
                 "divider_width": 0, "padding-block-start": 10, "padding-block-end": 10}},
  "header_section": {"type": "header", "blocks": {
    "header-logo": {"type": "_header-logo", "static": True, "settings": {"hide_logo_on_home_page": False,
                    "padding-block-start": 0, "padding-block-end": 0}, "blocks": {}},
    "header-menu": {"type": "_header-menu", "static": True, "settings": {
      "menu": "main-menu", "type_font_primary_size": "var(--font-size--body-md)", "menu_font_style": "inverse",
      "type_font_primary_link": "secondary", "type_case_primary_link": "none", "menu_style": "featured_collections",
      "featured_products_aspect_ratio": "4 / 5", "featured_collections_aspect_ratio": "4 / 5", "image_border_radius": 16,
      "navigation_bar": False, "drawer_accordion": True, "drawer_accordion_expand_first": True, "drawer_dividers": True},
      "blocks": {}}},
    "settings": {"logo_position": "center", "menu_position": "left", "menu_row": "top",
      "customer_account_menu": "customer-account-main-menu", "show_search": True, "search_position": "right",
      "search_row": "top", "show_country": True, "country_selector_style": True, "show_language": False,
      "localization_font": "body", "localization_font_size": "0.875rem", "localization_position": "right",
      "localization_row": "top", "section_width": "page-width", "section_height": "standard",
      "enable_sticky_header": "always", "divider_width": 0, "divider_size": "full-width", "border_width": 0,
      "actions_display_style": "icon", "actions_font_size": "0.875rem", "actions_font": "body",
      "actions_text_case": "none", "color_scheme_top": "scheme-1", "color_scheme_bottom": "",
      "color_scheme_transparent": "scheme-6", "enable_transparent_header_home": False, "home_color_scheme": "default",
      "enable_transparent_header_product": False, "product_color_scheme": "default",
      "enable_transparent_header_collection": False, "collection_color_scheme": "default"}}},
  "order": ["header_announcements_pbXTDf", "header_section"]}
json.dump(hg, open("sections__header-group.json", "w"), ensure_ascii=False, indent=2)
print(json.dumps({"themeId": "gid://shopify/OnlineStoreTheme/209095164243", "files": [{"filename": "sections/header-group.json",
  "body": {"type": "TEXT", "value": json.dumps(hg, ensure_ascii=False, separators=(",", ":"))}}]}, ensure_ascii=False))
