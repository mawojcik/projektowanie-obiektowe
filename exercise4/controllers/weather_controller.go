package controllers

import (
	"net/http"
	"time"
	"weather-api/models"
	"weather-api/proxy"
	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

func GetWeatherByCity(db *gorm.DB) echo.HandlerFunc {
	return func(c echo.Context) error {
		city := c.Param("city")
		weatherProxy := proxy.NewWeatherProxy()

		weatherData, err := weatherProxy.GetWeather(city)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, echo.Map{
				"error": "Couldn't load weather data: " + err.Error(),
			})
		}

		hour := time.Now().Format("15:04")
		newWeatherData := models.WeatherData{
			City:     weatherData.City,
			Time:    hour,
			Temperature: weatherData.Temperature,
		}

		if err := db.Create(&newWeatherData).Error; err != nil {
			return c.JSON(http.StatusInternalServerError, echo.Map{
				"error": "Problem with saving data to database: " + err.Error(),
			})
		}

		return c.JSON(http.StatusOK, echo.Map{
			"city":     newWeatherData.City,
			"time":    newWeatherData.Time,
			"temperature": newWeatherData.Temperature,
		})
	}
}
