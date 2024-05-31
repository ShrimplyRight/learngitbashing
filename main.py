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