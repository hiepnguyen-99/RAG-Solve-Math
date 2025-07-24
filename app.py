from flask import Flask, render_template, request
from model.rag_engine import solve_question

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    docs = []
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "")
        if question.strip():
            answer, docs = solve_question(question)

    return render_template("index.html", question=question, answer=answer, docs=docs)

if __name__ == "__main__":
    app.run(debug=True)
