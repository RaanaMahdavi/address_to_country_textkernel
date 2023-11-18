# data_input.py
import json
import re
from unidecode import unidecode
import pycountry

class AddressDataAccess:
    def __init__(self, cities_file, addresses_file):
        self.cities_file = cities_file
        self.addresses_file = addresses_file

    @staticmethod
    def normalize(text):
        text = text.lower()
        text = unidecode(text)
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^a-z\s]', '', text)
        return text.strip()

    def load_cities(self):
        try:
            with open(self.cities_file, 'r', encoding='utf-8') as file:
                cities_data = [json.loads(line) for line in file]
                return {self.normalize(item['city']): item['country'] for item in cities_data}
        except UnicodeDecodeError as e:
            print(f"Error decoding file {self.cities_file}: {e}")
            return {}
        except FileNotFoundError:
            print(f"Error: Cities file not found: {self.cities_file}")
            return {}

    def load_addresses(self):
        try:
            with open(self.addresses_file, 'r', encoding='utf-8') as file:
                return [json.loads(line) for line in file]
        except UnicodeDecodeError as e:
            print(f"Error decoding file {self.addresses_file}: {e}")
            return []
        except FileNotFoundError:
            print(f"Error: Addresses file not found: {self.addresses_file}")
            return []

    def create_country_mapping(self):
        country_mapping = {}
        for country in pycountry.countries:
            country_name = self.normalize(country.name)
            country_mapping[country_name.strip()] = country.alpha_2
        return country_mapping
