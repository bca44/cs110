from byu_pytest_utils import max_score, dialog, test_files


@max_score(4)
@dialog(
    test_files/"house_list.dialog.txt",
    "value_count.py",
    test_files/"house_list.csv",
    1
)
def test_val_count_one(): ...



@max_score(4)
@dialog(
    test_files/"nba_players.dialog.txt",
    "value_count.py",
    test_files/"nba_players.csv",
    4
)
def test_val_count_two(): ...