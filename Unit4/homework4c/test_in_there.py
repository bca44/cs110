from byu_pytest_utils import max_score, test_files, dialog


@max_score(4)
@dialog(test_files / 'in_there.txt', 'in_there.py', 'ar')
def test_in_there(): ...


@max_score(4)
@dialog(test_files / 'in_there_again.txt', 'in_there.py', 'duck')
def test_in_there_again(): ...

