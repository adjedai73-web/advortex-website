# -*- coding: utf-8 -*-
"""Assemble calculateur.html from packs.html shell + loss calculator widget."""
import re

src = open('packs.html', encoding='utf-8').read()

def section(s, start, end):
    i = s.index(start)
    j = s.index(end, i) + len(end)
    return s[i:j]

head = src[:src.index('<body>')].rstrip() + '\n</head>'
nav = section(src, '<nav id="nav">', '</nav>')
footer = section(src, '<footer>', '</footer>')
tail = src[src.index('<script>'):]

head = re.sub(r'<title>.*?</title>',
  '<title>Combien vous perdez chaque mois ? — Advortex</title>', head, count=1)
head = head.replace(
  'content="Advortex est une agence de marketing digital à Alger. Gestion Facebook, Instagram, TikTok, production vidéo et stratégie de contenu pour restaurants, salons et entreprises.">',
  'content="Calculez en 10 secondes combien votre business perd chaque mois sans marketing professionnel.">')
head = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
  r'\1https://advortex-agency.vercel.app/calculateur.html\2', head)

CALC_CSS = """<style>
.calc-box{max-width:680px;margin:0 auto;background:var(--bg2);border:1px solid var(--line);border-radius:24px;padding:44px}
.calc-field{margin-bottom:30px}
.calc-field label{display:flex;justify-content:space-between;align-items:baseline;font-size:15.5px;font-weight:600;margin-bottom:6px}
.calc-field label .val{color:#fff;font-weight:800;font-size:17px;white-space:nowrap}
.calc-field small{display:block;color:var(--muted);font-size:13px;margin-bottom:12px}
input[type=range]{width:100%;-webkit-appearance:none;appearance:none;height:6px;border-radius:3px;background:rgba(255,255,255,.15);outline:none;cursor:pointer}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:26px;height:26px;border-radius:50%;background:#fff;border:none;box-shadow:0 0 0 6px rgba(255,255,255,.12);cursor:pointer}
input[type=range]::-moz-range-thumb{width:26px;height:26px;border-radius:50%;background:#fff;border:none;box-shadow:0 0 0 6px rgba(255,255,255,.12);cursor:pointer}
.calc-result{text-align:center;background:rgba(255,80,80,.06);border:1px solid rgba(255,107,107,.35);border-radius:20px;padding:34px 20px;margin:8px 0 26px}
.calc-result .lbl{color:var(--muted);font-size:15px;margin-bottom:8px}
.calc-result .big{font-size:clamp(38px,7vw,58px);font-weight:800;color:#ff7b7b;letter-spacing:-1px;line-height:1.1}
.calc-result .per{color:var(--muted);font-size:15px;margin-top:8px}
.calc-result .per b{color:#fff}
.calc-punch{text-align:center;font-size:17px;font-weight:600;margin:0 0 26px}
.calc-note{text-align:center;color:var(--muted);font-size:13.5px;margin:20px 0 0}
@media(max-width:560px){.calc-box{padding:30px 22px}}
</style>
</head>"""
head = head.replace('</head>', CALC_CSS, 1)

body = """<header class="page-hero" id="top">
  <div class="wrap">
    <span class="eyebrow rv">Calculateur</span>
    <h1 class="rv">Combien vous perdez<br>chaque mois ?</h1>
    <p class="sub rv">Bla marketing pro, floussek rahoum yrouhou l concurrent. 7sebha f 10 secondes.</p>
  </div>
</header>

<section id="calculateur" style="padding-top:34px">
  <div class="wrap">
    <div class="calc-box rv">
      <div class="calc-field">
        <label>Clients potentiels par mois <span class="val" id="vClients">100</span></label>
        <small>Des gens qui voient votre business mais n\\u2019ach\\u00e8tent pas (encore).</small>
        <input type="range" id="rClients" min="10" max="500" step="10" value="100">
      </div>
      <div class="calc-field">
        <label>Panier moyen <span class="val" id="vPanier">5 000 DZD</span></label>
        <small>Combien d\\u00e9pense un client en moyenne chez vous, en DZD.</small>
        <input type="range" id="rPanier" min="1000" max="100000" step="1000" value="5000">
      </div>
      <div class="calc-field">
        <label>Clients r\\u00e9cup\\u00e9rables <span class="val" id="vTaux">15 %</span></label>
        <small>Estimation prudente : avec du bon contenu, cette part peut devenir cliente.</small>
        <input type="range" id="rTaux" min="5" max="30" step="1" value="15">
      </div>
      <div class="calc-result">
        <div class="lbl">Vous perdez environ</div>
        <div class="big" id="rBig">750 000 DZD</div>
        <div class="per">par mois &mdash; soit <b id="rYear">9 000 000 DZD</b> par an</div>
      </div>
      <p class="calc-punch">Hadi machi khsara 3adiya &mdash; hadi floussek li rahi trouh l concurrent.</p>
      <a class="btn btn-wa" id="calcGo" target="_blank" rel="noopener" href="#" style="width:100%;justify-content:center">Je veux r\\u00e9cup\\u00e9rer cet argent</a>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:14px">
        <a class="btn btn-ghost" href="quiz.html" style="font-size:14px;padding:12px 22px">Faire le quiz</a>
        <a class="btn btn-ghost" href="booking.html" style="font-size:14px;padding:12px 22px">R\\u00e9server un appel gratuit</a>
      </div>
      <p class="calc-note">Estimation bas\\u00e9e sur vos chiffres. Le vrai potentiel, on le calcule ensemble.</p>
    </div>
  </div>
</section>

<script>
(function(){
function fmt(n){return Math.round(n).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g," ");}
var rC=document.getElementById("rClients"),rP=document.getElementById("rPanier"),rT=document.getElementById("rTaux");
function upd(){
  var c=+rC.value,p=+rP.value,t=+rT.value;
  document.getElementById("vClients").textContent=c;
  document.getElementById("vPanier").textContent=fmt(p)+" DZD";
  document.getElementById("vTaux").textContent=t+" %";
  var mois=c*(t/100)*p, an=mois*12;
  document.getElementById("rBig").textContent=fmt(mois)+" DZD";
  document.getElementById("rYear").textContent=fmt(an)+" DZD";
  var msg="Bonjour Advortex ! J\\u2019ai fait le calculateur : je perds environ "+fmt(mois)+" DZD par mois. Je veux r\\u00e9cup\\u00e9rer cet argent !";
  document.getElementById("calcGo").href="https://wa.me/213672645825?text="+encodeURIComponent(msg);
}
[rC,rP,rT].forEach(function(r){r.addEventListener("input",upd);});
upd();
})();
</script>
"""

page = head + '\n<body>\n\n' + nav + '\n\n' + body + '\n' + footer + '\n\n' + tail
open('calculateur.html', 'w', encoding='utf-8').write(page)
print('calculateur.html written', len(page))
