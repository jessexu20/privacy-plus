import sys
import time
import json
import requests
import os
from facepp import API
API_KEY = "19e15e1bc1056ef1cf9ad76cff56b4a6"
API_SECRET = "XdoDpYtBr6DFWZPFfdPfZJiZa-TcpoWq"
api = API(API_KEY, API_SECRET)
def is_human(URL):
        ret = api.detection.detect(url = URL)
        if 'face' in ret:
                if len(ret['face']) == 0:
                        return "false"
                else:
                        return "true"
