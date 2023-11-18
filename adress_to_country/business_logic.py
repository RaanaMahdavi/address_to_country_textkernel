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
        self.multiword_cities = set(city for city in self.city_to_country if ' ' in city)
    def find_country_in_address(self, address):
        normalized_address = self.address_data_access.normalize(address)

        for multiword_city in self.multiword_cities:
            if multiword_city in normalized_address:
                return self.city_to_country.get(multiword_city, "Unknown")

        tokens = normalized_address.split()
        for token in tokens:
            if token in self.country_names_to_code:
                return self.country_names_to_code[token]
            elif token in self.city_to_country:
                return self.city_to_country[token]

            for city in self.city_to_country.keys():
                if Levenshtein.distance(token, city) <= 2:
                    return self.city_to_country[city]

        return "Unknown"
    def process_addresses(self):
        results = {}
        for address_dict in self.addresses_data:
            address_str = address_dict['address']
            country = self.find_country_in_address(address_str)
            results[address_str] = country
        return results

    @staticmethod
    def get_hash_of_results(results):
        results_str = json.dumps(results, sort_keys=True)
        return hashlib.sha256(results_str.encode()).hexdigest()
