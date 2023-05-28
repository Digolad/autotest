import json


class FileManager:
    @staticmethod
    def get_data_from_json_file(file='configurations/config.json') -> dict:
        """
        readying test_data from json file
        :return: test_data from json file
        """

        with open(file, 'r', encoding='utf-8') as config:
            data = json.load(config)
            return data
