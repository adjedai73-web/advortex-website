#!/usr/bin/env python3
"""Replace #etude-cas two-cards with an interactive before/after drag slider
showing a fictional boutique page transformation (detailed mockup). FR + AR."""
import re

BASE = "/home/hatch/workspace/your_files/advortex-website"

CSS = """
<style>
.ba-wrap{max-width:400px;margin:44px auto 0}
.ba-slider{position:relative;border-radius:26px;overflow:hidden;border:1px solid #2c2c2c;background:#000;aspect-ratio:9/14;touch-action:pan-y;cursor:ew-resize;user-select:none;-webkit-user-select:none}
.ba-layer{position:absolute;inset:0}
.ba-before{clip-path:inset(0 calc(100% - var(--pos,50%)) 0 0);z-index:2}
.ba-tag{position:absolute;top:14px;z-index:4;font-family:'Montserrat';font-weight:700;font-size:11px;letter-spacing:2px;padding:7px 14px;border-radius:100px}
.ba-tag-before{left:14px;background:#3a3a3a;color:#fff}
.ba-tag-after{right:14px;background:#fff;color:#000}
.ba-handle{position:absolute;top:0;bottom:0;left:var(--pos,50%);width:4px;background:#fff;z-index:3;transform:translateX(-50%);pointer-events:none}
.ba-handle span{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:48px;height:48px;border-radius:50%;background:#fff;color:#000;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:800;box-shadow:0 4px 18px rgba(0,0,0,.55)}
.ig{background:#000;color:#fff;height:100%;display:flex;flex-direction:column;font-size:12px}
.ig-top{display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-bottom:1px solid #1c1c1c;font-weight:700;font-size:13px}
.ig-profile{display:flex;gap:12px;padding:14px;align-items:center}
.ig-avatar{width:62px;height:62px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-family:'Montserrat';font-weight:800;font-size:22px}
.ig-stats{display:flex;flex:1;justify-content:space-around;text-align:center}
.ig-stats b{display:block;font-size:15px}
.ig-stats span{color:#999;font-size:10.5px}
.ig-bio{padding:0 14px;font-size:12.5px;line-height:1.55}
.ig-link{color:#d7d7d7;font-weight:600}
.ig-btns{display:flex;gap:8px;padding:12px 14px}
.ig-btn{flex:1;text-align:center;padding:8px;border-radius:8px;font-weight:700;font-size:13px}
.ig-hl{display:flex;gap:12px;padding:2px 14px 12px}
.ig-hl div{text-align:center;font-size:10px;color:#ccc}
.ig-hl i{width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:19px;margin-bottom:4px;font-style:normal;background:#111;border:1px solid #444}
.ig-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;flex:1;min-height:0}
.ig-grid>div{display:flex;align-items:center;justify-content:center;font-size:26px;overflow:hidden}.ig-grid img{width:100%;height:100%;object-fit:cover;display:block}.ig-avatar{overflow:hidden}.ig-avatar img{width:100%;height:100%;object-fit:cover;display:block}
</style>
"""

BEFORE = """
    <div class="ba-layer ba-before"><div class="ig">
      <div class="ig-top"><span>ma.boutique.dz</span><span style="color:#555">&#8942;</span></div>
      <div class="ig-profile">
        <div class="ig-avatar"><img src="assets/ba-avatar-avant.jpg" alt="Ma Boutique"></div>
        <div class="ig-stats"><div><b>9</b><span>posts</span></div><div><b>214</b><span>abonn&eacute;s</span></div><div><b>63</b><span>abonn.</span></div></div>
      </div>
      <div class="ig-bio"><b>Ma Boutique</b><br><span style="color:#999">Bienvenue dans notre boutique &#10084;&#65039;&#10084;&#65039;<br>Nouveaut&eacute;s chaque semaine &#127881;&#127881;</span></div>
      <div class="ig-btns"><div class="ig-btn" style="background:#2a2a2a;color:#fff">Suivre</div><div class="ig-btn" style="background:#161616;color:#777">Message</div></div>
      <div class="ig-grid">
        <div><img src="assets/ba-avant-1.jpg" alt=""></div>
        <div><img src="assets/ba-avant-2.jpg" alt=""></div>
        <div><img src="assets/ba-avant-3.jpg" alt=""></div>
        <div><img src="assets/ba-avant-4.jpg" alt=""></div>
        <div><img src="assets/ba-avant-5.jpg" alt=""></div>
        <div><img src="assets/ba-avant-6.jpg" alt=""></div>
      </div>
    </div></div>
"""

AFTER = """
    <div class="ba-layer"><div class="ig">
      <div class="ig-top"><span>ma.boutique.dz</span><span style="color:#555">&#8942;</span></div>
      <div class="ig-profile">
        <div class="ig-avatar" style="border:2px solid #fff"><img src="assets/ba-avatar-apres.jpg" alt="Ma Boutique"></div>
        <div class="ig-stats"><div><b>47</b><span>posts</span></div><div><b>1 842</b><span>abonn&eacute;s</span></div><div><b>120</b><span>abonn.</span></div></div>
      </div>
      <div class="ig-bio"><b>Ma Boutique | Alger &#128722;</b><br><span style="color:#ccc">&#10024; Nouveaut&eacute;s chaque semaine<br>&#128666; Livraison 58 wilayas<br>&#128071; Commandez ici</span><br><span class="ig-link">&#128279; linktr.ee/maboutique</span></div>
      <div class="ig-btns"><div class="ig-btn" style="background:#fff;color:#000">Suivre</div><div class="ig-btn" style="background:#161616;color:#fff;border:1px solid #3a3a3a">Contacter</div></div>
      <div class="ig-hl">
        <div><i>&#10024;</i>Nouveau</div>
        <div><i>&#11088;</i>Avis</div>
        <div><i>%</i>Promo</div>
        <div><i>&#128205;</i>Contact</div>
      </div>
      <div class="ig-grid">
        <div><img src="assets/ba-apres-1.jpg" alt=""></div>
        <div><img src="assets/ba-apres-2.jpg" alt=""></div>
        <div><img src="assets/ba-apres-3.jpg" alt=""></div>
        <div><img src="assets/ba-apres-4.jpg" alt=""></div>
        <div><img src="assets/ba-apres-5.jpg" alt=""></div>
        <div><img src="assets/ba-apres-6.jpg" alt=""></div>
      </div>
    </div></div>
"""

JS = """
<script>
(function(){var s=document.getElementById('baSlider');if(!s)return;
var set=function(x){var r=s.getBoundingClientRect();var p=(x-r.left)/r.width*100;p=Math.max(8,Math.min(92,p));s.style.setProperty('--pos',p+'%');};
var drag=false;
s.addEventListener('pointerdown',function(e){drag=true;try{s.setPointerCapture(e.pointerId);}catch(_){}set(e.clientX);});
s.addEventListener('pointermove',function(e){if(drag)set(e.clientX);});
s.addEventListener('pointerup',function(){drag=false;});
s.addEventListener('pointercancel',function(){drag=false;});})();
</script>
"""

def slider_section(tag_b, tag_a, note):
    return f"""
  <div class="ba-wrap rv">
    <div class="ba-slider" id="baSlider">
{AFTER}
{BEFORE}
      <span class="ba-tag ba-tag-before">{tag_b}</span>
      <span class="ba-tag ba-tag-after">{tag_a}</span>
      <div class="ba-handle"><span>&#8596;</span></div>
    </div>
    <p style="text-align:center;color:var(--dim);font-size:12.5px;margin-top:14px">{note}</p>
  </div>
"""

FR_SECTION = CSS + """
<section id="etude-cas" style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">Avant / Apr&egrave;s</span>
      <h2 class="rv">Tirez et voyez<br>la diff&eacute;rence.</h2>
      <p class="lead rv">Exemple : la transformation d'une page boutique avec notre m&eacute;thode.<br><b style="color:#fff">Tirez le curseur</b> pour comparer.</p>
    </div>
""" + slider_section("AVANT", "APR&Egrave;S", "Exemple illustratif &mdash; les chiffres sont fictifs, la m&eacute;thode est bien r&eacute;elle.") + """
    <div class="center rv" style="margin-top:36px">
      <p style="color:var(--muted);font-size:15px;margin-bottom:24px">Notre propre page : <b style="color:#fff">@advortex.off</b> &mdash; <b style="color:#fff">1 639</b> abonn&eacute;s <span style="color:var(--dim)">(chiffres r&eacute;els, sept. 2026)</span></p>
      <a class="btn btn-ghost" href="https://www.instagram.com/advortex.off" target="_blank" rel="noopener">Voir notre page &rarr;</a>
    </div>
  </div>
</section>
""" + JS

AR_SECTION = CSS + """
<section id="etude-cas" style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow rv">قبل / بعد</span>
      <h2 class="rv">جرّ وشوف<br>الفرق.</h2>
      <p class="lead rv">مثال: تحويل صفحة متجر بالمنهجية تاعنا.<br><b style="color:#fff">جرّ المؤشر</b> باش تقارن.</p>
    </div>
""" + slider_section("قبل", "بعد", "مثال توضيحي &mdash; الأرقام خيالية، والمنهجية حقيقية.") + """
    <div class="center rv" style="margin-top:36px">
      <p style="color:var(--muted);font-size:15px;margin-bottom:24px">صفحتنا: <b style="color:#fff">@advortex.off</b> &mdash; <b style="color:#fff">1 639</b> متابع <span style="color:var(--dim)">(أرقام حقيقية، سبتمبر 2026)</span></p>
      <a class="btn btn-ghost" href="https://www.instagram.com/advortex.off" target="_blank" rel="noopener">&larr; شوف صفحتنا</a>
    </div>
  </div>
</section>
""" + JS

PAT = re.compile(r'<section id="etude-cas".*?</section>', re.DOTALL)

for path, new in [("index.html", FR_SECTION), ("index-ar.html", AR_SECTION)]:
    p = f"{BASE}/{path}"
    src = open(p, encoding="utf-8").read()
    assert PAT.search(src), f"section not found in {path}"
    src = PAT.sub(new.strip(), src, count=1)
    open(p, "w", encoding="utf-8").write(src)
    print("slider ->", path)
