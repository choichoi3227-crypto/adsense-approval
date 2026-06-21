# -*- coding: utf-8 -*-
"""
모든 HTML 파일의 </head> 직전에 Google AdSense 스크립트를 삽입합니다.
이미 삽입된 파일은 건너뜁니다(중복 삽입 방지). 재실행해도 안전합니다.

사용법:
    python3 insert_adsense.py [대상 디렉토리]
    (디렉토리 생략 시 이 스크립트가 위치한 디렉토리 기준으로 동작)
"""
import os
import sys
import glob

ADSENSE_CLIENT = "ca-pub-5852370252252543"
ADSENSE_TAG = (
    f'<script async src="https://pagead2.googlesyndication.com/pagead/js/'
    f'adsbygoogle.js?client={ADSENSE_CLIENT}"\n     crossorigin="anonymous"></script>'
)


def insert_into_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if ADSENSE_CLIENT in content:
        return "skipped"  # 이미 삽입됨

    if "</head>" not in content:
        return "no-head"  # head 태그가 없는 파일(비정상)

    new_content = content.replace("</head>", f"{ADSENSE_TAG}\n</head>", 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return "inserted"


def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    html_files = glob.glob(os.path.join(target_dir, "**", "*.html"), recursive=True)

    counts = {"inserted": 0, "skipped": 0, "no-head": 0}
    for fp in sorted(html_files):
        result = insert_into_file(fp)
        counts[result] += 1
        rel = os.path.relpath(fp, target_dir)
        print(f"[{result}] {rel}")

    print("\n--- 요약 ---")
    print(f"전체 HTML 파일: {len(html_files)}")
    print(f"새로 삽입됨: {counts['inserted']}")
    print(f"이미 있어서 건너뜀: {counts['skipped']}")
    print(f"head 태그 없음(확인 필요): {counts['no-head']}")


if __name__ == "__main__":
    main()
