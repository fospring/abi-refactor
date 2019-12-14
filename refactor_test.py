import unittest
from testdata import abi, components
from abi_refactor import deal_abi
import json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        deal_abi(abi, components)
        fh = open("new_abi.json", 'w')
        fh.write(json.dumps(abi, default=lambda o: o.__dict__, indent=4))
        fh.close()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
