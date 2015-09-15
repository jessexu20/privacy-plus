import json
import requests
import os
# from oauth2client.client import OAuth2WebServerFlow
def google():
    API_KEY=os.environ.get("GOOGLE_API_KEY")
    print API_KEY
    # flow = OAuth2WebServerFlow(client_id='533853324479-q4u2bm7m3vl7jt31oqmj4vg4fu6qk42h.apps.googleusercontent.com',
    #                            client_secret='9SwUEKqUp1bnS6z8Em5QL0dD',
    #                            scope="https://www.googleapis.com/plus/v1/people/"+"118051310819094153327",
    #                            redirect_uri='http://example.com/auth_return')
    
    url = "https://www.googleapis.com/plus/v1/people/"+"114382286519521947458?key="+API_KEY
    # url="https://graph.facebook.com/search?q=feifei\ wang\ NCSU&type=user&access_token=CAACEdEose0cBAOu8ez4AhvS92jdK2KhmLUEHzf8IG3DGuApmE49Kk5RC3hPplNC5GxpJETx7uouNMHo1dPQGSTsug1wJZB18m2NqmjPdW1jom4YzocQBWj3ojRfB1lrrHDKoADkt0RWzTryypcZCZAU3F4crOa2kLmF5xUFVWFuvVdoaTK6YEg5XMieaFkZCkLjDQW7HBwZDZD"
    # url="https://graph.facebook.com/v2.4/905037456236914?fields=about%2Caddress%2Cage_range%2Cbio%2Cbirthday&access_token=CAACEdEose0cBAOu8ez4AhvS92jdK2KhmLUEHzf8IG3DGuApmE49Kk5RC3hPplNC5GxpJETx7uouNMHo1dPQGSTsug1wJZB18m2NqmjPdW1jom4YzocQBWj3ojRfB1lrrHDKoADkt0RWzTryypcZCZAU3F4crOa2kLmF5xUFVWFuvVdoaTK6YEg5XMieaFkZCkLjDQW7HBwZDZD"
    r = requests.get(url)
    if r.status_code == 200 :
        print r.json()
    else:
        print r
google()