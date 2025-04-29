package routes

import (
	"weather-api/controllers"
	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

func RegisterRoutes(e *echo.Echo, db *gorm.DB) {
	e.GET("/weather/:city", controllers.GetWeatherByCity(db))
}
