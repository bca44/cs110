from byu_pytest_utils import max_score, dialog, test_files


@max_score(8)
@dialog(
    test_files / 'out_of_stock.txt',
    'out_of_stock.py'
)
def test_out_of_stock(): ...
