"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState("");

  const handleSubmit = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    setTimeout(() => {
      setAnswer("Đây là lời giải cho: " + question);
      setLoading(false);
    }, 1500);
  };

  return (
    <main className="max-w-xl mx-auto px-4 py-10 flex flex-col gap-6">
      <h1 className="text-xl font-semibold text-center">SML Giải Toán</h1>

      <Textarea
        placeholder="Nhập câu hỏi toán học..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="min-h-[100px]"
      />

      <Button
        onClick={handleSubmit}
        disabled={loading}
        className="w-full"
      >
        {loading ? "Đang xử lý..." : "Giải toán"}
      </Button>

      {answer && (
        <div className="bg-gray-100 text-sm p-4 rounded-md">
          <strong>Kết quả:</strong> {answer}
        </div>
      )}

      <p className="text-xs text-center text-gray-400 mt-10">
        © 2025 AI Giải Toán
      </p>
    </main>
  );
}