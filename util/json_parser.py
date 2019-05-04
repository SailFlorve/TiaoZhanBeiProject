import json


class JsonParser:
    json_dict = None

    def __init__(self, s, is_path=True):
        if is_path:
            with open(s, encoding='utf-8') as fp:
                self.json_dict = json.load(fp)
        else:
            self.json_dict = json.loads(s)

    def get(self, key: str):
        return self.json_dict[key]

    def index(self, index: int):
        return self.json_dict[index]
