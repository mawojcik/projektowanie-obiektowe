package main

import (
	"weather-api/config"
	"weather-api/routes"

	"github.com/labstack/echo/v4"
	"github.com/joho/godotenv"
	"log"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	db := config.InitDB()
	e := echo.New()

	routes.RegisterRoutes(e, db)

	e.Logger.Fatal(e.Start(":8080"))
}
