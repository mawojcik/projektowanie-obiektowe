package com.example.shopapp.controller

import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/payments")
class PaymentController {

    data class Payment(val id: Long, val product: String, val amount: Double)

    private val payments = mutableListOf<Payment>()
    private var nextId = 1L

    @GetMapping
    fun getPayments(): List<Payment> = payments

    @PostMapping
    fun addPayment(@RequestBody payment: Payment): Payment {
        val newPayment = payment.copy(id = nextId++)
        payments.add(newPayment)
        return newPayment
    }
}
