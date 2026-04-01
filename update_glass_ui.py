import os

file_path = "claude_api_course 2.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- UPDATE STYLE ---
style_start = content.find("<style>")
style_end = content.find("</style>") + len("</style>")

new_style = """<style>
  :root {
    --bg: #F5F5F7;
    --glass-bg: rgba(255, 255, 255, 0.75);
    --card-bg: rgba(255, 255, 255, 0.5);
    --border: rgba(0, 0, 0, 0.08);
    --accent: #0066CC;
    --text: #1D1D1F;
    --muted: #86868B;
    --danger: #FF3B30;
    --shadow: 0 8px 32px rgba(0, 0, 0, 0.04);
  }
  body.dark-mode {
    --bg: #000000;
    --glass-bg: rgba(28, 28, 30, 0.75);
    --card-bg: rgba(44, 44, 46, 0.4);
    --border: rgba(255, 255, 255, 0.12);
    --accent: #2997FF;
    --text: #F5F5F7;
    --muted: #98989D;
    --danger: #FF453A;
    --shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    transition: background-color 0.3s ease, color 0.3s ease;
  }
  
  /* Background subtle gradient for better glass effect */
  body::before {
    content: ''; position: fixed; top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle at 50% 50%, var(--accent), transparent 60%);
    opacity: 0.03; pointer-events: none; z-index: -1;
  }

  header { padding: 60px 40px 40px; position: relative; z-index: 10; border-bottom: 1px solid var(--border); }
  .hi { max-width: 1000px; margin: 0 auto; position: relative; }
  
  .theme-btn {
    position: absolute; top: 0; right: 0;
    background: var(--card-bg); border: 1px solid var(--border);
    backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
    color: var(--text); border-radius: 50%; width: 40px; height: 40px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; font-size: 16px; transition: all 0.2s;
    box-shadow: var(--shadow);
  }
  .theme-btn:hover { transform: scale(1.05); }

  .eyebrow { font-family: 'Fira Code', monospace; font-size: 12px; color: var(--muted); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.5px; }
  h1 { font-size: 36px; font-weight: 600; color: var(--text); margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.5px; }
  .sub { font-size: 15px; color: var(--muted); max-width: 600px; }
  
  .stats { display: flex; gap: 24px; margin-top: 32px; flex-wrap: wrap; }
  .stat { display: flex; align-items: center; gap: 8px; font-family: 'Fira Code', monospace; font-size: 12px; color: var(--muted); }
  .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--border); }
  .dot.y { background: var(--accent); } .dot.g { background: var(--muted); }
  
  .pw { margin-top: 32px; }
  .pl { font-family: 'Fira Code', monospace; font-size: 11px; color: var(--muted); margin-bottom: 8px; display: flex; justify-content: space-between; }
  .pb { height: 4px; background: var(--border); border-radius: 2px; overflow: hidden; }
  .pf { height: 100%; background: var(--accent); width: 0%; transition: width 0.4s ease; border-radius: 2px; }
  
  /* Glass Nav */
  .ctrl { 
    position: sticky; top: 0; z-index: 20; 
    background: var(--glass-bg); 
    backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
    border-bottom: 1px solid var(--border); padding: 16px 40px; 
  }
  .ci { max-width: 1000px; margin: 0 auto; display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
  
  .sw { position: relative; flex: 1; min-width: 200px; }
  .si { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--muted); font-size: 14px; pointer-events: none; }
  input { 
    width: 100%; background: var(--card-bg); border: 1px solid var(--border);
    border-radius: 8px; padding: 10px 12px 10px 36px; color: var(--text); 
    font-family: 'Inter', sans-serif; font-size: 14px; outline: none; transition: border-color 0.2s; 
  }
  input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.15); }
  input::placeholder { color: var(--muted); }
  
  .fbs { display: flex; gap: 8px; flex-wrap: wrap; }
  .fb { 
    padding: 8px 16px; border-radius: 20px; border: 1px solid var(--border); 
    background: var(--card-bg); color: var(--muted); 
    font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500; 
    cursor: pointer; transition: all 0.2s; 
  }
  .fb:hover { border-color: var(--muted); color: var(--text); }
  .fb.on { background: var(--text); border-color: var(--text); color: var(--bg); }
  
  .main { position: relative; z-index: 5; max-width: 1000px; margin: 0 auto; padding: 40px 40px 80px; }
  .slbl { font-family: 'Fira Code', monospace; font-size: 11px; color: var(--muted); text-transform: uppercase; margin: 40px 0 20px; padding-bottom: 8px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 8px; letter-spacing: 0.5px; }
  
  .cg { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  
  /* Glass Cards */
  .card { 
    background: var(--card-bg); border: 1px solid var(--border); 
    backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    border-radius: 12px; overflow: hidden; cursor: pointer; 
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); position: relative; 
    box-shadow: var(--shadow);
  }
  .card:hover { border-color: var(--muted); transform: translateY(-2px); box-shadow: 0 12px 40px rgba(0,0,0,0.08); }
  .card.on { border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent), 0 12px 40px rgba(0,0,0,0.1); }
  .cab { display: none; }
  
  .ch { padding: 24px 24px 16px; display: flex; align-items: flex-start; gap: 16px; }
  .ci2 { font-size: 20px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--text); filter: grayscale(100%); opacity: 0.8; }
  .ct { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 6px; }
  .cp { font-size: 14px; color: var(--muted); line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
  .ctags { padding: 0 24px 24px; display: flex; flex-wrap: wrap; gap: 6px; display: none; }
  
  .hint { position: absolute; bottom: 20px; right: 24px; font-size: 11px; color: var(--muted); opacity: 0; transition: opacity 0.2s; font-family: 'Fira Code', monospace; }
  .card:hover .hint { opacity: 1; }
  .card.vis::after { content: ''; position: absolute; top: 16px; right: 16px; width: 6px; height: 6px; border-radius: 50%; background: var(--accent); opacity: 0.8; }
  
  /* Glass Details Panel */
  .dp { 
    display: none; grid-column: 1 / -1; margin-top: 8px; margin-bottom: 24px;
    background: var(--card-bg); border: 1px solid var(--border); 
    backdrop-filter: blur(32px); -webkit-backdrop-filter: blur(32px);
    border-radius: 16px; padding: 48px; box-shadow: var(--shadow);
  }
  .dp.show { display: block; animation: fadein 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
  @keyframes fadein { from { opacity: 0; transform: translateY(-8px) scale(0.98); } to { opacity: 1; transform: translateY(0) scale(1); } }
  
  .dh { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 32px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
  .dtitle { font-size: 24px; font-weight: 600; color: var(--text); display: flex; align-items: center; gap: 12px; filter: grayscale(100%); }
  .xbtn { 
    background: var(--card-bg); border: 1px solid var(--border); 
    color: var(--muted); cursor: pointer; padding: 8px 12px; border-radius: 20px; 
    font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500; transition: all 0.2s; 
  }
  .xbtn:hover { background: var(--border); color: var(--text); }
  
  .db { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; }
  .dst { font-family: 'Fira Code', monospace; font-size: 11px; text-transform: uppercase; color: var(--text); margin-bottom: 12px; letter-spacing: 0.5px; font-weight: 600; }
  .dtxt { font-size: 15px; color: var(--muted); line-height: 1.6; }
  
  .dlist { list-style: none; display: flex; flex-direction: column; gap: 12px; }
  .dlist li { font-size: 15px; color: var(--muted); padding-left: 20px; position: relative; line-height: 1.6; }
  .dlist li::before { content: '•'; position: absolute; left: 0; color: var(--border); font-size: 20px; top: -4px; }
  
  .cblk { 
    background: rgba(0,0,0,0.03); border: 1px solid var(--border); 
    border-radius: 8px; padding: 16px; font-family: 'Fira Code', monospace; 
    font-size: 13px; color: var(--text); line-height: 1.6; overflow-x: auto; 
    margin-top: 16px; margin-bottom: 24px; 
  }
  body.dark-mode .cblk { background: rgba(0,0,0,0.3); }

  .tip { border-left: 3px solid var(--accent); padding: 16px 20px; margin-top: 24px; font-size: 14px; color: var(--muted); line-height: 1.6; background: rgba(0, 102, 204, 0.05); border-radius: 0 8px 8px 0; }
  body.dark-mode .tip { background: rgba(41, 151, 255, 0.08); }
  .tip strong { color: var(--text); font-weight: 600; }
  
  .fsteps { display: flex; flex-direction: column; gap: 16px; margin-top: 12px; }
  .fstep { display: flex; gap: 16px; align-items: flex-start; }
  .snum { width: 24px; height: 24px; border-radius: 50%; background: var(--bg); border: 1px solid var(--border); color: var(--text); font-family: 'Fira Code', monospace; font-size: 11px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; }
  .stxt { font-size: 15px; color: var(--muted); line-height: 1.6; }
  
  .nr { text-align: center; padding: 80px 20px; color: var(--muted); font-family: 'Inter', sans-serif; font-size: 15px; display: none; }
  
  @media(max-width: 800px) { .db { grid-template-columns: 1fr; gap: 40px; } }
  @media(max-width: 600px) { header, .main { padding-left: 24px; padding-right: 24px; } .ctrl { padding: 16px 24px; } .cg { grid-template-columns: 1fr; } .dp { padding: 32px 24px; } .db { gap: 32px; } }
</style>"""

content = content[:style_start] + new_style + content[style_end:]

# --- INJECT TOGGLE BUTTON ---
if 'id="theme-toggle"' not in content:
    header_content = """<div class="hi">
    <button id="theme-toggle" class="theme-btn" onclick="toggleTheme()" title="Toggle Theme">🌓</button>
    <div class="eyebrow">"""
    content = content.replace('<div class="hi">\n    <div class="eyebrow">', header_content)

# --- INJECT JS LOGIC ---
js_logic = """<script>
// Theme Toggle Logic
function toggleTheme() {
  document.body.classList.toggle('dark-mode');
  localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
}

// Check initial preference
if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.body.classList.add('dark-mode');
}
"""
content = content.replace("<script>", js_logic)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated glass UI and theme toggle successfully!")
