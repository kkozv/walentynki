import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Walentynki 💘", page_icon="💘", layout="centered")

st.markdown(
    """
    <style>
      .block-container { padding-top: 3rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💘 Walentynki")

IMIE = "Piotrek"

# Możesz zmienić na inny gif z serduszkami
HEARTS_GIF_URL = "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"

html = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
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
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
    }}

    .wrap {{
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 430px;
    }}

    .card {{
      width: min(720px, 94vw);
      background: var(--card);
      border-radius: 18px;
      padding: 28px 22px;
      box-shadow: 0 10px 28px rgba(0,0,0,0.10);
      position: relative;
      overflow: hidden;
      text-align: center;
    }}

    .kitty {{
      width: 70px;
      height: 70px;
      margin: 0 auto 12px auto;
      border-radius: 50%;
      background: #f7c6a6;
      position: relative;
    }}
    .kitty:before {{
      content: "";
      position: absolute;
      left: 8px; top: 8px;
      width: 18px; height: 18px;
      background: #f1b993;
      clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
      transform: rotate(-20deg);
    }}
    .kitty:after {{
      content: "";
      position: absolute;
      right: 8px; top: 8px;
      width: 18px; height: 18px;
      background: #f1b993;
      clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
      transform: rotate(20deg);
    }}
    .heart {{
      position: absolute;
      right: 20px; top: 18px;
      width: 18px; height: 18px;
      background: #ff3b7a;
      transform: rotate(45deg);
      border-radius: 3px;
    }}
    .heart:before, .heart:after {{
      content: "";
      position: absolute;
      width: 18px; height: 18px;
      background: #ff3b7a;
      border-radius: 50%;
    }}
    .heart:before {{ left: -9px; top: 0; }}
    .heart:after  {{ left: 0; top: -9px; }}

    h1 {{
      font-size: 28px;
      margin: 8px 0 18px 0;
      color: var(--text);
      line-height: 1.2;
    }}

    .buttons {{
      display: flex;
      gap: 14px;
      justify-content: center;
      align-items: center;
      margin-top: 14px;
      position: relative;
      height: 56px;
    }}

    button {{
      border: 0;
      padding: 12px 22px;
      border-radius: 999px;
      font-size: 16px;
      cursor: pointer;
      user-select: none;
      transition: transform 0.05s ease;
    }}
    button:active {{ transform: scale(0.98); }}

    #yesBtn {{
      background: var(--yes);
      color: white;
      font-weight: 700;
    }}

    /* "Nie" będzie absolutnie pozycjonowane i uciekać */
    #noBtn {{
      background: var(--no);
      color: #111827;
      font-weight: 600;
      position: absolute;
      left: 50%;
      transform: translateX(120px);
    }}

    .hint {{
      margin-top: 8px;
      color: var(--muted);
      font-size: 12px;
    }}

    .yay {{
      display: none;
      margin-top: 18px;
      font-size: 30px;
      font-weight: 900;
    }}

    .gif {{
      display: none;
      margin-top: 14px;
    }}
    .gif img {{
      width: min(420px, 85vw);
      border-radius: 16px;
      box-shadow: 0 10px 24px rgba(0,0,0,0.10);
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card" id="card">
      <div class="kitty"><div class="heart"></div></div>

      <h1>Piotrek, zostaniesz moją walentynką?</h1>

      <div class="buttons" id="btnArea">
        <button id="yesBtn">Tak</button>
        <button id="noBtn" type="button">Nie</button>
      </div>

      <div class="hint">„Nie” i tak jest niemiłe 😈</div>

      <div class="yay" id="yayText">YAY!!! 🎉💖</div>
      <div class="gif" id="gifBox">
        <img src="{HEARTS_GIF_URL}" alt="serduszka gif">
      </div>
    </div>
  </div>

  <script>
    const noBtn = document.getElementById("noBtn");
    const btnArea = document.getElementById("btnArea");
    const yesBtn = document.getElementById("yesBtn");
    const yayText = document.getElementById("yayText");
    const gifBox = document.getElementById("gifBox");

    // Zablokuj realne kliknięcie "Nie"
    noBtn.addEventListener("click", (e) => {{
      e.preventDefault();
      e.stopPropagation();
      return false;
    }});

    function moveNoButton() {{
      const areaRect = btnArea.getBoundingClientRect();
      const btnRect = noBtn.getBoundingClientRect();

      // Maksymalne losowe pozycje w obrębie kontenera przycisków
      const maxX = areaRect.width - btnRect.width;
      const maxY = areaRect.height - btnRect.height;

      // Losuj, ale trzymaj w granicach
      const x = Math.max(0, Math.floor(Math.random() * maxX));
      const y = Math.max(0, Math.floor(Math.random() * maxY));

      noBtn.style.left = x + "px";
      noBtn.style.top  = y + "px";
      noBtn.style.transform = "translateX(0)";
    }}

    // Uciekanie przy zbliżeniu kursora
    noBtn.addEventListener("mouseenter", moveNoButton);
    noBtn.addEventListener("mousemove", moveNoButton);

    // Dla telefonów (dotknięcie też ucieka)
    noBtn.addEventListener("touchstart", (e) => {{
      e.preventDefault();
      moveNoButton();
    }}, {{ passive: false }});

    // Klik "Tak" -> pokaz YAY + gif
    yesBtn.addEventListener("click", () => {{
      yayText.style.display = "block";
      gifBox.style.display = "block";
      // Opcjonalnie schowaj przyciski po sukcesie:
      btnArea.style.display = "none";
    }});

    // Startowa pozycja "Nie"
    moveNoButton();
  </script>
</body>
</html>
"""

components.html(html, height=520)
