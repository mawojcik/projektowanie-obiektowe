import React, { useEffect, useState } from "react";

const Payments = () => {
    const [payments, setPayments] = useState([]);

    useEffect(() => {
        const interval = setInterval(() => {
            fetch("/api/payments")
                .then((res) => res.json())
                .then((data) => setPayments(data));
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h2>Historia płatności</h2>
            <ul>
                {payments.map((payment) => (
                    <li key={payment.id}>
                        {payment.product} – {payment.amount} zł
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Payments;
