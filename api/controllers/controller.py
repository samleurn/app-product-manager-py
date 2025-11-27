class Controller:
    def __init__(self): ...
    def home_controller(self):
        return {"msg": "Home"}

    def product_controller(self, route, uuid=None):
        if route == "/getall":
            return {"msg": "Products Route"}
        elif route == "/getone":
            return {"msg": "Product Route", "uuid": uuid}
        else:
            return {"msg": 404}

    def brand_controller(): ...
    def category_controller(): ...
