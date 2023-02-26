// Get canvas and context
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

// Set canvas dimensions
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Create particles
var particles = [];
var numParticles = 150;

for (var i = 0; i < numParticles; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2 + 1,
        vx: (Math.random() * 2 - 1) * 0.7,
        vy: (Math.random() * 2 - 1) * 0.7
    });
}

// Draw particles
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (var i = 0; i < particles.length; i++) {
        ctx.beginPath();
        ctx.arc(particles[i].x, particles[i].y, particles[i].radius, 0, Math.PI * 2);
        ctx.closePath();
        ctx.fillStyle = "#fff";
        ctx.fill();
    }
}

// Update particle positions
function update() {
    for (var i = 0; i < particles.length; i++) {
        particles[i].x += particles[i].vx;
        particles[i].y += particles[i].vy;

        if (particles[i].x < 0 || particles[i].x > canvas.width) {
            particles[i].vx *= -1;
        }

        if (particles[i].y < 0 || particles[i].y > canvas.height) {
            particles[i].vy *= -1;
        }
    }
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    update();
    draw();
}

animate();
