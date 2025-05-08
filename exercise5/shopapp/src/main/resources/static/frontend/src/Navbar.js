import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
    <nav style={{ display: "flex", gap: "1rem", padding: "1rem" }}>
        <Link to="/">Produkty</Link>
        <Link to="/cart">Koszyk</Link>
        <Link to="/payments">Płatności</Link>
    </nav>
);

export default Navbar;
