from flask import Flask, render_template, request, jsonify
from realestateBot import realestateBot

app = Flask(__name__)
bot = realestateBot()

@app.route("/")
def index():
    return render_template("bot.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").strip()
    bot_msg = bot.chat(user_msg)  # directly use chat() from the class
    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
