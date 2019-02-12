from os import path
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args(['--key', '1', '--value', 'Second'])

temp_file = path.join(tempfile.gettempdir(), 'storage.json')
obj = {}
with open(temp_file, 'w+') as f:
    some_string = f.read()
    if some_string:
        obj = json.loads(some_string)
        if args.value:
            if args.key in obj:
                item = obj.get(args.key)
                if type(item) is list:
                    item.append(args.value)
                elif item:
                    obj[args.key] = [item, args.value]
            else:
                obj[args.key] = args.value

    elif args.value:
        obj[args.key] = args.value
    json.dump(obj, f)
print(obj)
