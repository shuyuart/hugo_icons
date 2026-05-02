#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次修改 content/posts/ 底下所有 .md 檔案的 img alt 文字

支援兩種原始格式：
  1. 英文檔名格式（未改過）：alt="grilledsausage16_bk" → alt="烤香腸 像素圖示（黑框版）"
                             alt="grilledsausage16_cr" → alt="烤香腸 像素圖示（無框版）"

  2. 中文簡略格式（部分手改）：alt="珍珠奶茶黑框" → alt="珍珠奶茶 像素圖示（黑框版）"
                               alt="珍珠奶茶無框" → alt="珍珠奶茶 像素圖示（無框版）"

title 從每篇文章的 front matter 自動讀取，不需要手動對照。
"""

import re
import sys
from pathlib import Path

# ── 設定路徑（改成你的實際路徑）────────────────────────
POSTS_DIR = Path("content/posts")

# ── 從 front matter 讀取 title ───────────────────────
TITLE_RE = re.compile(r'^title:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)

# ── 比對兩種 alt 格式 ────────────────────────────────
# 格式1：英文檔名，結尾 _bk 或 _cr（可能接數字）
ALT_EN_BK = re.compile(r'alt="[a-z0-9_]+16_bk\d*"')
ALT_EN_CR = re.compile(r'alt="[a-z0-9_]+16_cr\d*"')

# 格式2：中文標題 + 黑框／無框
ALT_ZH_BK = re.compile(r'alt="(.+?)黑框"')
ALT_ZH_CR = re.compile(r'alt="(.+?)無框"')


def get_title(text: str) -> str | None:
    m = TITLE_RE.search(text)
    return m.group(1).strip() if m else None


def process_file(path: Path, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    title = get_title(original)

    if not title:
        print(f"[略過] {path}（找不到 title）")
        return False

    updated = original

    # 格式1：英文檔名 → 用 title 重組
    updated = ALT_EN_BK.sub(f'alt="{title} 像素圖示（黑框版）"', updated)
    updated = ALT_EN_CR.sub(f'alt="{title} 像素圖示（無框版）"', updated)

    # 格式2：中文簡略 → 補上完整說明
    updated = ALT_ZH_BK.sub(r'alt="\1 像素圖示（黑框版）"', updated)
    updated = ALT_ZH_CR.sub(r'alt="\1 像素圖示（無框版）"', updated)

    if updated == original:
        return False  # 沒有需要改的

    if dry_run:
        print(f"\n[預覽] {path}  （title: {title}）")
        orig_lines = original.splitlines()
        new_lines  = updated.splitlines()
        for i, (o, n) in enumerate(zip(orig_lines, new_lines), 1):
            if o != n:
                print(f"  第{i:>3}行  舊: {o.strip()}")
                print(f"           新: {n.strip()}")
    else:
        path.write_text(updated, encoding="utf-8")
        print(f"[已修改] {path}  （title: {title}）")

    return True


def main():
    dry_run = "--apply" not in sys.argv

    if dry_run:
        print("=== 預覽模式（不會修改任何檔案） ===")
        print("確認沒問題後，執行：  python3 fix_alt.py --apply\n")
    else:
        print("=== 套用模式，開始修改… ===\n")

    if not POSTS_DIR.exists():
        print(f"找不到資料夾：{POSTS_DIR.resolve()}")
        sys.exit(1)

    files   = sorted(POSTS_DIR.glob("**/*.md"))
    changed = 0
    for f in files:
        if process_file(f, dry_run):
            changed += 1

    print(f"\n共掃描 {len(files)} 篇，{'需修改' if dry_run else '已修改'} {changed} 篇。")


if __name__ == "__main__":
    main()
