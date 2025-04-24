package com.example.authdemo.service

import com.example.authdemo.model.AuthResponse
import org.springframework.stereotype.Component
import org.springframework.context.annotation.Scope
import org.springframework.context.annotation.Lazy

@Component
@Scope("singleton")
@Lazy
class LazyAuthService : AuthService {
    private val users = listOf("admin" to "admin", "user" to "user")

    override fun authenticate(username: String, password: String): AuthResponse {
        return if (users.any { it.first == username && it.second == password }) {
            AuthResponse(true, "Authentication successful (lazy)")
        } else {
            AuthResponse(false, "Invalid credentials (lazy)")
        }
    }
}
