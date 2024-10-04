import json

def fetch_all_bank_values(file_path):
    # Open and load the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    values = list(data.values())
    
    return values

def find_key_by_value(file_path, target_value):
    # Open and load the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Iterate through the dictionary to find the key by value
    for key, value in data.items():
        if value == target_value:
            return key
    
    return None

# Example usage
file_path = 'bank_codes.json'

# Fetch all bank values
values = fetch_all_bank_values(file_path)
print(values)

# Find the key for a specific bank
target_value = 'Zenith Bank International'
key = find_key_by_value(file_path, target_value)
print(f'The key for "{target_value}" is: {key}')
