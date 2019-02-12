from os import path
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args(['--key', '1'])

temp_file = path.join(tempfile.gettempdir(), 'storage.json')
obj = {}
f = open(temp_file, 'r')
obj = json.load(f)
f.close()
with open(temp_file, 'w') as f:
    #some_string = f.read()
    #if some_string:
    #    obj = json.loads(some_string)
    if obj:
        if args.value:
            if args.key in obj:
                item = obj.get(args.key)
                if type(item) is list:
                    item.append(args.value)
                elif item:
                    obj[args.key] = [item, args.value]
            else:
                obj[args.key] = args.value
        else:
            item = obj.get(args.key)
            if type(item) is list:
                print(*item, sep=", ")
            else:
                print(item)
    elif args.value:
        obj[args.key] = args.value
    json.dump(obj, f)

