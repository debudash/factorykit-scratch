import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from webhook.worker import is_permanent_failure


class TestPermanent(unittest.TestCase):
    def test_client_errors_are_permanent(self):
        self.assertTrue(is_permanent_failure(404))
        self.assertTrue(is_permanent_failure(400))

    def test_others_are_not(self):
        for status in (429, 500, 302, 200):
            self.assertFalse(is_permanent_failure(status))


if __name__ == "__main__":
    unittest.main()
