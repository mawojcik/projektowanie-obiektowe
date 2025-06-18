package com.example.categoryproductapp

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.ShoppingCart
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProductListScreen(
    category: String,
    onBack: () -> Unit,
    onAddToCart: (String) -> Unit,
    onCartClicked: () -> Unit
) {
    val products = when (category) {
        "Elektronika" -> listOf("Laptop", "Smartfon", "Telewizor")
        "Odzież" -> listOf("Koszulka", "Spodnie", "Buty")
        "Dom" -> listOf("Lampa", "Krzesło", "Zasłony")
        else -> emptyList()
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Produkty: $category") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Wróć")
                    }
                },
                actions = {
                    IconButton(onClick = onCartClicked) {
                        Icon(Icons.Default.ShoppingCart, contentDescription = "Koszyk")
                    }
                }
            )
        }
    ) { padding ->
        LazyColumn(modifier = Modifier
            .padding(padding)
            .padding(16.dp)
        ) {
            items(products) { product ->
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 8.dp),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Text(product, style = MaterialTheme.typography.bodyLarge)
                    Button(onClick = { onAddToCart(product) }) {
                        Text("Dodaj")
                    }
                }
            }
        }
    }
}
