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
                var selectedCategory by remember { mutableStateOf<String?>(null) }

                if (selectedCategory == null) {
                    CategoryListScreen(onCategorySelected = {
                        selectedCategory = it
                    })
                } else {
                    ProductListScreen(
                        category = selectedCategory!!,
                        onBack = { selectedCategory = null }
                    )
                }
            }
        }
    }
}
