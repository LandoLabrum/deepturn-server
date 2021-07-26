import json

def write_to_file(file, obj):
    with open(f'json/{file}.json', "w") as outfile:
        json.dump(obj, outfile, indent=4)