from byu_pytest_utils import max_score, dialog, test_files


@max_score(4)
@dialog(test_files / "voting_one.dialog.txt", "voting.py", "Favorite Cereal")
def test_voting_one(): ...

