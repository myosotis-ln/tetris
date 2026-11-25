# Tetris

단일 파일 SPA 웹 테트리스 (HTML/CSS/JS 모두 `src/tetris/static/index.html`에 포함).

## 실행
    uv sync
    uv run tetris            # http://127.0.0.1:8000 (브라우저 자동 열림)
    uv run tetris --port 9000 --no-browser

서버 없이 `src/tetris/static/index.html`을 브라우저로 직접 열어도 동작합니다.

## 조작
←/→ 이동, ↑/X 회전, Z 역회전, ↓ 소프트 드롭, Space 하드 드롭, P 일시정지, Enter 시작

- Updated to v2
