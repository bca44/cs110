from byu_pytest_utils import max_score, test_files, dialog


@max_score(5)
@dialog(
    test_files / 'pokemon.dialog.txt',
    'pokemon.py'
)
def test_pokemon(): ...


@max_score(5)
@dialog(
    test_files / 'pokemon2.dialog.txt',
    'pokemon.py'
)
def test_pokemon2(): ...
