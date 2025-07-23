import json
import os

def remove_price_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and 'price' in item:
                    del item['price']
        # Add other potential structures if needed, e.g. if data is a dict containing a list of products
        # elif isinstance(data, dict) and 'products' in data and isinstance(data['products'], list):
        #     for item in data['products']:
        #         if isinstance(item, dict) and 'price' in item:
        #             del item['price']

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2) # Using indent=2 to match common JSON formatting
        
        print(f"Successfully removed 'price' field from {filepath}")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Assuming the script is run from the project root, and the JSON file is at public/data/iphone_refined.json
    json_file_path = os.path.join('public', 'data', 'iphone_refined.json')
    remove_price_from_json(json_file_path)
