"""Tetris: 단일 HTML 파일 게임을 로컬 서버로 제공한다."""
import argparse
import functools
import http.server
import threading
import webbrowser
from pathlib import Path

STATIC = Path(__file__).parent / "static"


def main() -> None:
    p = argparse.ArgumentParser(description="웹 테트리스 서버")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--no-browser", action="store_true")
    a = p.parse_args()

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(STATIC))
    url = f"http://{a.host}:{a.port}/index.html"
    with http.server.ThreadingHTTPServer((a.host, a.port), handler) as srv:
        print(f"Tetris 실행 중: {url}  (종료: Ctrl+C)")
        if not a.no_browser:
            threading.Timer(0.5, webbrowser.open, args=(url,)).start()
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\n종료합니다.")
