package com.example.authdemo.service

import com.example.authdemo.model.AuthResponse
import org.springframework.stereotype.Service
import org.springframework.context.annotation.Scope

@Service
@Scope("singleton")
class EagerAuthService : AuthService {
    private val users = listOf("admin" to "admin", "user" to "user")

    override fun authenticate(username: String, password: String): AuthResponse {
        return if (users.any { it.first == username && it.second == password }) {
            AuthResponse(true, "Authentication successful")
        } else {
            AuthResponse(false, "Invalid credentials")
        }
    }
}
