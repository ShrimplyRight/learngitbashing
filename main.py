import json
import yaml
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

def load_and_validate_yaml(file_path, schema):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    validate(instance=data, schema=schema)
    return data

def main():
    parser = argparse.ArgumentParser(description='My Program Description')
    parser.add_argument('--input', type=str, help='Input file (JSON or YAML)')
    parser.add_argument('--output', type=str, help='Output JSON file')
    parser.add_argument('--format', type=str, choices=['json', 'yaml'], help='Input file format')
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
        if args.format == 'json':
            data = load_and_validate_json(args.input, schema)
            print("JSON is valid")
        elif args.format == 'yaml':
            data = load_and_validate_yaml(args.input, schema)
            print("YAML is valid")
        save_to_json(data, args.output)
        print(f"Data saved to {args.output}")
    except (jsonschema.exceptions.ValidationError, yaml.YAMLError) as e:
        print(f"Invalid file: {e}")

if __name__ == "__main__":
    main()
