package config

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"weather-api/models"
	"log"
)

func InitDB() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("weather.db"), &gorm.Config{})
	if err != nil {
		log.Fatalf("Can't connect with database: %v", err)
	}

	err = db.AutoMigrate(&models.WeatherData{})
	if err != nil {
		log.Fatalf("Can't create database: %v", err)
	}

	return db
}
