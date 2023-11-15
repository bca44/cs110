from byu_pytest_utils import max_score, dialog, test_files


@max_score(2)
@dialog(
    test_files/"cart1.dialog.txt",
    "shopping_total.py",
    test_files/"cart1_items.csv",
    test_files/"item_prices.csv"
)
def test_cart1_regular(): ...


@max_score(3)
@dialog(
    test_files/"cart1_sale.dialog.txt",
    "shopping_total.py",
    test_files/"cart1_items.csv",
    test_files/"item_sale_prices.csv"
)
def test_cart1_sale(): ...


@max_score(2)
@dialog(
    test_files/"cart2.dialog.txt",
    "shopping_total.py",
    test_files/"cart2_items.csv",
    test_files/"item_prices.csv"
)
def test_cart2_regular(): ...


@max_score(3)
@dialog(
    test_files/"cart2_sale.dialog.txt",
    "shopping_total.py",
    test_files/"cart2_items.csv",
    test_files/"item_sale_prices.csv"
)
def test_cart2_sale(): ...
