import unittest
from jsonschema import validate

import api
import json_helper
"""
API Documentation: https://restful-booker.herokuapp.com/apidoc/index.html
Backend repo: https://github.com/mwinteringham/restful-booker
"""


class APITests(unittest.TestCase):
    """

    """

    def setUp(self):
        self.api = api.EndPoints()
        self.json = json_helper.Helper()

    @unittest.skip("work is done here")
    def test_get_booking(self):
        """
        Tests a specific booking based upon the booking id provided
        HTTP: GET
        """
        json_data = self.api.get_booking(1)  # todo hardcoded BookID, may want to parameterized
        # todo move schemas to proper location - only tests should go in this module
        schema = self.json.load_json('get_booking.json')
        # print(type(validate(json_data, schema)))
        #  if request matches schema, none type will be returned

        self.assertEqual(None, validate(json_data, schema))

    @unittest.skip('skipping')
    def test_get_booking_ids(self):
        """
        Tests the ids of all the bookings that
        exist within the API. Can take optional
        query strings to search and return a subset of booking ids.
        HTTP: GET
        """
        json_data = self.api.get_booking_ids()
        # todo need to understand how to make schema robust - this api call will return all bookingids - resulting in unpredictable tests

        schema = self.json.load_json('get_booking_ids.json')
        self.assertEqual(None, validate(json_data, schema))

    @unittest.skip('Skipping for later')
    def test_create_booking(self):
        """
        Tests creating a new booking in the API
        HTTP: POST
        """
        json_data = self.api.create_booking()
        # todo: validation isn't working. data type is ignored
        # todo: remove json from this module4
        schema = self.json.load_json('create_booking.json')

        self.assertEqual(None, validate(json_data, schema))

    @unittest.skip("Not Completed")
    def test_update_booking(self):
        """
        Tests updating a current booking
        HTTP: PUT
        """
        pass

    @unittest.skip("Not Completed")
    def test_partial_update_booking(self):
        """
        Tests updating a current
        booking with a partial payload
        HTTP: PATCH
        """
        pass

    @unittest.skip("Not Completed")
    def test_delete_booking(self):
        """
        Tests the ids of all the bookings
        that exist within the API.
        Can take optional query
        strings to search and return a subset of booking ids.
        HTTP: DELETE
        """
        pass

    # todo add test cases for negative testing


if __name__ == '__main__':
    unittest.main()
# to execute tests python3 -m unittest  tests.py

# tests


# a = APITests()
# a.test_get_booking()
