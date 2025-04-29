package proxy

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type WeatherData struct {
	City        string  `json:"city"`
	Temperature float64 `json:"temperature"`
}

type WeatherProxy struct {
	APIKey string
}

func NewWeatherProxy() *WeatherProxy {
	return &WeatherProxy{
		APIKey: os.Getenv("OPENWEATHER_API_KEY"),
	}
}

func (w *WeatherProxy) GetWeather(city string) (*WeatherData, error) {
	url := fmt.Sprintf(
		"http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric&lang=en",
		city, w.APIKey,
	)

	resp, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("HTTP request error: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("API returned status %d", resp.StatusCode)
	}

	var result struct {
		Name string `json:"name"`
		Main struct {
			Temp float64 `json:"temp"`
		} `json:"main"`
	}

	err = json.NewDecoder(resp.Body).Decode(&result)
	if err != nil {
		return nil, fmt.Errorf("JSON decoding error: %v", err)
	}

	return &WeatherData{
		City:        result.Name,
		Temperature: result.Main.Temp,
	}, nil
}
