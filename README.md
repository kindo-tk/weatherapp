# Weather Forecast Web App using Flask

A simple and secure weather forecasting web application built using Flask that fetches real-time weather data from the OpenWeather API based on user-input city names.

The application follows best practices for API key security, environment variable management, and cloud deployment.

---

## Features

- Search current weather by city name
- Displays real-time temperature in Celsius
- Clean UI using Flask templates
- Secure handling of API keys using environment variables
- Ready for cloud deployment on Render
- No API keys exposed in frontend or GitHub

## Tech Stack

- Backend: Python, Flask
- API: OpenWeather API
- HTTP Client: Requests
- Frontend: HTML (Flask Jinja templates)
- Deployment: Render
- Version Control: Git & GitHub
  
---

## Project Structure

```text
weather_app/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and folders
├── templates/
│   ├── index.html          # Homepage with city input form
│   └── results.html        # Weather result display page
└── README.md               # Project documentation
```
---

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kindo-tk/weatherapp.git
   ```
2. **Navigate to the project directory:**

    ```sh
    cd weatherapp
    ```

3. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    ```

4. **Activate the virtual environment:**

   ```sh
   .venv\Scripts\activate
   ```

5. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```
6. **Create .env file:**

      ```
      Create a .env file in the project root:
    
      WEATHER_API_KEY=your_openweather_api_key_here
    ```
7. **Run the application:**

    ```sh
    python app.py
    ```
    The app will run at:

    ```sh
    http://127.0.0.1:5000
    ```
---

## Live Deployment

The application is deployed on Render and publicly accessible here:

🔗 Live App: https://weatherapp-hws1.onrender.com

---

## Deployment highlights:

- Environment variables configured directly on Render

- API key securely injected at runtime

- Backend-only API communication ensures key safety

---
## Contact

For any inquiries or feedback, please contact:

- [Tufan Kundu (LinkedIn)](https://www.linkedin.com/in/tufan-kundu-577945221/)
- Email: tufan.kundu11@gmail.com

---
## Demo
<img src="https://github.com/kindo-tk/images/blob/main/weather_app/weather_new1.png" width="600">
<img src="https://github.com/kindo-tk/images/blob/main/weather_app/weather_new2.png" width="600">


