from Example.constants import INPUT_DATA
import json


class Stock:
    def __init__(self):
        self.data = json.load(open(INPUT_DATA, 'r'))

    def check_stock(self, flowers_ordered):
        if len(flowers_ordered.keys()) >= 1:
            for k, v in self.data.items():
                if flowers_ordered[k] > self.data[k]:
                    return -1
            return 1
        return 0

    def show_stock(self):
        print('Flower -> Count')
        for k, v in self.data.items():
            print(f'{k} -> {v}')

    def update_stock(self, flowers_ordered):
        for k, v in self.data.items():
            self.data[k] = v - flowers_ordered[k]
        json.dump(self.data, open(INPUT_DATA, 'w'))
