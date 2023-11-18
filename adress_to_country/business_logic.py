import hashlib
import json
from data_input import AddressDataAccess
import Levenshtein

class AddressToCountryConverter:
    def __init__(self, address_data_access, addresses):
        self.address_data_access = address_data_access
        self.city_to_country = address_data_access.load_cities()
        self.addresses_data = addresses
        self.country_names_to_code = address_data_access.create_country_mapping()
        self.multiword_cities = {city for city, item in self.city_to_country.items() if ' ' in item}

    def find_country_in_address(self, address):
        normalized_address = self.address_data_access.normalize(address)

        for multiword_city in self.multiword_cities:
            if multiword_city in normalized_address:
                return next((item.get('country', "Unknown") for item in self.city_to_country if
                             item.get('city') == multiword_city), "Ujnknown")

        tokens = normalized_address.split()
        for token in tokens:
            if token in self.country_names_to_code:
                return self.country_names_to_code[token]
            elif any(Levenshtein.distance(token, city) <= 2 for city in self.multiword_cities):
                return next(
                    country for city, country in self.city_to_country.items() if Levenshtein.distance(token, city) <= 2
                )

        return "Unknown"
    def process_addresses(self):
        results = {}
        for address_dict in self.addresses_data:
            address_str = address_dict.get('address', '')
            country = self.find_country_in_address(address_str)
            results[address_str] = country
        return results
    def get_hash_of_results(results):
        results_str = json.dumps(results, sort_keys=True)
        return hashlib.sha256(results_str.encode()).hexdigest()
