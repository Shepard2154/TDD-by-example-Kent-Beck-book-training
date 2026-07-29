from custom_xunit import WasRun


def test_simple():
    test = WasRun("testMethod")
    assert test.wasRun is None
    test.testMethod()
    assert test.wasRun == 1 
