from byu_pytest_utils import with_import, max_score


@max_score(0.5)
@with_import('practice_problems')
def test_for_reals(for_reals):
    observed = for_reals('30%? That\'s crazy!')
    expected = '30 percent? That\'s crazy (for reals).'
    assert observed == expected


@max_score(0.5)
@with_import('practice_problems')
def test_for_reals_again(for_reals):
    observed = for_reals('I saw cow that was 50% bigger than my car!')
    expected = 'I saw cow that was 50 percent bigger than my car (for reals).'
    assert observed == expected


@max_score(0.5)
@with_import('practice_problems')
def test_doubles(doubles):
    observed = doubles('All week I look at roots.')
    expected = 'All weeeeeek I looooook at roooooots.'
    assert observed == expected


@max_score(0.5)
@with_import('practice_problems')
def test_doubles_again(doubles):
    observed = doubles('We seek good food with cheese.')
    expected = 'We seeeeeek gooooood fooooood with cheeeeeese.'
    assert observed == expected


@max_score(1)
@with_import('practice_problems')
def test_upper_vowels(upper_vowels):
    observed = upper_vowels('Do you like to code?')
    expected = 'DO yOU lIkE tO cOdE?'
    assert observed == expected


@max_score(1)
@with_import('practice_problems')
def test_upper_vowels_again(upper_vowels):
    observed = upper_vowels('And it came to pass...')
    expected = 'And It cAmE tO pAss...'
    assert observed == expected


@max_score(1)
@with_import('practice_problems')
def test_only_o(only_o):
    observed = only_o('I like to write code at BYU!')
    expected = 'O loko to wroto codo ot BYO!'
    assert observed == expected


@max_score(1)
@with_import('practice_problems')
def test_only_o_again(only_o):
    observed = only_o('And it came to pass...')
    expected = 'Ond ot como to poss...'
    assert observed == expected
