package models

import (
	"time"
)

type WeatherData struct {
	ID         uint
	City     string
	Time    string
	Temperature float64
	CreatedAt  time.Time
}
