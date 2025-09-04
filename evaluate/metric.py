import json
from typing import List, Dict
from sklearn.metrics import precision_score, recall_score
from bert_score import score as bertscore

# Đánh giá RAG lý thuyết
# answer_file: file json kết quả RAG, ground_truth_file: file json đáp án đúng
# Mỗi entry: {"index": ..., "input": ..., "output": ...}
def evaluate_rag_theory(answer_file: str, ground_truth_file: str, k: int = 1):
    with open(answer_file, 'r', encoding='utf-8') as f:
        answers = json.load(f)
    with open(ground_truth_file, 'r', encoding='utf-8') as f:
        ground_truth = json.load(f)
    # Giả sử ground_truth là list các đáp án đúng cho từng câu
    y_true = [gt['output'] for gt in ground_truth]
    y_pred = [ans['output'] for ans in answers]
    # Precision@k, Recall@k: với k=1, so sánh trực tiếp
    precision = precision_score(y_true, y_pred, average='micro', zero_division=0)
    recall = recall_score(y_true, y_pred, average='micro', zero_division=0)
    # BertScore
    P, R, F1 = bertscore(y_pred, y_true, lang="vi")
    print(f"Precision@{k}: {precision}")
    print(f"Recall@{k}: {recall}")
    print(f"BertScore F1: {F1.mean().item()}")
    return precision, recall, F1.mean().item()

# Đánh giá giải toán
# answer_file: file json kết quả giải toán, ground_truth_file: file json đáp án đúng
# Mỗi entry: {"index": ..., "input": ..., "output": ...}
def evaluate_math(answer_file: str, ground_truth_file: str):
    with open(answer_file, 'r', encoding='utf-8') as f:
        answers = json.load(f)
    with open(ground_truth_file, 'r', encoding='utf-8') as f:
        ground_truth = json.load(f)
    y_true = [gt['output'] for gt in ground_truth]
    y_pred = [ans['output'] for ans in answers]
    def step_by_step_consistency(pred_steps: list, true_steps: list) -> float:
        """
        Đánh giá độ nhất quán từng bước giữa kết quả và đáp án đúng.
        Tính tỉ lệ các bước giống nhau trên tổng số bước của đáp án đúng.
        """
        if not isinstance(pred_steps, list) or not isinstance(true_steps, list):
            return 0.0
        matches = sum([p.strip() == t.strip() for p, t in zip(pred_steps, true_steps)])
        return matches / max(len(true_steps), 1)

        # Step-by-step Consistency: dùng hàm step_by_step_consistency
        consistency_scores = []
        for pred, true in zip(y_pred, y_true):
            score = step_by_step_consistency(pred, true)
            consistency_scores.append(score)
        if consistency_scores:
            print(f"Step-by-step Consistency: {sum(consistency_scores)/len(consistency_scores)}")
        return accuracy, consistency_scores
