// Maakt 4:5 foto-advertenties (1080x1350) van de Heating Wrap.
// Zet de foto's in ads/input/ met deze namen en draai: node ads/make_ads.js
//   hero.jpg, lifestyle.jpg, sofa.jpg, vs.jpg, product.jpg   (ontbrekende worden overgeslagen)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const IN = path.join(__dirname, 'input'), OUT = path.join(__dirname, 'output');
const ADS = [
  { file: 'lifestyle.jpg', name: '1-bank', pos: 'top', title: 'Helpt tegen buikkrampen tijdens je menstruatie 🤍', sub: 'Warm in seconden · handsfree · blijft de hele avond warm' },
  { file: 'sofa.jpg', name: '2-metime', pos: 'bottom', title: 'Krampen? Wrap om, knopje aan.', sub: 'Helpt tegen buikkrampen tijdens je menstruatie' },
  { file: 'vs.jpg', name: '3-kruik', pos: 'top', title: 'Kruik ❌  Wrap ✅', sub: 'Helpt tegen buikkrampen tijdens je menstruatie – zonder koud worden' },
  { file: 'hero.jpg', name: '4-cadeau', pos: 'bottom', badge: '🎁 1 voor jou + 1 cadeau', title: 'Het cadeau dat écht helpt', sub: 'Helpt tegen buikkrampen tijdens je menstruatie · 2 stuks € 84,95' },
  { file: 'product.jpg', name: '5-product', pos: 'bottom', title: 'Helpt tegen buikkrampen tijdens je menstruatie', sub: 'Lovaire Period Heating Wrap · € 49,95 · gratis verzending' },
];
const html = (img, a) => `<!doctype html><html><head><style>
*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;font-family:Montserrat,Arial,sans-serif;overflow:hidden}
.ad{position:relative;width:1080px;height:1350px;background:#f5efe7}
.ad img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;left:0;right:0;height:62%;${a.pos==='top'?'top:0;background:linear-gradient(180deg,rgba(17,17,17,.62),rgba(17,17,17,0))':'bottom:0;background:linear-gradient(0deg,rgba(17,17,17,.68),rgba(17,17,17,0))'}}
.txt{position:absolute;left:70px;right:70px;${a.pos==='top'?'top:80px':'bottom:170px'};color:#fff;text-align:center}
.logo{position:absolute;left:0;right:0;${a.pos==='top'?'bottom:60px':'top:60px'};text-align:center;color:#fff;font-size:30px;letter-spacing:.42em;font-weight:600;text-shadow:0 2px 12px rgba(0,0,0,.35)}
h1{font-size:74px;line-height:1.05;font-weight:700;letter-spacing:-.01em;margin-bottom:24px;text-shadow:0 2px 18px rgba(0,0,0,.25)}
p{font-size:34px;line-height:1.35;opacity:.95}
.badge{display:inline-block;background:#fff;color:#111;font-size:30px;font-weight:700;letter-spacing:.06em;padding:14px 28px;margin-bottom:28px}
.cta{position:absolute;left:50%;transform:translateX(-50%);${a.pos==='top'?'top:auto;bottom:130px':'bottom:60px'};background:#fff;color:#111;font-size:28px;letter-spacing:.2em;text-transform:uppercase;padding:22px 54px;font-weight:600}
</style></head><body><div class="ad"><img src="${img}"><div class="shade"></div>
<div class="txt">${a.badge?`<div class="badge">${a.badge}</div>`:''}<h1>${a.title}</h1><p>${a.sub}</p></div>
<div class="logo">LOVAIRE</div><div class="cta">Shop nu</div></div></body></html>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const a of ADS) {
    const f = path.join(IN, a.file); if (!fs.existsSync(f)) { console.log('overgeslagen (geen foto):', a.file); continue; }
    const tmp = path.join(OUT, a.name + ".html"); fs.writeFileSync(tmp, html("file://" + f, { ...a, sub: a.sub.replace(/€ /g, "€&nbsp;"), title: a.title.replace(/€ /g, "€&nbsp;") }));
    await p.goto('file://' + tmp); await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(OUT, `lovaire-wrap-${a.name}.png`) }); fs.unlinkSync(tmp);
    console.log('gemaakt:', `lovaire-wrap-${a.name}.png`);
  }
  await b.close();
})();
