#!/usr/bin/env python3
"""
批量取 arXiv 摘要，供人工判断范围与撰写简介用。

用法：
    python3 scripts/abstracts.py 2609.27273,2609.22724
    python3 scripts/abstracts.py 2609.27273 2609.22724

输出每篇的 ID、v1 日期、comment（常含录用会议）、标题与完整摘要。
请求走 curl 优先（arXiv WAF 对 Python urllib 指纹不友好，见 docs/MAINTENANCE.md）。
"""
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

UA = "Awesome-GUI-Agent-Security/1.0 (weekly maintenance; +https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security)"
API = "https://export.arxiv.org/api/query"
BATCH = 40


def http_get(url):
    try:
        p = subprocess.run(["curl", "-sS", "--compressed", "--max-time", "90", "-A", UA, url],
                           capture_output=True, text=True)
        if p.returncode == 0 and "<feed" in p.stdout:
            return p.stdout
    except FileNotFoundError:
        pass
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=90).read().decode()


def get(ids):
    url = API + "?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    last = None
    for i in range(5):
        try:
            return http_get(url)
        except Exception as e:
            last = e
            wait = 20 * (i + 1)
            print(f"[retry {i + 1}] {e} -> {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"arXiv 请求连续失败：{last}")


def main():
    ids = [x for a in sys.argv[1:] for x in a.split(",") if x.strip()]
    if not ids:
        sys.exit(__doc__)
    xml = ""
    for i in range(0, len(ids), BATCH):
        if i:
            time.sleep(15)
        xml += get(ids[i:i + BATCH])
    for blk in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        ti = re.search(r"<title>(.*?)</title>", blk, re.S)
        su = re.search(r"<summary>(.*?)</summary>", blk, re.S)
        aid = re.search(r"<id>http://arxiv\.org/abs/([^<]+)</id>", blk)
        pub = re.search(r"<published>(.*?)</published>", blk)
        cm = re.search(r"<arxiv:comment[^>]*>(.*?)</arxiv:comment>", blk, re.S)
        print("=" * 78)
        print(aid.group(1) if aid else "?", "|", pub.group(1)[:10] if pub else "", "|",
              " ".join(cm.group(1).split())[:80] if cm else "")
        print(" ".join(ti.group(1).split()) if ti else "")
        print()
        print(" ".join(su.group(1).split()) if su else "")


if __name__ == "__main__":
    main()
