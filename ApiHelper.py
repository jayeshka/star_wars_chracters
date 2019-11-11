'''
@author: Jayesh Kariya
'''
import requests
import base64
import json
import logging
from requests import HTTPError
logging.basicConfig(filename="test.log",level=logging.DEBUG)

class ApiHelper:
    def __init__(self):
        self.base_url = "https://swapi.co/api/people/"
        self.success_status = 200

    def log_args(logging_function):
        def func(self, page_nr):

            logging.debug("{} is the argument passed.".format(page_nr))
            logging_function(self, page_nr)
        return func

    @log_args
    def star_wars_characters(self, page_nr):
        url = self.base_url + "?page={}".format(page_nr)
        print(url)
        try:
            header = {'Content-Type' : 'application/json'}
            response = requests.get(url, headers=header)
            if response.status_code == self.success_status:
                json_res = json.loads(response.text)

                if json_res['results'] != None:
                    star_wars_list = []
                    for each in json_res['results']:
                        #print(each)
                        star_wars_list.append([each['name'], each['height'], each['gender']])

                    return star_wars_list
                else:
                    return None
            else:
                print(response.status_code)
        except HTTPError as e:
            print("HTTPError : {}".format(e))
        except KeyError as e:
            print("KeyError: {}".format(e))
        except Exception as e:
            print("Exception: {}".format(e))


    def starWarCharacters(self, pageNum, filepath):
        response = self.star_wars_characters(pageNum)
        if response != None:
            for each in response:
                self.append_to_file(filepath, each[0], each[1], each[2])

    def append_to_file(self, filepath, name, height, gender):
        with open(filepath, 'a') as fp:
            fp.write("{},{},{}\n".format(name.encode("utf-8"), height.encode("utf-8"), gender.encode("utf-8")))

if __name__ == "__main__":
    args = len(sys.argv)
    if( args != 3):
        print "Usage example: ApiHelper.py page_number, filepath"
        exit(2)
    else:
        page_number = sys.argv[1]
        filepath = sys.argv[2]
        #filepath = "Star_Wars_Characters.txt"
    apiHelp = ApiHelper()
    with open(filepath, "w+") as fp:
        fp.write("Name,Height,Gender\n")
    apiHelp.starWarCharacters(page_number, filepath)

