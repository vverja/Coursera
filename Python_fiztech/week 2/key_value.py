from os import path
import tempfile
import argparse
import json


def make_work():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--value")
    args = parser.parse_args()

    temp_file = path.join(tempfile.gettempdir(), 'storage.data')
    obj = {}
    if path.isfile(temp_file):
        with open(temp_file, 'r') as f:
            file = f.read()
            if file:
                obj = json.loads(file)
    with open(temp_file, 'w') as f:
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


if __name__ == "__main__":
    make_work()
