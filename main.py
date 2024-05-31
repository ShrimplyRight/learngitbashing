import json
import yaml
import xml.etree.ElementTree as ET
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

def save_to_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, indent=4)

def load_and_validate_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8').decode('utf8')

def save_to_xml(data, file_path):
    root = ET.Element("root")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(file_path)

def main():
    parser = argparse.ArgumentParser(description='My Program Description')
    parser.add_argument('--input', type=str, help='Input file (JSON, YAML, or XML)')
    parser.add_argument('--output', type=str, help='Output file (JSON, YAML, or XML)')
    parser.add_argument('--format', type=str, choices=['json', 'yaml', 'xml'], help='Input file format')
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
            save_to_json(data, args.output)
        elif args.format == 'yaml':
            data = load_and_validate_yaml(args.input, schema)
            print("YAML is valid")
            save_to_yaml(data, args.output)
        elif args.format == 'xml':
            data = load_and_validate_xml(args.input)
            print("XML is valid")
            save_to_xml(data, args.output)
        print(f"Data saved to {args.output}")
    except (jsonschema.exceptions.ValidationError, yaml.YAMLError, ET.ParseError) as e:
        print(f"Invalid file: {e}")

if __name__ == "__main__":
    main()
