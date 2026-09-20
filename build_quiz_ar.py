# -*- coding: utf-8 -*-
"""Build quiz-ar.html from quiz.html (RTL + Arabic)."""
import re, sys
sys.path.insert(0, '.')
from build_ar import TR, RTL_CSS

QUIZ_TR = [
 ('<html lang="fr">', '<html lang="ar" dir="rtl">'),
 ('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap',
  'https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap'),
 ('<title>Quiz — Quel pack vous convient ? | Advortex</title>',
  '<title>اختبار — أي باقة تناسبك؟ | أدفورتكس</title>'),
 ('<meta name="description" content="Répondez à 4 questions rapides et découvrez le pack Advortex idéal pour votre business.">',
  '<meta name="description" content="أجب عن 4 أسئلة سريعة واكتشف باقة أدفورتكس المثالية لتجارتك.">'),
 ('<meta property="og:title" content="Advortex — Agence Marketing Digital à Alger">',
  '<meta property="og:title" content="أدفورتكس — وكالة التسويق الرقمي في الجزائر">\n<meta property="og:locale" content="ar_DZ">'),
 ('<meta property="og:description" content="On transforme votre présence en ligne en clients réels. Facebook • Instagram • TikTok • Vidéo.">',
  '<meta property="og:description" content="نحوّل حضورك على الإنترنت إلى زبائن حقيقيين. فيسبوك • إنستغرام • تيك توك • فيديو.">'),
 # links
 ('href="index.html', 'href="index-ar.html'),
 ('href="packs.html"', 'href="packs-ar.html"'),
 ('href="quiz.html" class="active">Quiz</a>', 'href="quiz-ar.html" class="active">اختبار</a>'),
 ('<a href="quiz.html">Quiz</a>', '<a href="quiz-ar.html">اختبار</a>'),
 ('href="quiz.html"', 'href="quiz-ar.html"'),
 # switcher -> FR (quiz nav comes from packs.html)
 ('href="packs-ar.html" class="lang-sw">عربية</a>', 'href="packs.html" class="lang-sw">FR</a>'),
 ('<a href="packs-ar.html">عربية</a>', '<a href="packs.html">FR</a>'),
 # hero
 ('<span class="eyebrow rv">Quiz</span>', '<span class="eyebrow rv">اختبار</span>'),
 ('Quel pack vous convient ?', 'أي باقة تناسبك؟'),
 ('Répondez à 4 questions rapides — on vous recommande la formule idéale pour votre business.',
  'أجب عن 4 أسئلة سريعة — وسنرشح لك الصيغة المثالية لتجارتك.'),
 # quiz JS strings
 ('Quel est votre secteur d\\u2019activit\\u00e9 ?', 'ما هو قطاع نشاطك؟'),
 ('"Restaurant"', '"مطعم"'),
 ('"Salon de beaut\\u00e9"', '"صالون تجميل"'),
 ('"Boutique"', '"متجر"'),
 ('"Entreprise"', '"شركة"'),
 ('"Autre"', '"أخرى"'),
 ('Combien de contenu voulez-vous par mois ?', 'كم من المحتوى تريد شهريًا؟'),
 ('"L\\u00e9ger \\u2014 pour commencer"', '"خفيف \\u2014 للبداية"'),
 ('"R\\u00e9gulier \\u2014 pour grandir vite"', '"منتظم \\u2014 للنمو السريع"'),
 ('"Maximum \\u2014 pour dominer"', '"مكث\\u00e7ف \\u2014 للسيطرة"'),
 ('La vid\\u00e9o (reels) est-elle une priorit\\u00e9 ?', 'هل الفيديو (ريلز) أولوية بالنسبة لك؟'),
 ('"Oui, c\\u2019est la priorit\\u00e9"', '"نعم، إنها الأولوية"'),
 ('"Un peu"', '"قليل\\u064bا"'),
 ('"Non, posts et stories suffisent"', '"لا، المنشورات والستوري تكفي"'),
 ('Votre budget mensuel ?', 'ما هي ميزانيتك الشهرية؟'),
 ('"Moins de 70 000 DZD"', '"أقل من 70 000 دج"'),
 ('"70 000 \\u2013 95 000 DZD"', '"70 000 \\u2013 95 000 دج"'),
 ('"Plus de 95 000 DZD"', '"أكثر من 95 000 دج"'),
 ('"Je veux du sur-mesure"', '"أريد شيئ\\u064bا مخصص\\u064bا"'),
 ('{name:"Premium"', '{name:"بريميوم"'),
 ('{name:"Pro"', '{name:"برو"'),
 ('{name:"Personnalis\\u00e9"', '{name:"مخص\\u00d8\\u00a9ة"'),
 ('70 000 DZD / mois', '70 000 دج / شهري\\u064bا'),
 ('95 000 DZD / mois', '95 000 دج / شهري\\u064bا'),
 ('Sur devis', 'حسب الطلب'),
 ('"Parfait pour lancer votre pr\\u00e9sence en ligne : un contenu r\\u00e9gulier et professionnel, sans vous ruiner."',
  '"مثالي لإطلاق حضورك على الإنترنت: محتوى منتظم واحترافي، دون إرهاق ميزانيتك."'),
 ('"Pour acc\\u00e9l\\u00e9rer : plus de contenu, stories illimit\\u00e9es, rapport d\\u00e9taill\\u00e9 et appel mensuel."',
  '"للتسريع: محتوى أكثر، ستوري غير محدودة، تقرير مفص\\u00d8\\u00b1ل ومكالمة شهرية."'),
 ('"Vos besoins sont sp\\u00e9cifiques \\u2014 construisons ensemble une formule sur mesure, sans engagement."',
  '"احتياجاتك خاصة \\u2014 لنبن\\u0650 مع\\u064bا صيغة مخصصة، بدون التزام."'),
 ('Question ', 'سؤال '),
 ('Vous préférez en parler ?', 'تفضل تتكلم معنا؟'),
 ('Réservez un appel gratuit', 'احجز مكالمة مجانية'),
 ('href="booking.html"', 'href="booking-ar.html"'),
 ('Retour', 'رجوع'),
 ('Votre résultat', 'نتيجتك'),
 ('Recommandé pour vous', 'موصى به لك'),
 ('Le pack ', 'باقة '),
 ('le pack ', 'باقة '),
 ('est fait pour vous.', 'هي الأنسب لك.'),
 ("Bonjour Advortex !", "مرحبا أدفورتكس!"),
 ("J'ai fait le quiz", "قمت بالاختبار"),
 ('me convient.', 'تناسبني.'),
 ('"+R.name+" me convient."', '"+R.name+" تناسبني."'),
 ('Choisir ', 'اختر '),
 ('sur WhatsApp', 'على واتساب'),
 ('Voir tous les packs', 'شاهد كل الباقات'),
 ('Refaire le quiz', 'إعادة الاختبار'),
]

def build():
    t = open('quiz.html', encoding='utf-8').read()
    t = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
               r'\1https://advortex-agency.vercel.app/quiz-ar.html\2', t)
    for fr, ar in sorted(QUIZ_TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
    # shared FR->AR translations (nav, footer, misc)
    for fr, ar in sorted(TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
    t = t.replace('</head>', RTL_CSS, 1)
    open('quiz-ar.html', 'w', encoding='utf-8').write(t)
    print('quiz-ar.html written', len(t))

if __name__ == '__main__':
    build()
