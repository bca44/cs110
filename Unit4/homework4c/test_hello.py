from byu_pytest_utils import max_score, test_files, dialog


@max_score(1)
@dialog(test_files / 'hello.txt', 'hello.py', 'Cosmo')
def test_hello(): ...


@max_score(1)
@dialog(test_files / 'hello_again.txt', 'hello.py', 'world')
def test_hello_again(): ...
