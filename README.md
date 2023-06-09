# Weather_App_GUI_Django

# What this project does?

This python program utilizes [WeatherAPI](https://www.weatherapi.com/) to retrieve data from Weather API. The data that are fetched by this project are: User's Localtime, temperature of the user given place, Longitude, Latitude, Condition, Wind Speed (milesperhour/kilometresperhour) and Humidity.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.

1. First of all create a isolated environment in your folder using following commands

```bash
i) virtualenv env
ii) env\Scripts\activate

```

2. Then install tools using  

 ```python
 pip install -r requirements.txt
```
3. To get the API Key you need to create an account on [WeatherAPI](https://www.weatherapi.com/). 
4. Then, copy your API key and paste it in `.env` file replacing <Your_Weather_API_Key> with your API key.
5. Then use

```python
 python manage.py makemigration
 python manage.py migrate
 python manage.py runserver
 ```

6. Copy the url(127.0.0.1:8000) and open it into your browser.
7. You must see this screen
![weather_app_django (2)](https://github.com/Krish123-lang/Weather_App_GUI_Django/assets/56486342/6c48dd54-7732-400d-b314-efb5cd337b4f)


THANK YOU 🙏
