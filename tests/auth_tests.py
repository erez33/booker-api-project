import unittest
import api

import json_helper
from jsonschema import validate


class auth_test(unittest.TestCase):

    def setUp(self) -> None:
        self.api = api.Auth()
        self.json = json_helper.Helper()

    def test_success_create_auth(self):
        '''

        :return:
        '''
        payload = {"username": "admin",
                   "password": "password123"}
        header = {"Content-Type": "application/json"}

        create_auth = self.api.create_auth(payload, header)
        schema = self.json.load_json('success_create_auth.json')

        self.assertEqual(None, validate(create_auth, schema))

    def test_fail_create_auth(self):
        '''

        :return:
        '''
        payload = {"username": "wrong_username",
                   "password": "wrong_password"}
        header = {"Content-Type": "application/json"}
        failed_create_auth = self.api.create_auth(payload, header)

        schema = self.json.load_json('failed_create_auth.json')

        'The validate function returns none if there '
        self.assertEqual(None, validate(failed_create_auth, schema))


if __name__ == '__main__':
    unittest.main()