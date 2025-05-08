import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Products from "./Products";
import Payments from "./Payments";
import Cart from "./Cart";
import Navbar from "./Navbar";
import { CartProvider } from "./CartContext";

function App() {
    return (
        <CartProvider>
            <Router>
                <Navbar />
                <Routes>
                    <Route path="/" element={<Products />} />
                    <Route path="/payments" element={<Payments />} />
                    <Route path="/cart" element={<Cart />} />
                </Routes>
            </Router>
        </CartProvider>
    );
}

export default App;
