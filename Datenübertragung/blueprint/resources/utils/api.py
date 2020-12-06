import json
from .config import config
from http.client import HTTPConnection, HTTPSConnection
from base64 import b64encode
from enum import Enum

class Endpoints(Enum):
    IT = '/it'
    TERMINAL = '/terminal'
    RADAR = '/radar'
    FLIGHTPLANS = '/flightplans'

class ApiRequest():
    def __init__(self):
        self.host = config['DATA-API']['host']
        self.port = config['DATA-API']['port']
        self.protocol = config['DATA-API']['protocol']
        self.username = config['DATA-API']['username']
        self.password = config['DATA-API']['password']

    def get(self, endpoint):
        """
        Sends a GET request and returns a JSON Object. If the request fails,
        an the statuscode (int) will be returned. 
        """

        # use SSL if self.protocol is https
        if (self.protocol == "https"):
            c = HTTPSConnection(self.host, int(self.port))
        else:
            # DATA-API - use not encrypted connection
            c = HTTPConnection(self.host, int(self.port))
        
        # prepare authorization header
        userAndPass = b64encode(bytes(self.username + ':' + self.password, 'utf-8')).decode("ascii")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass }
        
        # send request
        c.request('GET', endpoint.value, headers=headers)        
        response = c.getresponse()

        if (response.getcode() == 200):
            return json.loads(response.read().decode())
        
        # request returned non-success code, return error-code 
        return response.getcode();


# debug ApiRequest-class
if __name__ == '__main__':
    print('*'*10 + ' Debug: ApiRequest ' + '*'*10 )
    
    api = ApiRequest()
    print('#'*3 + ' IT')
    print(api.get(Endpoints.IT))
    print('#'*3 + ' FLIGHTPLANS')
    print(api.get(Endpoints.FLIGHTPLANS))
    print('#'*3 + ' RADAR')
    print(api.get(Endpoints.RADAR))
    print('#'*3 + ' TERMINAL')
    print(api.get(Endpoints.TERMINAL))
