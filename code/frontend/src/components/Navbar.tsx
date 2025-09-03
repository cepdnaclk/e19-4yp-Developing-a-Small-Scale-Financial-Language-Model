import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav className="bg-gray-800 text-white p-4 flex gap-4">
      <Link to="/chat">Chat</Link>
      <Link to="/admin">Admin</Link>
      {token ? (
        <button onClick={logout} className="ml-auto text-red-400">
          Logout
        </button>
      ) : (
        <Link to="/login" className="ml-auto">
          Login
        </Link>
      )}
    </nav>
  );
}
