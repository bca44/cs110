from byu_pytest_utils import max_score, dialog, test_files

@max_score(2)
@dialog(
    test_files/"count_letters_empty.dialog.txt",
    "count_letters.py",
    "abcde",
    test_files/"count_letters_empty.txt"
)
def test_count_empty(): ...


@max_score(6)
@dialog(
    test_files/"count_letters_text.dialog.txt",
    "count_letters.py",
    "abcde",
    test_files/"count_letters_text.txt"
)
def test_count_one(): ...