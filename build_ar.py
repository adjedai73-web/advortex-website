# -*- coding: utf-8 -*-
"""Build Arabic RTL versions: index-ar.html, packs-ar.html from index.html / packs.html."""
import re, urllib.parse

Q = urllib.parse.quote

WA = {
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Je%20veux%20un%20devis%20gratuit%20pour%20mon%20business.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! أريد عرض سعر مجاني لتجارتي."),
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Je%20veux%20discuter%20de%20mon%20projet.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! أريد مناقشة مشروعي."),
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Je%20veux%20voir%20plus%20de%20vos%20r%C3%A9alisations.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! أريد رؤية المزيد من أعمالكم."),
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Je%20veux%20un%20devis%20gratuit.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! أريد عرض سعر مجاني."),
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Le%20pack%20Premium%20m%27int%C3%A9resse.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! باقة بريميوم تهمني."),
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Le%20pack%20Pro%20m%27int%C3%A9resse.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! باقة برو تهمني."),
 "https://wa.me/213672645825?text=Bonjour%20Advortex%20!%20Je%20veux%20un%20pack%20personnalis%C3%A9%20sur%20mesure.":
 "https://wa.me/213672645825?text=" + Q("مرحبا أدفورتكس! أريد باقة مخصصة حسب الطلب."),
}

# (french, arabic) — applied longest-first
TR = [
 # ---- HEAD ----
 ('<html lang="fr">', '<html lang="ar" dir="rtl">'),
 ('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap',
  'https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap'),
 ('<meta name="description" content="Advortex est une agence de marketing digital à Alger. Gestion Facebook, Instagram, TikTok, production vidéo et stratégie de contenu pour restaurants, salons et entreprises.">',
  '<meta name="description" content="أدفورتكس وكالة تسويق رقمي في الجزائر. إدارة فيسبوك وإنستغرام وتيك توك، إنتاج فيديو واستراتيجية محتوى للمطاعم والصالونات والشركات.">'),
 ('<meta property="og:title" content="Advortex — Agence Marketing Digital à Alger">',
  '<meta property="og:title" content="أدفورتكس — وكالة التسويق الرقمي في الجزائر">\n<meta property="og:locale" content="ar_DZ">'),
 ('<meta property="og:description" content="On transforme votre présence en ligne en clients réels. Facebook • Instagram • TikTok • Vidéo.">',
  '<meta property="og:description" content="نحوّل حضورك على الإنترنت إلى زبائن حقيقيين. فيسبوك • إنستغرام • تيك توك • فيديو.">'),
 # ---- NAV ----
 ('aria-label="Menu"', 'aria-label="القائمة"'),
 ('alt="Advortex — Social Media Marketing Agency"', 'alt="أدفورتكس — وكالة التسويق عبر شبكات التواصل"'),
 ('>Services</a>', '>خدماتنا</a>'),
 ('>Réalisations</a>', '>أعمالنا</a>'),
 ('>Méthode</a>', '>منهجيتنا</a>'),
 ('>Packs</a>', '>الباقات</a>'),
 ('>FAQ</a>', '>الأسئلة الشائعة</a>'),
 ('>Accueil</a>', '>الرئيسية</a>'),
 ('Devis gratuit →', 'عرض سعر مجاني ←'),
 ('>Devis gratuit</a>', '>عرض سعر مجاني</a>'),
 # ---- HERO ----
 ('Agence marketing digital — Alger', 'وكالة تسويق رقمي — الجزائر'),
 ('Votre marque mérite <span class="stroke">plus</span> que des likes.', 'علامتك تستحق <span class="stroke">أكثر</span> من الإعجابات.'),
 ("Advortex transforme votre présence sur Facebook, Instagram et TikTok en clients réels. Stratégie, contenu vidéo et gestion complète — on s'occupe de tout, vous vous occupez de votre business.",
  'تحوّل أدفورتكس حضورك على فيسبوك وإنستغرام وتيك توك إلى زبائن حقيقيين. استراتيجية، محتوى فيديو وإدارة كاملة — نحن نتكفل بكل شيء، وأنت ركّز على تجارتك.'),
 ('Discuter sur WhatsApp', 'تحدث معنا على واتساب'),
 ('aria-label="Discuter sur WhatsApp"', 'aria-label="تحدث معنا على واتساب"'),
 ('>Voir nos réalisations</a>', '>شاهد أعمالنا</a>'),
 ('<span>Restaurants</span>', '<span>مطاعم</span>'),
 ('<span>Salons de thé</span>', '<span>مقاهي</span>'),
 ('<span>Salons de beauté</span>', '<span>صالونات تجميل</span>'),
 ('<span>Boutiques</span>', '<span>متاجر</span>'),
 ('<span>Entreprises</span>', '<span>شركات</span>'),
 ('<strong>Contenu qui convertit</strong>', '<strong>محتوى يحوّل المشاهدين إلى زبائن</strong>'),
 ('Reels • TikTok • Shooting pro', 'ريلز • تيك توك • تصوير احترافي'),
 ("var words=['FACEBOOK','INSTAGRAM','TIKTOK','PRODUCTION VIDÉO','STRATÉGIE DE CONTENU','PUBLICITÉ META','SHOOTING PRO','COMMUNITY MANAGEMENT'];",
  "var words=['فيسبوك','إنستغرام','تيك توك','إنتاج فيديو','استراتيجية محتوى','إعلانات ميتا','تصوير احترافي','إدارة المجتمع'];"),
 # ---- CHIFFRES ----
 ('>Nos résultats</span>', '>نتائجنا</span>'),
 ('Advortex en chiffres.', 'أدفورتكس بالأرقام.'),
 ('>Clients accompagnés</div>', '>زبائن رافقناهم</div>'),
 ('>Projets réalisés</div>', '>مشاريع أنجزناها</div>'),
 ('>Contenus créés</div>', '>محتوى أنشأناه</div>'),
 ('>Campagnes publicitaires</div>', '>حملات إعلانية</div>'),
 (">Secteurs d'activité</div>", '>قطاعات نشاط</div>'),
 ('>Créativité &amp; accompagnement</div>', '>إبداع ومرافقة</div>'),
 # ---- SERVICES ----
 ("<span class=\"eyebrow rv\">Ce qu'on fait</span>", '<span class="eyebrow rv">ماذا نفعل</span>'),
 ("Tout ce qu'il faut pour<br>dominer les réseaux.", 'كل ما تحتاجه<br>للسيطرة على الشبكات.'),
 ("Une seule équipe pour votre image entière : de la stratégie au tournage, jusqu'à la publication et le suivi.",
  'فريق واحد لصورتك الكاملة: من الاستراتيجية إلى التصوير، حتى النشر والمتابعة.'),
 ('<h3>Gestion des réseaux sociaux</h3>', '<h3>إدارة شبكات التواصل الاجتماعي</h3>'),
 ('On gère vos pages Facebook, Instagram et TikTok de A à Z : calendrier de contenu, publications, stories et réponses aux messages.',
  'ندير صفحاتكم على فيسبوك وإنستغرام وتيك توك من الألف إلى الياء: تقويم المحتوى، المنشورات، الستوري والرد على الرسائل.'),
 ('<h3>Production vidéo</h3>', '<h3>إنتاج الفيديو</h3>'),
 ("Tournage et montage professionnels : reels, TikToks, publicités vidéo. Un contenu qui arrête le scroll et donne envie d'acheter.",
  'تصوير ومونتاج احترافي: ريلز، تيك توك، إعلانات فيديو. محتوى يوقف التمرير ويشجّع على الشراء.'),
 ('<h3>Stratégie de contenu</h3>', '<h3>استراتيجية المحتوى</h3>'),
 ('Un plan clair chaque mois : quoi publier, quand et pourquoi. Chaque post a un objectif — visibilité, engagement ou ventes.',
  'خطة واضحة كل شهر: ماذا ننشر، متى ولماذا. لكل منشور هدف — ظهور، تفاعل أو مبيعات.'),
 ('<h3>Publicité ciblée</h3>', '<h3>إعلانات مستهدفة</h3>'),
 ('Des campagnes Meta Ads qui touchent les bonnes personnes, au bon endroit, avec le bon message. Chaque dinar est suivi.',
  'حملات ميتا الإعلانية تصل إلى الأشخاص المناسبين، في المكان المناسب، بالرسالة المناسبة. كل دينار مُتابَع.'),
 # ---- RÉALISATIONS ----
 ('<span class="eyebrow rv">Réalisations</span>', '<span class="eyebrow rv">أعمالنا</span>'),
 ('On ne promet pas.<br>On montre.', 'لا نَعِد.<br>نُظهِر.'),
 ("Voici un aperçu de notre univers : tournage, montage et contenu pensé pour convertir. Chaque client reçoit un contenu sur mesure, adapté à son secteur.",
  'إليك لمحة عن عالمنا: تصوير، مونتاج ومحتوى مصمّم للتحويل. كل زبون يحصل على محتوى مخصّص يناسب قطاعه.'),
 ('<b>Tournage sur place</b> — on vient chez vous avec notre équipe et notre matériel.',
  '<b>تصوير في عين المكان</b> — نأتي إليكم بفريقنا ومعدّاتنا.'),
 ("<b>Montage pro</b> — rythme, sous-titres, musique : un rendu qui retient l'attention.",
  '<b>مونتاج احترافي</b> — إيقاع، ترجمة، موسيقى: نتيجة تأسر الانتباه.'),
 ('<b>Validation avant publication</b> — vous voyez tout avant que ça sorte.',
  '<b>موافقة قبل النشر</b> — ترى كل شيء قبل أن يُنشر.'),
 ('Voir plus de réalisations', 'شاهد المزيد من أعمالنا'),
 ('alt="Stratégie digitale"', 'alt="استراتيجية رقمية"'),
 ('alt="Production et montage"', 'alt="إنتاج ومونتاج"'),
 ('alt="Image de marque"', 'alt="صورة العلامة"'),
 ('<span>Stratégie</span>', '<span>استراتيجية</span>'),
 ('<span>Production</span>', '<span>إنتاج</span>'),
 ('<span>Image de marque</span>', '<span>صورة العلامة</span>'),
 # ---- EN ACTION ----
 ('<span class="eyebrow rv">En action</span>', '<span class="eyebrow rv">في الميدان</span>'),
 ("<h2 class=\"rv\">Ce qu'on fait, en vrai.</h2>", '<h2 class="rv">ماذا نفعل، على أرض الواقع.</h2>'),
 ('Tournage sur le terrain, matériel pro et campagnes Meta Ads : un aperçu simple de notre quotidien, sans filtre.',
  'تصوير ميداني، معدّات احترافية وحملات ميتا الإعلانية: لمحة بسيطة عن يومياتنا، بدون فلتر.'),
 ('<span>Tournage</span>', '<span>تصوير</span>'),
 ('<span>Caméra</span>', '<span>كاميرا</span>'),
 ('<span>Meta Ads</span>', '<span>إعلانات ميتا</span>'),
 # ---- MÉTHODE ----
 ('<span class="eyebrow rv">Notre méthode</span>', '<span class="eyebrow rv">منهجيتنا</span>'),
 ('Simple. Claire. Efficace.', 'بسيطة. واضحة. فعّالة.'),
 ("Pas de jargon, pas de promesses floues. Un processus en 4 étapes que vous suivez en temps réel.",
  'بدون مصطلحات معقدة، وبدون وعود غامضة. عملية من 4 خطوات تتابعها لحظة بلحظة.'),
 ('<h3>Audit gratuit</h3>', '<h3>تدقيق مجاني</h3>'),
 ('On analyse vos pages, vos concurrents et votre marché. Vous savez exactement où vous en êtes.',
  'نحلّل صفحاتكم ومنافسيكم وسوقكم. ستعرف بالضبط أين أنت.'),
 ('<h3>Stratégie sur mesure</h3>', '<h3>استراتيجية مخصّصة</h3>'),
 ("Un plan de contenu clair, adapté à votre business et à vos objectifs. Rien n'est laissé au hasard.",
  'خطة محتوى واضحة تناسب تجارتك وأهدافك. لا شيء يُترك للصدفة.'),
 ('<h3>Production</h3>', '<h3>الإنتاج</h3>'),
 ('Tournage, montage, design : notre équipe crée le contenu. Vous validez chaque pièce avant publication.',
  'تصوير، مونتاج، تصميم: فريقنا يُنشئ المحتوى. توافق على كل قطعة قبل النشر.'),
 ('<h3>Publication & suivi</h3>', '<h3>النشر والمتابعة</h3>'),
 ('On publie, on répond à votre communauté, on mesure. Vous recevez un rapport clair chaque mois.',
  'ننشر، نردّ على مجتمعك، ونقيس النتائج. تتلقى تقريرًا واضحًا كل شهر.'),
 # ---- PACKS ----
 ('<span class="eyebrow rv">Nos packs</span>', '<span class="eyebrow rv">باقاتنا</span>'),
 ('Un pack pour chaque ambition.', 'باقة لكل طموح.'),
 ('Des formules mensuelles sans surprise, ajustées à votre secteur après un appel découverte gratuit.',
  'صيغ شهرية واضحة بدون مفاجآت، تُكيَّف مع قطاعك بعد مكالمة استكشافية مجانية.'),
 ('Voir les packs →', 'شاهد الباقات ←'),
 ('<h3>Premium</h3>', '<h3>بريميوم</h3>'),
 ('<h3>Pro</h3>', '<h3>برو</h3>'),
 ('<h3>Personnalisé</h3>', '<h3>مخصّصة</h3>'),
 ('<div class="price">70 000 DZD<span> / mois</span></div>', '<div class="price">70 000 دج<span> / شهريًا</span></div>'),
 ('<div class="price">95 000 DZD<span> / mois</span></div>', '<div class="price">95 000 دج<span> / شهريًا</span></div>'),
 ('<div class="price">Sur devis</div>', '<div class="price">حسب الطلب</div>'),
 ('<div class="tag">LE PLUS CHOISI</div>', '<div class="tag">الأكثر اختيارًا</div>'),
 ('Pour démarrer fort sur les réseaux', 'لانطلاقة قوية على الشبكات'),
 ('Pour accélérer et attirer des clients', 'للتسريع وجذب الزبائن'),
 ("Vous composez, on s'occupe du reste", 'أنت تختار، ونحن نتكفل بالباقي'),
 ('<li>4 reels / mois</li>', '<li>4 ريلز / شهريًا</li>'),
 ('<li>8 posts / mois</li>', '<li>8 منشورات / شهريًا</li>'),
 ('<li>30 stories / mois</li>', '<li>30 ستوري / شهريًا</li>'),
 ('<li>8 reels / mois</li>', '<li>8 ريلز / شهريًا</li>'),
 ('<li>16 posts / mois</li>', '<li>16 منشورًا / شهريًا</li>'),
 ('<li>Stories illimitées</li>', '<li>ستوري غير محدودة</li>'),
 ('<li>Gestion complète de vos pages</li>', '<li>إدارة كاملة لصفحاتكم</li>'),
 ('<li>Réponses aux messages</li>', '<li>الرد على الرسائل</li>'),
 ('<li>Réponses aux messages & commentaires</li>', '<li>الرد على الرسائل والتعليقات</li>'),
 ('<li>Publication du contenu</li>', '<li>نشر المحتوى</li>'),
 ('<li>Campagnes sponsorisées (budget à votre charge)</li>', '<li>حملات مموّلة (الميزانية على عاتقكم)</li>'),
 ('<li>Organisation du calendrier de contenu</li>', '<li>تنظيم تقويم المحتوى</li>'),
 ('<li>Rapport détaillé + appel mensuel</li>', '<li>تقرير مفصّل + مكالمة شهرية</li>'),
 ("Reels, posts, stories, tournages, gestion des pages, publicité… <b style=\"color:#fff\">c'est vous qui choisissez</b> ce dont votre business a besoin. On construit ensemble un pack sur mesure, avec un devis clair et sans engagement.",
  'ريلز، منشورات، ستوري، تصوير، إدارة الصفحات، إعلانات… <b style="color:#fff">أنت من يختار</b> ما تحتاجه تجارتك. نبني معًا باقة مخصّصة، مع عرض سعر واضح وبدون التزام.'),
 ('>Choisir Premium</a>', '>اختر بريميوم</a>'),
 ('>Choisir Pro</a>', '>اختر برو</a>'),
 ('>Demander un devis</a>', '>اطلب عرض سعر</a>'),
 ('Choisissez votre formule.', 'اختر صيغتك.'),
 ('Des formules mensuelles claires, sans surprise. Chaque pack est ajusté à votre secteur après un appel découverte gratuit.',
  'صيغ شهرية واضحة، بدون مفاجآت. تُكيَّف كل باقة مع قطاعك بعد مكالمة استكشافية مجانية.'),
 # ---- TÉMOIGNAGES ----
 ('<span class="eyebrow rv">Témoignages</span>', '<span class="eyebrow rv">آراء زبائننا</span>'),
 ('Ils nous font confiance.', 'يثقون بنا.'),
 ('Des business qui ont décidé de passer au niveau supérieur avec Advortex.',
  'تجار قرروا الارتقاء إلى المستوى الأعلى مع أدفورتكس.'),
 ('<span>Propriétaire de restaurant</span>', '<span>صاحب مطعم</span>'),
 ('<span>Entrepreneur</span>', '<span>مقاول</span>'),
 ("<span>Gérante d'entreprise</span>", '<span>مسؤولة شركة</span>'),
 # ---- FAQ ----
 ('<span class="eyebrow rv">FAQ</span>', '<span class="eyebrow rv">الأسئلة الشائعة</span>'),
 ('Questions fréquentes.', 'أسئلة شائعة.'),
 ('Combien coûtent vos services ?', 'كم تكلف خدماتكم؟'),
 ("Chaque business est différent : secteur, objectifs, volume de contenu. C'est pourquoi on commence toujours par un appel découverte gratuit, puis on vous envoie un devis clair et sans engagement. Pas de frais cachés, jamais.",
  'كل تجارة مختلفة: القطاع، الأهداف، حجم المحتوى. لذلك نبدأ دائمًا بمكالمة استكشافية مجانية، ثم نرسل لكم عرض سعر واضحًا وبدون التزام. لا رسوم خفية، أبدًا.'),
 ('En combien de temps verrai-je des résultats ?', 'متى سأرى النتائج؟'),
 ("Les premiers effets (plus de vues, plus d'engagement) arrivent généralement dès le premier mois. Pour des résultats solides et mesurables — abonnés qualifiés, messages clients, ventes — comptez 2 à 3 mois de travail régulier. Le marketing digital est un marathon, pas un sprint.",
  'التأثيرات الأولى (مزيد من المشاهدات والتفاعل) تظهر عادة من الشهر الأول. أما النتائج القوية والقابلة للقياس — متابعون مؤهلون، رسائل زبائن، مبيعات — فتتطلب 2 إلى 3 أشهر من العمل المنتظم. التسويق الرقمي ماراثون، وليس سباق سرعة.'),
 ('Avec quels secteurs travaillez-vous ?', 'مع أي القطاعات تعملون؟'),
 ('Notre spécialité : les restaurants, salons de thé, salons de beauté, boutiques et entreprises locales. Si votre business a besoin de visibilité et de clients, on peut vous aider — parlons-en.',
  'تخصصنا: المطاعم، المقاهي، صالونات التجميل، المتاجر والشركات المحلية. إذا كانت تجارتك تحتاج إلى الظهور والزبائن، يمكننا مساعدتك — لنتحدث.'),
 ('Dois-je fournir le contenu moi-même ?', 'هل يجب أن أقدّم المحتوى بنفسي؟'),
 ("Non. On s'occupe de tout : idées, tournage sur place, montage, textes, publication. Vous validez simplement chaque contenu avant qu'il soit publié. Vous n'avez qu'à gérer votre business.",
  'لا. نحن نتكفل بكل شيء: الأفكار، التصوير في عين المكان، المونتاج، النصوص، النشر. أنت فقط توافق على كل محتوى قبل نشره. كل ما عليك هو إدارة تجارتك.'),
 ('Puis-je arrêter mon abonnement quand je veux ?', 'هل يمكنني إيقاف اشتراكي متى أردت؟'),
 ('Oui. Nos formules sont mensuelles et sans engagement longue durée. Un simple préavis suffit. On préfère vous garder par nos résultats, pas par un contrat.',
  'نعم. صيغنا شهرية وبدون التزام طويل الأمد. يكفي إشعار بسيط. نفضّل أن نحتفظ بك بنتائجنا، لا بعقد.'),
 # ---- CONTACT ----
 ('<span class="eyebrow rv">Contact</span>', '<span class="eyebrow rv">اتصل بنا</span>'),
 ('Prêt à faire décoller<br>votre business ?', 'مستعد لإقلاع<br>تجارتك؟'),
 ("Laissez-nous un message — on vous répond vite, et le premier appel découverte est gratuit.",
  'اترك لنا رسالة — نردّ عليك بسرعة، والمكالمة الاستكشافية الأولى مجانية.'),
 ('<span><b>WhatsApp</b><br>', '<span><b>واتساب</b><br>'),
 ('<span><b>Téléphone</b><br>', '<span><b>هاتف</b><br>'),
 ('<span><b>Adresse</b><br>Alger, Algérie</span>', '<span><b>العنوان</b><br>الجزائر العاصمة، الجزائر</span>'),
 ('<span><b>Instagram</b><br>', '<span><b>إنستغرام</b><br>'),
 ('<span><b>Facebook</b><br>Advortex</span>', '<span><b>فيسبوك</b><br>أدفورتكس</span>'),
 ('Démarrer sur WhatsApp', 'ابدأ على واتساب'),
 ('<label>Votre nom</label>', '<label>اسمك</label>'),
 ('placeholder="Ex : Amine Benali"', 'placeholder="مثال: أمين بن علي"'),
 ('<label>Votre business</label>', '<label>تجارتك</label>'),
 ('placeholder="Ex : Restaurant Le Délice, Hydra"', 'placeholder="مثال: مطعم الديليس، حيدرة"'),
 ('<label>Pack souhaité</label>', '<label>الباقة المرغوبة</label>'),
 ('<option>Je ne sais pas encore</option>', '<option>لا أعرف بعد</option>'),
 ('<option>Premium</option>', '<option>بريميوم</option>'),
 ('<option>Pro</option>', '<option>برو</option>'),
 ('<option>Personnalisé</option>', '<option>مخصّصة</option>'),
 ('<label>Votre message</label>', '<label>رسالتك</label>'),
 ('placeholder="Parlez-nous de votre besoin..."', 'placeholder="حدثنا عن احتياجك..."'),
 ('>Envoyer via WhatsApp</button>', '>أرسل عبر واتساب</button>'),
 ("En cliquant, WhatsApp s'ouvre avec votre message pré-rempli. Rien n'est stocké en ligne.",
  'بالضغط، يُفتح واتساب برسالتك جاهزة. لا يُخزَّن أي شيء على الإنترنت.'),
 # ---- FOOTER ----
 ('Agence de marketing digital à Alger. On transforme votre présence en ligne en clients réels.',
  'وكالة تسويق رقمي في الجزائر. نحوّل حضورك على الإنترنت إلى زبائن حقيقيين.'),
 ('<h4>NAVIGATION</h4>', '<h4>روابط</h4>'),
 ('<h4>CONTACT</h4>', '<h4>اتصل بنا</h4>'),
 ('<h4>SUIVEZ-NOUS</h4>', '<h4>تابعنا</h4>'),
 ('>WhatsApp</a>', '>واتساب</a>'),
 ('>Instagram</a>', '>إنستغرام</a>'),
 ('>Facebook</a>', '>فيسبوك</a>'),
 ('© 2026 Advortex — Tous droits réservés.', '© 2026 أدفورتكس — جميع الحقوق محفوظة.'),
 ('<span>Alger, Algérie</span>', '<span>الجزائر العاصمة، الجزائر</span>'),
 # ---- leadForm JS ----
 ("var txt='Bonjour Advortex !%0A%0A'", "var txt='مرحبا أدفورتكس!%0A%0A'"),
 ("+'Nom : '+", "+'الاسم : '+"),
 ("+'Business : '+", "+'التجارة : '+"),
 ("+'Pack : '+", "+'الباقة : '+"),
 ("+'Message : '+", "+'الرسالة : '+"),
]

RTL_CSS = """<style>
/* ===== RTL / Arabic ===== */
html[dir="rtl"] body{font-family:'Cairo',sans-serif}
html[dir="rtl"] h1,html[dir="rtl"] h2,html[dir="rtl"] h3,html[dir="rtl"] h4,html[dir="rtl"] .btn,html[dir="rtl"] .faq-q,html[dir="rtl"] .g-item span,html[dir="rtl"] .pack .tag,html[dir="rtl"] .step::before{font-family:'Cairo',sans-serif}
html[dir="rtl"] .eyebrow,html[dir="rtl"] .pack .tag{letter-spacing:0}
html[dir="rtl"] .pack li{padding-left:0;padding-right:36px}
html[dir="rtl"] .pack li::before{left:auto;right:0}
html[dir="rtl"] .faq-q{text-align:right}
html[dir="rtl"] .hero-badge{left:auto;right:-30px}
@media(max-width:900px){html[dir="rtl"] .hero-badge{right:0}}
.lang-sw{border:1px solid var(--line);border-radius:100px;padding:8px 18px !important}
</style>
</head>"""

def build(src, dst, title, og_url, extra_link_fixes=None, switcher_flips=None):
    t = open(src, encoding='utf-8').read()
    # structural link fixes first
    if extra_link_fixes:
        for a, b in extra_link_fixes:
            t = t.replace(a, b)
    if switcher_flips:
        for a, b in switcher_flips:
            t = t.replace(a, b)
    # wa links
    for a, b in WA.items():
        t = t.replace(a, b)
    # title + og url
    t = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, t, count=1)
    t = re.sub(r'(<meta property="og:url" content=")[^"]*(")', r'\g<1>' + og_url + r'\g<2>', t)
    # translations longest-first
    for fr, ar in sorted(TR, key=lambda p: -len(p[0])):
        if fr in t:
            t = t.replace(fr, ar)
    # rtl css
    t = t.replace('</head>', RTL_CSS, 1)
    open(dst, 'w', encoding='utf-8').write(t)
    print('wrote', dst, len(t))

if __name__ == '__main__':
    build('index.html', 'index-ar.html',
          'أدفورتكس — وكالة التسويق الرقمي في الجزائر | شبكات التواصل، فيديو، استراتيجية',
          'https://advortex-agency.vercel.app/index-ar.html',
          extra_link_fixes=[('href="packs.html"', 'href="packs-ar.html"')],
          switcher_flips=[('href="index-ar.html" class="lang-sw">عربية</a>', 'href="index.html" class="lang-sw">FR</a>'),
                            ('<a href="index-ar.html">عربية</a>', '<a href="index.html">FR</a>')])
    build('packs.html', 'packs-ar.html',
          'باقاتنا — أدفورتكس | وكالة التسويق الرقمي في الجزائر',
          'https://advortex-agency.vercel.app/packs-ar.html',
          extra_link_fixes=[('href="index.html', 'href="index-ar.html'), ('href="packs.html"', 'href="packs-ar.html"')],
          switcher_flips=[('href="packs-ar.html" class="lang-sw">عربية</a>', 'href="packs.html" class="lang-sw">FR</a>'),
                            ('<a href="packs-ar.html">عربية</a>', '<a href="packs.html">FR</a>')])
