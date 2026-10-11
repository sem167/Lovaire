// Lovaire Period Heating Wrap – 4 Nederlandse + 4 Engelse foto-advertenties (4:5, 1080x1350) voor Meta.
// Elke advertentie: duidelijk probleem → oplossing. Bronfoto's (1000x1250) in ads/bron/.
// Draai: node ads/make_wrap_ads.js  -> ads/output/
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const BRON = path.join(__dirname, 'bron'), OUT = path.join(__dirname, 'output');
fs.mkdirSync(OUT, { recursive: true });

const C = { cream: '#f6f1eb', black: '#111111', white: '#ffffff', rose: '#b5776a', soft: 'rgba(17,17,17,.65)' };

// Uitsnede (x, y, w, h in bronpixels) van een bronfoto, gevuld in een vak van W x H.
const crop = (file, [x, y, w, h], W, H, extra = '') => {
  const s = Math.max(W / w, H / h);
  return `<div style="position:absolute;${extra};width:${W}px;height:${H}px;background:url('file://${path.join(BRON, file)}') no-repeat;background-size:${1000 * s}px ${1250 * s}px;background-position:${-x * s - (w * s - W) / 2}px ${-y * s - (h * s - H) / 2}px"></div>`;
};

// Probleem → oplossing-blok
const ps = (t, dark) => {
  const fg = dark ? C.white : C.black;
  const row = (icon, bg, col, label, labelCol, text) => `
  <div style="display:flex;align-items:center;gap:22px">
    <span style="flex:none;width:62px;height:62px;border-radius:50%;background:${bg};color:${col};display:grid;place-items:center;font-size:32px;font-weight:800">${icon}</span>
    <div><div style="font-size:22px;letter-spacing:.2em;font-weight:700;color:${labelCol}">${label}</div>
    <div style="font-size:38px;font-weight:700;color:${fg};line-height:1.2">${text}</div></div>
  </div>`;
  return `<div style="display:flex;flex-direction:column;gap:20px;text-align:left;max-width:920px;margin:0 auto">
    ${row('✕', C.rose, C.white, t.pLabel, C.rose, t.problem)}
    ${row('✓', dark ? C.white : C.black, dark ? C.black : C.white, t.sLabel, dark ? 'rgba(255,255,255,.7)' : C.soft, t.solution)}
  </div>`;
};

const CSS = `*{box-sizing:border-box;margin:0}body{font-family:Inter,'Noto Color Emoji',sans-serif;-webkit-font-smoothing:antialiased}
.ad{position:relative;overflow:hidden}
.eyebrow{font-size:26px;letter-spacing:.42em;font-weight:600;color:${C.rose}}
h1{font-family:'Inter Display',Inter,'Noto Color Emoji',sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.04}
.chip{display:inline-block;background:${C.white};color:${C.black};font-weight:600;border-radius:999px;box-shadow:0 6px 18px rgba(17,17,17,.10)}
.chip.d{background:${C.black};color:${C.white}}
.cta{display:inline-block;background:${C.black};color:${C.white};font-size:26px;letter-spacing:.18em;font-weight:700;text-transform:uppercase;padding:24px 56px}
.c{text-align:center}`;

const R = 'style="color:#b5776a"';
const T = {
  nl: { pLabel: 'HET PROBLEEM', sLabel: 'DE OPLOSSING', cta: 'Shop nu',
    a1: { h: 'Buikkrampen tijdens je menstruatie?', problem: 'Elke maand krampen in je buik en onderrug', solution: 'Zachte warmte die helpt tegen je buikkrampen' },
    a2: { h: `POV: je bent ongesteld en je kruik is <span ${R}>alwéér koud</span>`, problem: 'Je kruik koelt af en glijdt weg', solution: 'Blijft warm, blijft zitten en helpt tegen krampen' },
    a3: { e: 'JE MAANDELIJKSE ME-TIME', h: `Krampen? Even liggen.<br><span ${R}>Wrap om.</span>`, problem: 'Buikkrampen die je avond verpesten', solution: 'Handsfree warmte die helpt tegen buikkrampen' },
    a4: { h: 'Elke maand weer krampen?', problem: 'Pijnlijke buikkrampen tijdens je menstruatie', solution: 'De Lovaire Heating Wrap: warmte die helpt, in seconden', price: '€ 49,95 · Gratis verzending', gift: '🎁 2e voor een vriendin: −€ 14,95' } },
  en: { pLabel: 'THE PROBLEM', sLabel: 'THE SOLUTION', cta: 'Shop now',
    a1: { h: 'Period cramps again?', problem: 'Monthly cramps in your belly and lower back', solution: 'Soothing warmth that helps reduce your cramps' },
    a2: { h: `POV: you’re on your period and your hot water bottle is <span ${R}>cold again</span>`, problem: 'Hot water bottles cool down and slip away', solution: 'Stays warm, stays put and helps reduce cramps' },
    a3: { e: 'YOUR MONTHLY ME-TIME', h: `Cramps? Lie down.<br><span ${R}>Wrap it on.</span>`, problem: 'Period cramps that ruin your evening', solution: 'Hands-free warmth that helps reduce cramps' },
    a4: { h: 'Cramps every month?', problem: 'Painful belly cramps during your period', solution: 'The Lovaire Heating Wrap: warmth that helps, in seconds', price: '€49.95 · Free shipping', gift: '🎁 2nd for a friend: save €14.95' } },
};

const ADS = [];
for (const lang of ['nl', 'en']) {
  const t = T[lang];
  ADS.push({ name: `${lang}-1-probleem-oplossing`, body: () => `
    ${crop('wrap-model-bank.jpg', [0, 60, 1000, 760], 1080, 740, 'top:0;left:0')}
    <div style="position:absolute;top:40px;left:0;right:0" class="c"><span class="eyebrow" style="color:#111">LOVAIRE</span></div>
    <div style="position:absolute;left:0;right:0;top:700px;bottom:0;background:${C.cream};padding:64px 60px 0" class="c">
      <h1 style="font-size:64px;margin:0 0 40px;color:${C.black}">${t.a1.h}</h1>
      ${ps({ ...t, ...t.a1 })}
      <div style="margin-top:48px"><span class="cta">${t.cta}</span></div>
    </div>` });
  ADS.push({ name: `${lang}-2-koude-kruik`, body: () => `
    ${crop('wrap-model-bank.jpg', [156, 0, 688, 860], 1080, 1350, 'top:0;left:0')}
    <div style="position:absolute;left:0;right:0;top:0;height:470px;background:linear-gradient(180deg,rgba(245,239,231,.97) 60%,rgba(245,239,231,0))"></div>
    <div style="position:absolute;left:60px;right:60px;top:60px" class="c"><h1 style="font-size:62px;color:${C.black}">${t.a2.h}</h1></div>
    <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(17,17,17,.93);padding:44px 60px 50px">${ps({ ...t, ...t.a2 }, true)}</div>` });
  ADS.push({ name: `${lang}-3-me-time`, body: () => `
    <div style="position:absolute;inset:0;background:${C.cream}"></div>
    <div style="position:absolute;left:60px;right:60px;top:54px" class="c">
      <div class="eyebrow">${t.a3.e}</div>
      <h1 style="font-size:64px;margin:16px 0 30px;color:${C.black}">${t.a3.h}</h1>
      ${ps({ ...t, ...t.a3 })}
    </div>
    ${crop('wrap-liggend.jpg', [0, 182, 1000, 816], 1080, 820, 'bottom:0;left:0')}` });
  ADS.push({ name: `${lang}-4-product-prijs`, body: () => `
    <div style="position:absolute;inset:0;background:${C.cream}"></div>
    <div style="position:absolute;left:60px;right:60px;top:54px" class="c">
      <div class="eyebrow">LOVAIRE</div>
      <h1 style="font-size:66px;margin:14px 0 30px;color:${C.black}">${t.a4.h}</h1>
      ${ps({ ...t, ...t.a4 })}
    </div>
    ${crop('wrap-product.jpg', [80, 430, 840, 760], 820, 660, 'bottom:120px;left:130px')}
    <div style="position:absolute;left:0;right:0;bottom:48px" class="c">
      <span class="chip d" style="font-size:27px;padding:18px 28px">${t.a4.price}</span>
      <span class="chip" style="font-size:27px;padding:18px 28px;margin-left:10px">${t.a4.gift}</span>
    </div>` });
}

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const a of ADS) {
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}body{width:1080px;height:1350px}</style></head><body><div class="ad" style="width:1080px;height:1350px">${a.body()}</div></body></html>`;
    const tmp = path.join(OUT, a.name + '.html'); fs.writeFileSync(tmp, html);
    await p.goto('file://' + tmp); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(OUT, `lovaire-wrap-${a.name}.png`) });
    fs.unlinkSync(tmp); console.log('gemaakt:', a.name);
  }
  await b.close();
})();
