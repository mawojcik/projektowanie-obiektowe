import React from "react";
import { useCart } from "./CartContext";

const Cart = () => {
    const { cartItems, clearCart } = useCart();

    const handleBuy = () => {
        cartItems.forEach((item) => {
            fetch("/api/payments", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ id: 0, product: item.name, amount: item.price }),
            });
        });
        clearCart();
    };

    const total = cartItems.reduce((sum, item) => sum + item.price, 0);

    return (
        <div>
            <h2>Koszyk</h2>
            {cartItems.length === 0 ? (
                <p>Twój koszyk jest pusty</p>
            ) : (
                <>
                    <ul>
                        {cartItems.map((item, idx) => (
                            <li key={idx}>
                                {item.name} – {item.price} zł
                            </li>
                        ))}
                    </ul>
                    <p>Łącznie: {total.toFixed(2)} zł</p>
                    <button onClick={handleBuy}>Kup wszystko</button>
                </>
            )}
        </div>
    );
};

export default Cart;
