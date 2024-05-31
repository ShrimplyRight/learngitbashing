import json
import jsonschema
from jsonschema import validate
import argparse

def load_and_validate_json(file_path, schema):
    with open(file_path, 'r') as file:
        data = json.load(file)
    validate(instance=data, schema=schema)
    return data

def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='My Program Description')
    parser.add_argument('--input', type=str, help='Input JSON file')
    parser.add_argument('--output', type=str, help='Output JSON file')
    args = parser.parse_args()

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"},
        },
        "required": ["name", "age"]
    }

    try:
        data = load_and_validate_json(args.input, schema)
        print("JSON is valid")
        save_to_json(data, args.output)
        print(f"Data saved to {args.output}")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Invalid JSON: {e.message}")

if __name__ == "__main__":
    main()
