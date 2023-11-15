from byu_pytest_utils import max_score, test_files, dialog


@max_score(4)
@dialog(test_files / 'big_words.txt', 'big_words.py', 3)
def test_big_words(): ...


@max_score(4)
@dialog(test_files / 'more_big_words.txt', 'big_words.py', 4)
def test_more_big_words(): ...
