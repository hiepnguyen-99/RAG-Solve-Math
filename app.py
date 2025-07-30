from flask import Flask, render_template, request
from flask import render_template_string
import markdown
import os
from model.rag_4b import solve_question_4b
from model.rag_15b import solve_question_15b

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    docs = []
    question = ""
    k = 3
    model_choice = "4b"  # mặc định

    if request.method == "POST":
        question = request.form.get("question", "")
        k_str = request.form.get("k", "3")
        model_choice = request.form.get("model", "4b")

        try:
            k = int(k_str)
        except ValueError:
            k = 3

        if question.strip():
            if model_choice == "1_5b":
                answer, docs = solve_question_15b(question, k=k)
            else:
                answer, docs = solve_question_4b(question, k=k)

    return render_template("index.html", question=question, answer=answer, docs=docs, k=k, model=model_choice)

@app.route("/view/<path:filename>")
def view_markdown(filename):
    filepath = os.path.join("test", filename)
    if not os.path.exists(filepath):
        return "File not found", 404

    with open(filepath, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convert markdown to HTML
    html = markdown.markdown(md_content)

    # Wrap trong HTML template
    return render_template_string("""
    <html>
    <head>
        <title>{{ filename }}</title>
        <meta charset="utf-8">
    </head>
    <body style="font-family: sans-serif; padding: 40px;">
        <a href="/">⬅ Quay lại</a>
        <hr>
        {{ html_content|safe }}
    </body>
    </html>
    """, filename=filename, html_content=html)


if __name__ == "__main__":
    app.run(debug=True)
