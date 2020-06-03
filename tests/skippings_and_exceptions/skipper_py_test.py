from pytest import mark

@mark.skip(reason="deployment gets broken because of this that is why skip")
def test_skip_case():
    assert True
