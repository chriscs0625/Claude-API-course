import os

file_path = "claude_api_course 2.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

head_start = content.find("<head>")
head_end = content.find("</head>") + len("</head>")

new_head = """<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude API \u2014 Interactive Course</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #FAFAFA;
    --surface: #FFFFFF;
    --surface2: #F5F5F5;
    --border: #E5E5E5;
    --accent: #555555;
    --accent2: #777777;
    --accent3: #666666;
    --text: #222222;
    --muted: #666666;
    --danger: #D32F2F;
    --tag-bg: #F0F0F0;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #121212;
      --surface: #181818;
      --surface2: #202020;
      --border: #2A2A2A;
      --accent: #A0A0A0;
      --accent2: #888888;
      --accent3: #999999;
      --text: #E0E0E0;
      --muted: #888888;
      --danger: #EF5350;
      --tag-bg: #2A2A2A;
    }
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }
  header { padding: 60px 40px 40px; border-bottom: 1px solid var(--border); background: var(--bg); position: relative; z-index: 10; }
  .hi { max-width: 1000px; margin: 0 auto; }
  .eyebrow { font-family: 'Fira Code', monospace; font-size: 12px; color: var(--muted); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.5px; }
  h1 { font-size: 36px; font-weight: 500; color: var(--text); margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.5px; }
  .sub { font-size: 15px; color: var(--muted); max-width: 600px; }
  .stats { display: flex; gap: 24px; margin-top: 32px; flex-wrap: wrap; }
  .stat { display: flex; align-items: center; gap: 8px; font-family: 'Fira Code', monospace; font-size: 12px; color: var(--muted); }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--muted); }
  .pw { margin-top: 32px; }
  .pl { font-family: 'Fira Code', monospace; font-size: 11px; color: var(--muted); margin-bottom: 8px; display: flex; justify-content: space-between; }
  .pb { height: 2px; background: var(--border); overflow: hidden; }
  .pf { height: 100%; background: var(--text); width: 0%; transition: width 0.4s ease; }
  .ctrl { position: sticky; top: 0; z-index: 20; background: var(--bg); border-bottom: 1px solid var(--border); padding: 16px 40px; }
  .ci { max-width: 1000px; margin: 0 auto; display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
  .sw { position: relative; flex: 1; min-width: 200px; }
  .si { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--muted); font-size: 14px; pointer-events: none; }
  input { width: 100%; background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 10px 12px 10px 36px; color: var(--text); font-family: 'Inter', sans-serif; font-size: 14px; outline: none; transition: border-color 0.2s; }
  input:focus { border-color: var(--muted); }
  input::placeholder { color: var(--muted); }
  .fbs { display: flex; gap: 8px; flex-wrap: wrap; }
  .fb { padding: 8px 14px; border-radius: 4px; border: 1px solid var(--border); background: var(--surface); color: var(--muted); font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.2s; }
  .fb:hover { border-color: var(--muted); color: var(--text); }
  .fb.on { background: var(--text); border-color: var(--text); color: var(--bg); }
  .main { position: relative; z-index: 5; max-width: 1000px; margin: 0 auto; padding: 40px 40px 80px; }
  .slbl { font-family: 'Fira Code', monospace; font-size: 11px; color: var(--muted); text-transform: uppercase; margin: 40px 0 20px; padding-bottom: 8px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 8px; letter-spacing: 0.5px; }
  .cg { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: 6px; overflow: hidden; cursor: pointer; transition: border-color 0.2s; position: relative; }
  .card:hover { border-color: var(--muted); }
  .card.on { border-color: var(--text); }
  .cab { display: none; }
  .ch { padding: 24px 24px 16px; display: flex; align-items: flex-start; gap: 16px; }
  .ci2 { font-size: 20px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--text); opacity: 0.8; filter: grayscale(100%); }
  .ct { font-size: 15px; font-weight: 500; color: var(--text); margin-bottom: 6px; }
  .cp { font-size: 14px; color: var(--muted); line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
  .ctags { padding: 0 24px 24px; display: flex; flex-wrap: wrap; gap: 6px; display: none; }
  .tag { font-family: 'Fira Code', monospace; font-size: 10px; padding: 4px 8px; border-radius: 4px; background: var(--surface2); color: var(--muted); border: 1px solid var(--border); }
  .hint { position: absolute; bottom: 20px; right: 24px; font-size: 11px; color: var(--muted); opacity: 0; transition: opacity 0.2s; font-family: 'Fira Code', monospace; }
  .card:hover .hint { opacity: 1; }
  .card.vis::after { content: ''; position: absolute; top: 16px; right: 16px; width: 6px; height: 6px; border-radius: 50%; background: var(--text); opacity: 0.2; }
  .dp { display: none; grid-column: 1 / -1; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; padding: 48px; margin-top: 8px; margin-bottom: 24px; }
  .dp.show { display: block; animation: fadein 0.3s ease; }
  @keyframes fadein { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
  .dh { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 32px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
  .dtitle { font-size: 24px; font-weight: 500; color: var(--text); display: flex; align-items: center; gap: 12px; filter: grayscale(100%); }
  .xbtn { background: transparent; border: 1px solid var(--border); color: var(--muted); cursor: pointer; padding: 8px 12px; border-radius: 4px; font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500; transition: all 0.15s; }
  .xbtn:hover { background: var(--surface2); color: var(--text); }
  .db { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; }
  .dst { font-family: 'Fira Code', monospace; font-size: 11px; text-transform: uppercase; color: var(--text); margin-bottom: 12px; letter-spacing: 0.5px; font-weight: 500; }
  .dtxt { font-size: 15px; color: var(--muted); line-height: 1.6; }
  .dlist { list-style: none; display: flex; flex-direction: column; gap: 12px; }
  .dlist li { font-size: 15px; color: var(--muted); padding-left: 20px; position: relative; line-height: 1.6; }
  .dlist li::before { content: '\u2014'; position: absolute; left: 0; color: var(--border); font-weight: bold; }
  .cblk { background: var(--surface2); border: 1px solid var(--border); border-radius: 4px; padding: 16px; font-family: 'Fira Code', monospace; font-size: 13px; color: var(--text); line-height: 1.6; overflow-x: auto; margin-top: 16px; margin-bottom: 24px; }
  .tip { border-left: 2px solid var(--text); padding: 16px 20px; margin-top: 24px; font-size: 14px; color: var(--muted); line-height: 1.6; background: var(--surface2); border-radius: 0 4px 4px 0; }
  .tip strong { color: var(--text); font-weight: 500; }
  .fsteps { display: flex; flex-direction: column; gap: 16px; margin-top: 12px; }
  .fstep { display: flex; gap: 16px; align-items: flex-start; }
  .snum { width: 24px; height: 24px; border-radius: 4px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); font-family: 'Fira Code', monospace; font-size: 11px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; }
  .stxt { font-size: 15px; color: var(--muted); line-height: 1.6; }
  .nr { text-align: center; padding: 80px 20px; color: var(--muted); font-family: 'Inter', sans-serif; font-size: 15px; display: none; }
  @media(max-width: 800px) { .db { grid-template-columns: 1fr; gap: 40px; } }
  @media(max-width: 600px) { header, .main { padding-left: 24px; padding-right: 24px; } .ctrl { padding: 16px 24px; } .cg { grid-template-columns: 1fr; } .dp { padding: 32px 24px; } .db { gap: 32px; } }
</style>
</head>"""

new_content = content[:head_start] + new_head + content[head_end:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated HTML!")
