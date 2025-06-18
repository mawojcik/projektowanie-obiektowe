package com.example.categoryproductapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.runtime.*
import com.example.categoryproductapp.CategoryListScreen
import com.example.categoryproductapp.ProductListScreen
import com.example.categoryproductapp.CategoryProductAppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            CategoryProductAppTheme {
                var screen by remember { mutableStateOf<Screen>(Screen.CategoryList) }
                val cart = remember { mutableStateListOf<String>() }

                when (val currentScreen = screen) {
                    is Screen.CategoryList -> CategoryListScreen(
                        onCategorySelected = { category ->
                            screen = Screen.ProductList(category)
                        },
                        onCartClicked = {
                            screen = Screen.Cart
                        }
                    )
                    is Screen.ProductList -> ProductListScreen(
                        category = currentScreen.category,
                        onBack = { screen = Screen.CategoryList },
                        onAddToCart = { product -> cart.add(product) },
                        onCartClicked = { screen = Screen.Cart }
                    )
                    is Screen.Cart -> CartScreen(
                        cartItems = cart,
                        onBack = { screen = Screen.CategoryList }
                    )
                }
            }
        }
    }
}

sealed class Screen {
    object CategoryList : Screen()
    data class ProductList(val category: String) : Screen()
    object Cart : Screen()
}
