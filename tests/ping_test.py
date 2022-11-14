import unittest
import api


class PingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.api = api.Ping()

    def test_ping(self):
        ping = self.api.health_check()

        self.assertEqual(201, ping)


if __name__ == '__main__':
    unittest.main()