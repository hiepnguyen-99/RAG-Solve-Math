from flask import Flask, render_template, request
from model.rag_engine import solve_question

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    docs = []
    question = ""
    k = 3  # mặc định lấy 3 tài liệu nếu người dùng chưa chọn

    if request.method == "POST":
        question = request.form.get("question", "")
        k_str = request.form.get("k", "3")  # lấy giá trị từ select, luôn là chuỗi
        try:
            k = int(k_str)
        except ValueError:
            k = 3  # fallback nếu không chuyển được sang int

        if question.strip():
            answer, docs = solve_question(question, k=k)

    return render_template("index.html", question=question, answer=answer, docs=docs, k=k)

if __name__ == "__main__":
    app.run(debug=True)
