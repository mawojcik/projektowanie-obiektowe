package com.example.authdemo.service

import com.example.authdemo.model.AuthResponse

interface AuthService {
    fun authenticate(username: String, password: String): AuthResponse
}
