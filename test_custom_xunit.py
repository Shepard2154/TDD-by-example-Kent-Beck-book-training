from custom_xunit import TestCase, WasRun


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("testMethod")
        assert test.wasRun is None
        test.run()
        assert test.wasRun == 1

TestCaseTest("test_running").run()
