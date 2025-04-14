import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS og JavaScript-kode til spillet
html_code = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Skovspil</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
    }
    canvas {
      display: block;
      background-color: #90EE90; /* Lys grøn baggrund, der minder om en skov */
    }
  </style>
</head>
<body>
<canvas id="gameCanvas" width="800" height="600"></canvas>
<script>
  // Hent canvas-elementet og få 2D tegnekontekst
  const canvas = document.getElementById("gameCanvas");
  const ctx = canvas.getContext("2d");

  // Opret manden med startposition, størrelse og farve
  const man = {
      x: canvas.width / 2 - 10,
      y: canvas.height / 2 - 10,
      width: 20,
      height: 20,
      color: "blue"
  };
  const speed = 5;

  // Generer træerne én gang, så de forbliver statiske
  const trees = [];
  const antalTraeer = 20;
  for (let i = 0; i < antalTraeer; i++) {
      trees.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          radius: 10 + Math.random() * 10  // Varierende størrelse på træerne
      });
  }

  // Funktion til at tegne hele scenen
  function draw() {
      // Ryd canvasen
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Tegn baggrunden (skovbund)
      ctx.fillStyle = "#90EE90";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Tegn træerne
      trees.forEach(tree => {
          ctx.beginPath();
          ctx.arc(tree.x, tree.y, tree.radius, 0, 2 * Math.PI);
          ctx.fillStyle = "darkgreen";
          ctx.fill();
      });
      
      // Tegn manden
      ctx.fillStyle = man.color;
      ctx.fillRect(man.x, man.y, man.width, man.height);
  }

  // Opdater mandens position baseret på tryk på piletasterne
  function updatePosition(event) {
      switch (event.key) {
          case "ArrowUp":
              man.y -= speed;
              break;
          case "ArrowDown":
              man.y += speed;
              break;
          case "ArrowLeft":
              man.x -= speed;
              break;
          case "ArrowRight":
              man.x += speed;
              break;
          default:
              return; // Ingen relevant tast blev trykket
      }

      // Sørg for, at manden forbliver inden for canvasgrænserne
      man.x = Math.max(0, Math.min(canvas.width - man.width, man.x));
      man.y = Math.max(0, Math.min(canvas.height - man.height, man.y));

      // Gen-tegn scenen med den opdaterede position
      draw();
  }

  // Lyt efter tastetryk og kør funktionen for at opdatere positionen
  document.addEventListener("keydown", updatePosition);

  // Første kald til draw for at vise startscenen
  draw();
</script>
</body>
</html>
"""

st.title("Skovspil med bevægelig mand")
st.write("Brug piletasterne til at flytte manden rundt i skoven.")

# Embed HTML-appen i Streamlit via komponenten
components.html(html_code, height=620)
