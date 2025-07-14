from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Network & Location Viewer</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .card { margin: 20px 0; padding: 10px; border: 1px solid #ccc; border-radius: 10px; }
        img { width: 100%; max-width: 400px; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>📍 Your Network & Location Info</h1>
    <div class="card">
        <p><strong>Network Type:</strong> <span id="network-status">Detecting...</span></p>
        <p><strong>Location:</strong> <span id="location">Detecting...</span></p>
    </div>

    <h2>Nearby Event Venues (Lazy Loaded)</h2>
    <div class="card">
        <img data-src="https://placehold.co/400x200?text=Park" alt="Venue 1" class="lazy-img" />
    </div>
    <div class="card">
        <img data-src="https://placehold.co/400x200?text=Stadium" alt="Venue 2" class="lazy-img" />
    </div>
    <div class="card">
        <img data-src="https://placehold.co/400x200?text=Garden" alt="Venue 3" class="lazy-img" />
    </div>

    <script>
        // Network Info API
        const netStatus = document.getElementById("network-status");
        if ('connection' in navigator) {
            const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
            netStatus.innerText = conn.effectiveType;
        } else {
            netStatus.innerText = "Not supported";
        }

        // Geolocation API
        const locationTag = document.getElementById("location");
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude.toFixed(5);
                const lon = position.coords.longitude.toFixed(5);
                locationTag.innerText = `Latitude: ${lat}, Longitude: ${lon}`;
            }, function() {
                locationTag.innerText = "Permission denied";
            });
        } else {
            locationTag.innerText = "Geolocation not supported";
        }

        // Intersection Observer API - Lazy load images
        const imgs = document.querySelectorAll('.lazy-img');
        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute('data-src');
                    obs.unobserve(img);
                }
            });
        }, { threshold: 0.1 });

        imgs.forEach(img => observer.observe(img));
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
