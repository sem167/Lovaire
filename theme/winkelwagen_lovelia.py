import json, re, sys
def sub(path, old, new, count=1):
    s = open(path).read()
    assert s.count(old) == count, (path, old[:60], s.count(old))
    open(path, 'w').write(s.replace(old, new))

# 1) Settings: winkelwagen als lade (drawer) i.p.v. aparte pagina
s = open('config__settings_data.json').read()
assert s.count('"cart_type": "page"') == 1
open('config__settings_data.json', 'w').write(s.replace('"cart_type": "page"', '"cart_type": "drawer"'))

# 2) Lade: kop zonder teller, groene verzendbalk, retourregel boven de knop, betaalicoontjes eronder
H = 'snippets__header-actions.liquid'
sub(H, """                  {{ 'content.cart_title' | t }}
                  {% render 'cart-bubble' %}
                </h2>""", """                  {{ 'content.cart_title' | t }}
                </h2>""")
sub(H, """              <scroll-hint
                class="cart-drawer__content\"""", """              <div class="lv-cart-ship">Gratis verzending! (incl. Track &amp; Trace)</div>

              <scroll-hint
                class="cart-drawer__content\"""")
sub(H, """                  {% render 'cart-summary', section_id: section.id %}
                </div>""", """                  <p class="lv-cart-guarantee"><span aria-hidden="true">🔒</span> 30 dagen retourrecht</p>
                  {% render 'cart-summary', section_id: section.id %}
                  <ul class="lv-cart-pay" role="list" aria-label="Betaalmethoden">
                    {%- for type in shop.enabled_payment_types -%}
                      <li>{{ type | payment_type_svg_tag }}</li>
                    {%- endfor -%}
                  </ul>
                </div>""")
sub(H, "{% endstylesheet %}", """
  /* Lovaire – winkelwagen-lade in Lovelia-stijl */
  .cart-drawer__header { justify-content: center; position: sticky; border-bottom: 1px solid #1f3d2b; }
  .cart-drawer__heading { font-family: var(--font-body--family); font-weight: 800; font-size: 24px;
    letter-spacing: .02em; text-transform: none; color: #111; }
  .cart-drawer__header .cart-drawer__close-button { position: absolute; right: 16px; top: 50%; translate: 0 -50%;
    width: 36px; height: 36px; border-radius: 8px; background: #f2f2f2; }
  .cart-drawer--empty .cart-drawer__header .cart-drawer__close-button { position: static; translate: none; }
  .lv-cart-ship { padding: 10px 16px; background: #dbe9e4; border-bottom: 1px solid #1f3d2b; text-align: center;
    font-family: var(--font-body--family); font-size: 14px; font-weight: 700; letter-spacing: .04em; color: #111; }
  .cart-drawer__items { padding-block-start: 20px; }
  .cart-drawer__items .cart-items__price { display: none; }
  .cart-drawer__summary { background: #f7f7f7; mask-image: none; border-top: 1px solid #e6e6e6; gap: 14px; }
  .cart-drawer__summary .cart-totals__container { display: none; }
  .cart-drawer__summary .cart__summary-totals:not(:has(.cart__subtotal-container:empty)) { border: 0; padding-block-start: 0; }
  .lv-cart-guarantee { width: 100%; margin: 0; padding: 12px; border-radius: 10px; background: #f0f7f1; text-align: center;
    font-family: var(--font-body--family); font-size: 16px; font-weight: 700; letter-spacing: .03em; color: #2e7d32; }
  .cart-drawer__summary .cart__ctas { width: 100%; }
  .cart-drawer__summary .cart__checkout-button { width: 100%; min-height: 56px; border-radius: 8px; border: 0;
    background: #2b2b2b; color: #fff; font-size: 17px; font-weight: 700; letter-spacing: .06em; text-transform: none; }
  .cart-drawer__summary .cart__checkout-button:hover { background: #111; }
  .lv-cart-pay { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; margin: 0; padding: 0; list-style: none; }
  .lv-cart-pay svg { display: block; width: 38px; height: 24px; }
{% endstylesheet %}""")

# 3) Knop: 'Veilig afrekenen • €34,95'
sub('snippets__cart-summary.liquid', """      {{ 'content.checkout' | t }}
    </span>""", """      {{ 'content.checkout' | t }} • {{ cart.total_price | money }}
    </span>""")

# 4) Per product: '(Je bespaart €…)' in het groen
sub('snippets__cart-products.liquid', """                      {% endif %}
                    </div>
                  </div>
                </td>""", """                      {% endif %}
                    </div>
                    {%- liquid
                      assign lv_ref = item.variant.compare_at_price | default: 0
                      if lv_ref < item.original_price
                        assign lv_ref = item.original_price
                      endif
                      assign lv_save = lv_ref | minus: item.final_price | times: item.quantity
                    -%}
                    {%- if lv_save > 0 -%}
                      <p class="lv-cart-save">(Je bespaart {{ lv_save | money }})</p>
                    {%- endif -%}
                  </div>
                </td>""")
sub('snippets__cart-products.liquid', "{% stylesheet %}", """{% stylesheet %}
  .lv-cart-save { margin: 4px 0 0; font-size: 16px; font-weight: 700; letter-spacing: .03em; color: #2e9b3a; }
  .cart-items .compare-at-price { color: #9a9a9a; }
  .cart-items .quantity-selector { border: 1px solid #cfcfcf; border-radius: 6px; }
""")
print('ok')
