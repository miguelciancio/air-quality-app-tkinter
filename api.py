import requests
import json


class MyApi:
    def __init__(self):
        self.api_request = None
        self.api = None
        self.get_local_authorities_list = []
        self.site_names = []

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
        key_to_check = "Site"

        for value in self.api:
            for local_authority_name in self.api[value]["LocalAuthority"]:
                if key_to_check in local_authority_name.keys():
                    self.get_local_authorities_list.append(
                        local_authority_name["@LocalAuthorityName"]
                    )
                else:
                    pass

        return self.get_local_authorities_list

    def get_air_quality_data(self, local_authority_name):
        self.site_names = []
        key_to_check = "Site"
        for index, value in enumerate(self.api):
            for x in self.api[value]["LocalAuthority"]:
                if key_to_check in x.keys():
                    # print(x)
                    if local_authority_name == x['@LocalAuthorityName']:
                        # print(x)
                        if isinstance(x["Site"], dict):
                            # print(x)
                            self.site_names.append((x["Site"]["@SiteName"], x["Site"]["Species"]))
                        else:
                            i = 0
                            while i < len(x["Site"]):
                                self.site_names.append((x["Site"][i]["@SiteName"], x["Site"][i]["Species"]))
                                # print(x["Site"][i])
                                i += 1

        return self.site_names
