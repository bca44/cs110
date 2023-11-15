from byu_pytest_utils import max_score, dialog, test_files


@max_score(2)
@dialog(test_files / "sum_nums_small.txt", "sum_nums.py", test_files / "sum_nums_small.input.txt")
def test_sum_nums_small(): ...
