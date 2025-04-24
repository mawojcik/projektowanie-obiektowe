package com.example.authdemo.config

import com.example.authdemo.service.AuthService
import com.example.authdemo.service.EagerAuthService
 import com.example.authdemo.service.LazyAuthService
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration

@Configuration
class AuthConfig {
    @Bean
    fun authService(): AuthService {
//        return EagerAuthService()
        return LazyAuthService()
    }
}
