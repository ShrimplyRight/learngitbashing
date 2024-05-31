import argparse

def main():
    parser = argparse.ArgumentParser(description='My Program Description')
    parser.add_argument('--input', type=str, help='Input file')
    parser.add_argument('--output', type=str, help='Output file')
    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")

if __name__ == "__main__":
    main()
    
import json
import jsonschema
from jsonschema import validate
import argparse

def load_and_validate_json(file_path, schema):
    with open(file_path, 'r') as file:
        data = json.load(file)
    validate(instance=data, schema=schema)
    return data

def main():
    parser = argparse.ArgumentParser(description='My Program Description')
    parser.add_argument('--input', type=str, help='Input JSON file')
    parser.add_argument('--output', type=str, help='Output file')
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
        print(data)
    except jsonschema.exceptions.ValidationError as e:
        print(f"Invalid JSON: {e.message}")

if __name__ == "__main__":
    main()
