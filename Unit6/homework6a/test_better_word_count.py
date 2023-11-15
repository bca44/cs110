from byu_pytest_utils import max_score, test_files, dialog


@max_score(10)
@dialog(
    test_files / "word_count.dialog.txt",
    "better_word_count.py",
    test_files / "1Nephi.txt"
)
def test_better_word_count(): ...

