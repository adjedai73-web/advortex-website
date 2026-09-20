#!/usr/bin/env python3
"""Add 'Audit gratuit' + 'Plan 30 jours' sections to packs.html and packs-ar.html."""
from urllib.parse import quote

BASE = "/home/hatch/workspace/your_files/advortex-website"

FR_AUDIT = """
<section id="audit">
  <div class="wrap center">
    <span class="eyebrow rv">Offert</span>
    <h2 class="rv">Audit Instagram gratuit &mdash; sous 48h.</h2>
    <p class="lead rv">On analyse votre page : bio, contenu, stories, engagement&hellip; Vous recevez un rapport clair avec 5 actions concr&egrave;tes &agrave; appliquer &mdash; m&ecirc;me si vous ne travaillez pas avec nous. Sans engagement.</p>
    <div class="rv" style="margin-top:32px">
      <a class="btn btn-wa" href="AUDIT_WA" target="_blank" rel="noopener">Recevoir mon audit gratuit</a>
    </div>
  </div>
</section>
""".replace("AUDIT_WA", "https://wa.me/213672645825?text=" + quote("Bonjour Advortex ! Je veux mon audit Instagram gratuit."))

FR_PLAN = """
<section id="plan30" style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">Onboarding</span>
      <h2 class="rv">Vos 30 premiers jours avec Advortex.</h2>
      <p class="lead rv">Une m&eacute;thode claire, semaine par semaine. Vous savez toujours o&ugrave; on en est.</p>
    </div>
    <div class="steps">
      <div class="step rv"><h3>Semaine 1 &mdash; Audit + Strat&eacute;gie</h3><p>On analyse votre page et vos concurrents, on d&eacute;finit la ligne &eacute;ditoriale et le calendrier de contenu.</p></div>
      <div class="step rv"><h3>Semaine 2 &mdash; Tournage</h3><p>Notre &eacute;quipe vient filmer (reels, photos) et on optimise votre page : bio, highlights, photo de profil.</p></div>
      <div class="step rv"><h3>Semaine 3 &mdash; Lancement</h3><p>Publication du contenu, stories quotidiennes, lancement du sponsoris&eacute; si besoin.</p></div>
      <div class="step rv"><h3>Semaine 4 &mdash; Bilan</h3><p>Rapport simple avec les stats du mois, ajustements, et plan du mois suivant.</p></div>
    </div>
    <div class="center rv" style="margin-top:44px">
      <a class="btn btn-white" href="booking.html">R&eacute;server un appel gratuit</a>
    </div>
  </div>
</section>
"""

AR_AUDIT = """
<section id="audit">
  <div class="wrap center">
    <span class="eyebrow rv">مجانًا</span>
    <h2 class="rv">تدقيق إنستغرام مجاني &mdash; خلال 48 ساعة.</h2>
    <p class="lead rv">نحلّل صفحتك: البايو، المحتوى، الستوري، التفاعل&hellip; تستلم تقريرًا واضحًا مع 5 خطوات عملية تطبّقها &mdash; حتى لو ما اشتغلتش معانا. بدون أي التزام.</p>
    <div class="rv" style="margin-top:32px">
      <a class="btn btn-wa" href="AUDIT_WA" target="_blank" rel="noopener">استلم التدقيق المجاني</a>
    </div>
  </div>
</section>
""".replace("AUDIT_WA", "https://wa.me/213672645825?text=" + quote("مرحبا أدفورتكس! أريد التدقيق المجاني لحسابي على إنستغرام."))

AR_PLAN = """
<section id="plan30" style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">الانطلاقة</span>
      <h2 class="rv">أول 30 يوم مع أدفورتكس.</h2>
      <p class="lead rv">منهجية واضحة، أسبوع بأسبوع. دايمًا تعرف وين رانا واصلين.</p>
    </div>
    <div class="steps">
      <div class="step rv"><h3>الأسبوع 1 &mdash; التدقيق + الاستراتيجية</h3><p>نحلّل صفحتك ومنافسيك، نحدّد الخط التحريري وتقويم المحتوى.</p></div>
      <div class="step rv"><h3>الأسبوع 2 &mdash; التصوير</h3><p>فريقنا يجي يصوّر (ريلز، صور) ونحسّن صفحتك: البايو، الهايلايت، صورة البروفايل.</p></div>
      <div class="step rv"><h3>الأسبوع 3 &mdash; الإطلاق</h3><p>نشر المحتوى، ستوري يومية، وإطلاق الإعلانات المموّلة إذا لزم الأمر.</p></div>
      <div class="step rv"><h3>الأسبوع 4 &mdash; الحصيلة</h3><p>تقرير بسيط مع إحصائيات الشهر، تعديلات، وخطة الشهر الموالي.</p></div>
    </div>
    <div class="center rv" style="margin-top:44px">
      <a class="btn btn-white" href="booking-ar.html">احجز مكالمة مجانية</a>
    </div>
  </div>
</section>
"""

for fname, audit, plan in [("packs.html", FR_AUDIT, FR_PLAN), ("packs-ar.html", AR_AUDIT, AR_PLAN)]:
    p = f"{BASE}/{fname}"
    with open(p, encoding="utf-8") as f:
        html = f.read()
    assert html.count('id="audit"') == 0, f"already added in {fname}"
    marker = '<section id="contact"'
    assert marker in html, f"contact section not found in {fname}"
    html = html.replace(marker, audit + "\n" + plan + "\n" + marker, 1)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print("updated", fname)
