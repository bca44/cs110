from byu_pytest_utils import max_score, test_files, dialog


@max_score(5)
@dialog(
    test_files / 'date_ideas.dialog.txt',
    'date_ideas.py'
)
def test_date_ideas(): ...


@max_score(5)
@dialog(
    test_files / 'date_ideas2.dialog.txt',
    'date_ideas.py'
)
def test_date_ideas2(): ...