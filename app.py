from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Samarth SMS Bomber - OSINT Intelligence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
        body { font-family: 'Inter', system-ui, sans-serif; background: #05050a; color: #fff; }
        .glass { background: rgba(15,23,42,0.85); backdrop-filter: blur(24px); border: 1px solid rgba(103,232,249,0.2); }
        .neon { text-shadow: 0 0 20px #22d3ee, 0 0 40px #22d3ee; }
    </style>
</head>
<body class="min-h-screen">
    <div class="max-w-6xl mx-auto p-8">
        <!-- Header -->
        <div class="flex justify-between items-center mb-16">
            <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-cyan-500 rounded-2xl flex items-center justify-center text-4xl">💥</div>
                <div>
                    <h1 class="text-5xl font-bold tracking-tighter neon">SAMARTH BOMBER</h1>
                    <p class="text-cyan-400">SMS • CALL • WHATSAPP OSINT</p>
                </div>
            </div>
            <div class="text-sm text-emerald-400">Made by Samarth • 2026</div>
        </div>

        <!-- Search -->
        <div class="glass rounded-3xl p-16 text-center mb-20">
            <h2 class="text-6xl font-bold mb-6">Welcome to Samarth SMS Bomber</h2>
            <p class="text-xl text-slate-400 max-w-md mx-auto">Enter email or phone for full intelligence + bombing tools</p>
            <div class="mt-12 max-w-md mx-auto">
                <input id="target" placeholder="email@example.com or 9876543210" class="w-full bg-black border border-cyan-400 rounded-3xl px-8 py-6 text-xl focus:outline-none focus:border-cyan-300">
                <button onclick="searchTarget()" class="mt-6 w-full py-6 bg-gradient-to-r from-cyan-400 to-blue-500 text-black font-bold text-xl rounded-3xl">SEARCH + BOMB</button>
            </div>
        </div>

        <!-- Results -->
        <div class="grid md:grid-cols-2 gap-8">
            <div class="glass rounded-3xl p-8">
                <h3 class="text-cyan-400 mb-6">Live Lookup Results</h3>
                <div class="space-y-8">
                    <div class="flex gap-6">
                        <div class="text-5xl">📧</div>
                        <div class="flex-1">
                            <div class="font-mono text-xl">user@example.com</div>
                            <div class="text-green-400">Registered on 47 platforms</div>
                            <div class="mt-4 text-sm text-slate-400">Last seen: Jan 2, 2024</div>
                        </div>
                    </div>
                    <div class="flex gap-6">
                        <div class="text-5xl">📱</div>
                        <div class="flex-1">
                            <div class="font-mono text-xl">+91 9876543210</div>
                            <div class="text-green-400">Active on 18 services</div>
                            <div class="mt-4 text-sm text-slate-400">Breaches: 4</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="glass rounded-3xl p-8">
                <h3 class="text-cyan-400 mb-6">Real-Time Stats</h3>
                <div class="grid grid-cols-2 gap-8 text-center">
                    <div><div class="text-6xl font-bold text-cyan-400">42B+</div><div class="text-sm text-slate-400">Records</div></div>
                    <div><div class="text-6xl font-bold text-emerald-400">&lt;3s</div><div class="text-sm text-slate-400">Lookup Time</div></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function searchTarget() {
            const target = document.getElementById('target').value;
            if (target) alert('Intelligence + Bomber activated for: ' + target);
        }
    </script>
</body>
</html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
