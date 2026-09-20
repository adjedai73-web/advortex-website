# -*- coding: utf-8 -*-
"""Post-process quiz-ar.html: replace whole QUESTIONS/RESULTS JS blocks + waMsg with Arabic."""
import re

AR_Q = '''var QUESTIONS=[
 {q:"ما هو قطاع نشاطك؟",o:["مطعم","صالون تجميل","متجر","شركة","أخرى"]},
 {q:"كم من المحتوى تريد شهريًا؟",o:["خفيف — للبداية","منتظم — للنمو السريع","مكثّف — للسيطرة"]},
 {q:"هل الفيديو (ريلز) أولوية بالنسبة لك؟",o:["نعم، إنها الأولوية","قليلًا","لا، المنشورات والستوري تكفي"]},
 {q:"ما هي ميزانيتك الشهرية؟",o:["أقل من 70 000 دج","70 000 – 95 000 دج","أكثر من 95 000 دج","أريد شيئًا مخصصًا"]}
];'''

AR_R = '''var RESULTS={
 premium:{name:"بريميوم",price:"70 000 دج / شهريًا",desc:"مثالي لإطلاق حضورك على الإنترنت: محتوى منتظم واحترافي، دون إرهاق ميزانيتك."},
 pro:{name:"برو",price:"95 000 دج / شهريًا",desc:"للتسريع: محتوى أكثر، ستوري غير محدودة، تقرير مفصّل ومكالمة شهرية."},
 perso:{name:"مخصّصة",price:"حسب الطلب",desc:"احتياجاتك خاصة — لنبنِ معًا صيغة مخصصة، بدون التزام."}
};'''

t = open('quiz-ar.html', encoding='utf-8').read()
t2 = re.sub(r'var QUESTIONS=\[.*?\];', AR_Q, t, flags=re.S)
assert t2 != t, 'QUESTIONS block not found'
t = t2
t2 = re.sub(r'var RESULTS=\{.*?\};', AR_R, t, flags=re.S)
assert t2 != t, 'RESULTS block not found'
t = t2
# waMsg: ASCII-safe anchors around the U+2019 apostrophe
t2 = re.sub(r'"Bonjour Advortex ! J.*?ai fait le quiz : le pack "',
            '"مرحبا أدفورتكس! قمت بالاختبار: باقة "', t)
assert t2 != t, 'waMsg not found'
t = t2
open('quiz-ar.html', 'w', encoding='utf-8').write(t)
print('blocks replaced OK')
