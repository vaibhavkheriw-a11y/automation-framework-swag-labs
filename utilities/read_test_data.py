import json
import os

class ReadTestData:
    test_data_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "test_data",
        "login_data.json"
    )

    @staticmethod
    def get_login_data():
        with open(ReadTestData.test_data_path, "r") as file:
            return json.load(file)
