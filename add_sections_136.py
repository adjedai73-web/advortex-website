#!/usr/bin/env python3
"""Add to index.html + index-ar.html: comparison table, case study, blog teaser.
Create 6 article pages (3 FR + 3 AR)."""
import os

BASE = "/home/hatch/workspace/your_files/advortex-website"
WA = "https://wa.me/213672645825"

# ---------------------------------------------------------------- COMPARATIF FR
CMP_CSS = """
<style>
.cmp-wrap{overflow-x:auto}
.cmp{width:100%;border-collapse:separate;border-spacing:0;margin-top:50px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;font-size:15px;min-width:560px}
.cmp th,.cmp td{padding:18px 16px;text-align:center;border-bottom:1px solid #1b1b1b}
.cmp th:first-child,.cmp td:first-child{text-align:start;color:var(--muted)}
.cmp thead th{font-family:'Montserrat';font-size:15px}
.cmp thead th.hot{background:#fff;color:#0a0a0a}
.cmp tbody td.hot{background:rgba(255,255,255,.045);font-weight:700;color:#fff}
.cmp .yes{color:#fff;font-weight:700;font-size:18px}
.cmp .mid{color:var(--dim);font-weight:700;font-size:18px}
.cmp .no{color:#3d3d3d;font-weight:700;font-size:18px}
.cmp tr:last-child td{border-bottom:0}
.cmp-legend{text-align:center;color:var(--dim);font-size:13px;margin-top:16px}
</style>
"""

CMP_FR = CMP_CSS + """
<section id="comparatif">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">Pourquoi nous</span>
      <h2 class="rv">Advortex, ou le reste ?</h2>
      <p class="lead rv">Comparez par vous-m&ecirc;me. Pas de discours &mdash; des faits.</p>
    </div>
    <div class="cmp-wrap rv">
    <table class="cmp">
      <thead><tr><th></th><th class="hot">Advortex</th><th>G&eacute;rer seul</th><th>Freelancer</th></tr></thead>
      <tbody>
        <tr><td>Tournage pro sur place</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="mid">~</span></td></tr>
        <tr><td>Strat&eacute;gie de contenu</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="mid">~</span></td></tr>
        <tr><td>Publication r&eacute;guli&egrave;re</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="yes">&#10003;</span></td></tr>
        <tr><td>R&eacute;ponses aux messages 7j/7</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="no">&#10005;</span></td></tr>
        <tr><td>Rapport mensuel clair</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="mid">~</span></td></tr>
        <tr><td>Co&ucirc;t</td><td class="hot">Un pack fixe / mois</td><td style="color:var(--muted)">Un salaire &agrave; plein temps</td><td style="color:var(--muted)">Impr&eacute;visible</td></tr>
      </tbody>
    </table>
    </div>
    <p class="cmp-legend rv">&#10003; Inclus &nbsp;&middot;&nbsp; ~ Partiel &nbsp;&middot;&nbsp; &#10005; Non inclus</p>
  </div>
</section>
"""

# ---------------------------------------------------------------- ETUDE DE CAS FR
CASE_FR = """
<section id="etude-cas" style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">&Eacute;tude de cas</span>
      <h2 class="rv">On fait pour nous<br>ce qu'on fait pour vous.</h2>
      <p class="lead rv">Notre propre page Instagram, transform&eacute;e avec notre m&eacute;thode. Des preuves, pas des promesses.</p>
    </div>
    <div class="testi-grid" style="grid-template-columns:1fr 1fr;max-width:920px;margin-left:auto;margin-right:auto">
      <div class="testi rv">
        <h3 style="color:var(--dim);font-size:20px">Avant</h3>
        <ul style="list-style:none;display:grid;gap:12px;color:var(--muted);font-size:15px;padding:0;margin:0">
          <li>&#10005; Bio g&eacute;n&eacute;rique, sans appel &agrave; l'action</li>
          <li>&#10005; Publications irr&eacute;guli&egrave;res, sans ligne &eacute;ditoriale</li>
          <li>&#10005; Identit&eacute; visuelle floue</li>
          <li>&#10005; Stories publi&eacute;es au hasard</li>
        </ul>
      </div>
      <div class="testi rv" style="border-color:#fff">
        <h3 style="font-size:20px">Apr&egrave;s</h3>
        <ul style="list-style:none;display:grid;gap:12px;color:#d5d5d5;font-size:15px;padding:0;margin:0">
          <li>&#10003; Bio orient&eacute;e r&eacute;sultats</li>
          <li>&#10003; Identit&eacute; premium noir &amp; blanc</li>
          <li>&#10003; Calendrier de contenu 30 jours</li>
          <li>&#10003; Stories quotidiennes + 3 publications / semaine</li>
        </ul>
      </div>
    </div>
    <div class="center rv" style="margin-top:40px">
      <p style="color:var(--muted);font-size:15px;margin-bottom:24px"><b style="color:#fff">1 639</b> abonn&eacute;s &middot; <b style="color:#fff">15</b> publications &middot; chiffres r&eacute;els, sept. 2026</p>
      <a class="btn btn-ghost" href="https://www.instagram.com/advortex.off" target="_blank" rel="noopener">Voir la page &rarr;</a>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- BLOG TEASER FR
BLOG_FR = """
<section id="conseils">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">Conseils</span>
      <h2 class="rv">Le blog des business<br>qui veulent grandir.</h2>
      <p class="lead rv">Des conseils concrets, pens&eacute;s pour le march&eacute; alg&eacute;rien. Z&eacute;ro jargon.</p>
    </div>
    <div class="testi-grid">
      <a class="testi rv" href="article-cout-community-manager.html" style="text-decoration:none">
        <span class="eyebrow" style="margin-bottom:0">Prix</span>
        <h3 style="font-size:20px">Combien co&ucirc;te un community manager &agrave; Alger ?</h3>
        <p style="color:var(--muted);font-size:14.5px">Employ&eacute;, freelancer ou agence : le vrai calcul, sans langue de bois.</p>
        <span style="color:#fff;font-weight:600;font-size:14px">Lire l'article &rarr;</span>
      </a>
      <a class="testi rv" href="article-erreurs-instagram.html" style="text-decoration:none">
        <span class="eyebrow" style="margin-bottom:0">Erreurs</span>
        <h3 style="font-size:20px">5 erreurs qui tuent ton business sur Instagram</h3>
        <p style="color:var(--muted);font-size:14.5px">Tu fais s&ucirc;rement au moins deux d'entre elles. Voici comment les corriger.</p>
        <span style="color:#fff;font-weight:600;font-size:14px">Lire l'article &rarr;</span>
      </a>
      <a class="testi rv" href="article-reels-ou-posts.html" style="text-decoration:none">
        <span class="eyebrow" style="margin-bottom:0">Strat&eacute;gie</span>
        <h3 style="font-size:20px">Reels ou posts : qu'est-ce qui apporte vraiment des clients ?</h3>
        <p style="color:var(--muted);font-size:14.5px">Port&eacute;e, confiance, vente : chaque format a son r&ocirc;le. Voici la combinaison gagnante.</p>
        <span style="color:#fff;font-weight:600;font-size:14px">Lire l'article &rarr;</span>
      </a>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- AR VERSIONS
CMP_AR = CMP_CSS + """
<section id="comparatif">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">علاش حنا</span>
      <h2 class="rv">أدفورتكس، ولا الباقي؟</h2>
      <p class="lead rv">قارن بنفسك. بلا هدرة &mdash; بالأدلة.</p>
    </div>
    <div class="cmp-wrap rv">
    <table class="cmp">
      <thead><tr><th></th><th class="hot">أدفورتكس</th><th>تسيير وحدك</th><th>فريلانسر</th></tr></thead>
      <tbody>
        <tr><td>تصوير احترافي في عين المكان</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="mid">~</span></td></tr>
        <tr><td>استراتيجية محتوى</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="mid">~</span></td></tr>
        <tr><td>نشر منتظم</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="yes">&#10003;</span></td></tr>
        <tr><td>الرد على الرسائل 7 أيام / 7</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="no">&#10005;</span></td></tr>
        <tr><td>تقرير شهري واضح</td><td class="hot"><span class="yes">&#10003;</span></td><td><span class="no">&#10005;</span></td><td><span class="mid">~</span></td></tr>
        <tr><td>التكلفة</td><td class="hot">باقة ثابتة / شهريًا</td><td style="color:var(--muted)">راتب شهري كامل</td><td style="color:var(--muted)">غير متوقعة</td></tr>
      </tbody>
    </table>
    </div>
    <p class="cmp-legend rv">&#10003; مشمول &nbsp;&middot;&nbsp; ~ جزئي &nbsp;&middot;&nbsp; &#10005; غير مشمول</p>
  </div>
</section>
"""

CASE_AR = """
<section id="etude-cas" style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">دراسة حالة</span>
      <h2 class="rv">نطبّق على أنفسنا<br>واش نبيعوه.</h2>
      <p class="lead rv">صفحة الإنستغرام تاعنا، بدّلناها بالمنهجية تاعنا. أدلة، ماشي وعود.</p>
    </div>
    <div class="testi-grid" style="grid-template-columns:1fr 1fr;max-width:920px;margin-left:auto;margin-right:auto">
      <div class="testi rv">
        <h3 style="color:var(--dim);font-size:20px">قبل</h3>
        <ul style="list-style:none;display:grid;gap:12px;color:var(--muted);font-size:15px;padding:0;margin:0">
          <li>&#10005; بايو عادي بلا دعوة للتواصل</li>
          <li>&#10005; منشورات غير منتظمة بلا خط تحريري</li>
          <li>&#10005; هوية بصرية ضبابية</li>
          <li>&#10005; ستوري منشورة عشوائيًا</li>
        </ul>
      </div>
      <div class="testi rv" style="border-color:#fff">
        <h3 style="font-size:20px">بعد</h3>
        <ul style="list-style:none;display:grid;gap:12px;color:#d5d5d5;font-size:15px;padding:0;margin:0">
          <li>&#10003; بايو موجّه للنتائج</li>
          <li>&#10003; هوية بريميوم بالأبيض والأسود</li>
          <li>&#10003; تقويم محتوى 30 يوم</li>
          <li>&#10003; ستوري يومية + 3 منشورات أسبوعيًا</li>
        </ul>
      </div>
    </div>
    <div class="center rv" style="margin-top:40px">
      <p style="color:var(--muted);font-size:15px;margin-bottom:24px"><b style="color:#fff">1 639</b> متابع &middot; <b style="color:#fff">15</b> منشور &middot; أرقام حقيقية، سبتمبر 2026</p>
      <a class="btn btn-ghost" href="https://www.instagram.com/advortex.off" target="_blank" rel="noopener">&larr; شوف الصفحة</a>
    </div>
  </div>
</section>
"""

BLOG_AR = """
<section id="conseils">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">نصائح</span>
      <h2 class="rv">مدونة المشاريع<br>اللي تحب تكبر.</h2>
      <p class="lead rv">نصائح عملية، مصممة للسوق الجزائري. بلا تعقيد.</p>
    </div>
    <div class="testi-grid">
      <a class="testi rv" href="article-cout-community-manager-ar.html" style="text-decoration:none">
        <span class="eyebrow" style="margin-bottom:0">الأسعار</span>
        <h3 style="font-size:20px">شحال يكلّف كوميونيتي مانجر في الجزائر؟</h3>
        <p style="color:var(--muted);font-size:14.5px">موظف، فريلانسر ولا وكالة: الحساب الصحيح بلا لف ودوران.</p>
        <span style="color:#fff;font-weight:600;font-size:14px">اقرا المقال &larr;</span>
      </a>
      <a class="testi rv" href="article-erreurs-instagram-ar.html" style="text-decoration:none">
        <span class="eyebrow" style="margin-bottom:0">أخطاء</span>
        <h3 style="font-size:20px">5 أخطاء تقتل تجارتك على إنستغرام</h3>
        <p style="color:var(--muted);font-size:14.5px">أكيد راك تدير زوج منهم على الأقل. هاو كيفاش تصلّحهم.</p>
        <span style="color:#fff;font-weight:600;font-size:14px">اقرا المقال &larr;</span>
      </a>
      <a class="testi rv" href="article-reels-ou-posts-ar.html" style="text-decoration:none">
        <span class="eyebrow" style="margin-bottom:0">استراتيجية</span>
        <h3 style="font-size:20px">ريلز ولا منشورات: واش يجيب الزبائن صح؟</h3>
        <p style="color:var(--muted);font-size:14.5px">الانتشار، الثقة، البيع: كل صيغة عندها دورها. هاهي التركيبة الرابحة.</p>
        <span style="color:#fff;font-weight:600;font-size:14px">اقرا المقال &larr;</span>
      </a>
    </div>
  </div>
</section>
"""

def insert_before(path, marker, html):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    assert marker in src, f"marker missing in {path}: {marker[:40]}"
    key = html.split('id="')[1].split('"')[0]
    assert f'id="{key}"' not in src, f"already present in {path}: {key}"
    src = src.replace(marker, html + "\n" + marker, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    print("inserted", key, "->", os.path.basename(path))

insert_before(f"{BASE}/index.html", '<section id="methode">', CASE_FR)
insert_before(f"{BASE}/index.html", '<section id="packs"', CMP_FR)
insert_before(f"{BASE}/index.html", '<section id="faq">', BLOG_FR)
insert_before(f"{BASE}/index-ar.html", '<section id="methode">', CASE_AR)
insert_before(f"{BASE}/index-ar.html", '<section id="packs"', CMP_AR)
insert_before(f"{BASE}/index-ar.html", '<section id="faq">', BLOG_AR)

# nav links
for path, fr_link, ar_link in [
    (f"{BASE}/index.html",
     '<a href="quiz.html">Quiz</a>', '<a href="quiz.html">Quiz</a><a href="#conseils">Conseils</a>'),
    (f"{BASE}/index-ar.html",
     '<a href="quiz-ar.html">الاختبار</a>', '<a href="quiz-ar.html">الاختبار</a><a href="#conseils">نصائح</a>'),
]:
    with open(path, encoding="utf-8") as f:
        src = f.read()
    n = src.count(fr_link)
    src = src.replace(fr_link, ar_link)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    print("nav updated", os.path.basename(path), "x", n)
