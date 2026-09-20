#!/usr/bin/env python3
"""Swap emoji tiles/letter avatars in the before/after slider for real photos.
Run only after all 14 ba-*.jpg assets exist."""
import os, re, sys

BASE = "/home/hatch/workspace/your_files/advortex-website"
A = f"{BASE}/assets"

need = ["ba-avatar-avant.jpg", "ba-avatar-apres.jpg"] + \
       [f"ba-avant-{i}.jpg" for i in range(1, 7)] + \
       [f"ba-apres-{i}.jpg" for i in range(1, 7)]
missing = [f for f in need if not os.path.exists(f"{A}/{f}")]
if missing:
    sys.exit(f"MISSING: {missing}")

CSS_ADD = (".ig-grid img{width:100%;height:100%;object-fit:cover;display:block}"
           ".ig-avatar{overflow:hidden}"
           ".ig-avatar img{width:100%;height:100%;object-fit:cover;display:block}")

def patch_html(src):
    # css
    assert ".ig-grid>div{display:flex" in src
    src = src.replace(".ig-grid>div{display:flex;align-items:center;justify-content:center;font-size:26px;overflow:hidden}",
                      ".ig-grid>div{display:flex;align-items:center;justify-content:center;font-size:26px;overflow:hidden}" + CSS_ADD, 1)
    # avatars
    src = src.replace('<div class="ig-avatar" style="background:#3d3d3d;color:#777">M</div>',
                      '<div class="ig-avatar"><img src="assets/ba-avatar-avant.jpg" alt="Ma Boutique"></div>', 1)
    src = src.replace('<div class="ig-avatar" style="background:#000;color:#fff;border:2px solid #fff">M</div>',
                      '<div class="ig-avatar" style="border:2px solid #fff"><img src="assets/ba-avatar-apres.jpg" alt="Ma Boutique"></div>', 1)
    # before grid tiles (gradient divs) -> ba-avant-N
    n = [0]
    def rep_before(m):
        n[0] += 1
        return f'<div><img src="assets/ba-avant-{n[0]}.jpg" alt=""></div>'
    src = re.sub(r'<div style="background:linear-gradient\(135deg,#[0-9a-f]+,#[0-9a-f]+\)">[^<]*</div>', rep_before, src)
    assert n[0] == 6, f"before tiles: {n[0]}"
    # after grid tiles (dark tiles with span) -> ba-apres-N
    m2 = [0]
    def rep_after(m):
        m2[0] += 1
        return f'<div><img src="assets/ba-apres-{m2[0]}.jpg" alt=""></div>'
    src = re.sub(r'<div style="background:#(?:151515|202020)"><span[^<]*</span></div>', rep_after, src)
    assert m2[0] == 6, f"after tiles: {m2[0]}"
    return src

for fn in ["index.html", "index-ar.html", "build_slider.py"]:
    p = f"{BASE}/{fn}"
    src = open(p, encoding="utf-8").read()
    if "ba-avant-1.jpg" in src:
        print("already patched ->", fn); continue
    open(p, "w", encoding="utf-8").write(patch_html(src))
    print("photos in ->", fn)
