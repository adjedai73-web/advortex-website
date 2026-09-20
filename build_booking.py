# -*- coding: utf-8 -*-
"""Assemble booking.html from packs.html shell + booking widget. Direct UTF-8, no backslash escapes."""
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
  '<title>Réserver un appel découverte — Advortex</title>', head, count=1)
head = head.replace(
  'content="Advortex est une agence de marketing digital à Alger. Gestion Facebook, Instagram, TikTok, production vidéo et stratégie de contenu pour restaurants, salons et entreprises.">',
  'content="Réservez un appel découverte gratuit de 20 minutes avec Advortex. Sans engagement.">')
head = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
  r'\1https://advortex-agency.vercel.app/booking.html\2', head)

BOOK_CSS = """<style>
.book-box{max-width:680px;margin:0 auto;background:var(--bg2);border:1px solid var(--line);border-radius:24px;padding:44px}
.book-step{margin-bottom:32px}
.book-step h3{font-size:17px;font-weight:700;margin:0 0 16px;display:flex;align-items:center;gap:10px}
.book-step h3 .n{width:28px;height:28px;border-radius:50%;background:#fff;color:#000;font-size:14px;display:inline-flex;align-items:center;justify-content:center;font-weight:800;flex:none}
.days{display:flex;gap:10px;overflow-x:auto;padding-bottom:8px;scrollbar-width:thin}
.day{flex:0 0 auto;min-width:86px;background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:16px;padding:12px 8px;color:#fff;cursor:pointer;text-align:center;font-family:inherit;transition:.15s}
.day small{display:block;color:var(--muted);font-size:12px;margin-bottom:4px;text-transform:capitalize}
.day b{font-size:16px}
.day:hover{border-color:rgba(255,255,255,.5)}
.day.sel{background:#fff;color:#000;border-color:#fff}
.day.sel small{color:#555}
.slots{display:grid;grid-template-columns:repeat(auto-fill,minmax(104px,1fr));gap:10px}
.slot{background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:14px;padding:13px 8px;color:#fff;cursor:pointer;font-family:inherit;font-size:15px;font-weight:600;transition:.15s}
.slot:hover{border-color:rgba(255,255,255,.5)}
.slot.sel{background:#fff;color:#000;border-color:#fff}
.book-input{width:100%;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:14px;padding:15px 18px;color:#fff;font-size:16px;font-family:inherit;margin-bottom:12px;box-sizing:border-box}
.book-input:focus{outline:none;border-color:#fff}
.book-input::placeholder{color:var(--dim)}
.book-err{color:#ff8a8a;font-size:14px;min-height:22px;margin:0 0 8px}
.book-note{text-align:center;color:var(--muted);font-size:14px;margin:18px 0 0}
.book-ok{text-align:center;padding:20px 0}
.book-ok .big{font-size:44px;margin-bottom:12px}
@media(max-width:560px){.book-box{padding:30px 22px}}
</style>
</head>"""
head = head.replace('</head>', BOOK_CSS, 1)

body = """<header class="page-hero" id="top">
  <div class="wrap">
    <span class="eyebrow rv">Appel découverte</span>
    <h1 class="rv">Réservez votre appel gratuit</h1>
    <p class="sub rv">20 minutes pour parler de votre business, vos objectifs et comment on peut vous aider. Sans engagement.</p>
  </div>
</header>

<section id="booking" style="padding-top:34px">
  <div class="wrap">
    <div class="book-box rv">
      <div class="book-step">
        <h3><span class="n">1</span> Choisissez un jour</h3>
        <div class="days" id="days"></div>
      </div>
      <div class="book-step">
        <h3><span class="n">2</span> Choisissez une heure <span style="color:var(--muted);font-weight:400;font-size:13px">(heure d'Alger)</span></h3>
        <div class="slots" id="slots"></div>
      </div>
      <div class="book-step">
        <h3><span class="n">3</span> Vos coordonnées</h3>
        <input class="book-input" id="bkName" type="text" placeholder="Votre nom" autocomplete="name">
        <input class="book-input" id="bkPhone" type="tel" placeholder="Votre numéro de téléphone" autocomplete="tel" inputmode="tel">
      </div>
      <p class="book-err" id="bkErr"></p>
      <button class="btn btn-wa" id="bkGo" style="width:100%;justify-content:center;border:0;cursor:pointer;font-family:inherit;font-size:16px">Confirmer sur WhatsApp</button>
      <p class="book-note">Gratuit &bull; 20 minutes &bull; Sans engagement &bull; Réponse rapide</p>
    </div>
  </div>
</section>

<script>
(function(){
var SLOTS=["10:00","11:30","14:00","15:30","17:00"];
var selDay=null, selSlot=null;
var daysEl=document.getElementById("days"), slotsEl=document.getElementById("slots");
var errEl=document.getElementById("bkErr");
function fmtLong(d){return d.toLocaleDateString("fr-FR",{weekday:"long",day:"numeric",month:"long"});}
var days=[];
(function(){
  var d=new Date(), n=0;
  while(days.length<10 && n<21){
    d=new Date(); d.setDate(d.getDate()+n);
    if(d.getDay()!==5){days.push(new Date(d));}
    n++;
  }
})();
days.forEach(function(d,i){
  var b=document.createElement("button");
  b.className="day"; b.type="button";
  b.innerHTML="<small>"+d.toLocaleDateString("fr-FR",{weekday:"short"})+"</small><b>"+d.getDate()+"</b><small>"+d.toLocaleDateString("fr-FR",{month:"short"})+"</small>";
  b.addEventListener("click",function(){
    selDay=d;
    daysEl.querySelectorAll(".day").forEach(function(x){x.classList.remove("sel")});
    b.classList.add("sel"); errEl.textContent="";
  });
  daysEl.appendChild(b);
});
SLOTS.forEach(function(s){
  var b=document.createElement("button");
  b.className="slot"; b.type="button"; b.textContent=s;
  b.addEventListener("click",function(){
    selSlot=s;
    slotsEl.querySelectorAll(".slot").forEach(function(x){x.classList.remove("sel")});
    b.classList.add("sel"); errEl.textContent="";
  });
  slotsEl.appendChild(b);
});
document.getElementById("bkGo").addEventListener("click",function(){
  var name=document.getElementById("bkName").value.trim();
  var phone=document.getElementById("bkPhone").value.replace(/[^0-9+]/g,"");
  if(!selDay){errEl.textContent="Choisissez un jour pour l\u2019appel.";return;}
  if(!selSlot){errEl.textContent="Choisissez une heure.";return;}
  if(name.length<2){errEl.textContent="Indiquez votre nom.";return;}
  if(phone.replace("+","").length<9){errEl.textContent="Indiquez un num\u00e9ro de t\u00e9l\u00e9phone valide.";return;}
  errEl.textContent="";
  var msg="Bonjour Advortex ! Je r\u00e9serve un appel d\u00e9couverte gratuit le "+fmtLong(selDay)+" \u00e0 "+selSlot+". Nom : "+name+", T\u00e9l : "+phone+".";
  window.open("https://wa.me/213672645825?text="+encodeURIComponent(msg),"_blank");
});
})();
</script>
"""

page = head + '\n<body>\n\n' + nav + '\n\n' + body + '\n' + footer + '\n\n' + tail
open('booking.html', 'w', encoding='utf-8').write(page)
print('booking.html written', len(page))
