# -*- coding: utf-8 -*-
"""Build calculateur-ar.html from calculateur.html (RTL + Arabic, direct UTF-8)."""
import re, sys
sys.path.insert(0, '.')
from build_ar import TR, RTL_CSS

CALC_TR = [
 ('<html lang="fr">', '<html lang="ar" dir="rtl">'),
 ('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap',
  'https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap'),
 ('<title>Combien vous perdez chaque mois ? — Advortex</title>',
  '<title>كم تخسر كل شهر؟ — أدفورتكس</title>'),
 ('<meta name="description" content="Calculez en 10 secondes combien votre business perd chaque mois sans marketing professionnel.">',
  '<meta name="description" content="احسب في 10 ثوانٍ كم تخسر تجارتك كل شهر بدون تسويق احترافي.">'),
 ('<meta property="og:title" content="Advortex — Agence Marketing Digital à Alger">',
  '<meta property="og:title" content="أدفورتكس — وكالة التسويق الرقمي في الجزائر">\n<meta property="og:locale" content="ar_DZ">'),
 ('<meta property="og:description" content="On transforme votre présence en ligne en clients réels. Facebook • Instagram • TikTok • Vidéo.">',
  '<meta property="og:description" content="نحوّل حضورك على الإنترنت إلى زبائن حقيقيين. فيسبوك • إنستغرام • تيك توك • فيديو.">'),
 ('href="index.html', 'href="index-ar.html'),
 ('href="packs.html"', 'href="packs-ar.html"'),
 ('href="quiz.html"', 'href="quiz-ar.html"'),
 ('href="booking.html"', 'href="booking-ar.html"'),
 ('href="calculateur.html"', 'href="calculateur-ar.html"'),
 ('href="packs-ar.html" class="lang-sw">عربية</a>', 'href="calculateur.html" class="lang-sw">FR</a>'),
 ('<a href="packs-ar.html">عربية</a>', '<a href="calculateur.html">FR</a>'),
 ('<span class="eyebrow rv">Calculateur</span>', '<span class="eyebrow rv">حاسبة</span>'),
 ('Combien vous perdez<br>chaque mois ?', 'كم تخسر<br>كل شهر؟'),
 ('Bla marketing pro, floussek rahoum yrouhou l concurrent. 7sebha f 10 secondes.',
  'بدون تسويق احترافي، أموالك تذهب إلى المنافس. احسبها في 10 ثوانٍ.'),
 ('Clients potentiels par mois', 'زبائن محتملون في الشهر'),
 ('Des gens qui voient votre business mais n’achètent pas (encore).',
  'أشخاص يرون تجارتك لكن لا يشترون (بعد).'),
 ('Panier moyen', 'متوسط سلة الشراء'),
 ('Combien dépense un client en moyenne chez vous, en DZD.',
  'كم ينفق الزبون في المتوسط عندك، بالدينار.'),
 ('Clients récupérables', 'زبائن يمكن استرجاعهم'),
 ('Estimation prudente : avec du bon contenu, cette part peut devenir cliente.',
  'تقدير حذر: مع محتوى جيد، هذه النسبة يمكن أن تصبح زبائن.'),
 ('Vous perdez environ', 'أنت تخسر حوالي'),
 ('par mois &mdash; soit', 'شهرياً &mdash; أي'),
 ('par an', 'سنوياً'),
 ('Hadi machi khsara 3adiya &mdash; hadi floussek li rahi trouh l concurrent.',
  'هذه ليست خسارة عادية &mdash; هذه أموالك التي تذهب إلى المنافس.'),
 ('Je veux récupérer cet argent', 'أريد استرجاع هذه الأموال'),
 ('Faire le quiz', 'قم بالاختبار'),
 ('Réserver un appel gratuit', 'احجز مكالمة مجانية'),
 ('Estimation basée sur vos chiffres. Le vrai potentiel, on le calcule ensemble.',
  'تقدير مبني على أرقامك. الإمكانية الحقيقية نحسبها معاً.'),
 ("Bonjour Advortex ! J’ai fait le calculateur : je perds environ ",
  "مرحبا أدفورتكس! قمت بالحاسبة: أخسر حوالي "),
 (" DZD par mois. Je veux récupérer cet argent !",
  " دج شهرياً. أريد استرجاع هذه الأموال!"),
]

def build():
    t = open('calculateur.html', encoding='utf-8').read()
    t = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
               r'\1https://advortex-agency.vercel.app/calculateur-ar.html\2', t)
    missed = []
    for fr, ar in sorted(CALC_TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
        else:
            missed.append(fr[:50])
    for fr, ar in sorted(TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
    t = t.replace('</head>', RTL_CSS, 1)
    open('calculateur-ar.html', 'w', encoding='utf-8').write(t)
    print('calculateur-ar.html written', len(t))
    if missed:
        print('MISSED:')
        for m in missed:
            print('  -', repr(m))

if __name__ == '__main__':
    build()
