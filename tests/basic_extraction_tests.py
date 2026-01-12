import os
from pathlib import Path
import json

def test_extraction_has_description():
    path = Path('../raw_samples/')

    files_to_test = []

    for item in path.iterdir():
        files_to_test.append(item)

    for file in files_to_test:
        with open(file, "r") as f:
            data = f.read()
            data = json.loads(data)

            assert "description" in data.keys(), "Config file missing description"
            assert data["description"], f"Description is falsy, of type {type(data['description'])}"


def test_extraction_desc_size():
    path = Path('../raw_samples/')

    files_to_test = []

    for item in path.iterdir():
        files_to_test.append(item)

    for file in files_to_test:
        with open(file, "r") as f:
            data = f.read()
            data = json.loads(data)

            assert len(data['description']), f"Description is falsy, of type {type(data['description'])}"


def test_extraction_has_price():
    path = Path('../raw_samples/')
    files_to_test = []
    for item in path.iterdir():
        files_to_test.append(item)
    for file in files_to_test:
        with open(file, "r") as f:
            data = f.read()
            data = json.loads(data)
            assert "price" in data.keys(), f"Config file missing price in {file}"

def test_extraction_price_is_num():
    path = Path('../raw_samples/')
    files_to_test = []
    for item in path.iterdir():
        files_to_test.append(item)
    for file in files_to_test:
        with open(file, "r") as f:
            data = f.read()
            data = json.loads(data)
            assert isinstance(data['price'], (int, float)), f"Price is not numeric, got {type(data['price'])} in {file}"
            assert data['price'] > 0, f"Price must be positive, got {data['price']} in {file}"
            assert data['price'] < 100000, f"Price suspiciously high: {data['price']} in {file}"  # Sanity check

def test_extraction_has_address():
    path = Path('../raw_samples/')
    files_to_test = []
    for item in path.iterdir():
        files_to_test.append(item)
    for file in files_to_test:
        with open(file, "r") as f:
            data = f.read()
            data = json.loads(data)
            assert "address" in data.keys(), f"Config file missing address in {file}"
            assert data["address"], f"Address is falsy in {file}"

def test_extraction_valid_address():
    path = Path('../raw_samples/')
    files_to_test = []
    for item in path.iterdir():
        files_to_test.append(item)
    for file in files_to_test:
        with open(file, "r") as f:
            data = f.read()
            data = json.loads(data)
            address = data.get('address', '')
            # Basic validation: has street name and postcode pattern
            assert len(address) > 10, f"Address too short: '{address}' in {file}"
            # Check for NSW postcode pattern (or adjust for your region)
            assert any(char.isdigit() for char in address), f"Address missing numbers: '{address}' in {file}"
            # Check has some alphabetic characters (street name)
            assert any(char.isalpha() for char in address), f"Address missing letters: '{address}' in {file}"


test_extraction_desc_size()
test_extraction_has_address()
test_extraction_has_description()
test_extraction_has_price()
test_extraction_price_is_num()
test_extraction_valid_address()
