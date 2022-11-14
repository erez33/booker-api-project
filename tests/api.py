import requests as re
import json
# from schemas import json_helper as jh
"""

"""


class Auth:
    def create_auth(self, payload, header):
        """
        Creates a new auth token to use
        for access to the PUT and DELETE /booking
        :return: token string in dictionary type
        """
        try:
            # payload = {"username": "admin",
            #            "password": "password123"}
            # header = {"Content-Type": "application/json"}
            r = re.post('https://restful-booker.herokuapp.com/auth', json=payload, headers=header)
            return json.loads(r.text)
        except ValueError:
            print("Failed decoding json in create_auth")


class Ping:
    def health_check(self):
        """
        A simple health check
        endpoint to confirm whether
        the API is up and running.
        :return: status code for server
        """
        try:
            r = re.get('https://restful-booker.herokuapp.com/ping')
            return r.status_code
        except ValueError:
            print('Failed decoding json in healthcheck')


class EndPoints:

    def get_booking(self, booking_id):
        """

        :param booking_id:
        :return:
        """
        try:
            r = re.get('https://restful-booker.herokuapp.com/booking/' + str(booking_id)).json()
            return r
        except ValueError:
            print('Decoding json has failed in get_booking')  # booking id 2 was throwing json decoding error

    def get_booking_ids(self):
        """

        :return:
        """
        try:
            r = re.get('https://restful-booker.herokuapp.com/booking').json()
            return r
        except ValueError:
            print('Decoding json has failed in get_booking_ids')

    def create_booking(self):
        """

        :return:
        """
        try:
            payload = {
                "firstname": "Gal",
                "lastname": "Gadot",
                "totalprice": 2010,
                "depositpaid": "false",
                "bookingdates": {
                    "checkin": "2021-01-01",
                    "checkout": "2021-02-01"
                },
                "additionalneeds": "Dinner"
            }
            headers = {"content-Type": "application/json"}
            r = re.post('https://restful-booker.herokuapp.com/booking', json=payload, headers=headers)

            return r.text
        except ValueError:
            print('error decoding json in create_booking')

    def update_booking(self):
        """

        :return:
        """
        try:
            json = {
                "firstname": "Jean Claude",
                "lastname": "Van Dam",
                "totalprice": 4510,
                "depositpaid": "False",
                "bookingdates": {
                    "checkin": "2021-01-01",
                    "checkout": "2021-01-01"
                },
                "additionalneeds": "Karate"
            }
            header = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": "token=abc123"
            }
            # todo: id will be hardcode here, remove later
            r = re.put("https://restful-booker.herokuapp.com/booking/1", json=json, headers=header)
            return r.text, r.status_code, r.reason, r.content
        except ValueError:
            print('Json decoding failed in update_booking')

    def partial_update_booking(self):
        """

        :return:
        """
        header = {

        }
        try:
            r = re.patch('https://restful-booker.herokuapp.com/booking/:id')

        except ValueError:
            pass

    def delete_booking(self):
        """

        :return:
        """
        header = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": "token=731d2fe6c4e533d"
        }
        try:
            r = re.delete('https://restful-booker.herokuapp.com/booking/3', headers=header)
            return r
        except ValueError:
            print('Json decoding failed in delete_booking')


# testing this class