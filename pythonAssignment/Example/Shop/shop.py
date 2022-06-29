from Example.Stock.stock import Stock
from Example.Order.order import Order
from Example.Shop.dataError import DataError


class Shop:

    def __init__(self):
        self.order_request = {}
        self.flowers = list(Stock().data.keys())
        print("We have...")
        Stock().show_stock()
        self.get_order()
        Order(self.order_request).place_order()

    def get_order(self):
        print("Please enter how many flowers you need...")
        for i in self.flowers:
            try:
                n = input(f"{i} : ")
                if not n.isdigit():
                    raise DataError("Input value must be an integer. We can't process your request")
                else:
                    value = int(n)
                    if value > 0:
                        self.order_request[i] = value

            except DataError as e:
                print(e)
                break

