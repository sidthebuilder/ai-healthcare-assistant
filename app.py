from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "your-openai-api-key"  # Replace with your key or mock

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        question = request.form["question"]
        response = ask_openai(question)
    return render_template("index.html", response=response)

def ask_openai(question):
    # Mock for safety
    return f"Simulated response to: {question}"

if __name__ == "__main__":
    app.run(debug=True)
