#1
import requests
class InvalidUrlError(Exception):
    def __init__(self, url):
        self.url = url
        super().__init__(f"Invalid URL: {url}")
def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        data = response.text
        print(data)
    except requests.exceptions.RequestException:
        raise InvalidUrlError(url)
def Unable_url_len(url):
    if len.url > 20:
        raise InvalidUrlError(url)
try:
    data = fetch_data_from_url("https://google.com")
except InvalidUrlError as i:
    print(f"Error: {i}")
except ValueError as i:
    print(f"Value Error: {i}")

 #2
class UserNotFoundError(Exception):
    def __init__(self, user):
        self.user = user
class USerInfoFoundError(Exception):
    def __init__(self, user):
        self.user = user
class UserDatabase:
    def __init__(self):
         self.base = {}
    def get_user(self, user):
        if user not in self.base:
            raise UserNotFoundError(user)
        else:
            print(f'Username: {user}')
    def get_info(self, user):
        if user in self.base:
            for value, key in self.base[user].items():
                if key == None:
                    raise USerInfoFoundError(user)
            print(f'User info: {self.base[user]}')
        else:
            return None

U_base = UserDatabase()
U_base.base = {'oleg123': {'name': 'Oleg', 'surname': 'Bondar'},
               'liza253': {'name': None, 'surname': None}
               }

user = input('Enter username: ')
try:
    U_base.get_user(user)
except UserNotFoundError as e:
    print(f'Користувача з іменем "{e}" не було знайдено')
try:
    U_base.get_info(user)
except USerInfoFoundError as i:
    print(f'Дані користувача з іменем "{i}" не було знайдено')

#3
class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        try:
            fahrenheit = (celsius * 1.8) + 32
            fahrenheit = round(fahrenheit, 2)
            if fahrenheit < 0 or fahrenheit > 100:
                raise ValueError(fahrenheit)
            return round(fahrenheit, 2)
        except Exception as e:
            raise e
    def fahrenheit_to_celsius(self, fahrenheit):
        try:
            celsius = (fahrenheit - 32) / 1.8
            celsius = round(celsius, 2)
            if celsius < 0 or celsius > 100:
                raise ValueError(celsius)
            return round(celsius, 2)
        except Exception as e:
            raise e
t =TemperatureConverter()
try:
    print(t.celsius_to_fahrenheit('введіть значення'))
except ValueError as i:
    print(f'Значення не має бути меншим за нуль та більшим за 100: {i}')
except Exception as e:
    print(f"Error: {e}")


try:
    print(t.fahrenheit_to_celsius('введіть значення'))
except ValueError as i:
    print(f'Значення не має бути меншим за нуль та більшим за 100: {i}')
except Exception as e:
    print(f"Error: {e}")

