package com.example.authdemo.controller

import com.example.authdemo.model.AuthRequest
import com.example.authdemo.model.AuthResponse
import com.example.authdemo.service.AuthService
import org.springframework.web.bind.annotation.*
import org.springframework.beans.factory.annotation.Autowired

@RestController
@RequestMapping("/api")
class AuthController @Autowired constructor(private val authService: AuthService) {

    @PostMapping("/login")
    fun login(@RequestBody authRequest: AuthRequest): AuthResponse {
        return authService.authenticate(authRequest.username, authRequest.password)
    }

    @GetMapping("/users")
    fun getUsers(): List<String> = listOf("admin", "user")
}
