# 🤖 Claude API — Interactive Course

An interactive, single-file HTML course application covering the core concepts of the Anthropic Claude API. Redesigned with a modern, Apple-like glassmorphism UI, real-time dark/light mode, and fluid GSAP scroll animations.

🚀 **[Live Demo on Cloudflare Pages](https://chris-claude-api.pages.dev)** *(Update this link to your new Option 2 URL!)*

## ✨ Features
- **Minimalist Glassmorphism UI**: Clean, distraction-free reading experience using frosted glass effects.
- **Dark / Light Mode**: Manual toggle `🌓` with system-preference detection and local storage persistence.
- **Fluid Animations**: Smooth scrolling and entry animations powered by GSAP & ScrollTrigger.
- **Progress Tracking**: Automatically tracks and saves explored course modules.
- **Interactive Filtering & Search**: Instantly find concepts using the search bar or category tags.

## 📚 Course Modules Covered
1. **API Basics**: Models (Opus, Sonnet, Haiku), Accessing the API, Multi-Turn Conversations.
2. **Prompting & Evals**: System Prompts, Temperature, Model-Based Grading, Code-Based Grading.
3. **Tools & MCP**: Tool Schemas, Built-in Tools, Model Context Protocol (MCP).
4. **Advanced Features**: Respose Streaming, Pre-filling, Prompt Caching, Vision, Code Execution.
5. **Retrieval Augmented Generation (RAG)**: Chunking Stratergies, Vectors/Embeddings, Contextual Retrieval.
6. **Agents & Workflows**: Chaining, Routing, Evaluator-Optimizer, Claude Code.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Animations**: GSAP (GreenSock) & ScrollTrigger (Loaded via CDN)
- **Typography**: Google Fonts (Inter, Fira Code)
- **Deployment**: Configured for continuous deployment via Cloudflare Pages (`index.html`).

## 🚀 Running Locally
Since this is a vanilla HTML/JS application without a modern build step or `node_modules`, you can run it instantly. No installation required!

1. Clone the repository:
   ```bash
   git clone https://github.com/chriscs0625/Claude-API-course.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Claude-API-course
   ```
3. Open `index.html` directly in your favorite web browser, or serve it using a lightweight local server:
   ```bash
   # Using Python 3
   python -m http.server 8000
   ```
4. Visit `http://localhost:8000` in your browser.

## 📝 About the Python Scripts
This repository contains several Python scripts (`update_ui.py`, `update_glass_ui.py`, `add_gsap_animations.py`). 

Because all the HTML, CSS, and JS is housed inside a single `index.html` file, these scripts were used to procedurally inject code and rewrite sections of the DOM during development. You do not need to run these scripts to use the app; they are kept for educational purposes and version history.

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.