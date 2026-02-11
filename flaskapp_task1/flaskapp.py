from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                margin: 0;
                height: 100vh;
                background-image: url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f');
                background-size: cover;
                background-position: center;
                font-family: Arial, sans-serif;
            }

            .overlay {
                background: rgba(255, 255, 255, 0.85);
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            h1 {
                color: #2c3e50;
                margin-bottom: 10px;
            }

            p {
                font-size: 18px;
                margin-bottom: 20px;
            }

            input {
                padding: 12px;
                width: 240px;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 16px;
                margin-bottom: 25px;
                text-align: center;
            }

            .btn {
                width: 240px;
                padding: 14px;
                margin: 8px 0;
                text-align: center;
                text-decoration: none;
                color: white;
                font-size: 18px;
                border-radius: 12px;
                display: block;
                border: none;
                cursor: pointer;
            }

            .blue { background: #3498db; }
            .purple { background: #9b59b6; }
            .green { background: #27ae60; }
            .orange { background: #e67e22; }
        </style>
    </head>

    <body>
        <div class="overlay">
            <h1>✨ Welcome to the Flask Fun App ✨</h1>
            <p>Enter your name 👇</p>

            <form method="get">
                <input type="text" name="name" placeholder="Type your name" required>

                <button formaction="/upper" class="btn blue">UPPER CASE 🔠</button>
                <button formaction="/reverse" class="btn purple">REVERSE NAME 🔁</button>
                <button formaction="/length" class="btn green">NAME LENGTH 📏</button>
                <button formaction="/style" class="btn orange">STYLED PAGE 🎨</button>
            </form>
        </div>
    </body>
    </html>
    """


@app.route('/upper')
def upper():
    name = request.args.get('name', 'Guest')
    return f"""
    <html>
    <body style="background:#e8f4fd; text-align:center; font-family:Verdana;">

        <h1 style="margin-top:80px; color:#1f3a8a;">
            🔠 HELLO {name.upper()}
        </h1>

        <p style="font-size:20px; margin-top:20px;">
            Converted to UPPER CASE ✨
        </p>

        <div style="margin-top:40px;">
            👉 <a href="/" style="background:#1f3a8a; color:white;
            padding:12px 22px; text-decoration:none; border-radius:8px;">
            🏠 Back Home
            </a>
        </div>

    </body>
    </html>
    """

@app.route('/reverse')
def reverse():
    name = request.args.get('name', 'Guest')
    return f"""
    <html>
    <body style="background:#fbeffb; text-align:center; font-family:Tahoma;">

        <h1 style="margin-top:80px; color:#6a0572;">
            🔁 {name[::-1]}
        </h1>

        <p style="font-size:20px; margin-top:20px;">
            Name reversed successfully ✨
        </p>

        <div style="margin-top:40px;">
            👉 <a href="/" style="background:#6a0572; color:white;
            padding:12px 22px; text-decoration:none; border-radius:8px;">
            🏠 Back Home
            </a>
        </div>

    </body>
    </html>
    """

# ---------------- LENGTH PAGE ----------------
@app.route('/length')
def length():
    name = request.args.get('name', 'Guest')
    return f"""
    <html>
    <body style="background:#ecf9f1; text-align:center; font-family:Georgia;">

        <h1 style="margin-top:80px; color:#145a32;">
            📏 Length: {len(name)}
        </h1>

        <p style="font-size:20px; margin-top:20px;">
            Total number of characters 🔢
        </p>

        <div style="margin-top:40px;">
            👉 <a href="/" style="background:#145a32; color:white;
            padding:12px 22px; text-decoration:none; border-radius:8px;">
            🏠 Back Home
            </a>
        </div>

    </body>
    </html>
    """

# ---------------- STYLED PAGE ----------------
@app.route('/style')
def style():
    name = request.args.get('name', 'Guest').upper()
    return f"""
    <html>
    <body style="background:linear-gradient(to right,#ff9a9e,#fad0c4);
    text-align:center; font-family:'Comic Sans MS';">

        <h1 style="margin-top:90px; color:#4a0635; font-size:42px;">
            ✨ WELCOME {name} ✨
        </h1>

        <p style="font-size:22px; margin-top:25px;">
            Flask + Creativity = 💖
        </p>

        <div style="margin-top:50px;">
            👉 <a href="/" style="background:white; color:#ff6f91;
            padding:14px 26px; text-decoration:none; border-radius:25px;">
            🏠 Go Home
            </a>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
