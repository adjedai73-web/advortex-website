# -*- coding: utf-8 -*-
"""Build booking-ar.html from booking.html (RTL + Arabic). Verifies every key matched."""
import re, sys
sys.path.insert(0, '.')
from build_ar import TR, RTL_CSS

BOOK_TR = [
 ('<html lang="fr">', '<html lang="ar" dir="rtl">'),
 ('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap',
  'https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap'),
 ('<title>Réserver un appel découverte — Advortex</title>',
  '<title>احجز مكالمة تعريفية — أدفورتكس</title>'),
 ('<meta name="description" content="Réservez un appel découverte gratuit de 20 minutes avec Advortex. Sans engagement.">',
  '<meta name="description" content="احجز مكالمة تعريفية مجانية لمدة 20 دقيقة مع أدفورتكس. بدون التزام.">'),
 ('<meta property="og:title" content="Advortex — Agence Marketing Digital à Alger">',
  '<meta property="og:title" content="أدفورتكس — وكالة التسويق الرقمي في الجزائر">\n<meta property="og:locale" content="ar_DZ">'),
 ('<meta property="og:description" content="On transforme votre présence en ligne en clients réels. Facebook • Instagram • TikTok • Vidéo.">',
  '<meta property="og:description" content="نحوّل حضورك على الإنترنت إلى زبائن حقيقيين. فيسبوك • إنستغرام • تيك توك • فيديو.">'),
 # links
 ('href="index.html', 'href="index-ar.html'),
 ('href="packs.html"', 'href="packs-ar.html"'),
 ('href="quiz.html"', 'href="quiz-ar.html"'),
 ('href="booking.html"', 'href="booking-ar.html"'),
 # switcher -> FR (nav comes from packs.html)
 ('href="packs-ar.html" class="lang-sw">عربية</a>', 'href="packs.html" class="lang-sw">FR</a>'),
 ('<a href="packs-ar.html">عربية</a>', '<a href="packs.html">FR</a>'),
 # hero
 ('<span class="eyebrow rv">Appel découverte</span>', '<span class="eyebrow rv">مكالمة تعريفية</span>'),
 ('Réservez votre appel gratuit', 'احجز مكالمتك المجانية'),
 ('20 minutes pour parler de votre business, vos objectifs et comment on peut vous aider. Sans engagement.',
  '20 دقيقة للحديث عن تجارتك، أهدافك وكيف يمكننا مساعدتك. بدون التزام.'),
 # widget
 ('Choisissez un jour', 'اختر اليوم'),
 ('Choisissez une heure', 'اختر الساعة'),
 ("(heure d'Alger)", '(بتوقيت الجزائر)'),
 ('Vos coordonnées', 'معلوماتك'),
 ('placeholder="Votre nom"', 'placeholder="اسمك"'),
 ('placeholder="Votre numéro de téléphone"', 'placeholder="رقم هاتفك"'),
 ('Confirmer sur WhatsApp', 'تأكيد عبر واتساب'),
 ('Gratuit &bull; 20 minutes &bull; Sans engagement &bull; Réponse rapide',
  'مجاني &bull; 20 دقيقة &bull; بدون التزام &bull; رد سريع'),
 # JS strings
 ('Choisissez un jour pour l\u2019appel.', 'اختر يوم المكالمة.'),
 ('Choisissez une heure.', 'اختر الساعة.'),
 ('Indiquez votre nom.', 'اكتب اسمك.'),
 ('Indiquez un numéro de téléphone valide.', 'اكتب رقم هاتف صحيح.'),
 ('"fr-FR"', '"ar-DZ"'),
]

WA_FRAGMENTS = [
 ('Bonjour Advortex ! Je réserve un appel découverte gratuit le ', 'مرحبا أدفورتكس! أحجز مكالمة تعريفية مجانية يوم '),
 ('+fmtLong(selDay)+" à "+selSlot', '+fmtLong(selDay)+" على الساعة "+selSlot'),
 ('". Nom : "', '". الاسم: "'),
 ('", Tél : "', '", الهاتف: "'),
]

def build():
    t = open('booking.html', encoding='utf-8').read()
    t = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
               r'\1https://advortex-agency.vercel.app/booking-ar.html\2', t)
    missed = []
    for fr, ar in sorted(BOOK_TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
        else:
            missed.append(fr[:50])
    for fr, ar in WA_FRAGMENTS:
        if fr in t:
            t = t.replace(fr, ar)
        else:
            missed.append('WA:' + fr[:50])
    for fr, ar in sorted(TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
    t = t.replace('</head>', RTL_CSS, 1)
    open('booking-ar.html', 'w', encoding='utf-8').write(t)
    print('booking-ar.html written', len(t))
    if missed:
        print('MISSED KEYS:')
        for m in missed:
            print('  -', repr(m))

if __name__ == '__main__':
    build()
