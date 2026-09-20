#!/usr/bin/env python3
"""Build 6 blog article pages (3 FR + 3 AR) for the Advortex site."""
import os
from urllib.parse import quote

BASE = "/home/hatch/workspace/your_files/advortex-website"
WA = "https://wa.me/213672645825"

def page(lang, slug, cat, title, excerpt, date, minutes, body, back_label, back_href,
         cta_title, cta_text, cta_btn, wa_text, home):
    wa_link = f"{WA}?text={quote(wa_text)}"
    rtl = ' dir="rtl" lang="ar"' if lang == "ar" else ' lang="fr"'
    arrow = "&larr;" if lang == "ar" else "&rarr;"
    html = f"""<!DOCTYPE html>
<html{rtl}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &mdash; Advortex</title>
<meta name="description" content="{excerpt}">
<meta property="og:title" content="{title} &mdash; Advortex">
<meta property="og:description" content="{excerpt}">
<meta property="og:type" content="article">
<link rel="icon" href="assets/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#060606;--bg2:#0c0c0c;--card:#111;--line:#232323;--text:#f5f5f5;--muted:#a8a8a8;--dim:#6e6e6e;--wa:#25d366}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;line-height:1.8;-webkit-font-smoothing:antialiased}}
h1,h2{{font-family:'Montserrat',sans-serif}}
a{{color:inherit}}
.wrap{{max-width:760px;margin:0 auto;padding:0 22px}}
nav{{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(6,6,6,.85);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}}
.nav-in{{display:flex;align-items:center;justify-content:space-between;height:76px;max-width:1180px;margin:0 auto;padding:0 22px}}
.nav-in img{{height:56px}}
.btn{{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:14px;padding:12px 24px;border-radius:100px;text-decoration:none;transition:transform .15s}}
.btn:active{{transform:scale(.97)}}
.btn-wa{{background:var(--wa);color:#062b16}}
.btn-ghost{{border:1px solid var(--line);color:var(--text)}}
.art-hero{{padding:150px 0 40px;text-align:center}}
.eyebrow{{display:inline-block;font-size:12px;letter-spacing:3px;font-weight:600;color:var(--muted);text-transform:uppercase;margin-bottom:18px;border:1px solid var(--line);padding:8px 16px;border-radius:100px}}
.art-hero h1{{font-size:clamp(30px,5vw,46px);font-weight:800;line-height:1.2;letter-spacing:-.5px;margin-bottom:16px}}
.meta{{color:var(--dim);font-size:14px}}
.art-body{{padding:10px 0 30px;font-size:17px;color:#d8d8d8}}
.art-body p{{margin-bottom:22px}}
.art-body h2{{font-size:24px;margin:44px 0 16px;color:#fff}}
.art-body ul,.art-body ol{{margin:0 0 22px;padding-inline-start:22px;display:grid;gap:10px}}
.art-body strong{{color:#fff}}
.cta-box{{background:linear-gradient(180deg,#101010,#0a0a0a);border:1px solid var(--line);border-radius:22px;padding:44px 36px;text-align:center;margin:40px 0 80px}}
.cta-box h2{{font-size:26px;margin-bottom:12px}}
.cta-box p{{color:var(--muted);margin-bottom:26px}}
footer{{border-top:1px solid var(--line);padding:34px 0;background:var(--bg2);text-align:center;color:var(--dim);font-size:13px}}
</style>
</head>
<body>
<nav><div class="nav-in">
<a href="{home}"><img src="assets/logo.png" alt="Advortex"></a>
<a class="btn btn-ghost" href="{back_href}">{arrow} {back_label}</a>
</div></nav>
<header class="art-hero"><div class="wrap">
<span class="eyebrow">{cat}</span>
<h1>{title}</h1>
<p class="meta">{date} &middot; {minutes} min de lecture</p>
</div></header>
<article class="art-body"><div class="wrap">
{body}
</div></article>
<div class="wrap"><div class="cta-box">
<h2>{cta_title}</h2>
<p>{cta_text}</p>
<a class="btn btn-wa" href="{wa_link}" target="_blank" rel="noopener">{cta_btn}</a>
</div></div>
<footer>&copy; 2026 Advortex &mdash; Alger, Alg&eacute;rie</footer>
</body>
</html>"""
    path = os.path.join(BASE, slug)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug, len(html), "bytes")

# ============================================================ ARTICLE 1 FR
page("fr", "article-cout-community-manager.html", "Prix",
     "Combien coûte un community manager à Alger ?",
     "Employé, freelancer ou agence : le vrai calcul du coût d'un community manager à Alger, sans langue de bois.",
     "18 sept. 2026", 5,
     """<p>C'est la première question que nous posent les business à Alger : <strong>combien ça coûte, un community manager ?</strong> Et la réponse honnête, c'est : ça dépend de ce que vous comparez vraiment.</p>
<h2>Option 1 : un employé à plein temps</h2>
<p>Un salaire chaque mois, les charges, les congés, le matériel… Et surtout : <strong>une seule personne ne peut pas tout faire.</strong> Filmer, monter, designer, écrire, répondre aux messages, analyser les stats — c'est le travail de toute une équipe. Vous payez un salaire complet pour un résultat partiel.</p>
<h2>Option 2 : un freelancer</h2>
<p>Moins cher, plus flexible. Mais la disponibilité est limitée, il n'y a <strong>pas de tournage sur place</strong>, et s'il est malade ou débordé, votre page s'arrête net. Vous gérez tout, tout seul.</p>
<h2>Option 3 : une agence comme Advortex</h2>
<p>Un <strong>pack fixe par mois</strong> : tournage, montage, publication, réponses aux messages, rapport mensuel. Une équipe complète — pour souvent moins cher qu'un seul salaire.</p>
<h2>Le vrai calcul</h2>
<p>Ne comparez pas les prix, <strong>comparez le coût par client acquis</strong>. Une page Instagram qui ne vend pas, même gérée « gratuitement », vous coûte cher : c'est du temps perdu et des clients qui vont chez le concurrent.</p>""",
     "Accueil", "index.html",
     "Vous voulez le calcul pour VOTRE business ?",
     "Audit gratuit de votre page sous 48h — on vous dit exactement ce qu'il vous faut, sans engagement.",
     "Recevoir mon audit gratuit",
     "Bonjour Advortex ! Je veux mon audit Instagram gratuit.", "index.html")

# ============================================================ ARTICLE 2 FR
page("fr", "article-erreurs-instagram.html", "Erreurs",
     "5 erreurs qui tuent ton business sur Instagram",
     "Bio floue, publications au hasard, messages ignorés… Les 5 erreurs les plus fréquentes des business algériens sur Instagram — et comment les corriger.",
     "18 sept. 2026", 4,
     """<p>On analyse des dizaines de pages de business algériens chaque mois. Et on retrouve <strong>toujours les mêmes 5 erreurs</strong>. Tu en fais sûrement au moins deux — voici comment les corriger.</p>
<h2>1. Une bio floue</h2>
<p>On ne comprend pas ce que tu vends, ni comment te contacter. <strong>Ta bio doit dire en 3 secondes : quoi, pour qui, et où cliquer.</strong></p>
<h2>2. Publier quand tu t'en souviens</h2>
<p>Trois posts en un jour, puis rien pendant trois semaines. L'algorithme récompense la régularité — <strong>mieux vaut 3 posts par semaine, toute l'année</strong>, que 20 posts en panique.</p>
<h2>3. Que des photos de produits</h2>
<p>Les gens achètent à des humains, pas à des catalogues. <strong>Montre ton équipe, ton atelier, tes clients.</strong> C'est ça qui crée la confiance.</p>
<h2>4. Ignorer les messages</h2>
<p>Chaque message sans réponse, c'est <strong>un client qui va chez le concurrent</strong>. Réponds vite, ou confie-le à quelqu'un dont c'est le métier.</p>
<h2>5. Booster sans stratégie</h2>
<p>Mettre du budget sponsorisé sur un mauvais contenu, c'est jeter de l'argent par la fenêtre. <strong>D'abord le contenu qui convertit, ensuite le budget.</strong></p>""",
     "Accueil", "index.html",
     "On corrige ça ensemble ?",
     "Audit gratuit de ta page sous 48h : on te montre tes erreurs et comment les réparer.",
     "Recevoir mon audit gratuit",
     "Bonjour Advortex ! Je veux mon audit Instagram gratuit.", "index.html")

# ============================================================ ARTICLE 3 FR
page("fr", "article-reels-ou-posts.html", "Stratégie",
     "Reels ou posts : qu'est-ce qui apporte vraiment des clients ?",
     "Reels, posts, stories : chaque format a son rôle dans la vente. Voici la combinaison qui transforme des abonnés en clients.",
     "18 sept. 2026", 4,
     """<p>« On doit faire plus de reels ou plus de posts ? » On nous pose la question chaque semaine. <strong>La réponse : les deux — mais pas pour la même raison.</strong></p>
<h2>Les reels : la découverte</h2>
<p>Les reels, c'est comme ça que <strong>des inconnus te trouvent</strong>. L'algorithme les pousse à des gens qui ne te suivent pas encore. C'est ta vitrine vers l'extérieur.</p>
<h2>Les posts : la confiance</h2>
<p>Les carrousels et les posts prouvent ton <strong>expertise</strong>. Quand un visiteur arrive sur ta page, c'est ton feed qui le convainc que tu es sérieux.</p>
<h2>Les stories : la vente</h2>
<p>C'est là que ta communauté <strong>achète</strong> : promos, nouveautés, coulisses, sondages. Le lien direct avec ceux qui te suivent déjà.</p>
<h2>La combinaison gagnante</h2>
<p><strong>Reels pour attirer, posts pour convaincre, stories pour vendre.</strong> Un seul format ne suffit jamais — c'est le système complet qui transforme des abonnés en clients.</p>""",
     "Accueil", "index.html",
     "Tu veux ce système pour ton business ?",
     "Réserve un appel découverte gratuit — on te montre comment l'appliquer à ta page.",
     "Réserver mon appel gratuit",
     "Bonjour Advortex ! Je veux réserver un appel découverte gratuit.", "index.html")

# ============================================================ ARTICLE 1 AR
page("ar", "article-cout-community-manager-ar.html", "الأسعار",
     "شحال يكلّف كوميونيتي مانجر في الجزائر؟",
     "موظف، فريلانسر ولا وكالة: الحساب الصحيح لتكلفة الكوميونيتي مانجر في الجزائر، بلا لف ودوران.",
     "18 سبتمبر 2026", 5,
     """<p>هذا أول سؤال يطرحوه علينا أصحاب المشاريع في الجزائر: <strong>شحال يكلّف كوميونيتي مانجر؟</strong> والجواب الصادق هو: يعتمد على واش راك تقارن صح.</p>
<h2>الخيار 1: موظف بدوام كامل</h2>
<p>راتب كل شهر، الضمان، العطل، المعدات… والأهم: <strong>شخص واحد ما يقدرش يدير كلش.</strong> التصوير، المونتاج، التصميم، الكتابة، الرد على الرسائل، تحليل الإحصائيات — هذه خدمة فريق كامل. تخلّص راتب كامل على نتيجة ناقصة.</p>
<h2>الخيار 2: فريلانسر</h2>
<p>أرخص ومرن أكثر. لكن التوفر محدود، <strong>ما كاش تصوير في عين المكان</strong>، وإذا مرض ولا تخدم بزاف، صفحتك تحبس. وأنت تدير كلش وحدك.</p>
<h2>الخيار 3: وكالة كيما أدفورتكس</h2>
<p><strong>باقة ثابتة في الشهر</strong>: تصوير، مونتاج، نشر، رد على الرسائل، تقرير شهري. فريق كامل — وغالبًا أرخص من راتب واحد.</p>
<h2>الحساب الصحيح</h2>
<p>ما تقارنش الأسعار، <strong>قارن تكلفة الزبون الواحد</strong>. صفحة إنستغرام ما تبيعش، حتى لو كانت «باطل»، تكلّفك غالي: وقت ضايع وزبائن يروحوا للمنافس.</p>""",
     "الرئيسية", "index-ar.html",
     "تحب الحساب الخاص بمشروعك؟",
     "تدقيق مجاني لصفحتك خلال 48 ساعة — نقولولك بالضبط واش تحتاج، بدون التزام.",
     "استلم التدقيق المجاني",
     "مرحبا أدفورتكس! أريد التدقيق المجاني لحسابي على إنستغرام.", "index-ar.html")

# ============================================================ ARTICLE 2 AR
page("ar", "article-erreurs-instagram-ar.html", "أخطاء",
     "5 أخطاء تقتل تجارتك على إنستغرام",
     "بايو ضبابي، نشر عشوائي، رسائل مهملة… أشهر 5 أخطاء لأصحاب المشاريع الجزائريين على إنستغرام — وكيفاش تصلّحهم.",
     "18 سبتمبر 2026", 4,
     """<p>نحلّلوا عشرات صفحات المشاريع الجزائرية كل شهر. ودايمًا نلقاو <strong>نفس الأخطاء الخمسة</strong>. أكيد راك تدير زوج منهم على الأقل — هاو كيفاش تصلّحهم.</p>
<h2>1. بايو ضبابي</h2>
<p>ما نفهموش واش تبيع ولا كيفاش نتواصلوا معاك. <strong>البايو لازم يقول في 3 ثواني: واش، لمن، ووين نكليكي.</strong></p>
<h2>2. تنشر كي تتفكر</h2>
<p>ثلاثة منشورات في نهار، وبعدها والو لثلاثة أسابيع. الخوارزمية تكافئ الانتظام — <strong>3 منشورات في الأسبوع طول العام خير</strong> من 20 منشور في الزحمة.</p>
<h2>3. غير صور المنتجات</h2>
<p>الناس تشري من البشر، ماشي من الكاتالوغ. <strong>ورّي فريقك، ورشتك، زبائنك.</strong> هكذا تتبنى الثقة.</p>
<h2>4. تتجاهل الرسائل</h2>
<p>كل رسالة بلا رد هي <strong>زبون يروح للمنافس</strong>. رد بالخف، ولا خليها للي خدمتو هي الرد.</p>
<h2>5. تموّل بلا استراتيجية</h2>
<p>تحط دراهم سبونسور على محتوى ضعيف، راك ترمي دراهمك من النافذة. <strong>الأول المحتوى اللي يبيع، وبعدها الميزانية.</strong></p>""",
     "الرئيسية", "index-ar.html",
     "نصلّحوها مع بعض؟",
     "تدقيق مجاني لصفحتك خلال 48 ساعة: نوريلك أخطاءك وكيفاش تصلّحهم.",
     "استلم التدقيق المجاني",
     "مرحبا أدفورتكس! أريد التدقيق المجاني لحسابي على إنستغرام.", "index-ar.html")

# ============================================================ ARTICLE 3 AR
page("ar", "article-reels-ou-posts-ar.html", "استراتيجية",
     "ريلز ولا منشورات: واش يجيب الزبائن صح؟",
     "ريلز، منشورات، ستوري: كل صيغة عندها دورها في البيع. هاهي التركيبة اللي تحوّل المتابعين لزبائن.",
     "18 سبتمبر 2026", 4,
     """<p>«لازم نديروا ريلز أكثر ولا منشورات أكثر؟» يسقسيونا كل أسبوع. <strong>الجواب: في زوج — لكن ماشي لنفس السبب.</strong></p>
<h2>الريلز: الاكتشاف</h2>
<p>الريلز هو كيفاش <strong>الناس اللي ما يعرفوكش يلقاوك</strong>. الخوارزمية تدفعهم لناس ما يتابعوكش. هي الواجهة تاعك للبرا.</p>
<h2>المنشورات: الثقة</h2>
<p>الكاروسيل والمنشورات يثبتوا <strong>الخبرة</strong> تاعك. كي يزور واحد صفحتك، الفيد هو اللي يقنعو بلي راك جدي.</p>
<h2>الستوري: البيع</h2>
<p>هنا مجتمعك <strong>يشري</strong>: عروض، جديد، كواليس، استطلاعات. التواصل المباشر مع اللي يتابعوك.</p>
<h2>التركيبة الرابحة</h2>
<p><strong>ريلز للجذب، منشورات للإقناع، ستوري للبيع.</strong> صيغة وحدة ما تكفيش أبدًا — المنظومة الكاملة هي اللي تحوّل المتابعين لزبائن.</p>""",
     "الرئيسية", "index-ar.html",
     "تحب هذه المنظومة لمشروعك؟",
     "احجز مكالمة تعارف مجانية — نوريلك كيفاش تطبّقها على صفحتك.",
     "احجز مكالمتك المجانية",
     "مرحبا أدفورتكس! أريد حجز مكالمة تعارف مجانية.", "index-ar.html")
