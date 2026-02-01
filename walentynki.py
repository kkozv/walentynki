import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💖", page_icon="💖", layout="centered")

st.markdown(
    """
    <style>
      body {
        background-color: #ffe4ef;
      }
      .block-container {
        padding-top: 3rem;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

HEARTS_GIF_URL = "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"

html = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<style>
:root {{
  --card: #ffffff;
  --text: #111827;
  --muted: #6b7280;
  --yes: #ff3b7a;
  --no: #e5e7eb;
}}

body {{
  margin: 0;
  background: transparent;
  font-family: system-ui, sans-serif;
}}

.wrap {{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 420px;
}}

.card {{
  width: min(720px, 94vw);
  background: var(--card);
  border-radius: 20px;
  padding: 30px 22px;
  box-shadow: 0 10px 28px rgba(0,0,0,0.15);
  text-align: center;
}}

.heart-icon {{
  font-size: 64px;
  margin-bottom: 10px;
}}

h1 {{
  font-size: 28px;
  margin-bottom: 20px;
}}

.buttons {{
  display: flex;
  justify-content: center;
  gap: 20px;
  position: relative;
  height: 60px;
}}

button {{
  border: none;
  padding: 12px 24px;
  border-radius: 999px;
  font-size: 16px;
  cursor: pointer;
}}

#yesBtn {{
  background: var(--yes);
  color: white;
  font-weight: 700;
}}

#noBtn {{
  background: var(--no);
  position: absolute;
}}

.hint {{
  margin-top: 10px;
  font-size: 13px;
  color: var(--muted);
}}

.yay {{
  display: none;
  font-size: 32px;
  font-weight: 900;
  margin-top: 20px;
}}

.gif {{
  display: none;
  margin-top: 14px;
}}

.gif img {{
  width: min(420px, 85vw);
  border-radius: 16px;
}}
</style>
</head>
<body>
<div class="wrap">
  <div class="card">
    <div class="heart-icon">❤️</div>

    <h1>Kochanie, zostaniesz moją walentynką?</h1>

    <div class="buttons" id="btnArea">
      <button id="yesBtn">Tak</button>
      <button id="noBtn">Nie</button>
    </div>

    <div class="hint">"nie" jest trochę nieśmiałe 😈</div>

    <div class="yay" id="yayText">YAY!!! 💖</div>
    <div class="gif" id="gifBox">
      <img src="{HEARTS_GIF_URL}">
    </div>
  </div>
</div>

<script>
const noBtn = document.getElementById("noBtn");
const btnArea = document.getElementById("btnArea");
const yesBtn = document.getElementById("yesBtn");
const yayText = document.getElementById("yayText");
const gifBox = document.getElementById("gifBox");

function moveNo() {{
  const area = btnArea.getBoundingClientRect();
  const btn = noBtn.getBoundingClientRect();
  const x = Math.random() * (area.width - btn.width);
  const y = Math.random() * (area.height - btn.height);
  noBtn.style.left = x + "px";
  noBtn.style.top = y + "px";
}}

noBtn.addEventListener("mouseenter", moveNo);
noBtn.addEventListener("mousemove", moveNo);
noBtn.addEventListener("touchstart", moveNo);

noBtn.addEventListener("click", e => {{
  e.preventDefault();
}});

yesBtn.addEventListener("click", () => {{
  yayText.style.display = "block";
  gifBox.style.display = "block";
  btnArea.style.display = "none";
}});

moveNo();
</script>
</body>
</html>
"""

components.html(html, height=520)
