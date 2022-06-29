from Example.Stock.stock import Stock


class Order:
    def __init__(self, flowers_ordered):
        self.flowers_ordered = flowers_ordered
        pass

    def show_cost_of_the_order(self):
        pass

    def place_order(self):
        if Stock().check_stock(self.flowers_ordered) == 1:
            Stock().update_stock(self.flowers_ordered)
            print('Thank you for coming.')
        elif Stock().check_stock(self.flowers_ordered) == -1:
            print("Sorry, we don't have that much stock!!")
        else:
            print("Invalid input request!!")
