import React, { useEffect, useState } from "react";
import { useCart } from "./CartContext";

const Products = () => {
    const [products, setProducts] = useState([]);
    const { addToCart } = useCart();

    useEffect(() => {
        fetch("/api/products")
            .then((res) => res.json())
            .then(setProducts);
    }, []);

    return (
        <div>
            <h2>Produkty</h2>
            <ul>
                {products.map((product) => (
                    <li key={product.id}>
                        {product.name} – {product.price} zł
                        <button onClick={() => addToCart(product)}>Dodaj do koszyka</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Products;
