package com.example.shopapp.controller

import com.example.shopapp.model.Product
import com.example.shopapp.model.Payment
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/products")
class ProductController {
    @GetMapping
    fun getProducts(): List<Product> {
        return listOf(
            Product(1, "Laptop", 2999.99),
            Product(2, "Smartphone", 1999.99)
        )
    }
}