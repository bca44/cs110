from byu_pytest_utils import max_score, with_import


@max_score(1)
@with_import
def test_random_asterisks_zero(random_asterisks):
    text = " ".join(["a" for _ in range(1000)])
    result = random_asterisks(text, 0)
    assert 0 == result.count("*")


@max_score(1)
@with_import
def test_random_asterisks_one(random_asterisks):
    text = " ".join(["a" for _ in range(1000)])
    result = random_asterisks(text, 1)
    assert 1000 == result.count('*')


@max_score(3)
@with_import
def test_random_asterisks_half_a(random_asterisks):
    text = " ".join(["a" for _ in range(10000)])
    result = random_asterisks(text, 0.5)
    result = result.replace(' ', '')
    assert 0.45 < result.count('*') / 10000 < 0.55
    assert 0.45 < result[:1000].count('*') / 1000 < 0.55
    assert 0.45 < result[-1000:].count('*') / 1000 < 0.55
