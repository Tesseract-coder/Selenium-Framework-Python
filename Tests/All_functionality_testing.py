import unittest


class MyTestCase(unittest.TestCase):
    browser_1 = 'chrome'

    def setUp(self):
        print("This is setup method")

    @unittest.skipIf(browser_1 == 'chrome', "Skipping because condition did not satisfied")
    def test_something(self):
        print("First Test")
        assert 'Kunal' in 'Kunal Ramkrishna'

    def test_somethingaginm(self):
        print("Second test")
        assert 'Kunalss' in 'Kunal Ramkrishna'

    def tearDown(self):
        print("This is Teardown Method")


if __name__ == '__main__':
    unittest.main()
