import json
from os.path import abspath, join


class Helper:

    def load_json(self, file_name):
        """

        :param file_name:
        :return:
        """
        relative_path = join('schemas', file_name)
        with open(abspath(relative_path)) as schema_file:
            return json.loads(schema_file.read())


# j = Helper()
# print(j.load_json('get_booking.json'))
# print(j.load_json('create_booking.json'))