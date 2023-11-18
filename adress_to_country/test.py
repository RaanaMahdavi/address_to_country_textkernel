from business_logic import AddressToCountryConverter
from data_input import AddressDataAccess
import hashlib
import random

cities_path = 'dataset/cities.jsonl'
addresses_path = 'dataset/addresses.jsonl'

address_data_access = AddressDataAccess(cities_path, addresses_path)
all_addresses = address_data_access.load_addresses()
sample_n=100
subset_addresses = random.sample(all_addresses, sample_n)
converter = AddressToCountryConverter(address_data_access, subset_addresses)

result = converter.process_addresses()
known_count = 0

for address, country in result.items():
    result_str = f"Address: {address} >> Country: {country}"
    result_hash = hashlib.sha256(result_str.encode()).hexdigest()
    print(f"{result_str} >> Hash: {result_hash}")
    if country != "Unknown":
        known_count += 1
print(f"Number of addresses with detected country: {known_count} out of 100 samples")
