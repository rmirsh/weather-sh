USE_ROUNDED_COORDS = True
OPENWEATHER_API = 'ccd50abc9a933170ba5ea24670e9c010'
OPENWEATHER_URL =(
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + OPENWEATHER_API + "&lang=ru&"
        "units=metric"
        )
