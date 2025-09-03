import jwtDecode from "jwt-decode";

interface Props {
  roles: string[];
  children: JSX.Element;
}

interface DecodedToken {
  sub: string;
  role: string;
  exp: number;
}

export default function RoleGuard({ roles, children }: Props) {
  const token = localStorage.getItem("token");
  if (!token) return null;

  const decoded = jwtDecode<DecodedToken>(token);

  if (roles.includes(decoded.role)) {
    return children;
  }

  return <p className="p-4 text-red-500">Access denied</p>;
}
