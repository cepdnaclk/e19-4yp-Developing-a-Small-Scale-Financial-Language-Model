import { useState } from "react";
import API from "../api";
import MessageBubble from "../components/MessageBubble";

export default function Chat() {
  const [messages, setMessages] = useState<{ sender: string; text: string }[]>(
    []
  );
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    setMessages([...messages, { sender: "user", text: input }]);
    const res = await API.post("/rag/query", { query: input });
    setMessages((prev) => [...prev, { sender: "bot", text: res.data.answer }]);
    setInput("");
  };

  return (
    <div className="flex flex-col p-4">
      <div className="flex-1 space-y-2">
        {messages.map((m, i) => (
          <MessageBubble key={i} sender={m.sender} text={m.text} />
        ))}
      </div>
      <div className="flex gap-2 mt-4">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border p-2 rounded"
        />
        <button
          onClick={sendMessage}
          className="bg-green-600 text-white px-4 py-2 rounded"
        >
          Send
        </button>
      </div>
    </div>
  );
}
