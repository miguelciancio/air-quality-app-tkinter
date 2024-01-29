import requests
import json


class MyApi:
    def __init__(self):
        self.api_request = None
        self.api = None
        self.get_local_authorities_list = []

    def load_api(self):
        try:
            self.api_request = requests.get(
                "http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json"
            )
            self.api = json.loads(self.api_request.content)
        except Exception as e:
            self.api = f"Error - {e}"
            print(self.api)

    def get_local_authorities(self):
        for index, value in enumerate(self.api):
            for x in self.api[value]["LocalAuthority"]:
                self.get_local_authorities_list.append(
                    self.api[value]["LocalAuthority"][index].get("@LocalAuthorityName")
                )
                index += 1
            # print(self.api["HourlyAirQualityIndex"]["LocalAuthority"][1].get("@LocalAuthorityName"))

        return self.get_local_authorities_list
