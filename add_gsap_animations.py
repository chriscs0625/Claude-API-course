import os

file_path = "claude_api_course 2.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject GSAP CDN scripts right before the first script tag
gsap_scripts = """<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.4/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.4/ScrollTrigger.min.js"></script>
<script>"""

content = content.replace("<script>", gsap_scripts, 1)

# 2. Append Animation Logic & Hook into existing functions
gsap_logic = """
// --- GSAP Scroll Animations ---
gsap.registerPlugin(ScrollTrigger);

function initAnimations() {
  // Staggered hero element fade-ins
  gsap.from(".hi > *, .stats, .pw", {
    y: 20, opacity: 0, duration: 0.8, stagger: 0.08, ease: "power3.out", delay: 0.1
  });

  // Control bar slides down slightly
  gsap.from(".ctrl", {
    y: -15, opacity: 0, duration: 0.8, ease: "power3.out", delay: 0.4
  });

  animateCards();
}

function animateCards() {
  // Kill old triggers to avoid layout shift bugs on filter
  ScrollTrigger.getAll().forEach(t => t.kill());

  const cards = document.querySelectorAll('.card');
  cards.forEach((card) => {
    // Only animate if the card is currently visible from the filter
    if (card.style.display !== 'none') {
      gsap.fromTo(card, 
        { y: 30, opacity: 0 },
        {
          scrollTrigger: { 
            trigger: card, 
            start: "top 92%", 
            toggleActions: "play none none none" 
          },
          y: 0, opacity: 1, duration: 0.7, ease: "power2.out", clearProps: "transform"
        }
      );
    }
  });
}

// Intercept original init
const originalInit = init;
init = function() {
  originalInit();
  setTimeout(initAnimations, 50); // slight delay to ensure DOM is drawn
};

// Intercept original filter function
const originalFc2 = fc2;
fc2 = function() {
  originalFc2();
  setTimeout(animateCards, 50); // Re-trigger animations for freshly visible cards
};
"""

# Inject before the final init() call
content = content.replace("init();\n</script>", gsap_logic + "\ninit();\n</script>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("GSAP UI animations injected successfully.")
