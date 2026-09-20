#!/usr/bin/env python3
"""Deploy advortex-website to Vercel via file-upload API, then move the prod alias."""
import hashlib, json, os, sys, urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

BASE = "https://api.vercel.com"
ALLOWED = ["api.vercel.com"]
PROJECT_ID = "prj_PV7HCt4xvEso62OwEEpmqKwuZNWR"
ALIAS = "advortex-agency.vercel.app"
SITE = os.path.expanduser("~/workspace/your_files/advortex-website")

def req(method, path, data=None, headers=None):
    r = urllib.request.Request(BASE + path, data=data, method=method)
    for k, v in (headers or {}).items():
        r.add_header(k, v)
    add_surrogate_to_request(r, "custom.vercel", entry_name="access_token", allowed_hosts=ALLOWED)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return read_json_response(resp)

def collect():
    out = []
    for root, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', 'previews')]
        for fn in files:
            p = os.path.join(root, fn)
            if fn.endswith(('.py', '.md')) and root == SITE:
                continue
            rel = os.path.relpath(p, SITE)
            out.append((rel, p))
    return sorted(out)

def main():
    files = collect()
    print(f"{len(files)} files to upload")
    tree = []
    for rel, p in files:
        data = open(p, 'rb').read()
        sha = hashlib.sha1(data).hexdigest()
        r = req("POST", "/v2/files", data=data,
                headers={"Content-Type": "application/octet-stream", "x-vercel-digest": sha})
        # dedupe: API returns existing file info
        fsha = r.get("sha", sha)
        tree.append({"file": rel, "sha": fsha, "size": len(data)})
    print("uploaded, creating deployment...")
    dep = req("POST", "/v13/deployments", data=json.dumps({
        "name": "advortex-agency",
        "project": PROJECT_ID,
        "target": "production",
        "files": tree,
    }).encode(), headers={"Content-Type": "application/json"})
    uid = dep["id"]
    print("deployment:", uid, dep.get("url"))
    # wait for ready
    import time
    for _ in range(40):
        d = req("GET", f"/v13/deployments/{uid}")
        st = d.get("readyState")
        if st == "READY":
            break
        if st == "ERROR":
            print("DEPLOY ERROR", json.dumps(d)[:500]); return 1
        time.sleep(10)
    print("state:", st)
    # move alias
    a = req("POST", f"/v2/deployments/{uid}/aliases",
            data=json.dumps({"alias": ALIAS}).encode(),
            headers={"Content-Type": "application/json"})
    print("alias moved:", a.get("alias"))
    print("DONE", uid)

if __name__ == "__main__":
    main()
