# OOCA Assignment

This project is for OOCA assignment. Using `python` to implement a calculator class.

## Requirements

In project directory run:

```
pip install -r requirements.txt
```

## Calculator class

The calculator class is implemented in `calculator.py`. 

To calculate the order price, use the `calculate` method. The method require 2 parameters `order` and `is_member` For example:

```
from calculator import Calculator

calculator = Calculator()

order_price = calculator.order({"red": 1}, False)
```

for `order` parameter, it is a dictionary with key as the item name and value as the quantity. For example, `{"red": 1}` means 1 red item.


## Unit test

To run the unit test, run:

```
pytest
```

you can find unit test sample in `test_calculator.py`

which has 4 tests 
- `test_order_no_member`

    The base case that the user is not a member and don't get any discount

- `test_order_member`

    if the user is a member and get 10% discount

- `test_order_double_no_member`

    if the user is not a member and order `orange` , `pink` or `green` more than 2 sets, the user will get 5% discount for the whole bill

- `test_order_double_member`

    if the user is a member and order `orange` , `pink` or `green` more than 2 sets, the user will get 10% for member and the other 5% discount for the whole bill