class Calculator:
    def __init__(self) -> None:
        self.price_list = {
            "red": 50,
            "green": 40,
            "blue": 30,
            "yellow": 50,
            "pink": 80,
            "purple": 90,
            "orange": 120
        }

    def calculate(self, order: dict, is_member: bool) -> float:
        total = 0
        discount = 0.9 if is_member else 1
        dis_5 = False
        for color, value in order.items():

            total += value * self.price_list[color]

            # check if orange, pink or green to check discount
            if not dis_5 and color in ["orange", "pink", "green"]:
                # check if its more than 2
                if value >= 2:
                    dis_5 = True
                    discount = discount - 0.05

        return total * discount
