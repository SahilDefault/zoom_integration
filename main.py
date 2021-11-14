import jwt
import requests
import json
from time import time

API_KEY = 'KUF61uZxR1-yUzKDp49tQQ'
API_SEC = '8zTRhEmKS0NuIrs6natyhkLcXSvcOLkkVIYT'


def generateToken():
    token = jwt.encode(

        {'iss': API_KEY, 'exp': time() + 5000},
        API_SEC,

        algorithm='HS256'
    )
    return token


meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "2021-11-16T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }


def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")

    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]

    print(
        f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n')


createMeeting()
