from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

API_KEY = os.getenv("WEATHER_API_KEY")

if API_KEY is None:
    raise RuntimeError("WEATHER_API_KEY not found in environment variables")

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=['POST'])
def get_weatherdata():
    try:
        city = request.form.get("city")

        if not city:
            raise ValueError("City not provided")

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        temp = data['main']['temp']
        result = f"City: {city}, Temperature: {temp}°C"

    except Exception:
        result = "Sorry, city not found! Try another city."

    return render_template("results.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
