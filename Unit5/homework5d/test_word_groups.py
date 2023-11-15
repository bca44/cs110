from byu_pytest_utils import max_score, test_files, dialog


@max_score(6)
@dialog(
    test_files/"words.dialog.txt",
    "word_groups.py", test_files/"words.txt"
)
def test_word_groups(): ...
