from byu_pytest_utils import max_score, dialog, test_files


@max_score(3)
@dialog(test_files / "compare_strings_one.txt", "compare_strings.py")
def test_compare_strings_one(): ...


@max_score(2)
@dialog(test_files / "compare_strings_two.txt", "compare_strings.py")
def test_compare_strings_two(): ...
