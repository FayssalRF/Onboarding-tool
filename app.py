import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS og JavaScript kode til 3D-spillet
html_code = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>3D Skovspil - Counter Strike Stil</title>
  <style>
    body { margin: 0; overflow: hidden; }
    canvas { display: block; }
  </style>
</head>
<body>
<!-- Import af Three.js fra CDN -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r150/three.min.js"></script>
<script>
// Opret scene, kamera og renderer
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Opret jorden som en stor grøn plan
var groundGeometry = new THREE.PlaneGeometry(500, 500);
var groundMaterial = new THREE.MeshPhongMaterial({ color: 0x228B22 });
var ground = new THREE.Mesh(groundGeometry, groundMaterial);
ground.rotation.x = -Math.PI / 2;
scene.add(ground);

// Tilføj lys til scenen
var ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);
var directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(50, 50, 50);
scene.add(directionalLight);

// Funktion til at tilføje træer i skoven
function addTree(x, z) {
    // Træstamme
    var trunkGeometry = new THREE.CylinderGeometry(0.5, 0.5, 5);
    var trunkMaterial = new THREE.MeshPhongMaterial({ color: 0x8B4513 });
    var trunk = new THREE.Mesh(trunkGeometry, trunkMaterial);
    trunk.position.set(x, 2.5, z);
    scene.add(trunk);
    // Trækroner
    var crownGeometry = new THREE.ConeGeometry(2.5, 8, 8);
    var crownMaterial = new THREE.MeshPhongMaterial({ color: 0x006400 });
    var crown = new THREE.Mesh(crownGeometry, crownMaterial);
    crown.position.set(x, 7, z);
    scene.add(crown);
}
// Tilføj 50 træer med tilfældige positioner
for (var i = 0; i < 50; i++) {
    var x = Math.random() * 400 - 200;
    var z = Math.random() * 400 - 200;
    addTree(x, z);
}

// Placér kameraet (førstepersons)
camera.position.set(0, 2, 0);

// Variabler for bevægelse
var moveForward = false, moveBackward = false, moveLeft = false, moveRight = false;
var speed = 0.5;

// Lyt efter tastetryk for at styre bevægelsen
document.addEventListener('keydown', function(event) {
    switch(event.code) {
        case 'ArrowUp':
        case 'KeyW':
            moveForward = true;
            break;
        case 'ArrowLeft':
        case 'KeyA':
            moveLeft = true;
            break;
        case 'ArrowDown':
        case 'KeyS':
            moveBackward = true;
            break;
        case 'ArrowRight':
        case 'KeyD':
            moveRight = true;
            break;
    }
}, false);
document.addEventListener('keyup', function(event) {
    switch(event.code) {
        case 'ArrowUp':
        case 'KeyW':
            moveForward = false;
            break;
        case 'ArrowLeft':
        case 'KeyA':
            moveLeft = false;
            break;
        case 'ArrowDown':
        case 'KeyS':
            moveBackward = false;
            break;
        case 'ArrowRight':
        case 'KeyD':
            moveRight = false;
            break;
    }
}, false);

// Animer scenen og opdater kameraets position
function animate() {
    requestAnimationFrame(animate);

    // Bestem bevægelsesretningen baseret på kameraets fremadrettede vektor
    var direction = new THREE.Vector3();
    camera.getWorldDirection(direction);
    direction.y = 0;  // Ignorer lodret retning
    direction.normalize();

    // Beregn "højre" vektor (vinkelret på kameraets retning)
    var right = new THREE.Vector3();
    right.crossVectors(camera.up, direction).normalize();

    // Saml bevægelsesvektoren
    var moveVector = new THREE.Vector3();
    if (moveForward) moveVector.add(direction);
    if (moveBackward) moveVector.sub(direction);
    if (moveLeft) moveVector.add(right);
    if (moveRight) moveVector.sub(right);

    moveVector.normalize().multiplyScalar(speed);
    camera.position.add(moveVector);

    renderer.render(scene, camera);
}
animate();

// Sørg for, at canvas tilpasses ved vinduesændringer
window.addEventListener('resize', function(){
    var width = window.innerWidth;
    var height = window.innerHeight;
    renderer.setSize(width, height);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
});
</script>
</body>
</html>
"""

st.title("3D Skovspil i Counter Strike Stil")
st.write("Brug piletasterne (eller WASD) til at navigere gennem skoven.")

# Indlejr HTML/JS-spillet i Streamlit-appen
components.html(html_code, height=600, scrolling=True)
