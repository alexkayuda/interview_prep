import sys
import json


def parse_json_from_argument():
    if len(sys.argv) < 2:
        print("Usage: python script.py '<json_string>'")
        return

    json_string = sys.argv[1]

    try:
        json_data = json.loads(json_string)
        print("Parsed JSON data:")
        print(json_data)
        print(type(json_data))
        print(isinstance(json_data, dict))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

def parse_json(input: str) -> str:

    try:
        json_data = json.loads(input)

        # Validation
        # print("Parsed JSON data:")
        # print(json_data)
        # print(type(json_data))
        print(isinstance(json_data, dict)) # True. Json is converted to dict data structure

        return json_data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

def convert_to_json(input: str) -> str:
    try:
        json_data = json.dumps(input)
        # print(json_data)
        return json_data
    except TypeError as e:
        print(f"Error serializing object to JSON: {e}")

if __name__ == "__main__":

    dict_data = {
        "name": "John",
        "age": 40,
        "city": "Los Angeles"
    }

    json_data = '{"name": "Mike", "age": 30, "city": "New York"}'

    print(parse_json(json_data)) # valid JSON
    print(convert_to_json(dict_data)) # valid dict
