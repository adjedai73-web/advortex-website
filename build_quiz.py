# -*- coding: utf-8 -*-
"""Assemble quiz.html from packs.html shell + quiz body. No backslash escapes: direct UTF-8."""
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
  '<title>Quiz \u2014 Quel pack vous convient ? | Advortex</title>', head, count=1)
head = head.replace(
  '<meta name="description" content="Advortex est une agence de marketing digital \u00e0 Alger. Gestion Facebook, Instagram, TikTok, production vid\u00e9o et strat\u00e9gie de contenu pour restaurants, salons et entreprises.">',
  '<meta name="description" content="R\u00e9pondez \u00e0 4 questions rapides et d\u00e9couvrez le pack Advortex id\u00e9al pour votre business.">')
head = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
  r'\1https://advortex-agency.vercel.app/quiz.html\2', head)

QUIZ_CSS = """<style>
.quiz-box{max-width:680px;margin:0 auto;background:var(--bg2);border:1px solid var(--line);border-radius:24px;padding:44px;position:relative}
.quiz-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;color:var(--muted);font-size:13.5px}
.quiz-bar{height:6px;background:rgba(255,255,255,.08);border-radius:100px;overflow:hidden;margin-bottom:30px}
.quiz-bar i{display:block;height:100%;width:0;background:#fff;border-radius:100px;transition:width .45s cubic-bezier(.2,.8,.2,1)}
.quiz-q{font-size:clamp(20px,3vw,25px);font-weight:700;margin:0 0 24px;line-height:1.4}
.quiz-opts{display:grid;gap:12px}
.quiz-opt{background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:16px;padding:17px 22px;color:#fff;font-size:16px;cursor:pointer;text-align:start;font-family:inherit;transition:transform .15s,border-color .2s,background .2s;width:100%}
.quiz-opt:hover{border-color:rgba(255,255,255,.6);background:rgba(255,255,255,.07);transform:translateY(-2px)}
.quiz-back{background:none;border:0;color:var(--muted);margin-top:22px;cursor:pointer;font-size:14px;font-family:inherit;padding:0}
.quiz-back:hover{color:#fff}
.quiz-result{text-align:center;padding:6px 0}
.quiz-result .r-price{font-size:clamp(30px,4vw,40px);font-weight:800;margin:14px 0 6px}
.quiz-result .r-desc{color:var(--muted);max-width:460px;margin:0 auto 28px;line-height:1.7}
.quiz-result .r-ctas{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.quiz-step{animation:qin .35s ease}
@keyframes qin{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media(max-width:560px){.quiz-box{padding:30px 22px}}
</style>
</head>"""
head = head.replace('</head>', QUIZ_CSS, 1)

nav = nav.replace('<a href="packs.html" class="active">Packs</a>', '<a href="packs.html">Packs</a>')
nav = nav.replace('<a href="quiz.html">Quiz</a>', '<a href="quiz.html" class="active">Quiz</a>')

body = """<header class="page-hero" id="top">
  <div class="wrap">
    <span class="eyebrow rv">Quiz</span>
    <h1 class="rv">Quel pack vous convient ?</h1>
    <p class="sub rv">R\u00e9pondez \u00e0 4 questions rapides \u2014 on vous recommande la formule id\u00e9ale pour votre business.</p>
  </div>
</header>

<section id="quiz" style="padding-top:34px">
  <div class="wrap">
    <div class="quiz-box rv" id="quizBox"></div>
  </div>
</section>

<script>
(function(){
var QUESTIONS=[
 {q:"Quel est votre secteur d\u2019activit\u00e9 ?",o:["Restaurant","Salon de beaut\u00e9","Boutique","Entreprise","Autre"]},
 {q:"Combien de contenu voulez-vous par mois ?",o:["L\u00e9ger \u2014 pour commencer","R\u00e9gulier \u2014 pour grandir vite","Maximum \u2014 pour dominer"]},
 {q:"La vid\u00e9o (reels) est-elle une priorit\u00e9 ?",o:["Oui, c\u2019est la priorit\u00e9","Un peu","Non, posts et stories suffisent"]},
 {q:"Votre budget mensuel ?",o:["Moins de 70 000 DZD","70 000 \u2013 95 000 DZD","Plus de 95 000 DZD","Je veux du sur-mesure"]}
];
var RESULTS={
 premium:{name:"Premium",price:"70 000 DZD / mois",desc:"Parfait pour lancer votre pr\u00e9sence en ligne : un contenu r\u00e9gulier et professionnel, sans vous ruiner."},
 pro:{name:"Pro",price:"95 000 DZD / mois",desc:"Pour acc\u00e9l\u00e9rer : plus de contenu, stories illimit\u00e9es, rapport d\u00e9taill\u00e9 et appel mensuel."},
 perso:{name:"Personnalis\u00e9",price:"Sur devis",desc:"Vos besoins sont sp\u00e9cifiques \u2014 construisons ensemble une formule sur mesure, sans engagement."}
};
var step=0,answers=[];
function score(){
 if(answers[3]===3)return "perso";
 if(answers[3]===2||answers[1]===2||answers[2]===0)return "pro";
 return "premium";
}
function render(){
 var box=document.getElementById("quizBox");
 if(step<QUESTIONS.length){
  var Q=QUESTIONS[step],h='<div class="quiz-step">';
  h+='<div class="quiz-top"><span>Question '+(step+1)+' / '+QUESTIONS.length+'</span><span>'+Math.round(step/QUESTIONS.length*100)+'%</span></div>';
  h+='<div class="quiz-bar"><i style="width:'+(step/QUESTIONS.length*100)+'%"></i></div>';
  h+='<h2 class="quiz-q">'+Q.q+'</h2><div class="quiz-opts">';
  Q.o.forEach(function(opt,i){h+='<button class="quiz-opt" data-i="'+i+'">'+opt+'</button>'});
  h+="</div>";
  if(step>0)h+='<button class="quiz-back" id="qback">\u2190 Retour</button>';
  box.innerHTML=h;
  box.querySelectorAll(".quiz-opt").forEach(function(b){b.addEventListener("click",function(){answers[step]=+b.dataset.i;step++;render()})});
  var back=document.getElementById("qback");
  if(back)back.addEventListener("click",function(){step--;render()});
 }else{
  var R=RESULTS[score()];
  var wa="https://wa.me/213672645825?text="+encodeURIComponent("Bonjour Advortex ! J\u2019ai fait le quiz : le pack "+R.name+" me convient.");
  var h='<div class="quiz-step quiz-result">';
  h+='<div class="quiz-top" style="justify-content:center"><span>Votre r\u00e9sultat</span></div>';
  h+='<div class="quiz-bar"><i style="width:100%"></i></div>';
  h+='<span class="eyebrow">Recommand\u00e9 pour vous</span>';
  h+='<h2 class="quiz-q">Le pack '+R.name+' est fait pour vous.</h2>';
  h+='<div class="r-price">'+R.price+'</div>';
  h+='<p class="r-desc">'+R.desc+'</p>';
  h+='<div class="r-ctas"><a class="btn btn-wa" target="_blank" rel="noopener" href="'+wa+'">Choisir '+R.name+' sur WhatsApp</a>';
  h+='<a class="btn btn-ghost" href="packs.html">Voir tous les packs</a></div>';
  h+='<div style="margin-top:20px"><a href="booking.html" style="color:var(--muted);font-size:14.5px">Vous préférez en parler ? <u>Réservez un appel gratuit →</u></a></div>';
  h+='<div><button class="quiz-back" id="qrestart">\u21ba Refaire le quiz</button></div>';
  box.innerHTML=h;
  document.getElementById("qrestart").addEventListener("click",function(){step=0;answers=[];render()});
 }
}
render();
})();
</script>
"""

page = head + '\n<body>\n\n' + nav + '\n\n' + body + '\n' + footer + '\n\n' + tail
open('quiz.html', 'w', encoding='utf-8').write(page)
print('quiz.html written', len(page))
