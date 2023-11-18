from business_logic import AddressToCountryConverter
from data_input import AddressDataAccess
import hashlib
import random

cities_path = 'dataset/cities.jsonl'
addresses_path = 'dataset/addresses.jsonl'

address_data_access = AddressDataAccess(cities_path, addresses_path)
all_addresses = address_data_access.load_addresses()
subset_addresses = random.sample(all_addresses, 100)
converter = AddressToCountryConverter(address_data_access, subset_addresses)
result = converter.process_addresses()

for address, country in result.items():
    result_str = f"Address: {address} >> Country: {country}"
    result_hash = hashlib.sha256(result_str.encode()).hexdigest()
    print(f"{result_str} >> Hash: {result_hash}")
