# Weather_App_GUI_Django

# What this project does?

This python program uses [WeatherAPI](https://www.weatherapi.com/) to get the localtime and current temperature of the user's given location.

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

![weather_app_django](https://github.com/Krish123-lang/Weather_App_GUI_Django/assets/56486342/ff26a4e6-6771-4219-8018-c7a62f2d729c)

THANK YOU 🙏
