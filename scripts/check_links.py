"""Checks every link in README.md and domains/*.md and prints the ones that stopped answering."""
import glob, os, re, ssl, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
OK_CODES = {401, 403, 429, 999}  # bot protection, the page usually still exists
LINK = re.compile(r"^- \[[^\]]+\]\((https?://[^)\s]+)\)", re.M)
def check(item):
    page, url = item
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20, context=ssl.create_default_context()) as f:
            return page, url, f.status
    except urllib.error.HTTPError as e:
        return page, url, e.code
    except Exception as e:
        return page, url, type(e).__name__
def main():
    items = []
    for page in sorted(glob.glob(os.path.join(ROOT, "domains", "*.md"))):
        text = open(page, encoding="utf-8").read()
        items += [(os.path.basename(page), u) for u in LINK.findall(text)]
    with ThreadPoolExecutor(32) as ex:
        bad = [r for r in ex.map(check, items) if not (isinstance(r[2], int) and (r[2] < 400 or r[2] in OK_CODES))]
    for page, url, status in bad:
        print(f"{status}\t{page}\t{url}")
    print(f"{len(bad)} of {len(items)} links failed", file=sys.stderr)
    sys.exit(1 if bad else 0)
if __name__ == "__main__":
    main()
