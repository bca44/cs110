from byu_pytest_utils import max_score, dialog, test_files


@max_score(6)
@dialog(
    test_files / 'reverse_wordle.txt', 'reverse_wordle.py'
)
def test_reverse_wordle(): ...
