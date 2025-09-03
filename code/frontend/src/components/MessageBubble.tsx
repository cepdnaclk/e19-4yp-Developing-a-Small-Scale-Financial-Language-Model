interface Props {
  sender: string;
  text: string;
}

export default function MessageBubble({ sender, text }: Props) {
  const isUser = sender === "user";
  return (
    <div
      className={`p-2 rounded max-w-xs ${
        isUser
          ? "bg-blue-500 text-white self-end ml-auto"
          : "bg-gray-200 text-black self-start mr-auto"
      }`}
    >
      {text}
    </div>
  );
}
