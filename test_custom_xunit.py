from custom_xunit import WasRun


def test_simple():
    test = WasRun("testMethod")
    assert test.wasRun is None
    test.run()
    assert test.wasRun == 1
