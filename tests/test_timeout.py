import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from webhook import worker


class TestTimeout(unittest.TestCase):
    def test_attempt_timeout_is_five_seconds(self):
        self.assertEqual(worker.ATTEMPT_TIMEOUT_SECONDS, 5.0)


if __name__ == "__main__":
    unittest.main()
