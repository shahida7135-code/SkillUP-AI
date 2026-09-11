from flask import Flask, redirect
from part4.routes import part4_bp

app = Flask(__name__)

# Register Part 4 routes
app.register_blueprint(part4_bp)


@app.route("/")
def home():
    # Open the existing AI Assistant page
    return redirect("/ai")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )