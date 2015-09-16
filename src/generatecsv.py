import json
import requests
import os
def generateCSV():
    f=open("input.txt",'r')
    wr=open("output.csv",'a')
    API_KEY=os.environ.get("GOOGLE_API_KEY")
    param={
        "user_id":' ',
        "url":' ',
        "display_name":' ',
        "last_name": ' ',
        "first_name": ' ',
        "gender":' ',
        "image_url": ' ',
        "image_is_default":' ',
        "birthday":' ',
        "about_me":' ',
        "relationship":' ',
        'org':' ',
        'places':' ',
        'age_min':' ',
        'age_max': ' ',
        'language':' ',
        'emails':' ',
        'occupations':' ',
        'skills':' '
    }
    title=""
    for i in sorted(param.keys()):
        title=title+i+","
    wr.write(title+"\n")
    for line in f:
        userid=line[:-1]
        url = "https://www.googleapis.com/plus/v1/people/"+str(userid)+"?key="+API_KEY
        r = requests.get(url)
        if r.status_code == 200 :
            w=r.json()
            # print w
            if w.has_key('id'):
                param['user_id']=w['id']
            if w.has_key('url'):
                param['url']=w['url']
            if w.has_key('displayName'):
                param['display_name']=w['displayName']
            if w.has_key('name'):
                param["last_name"]=w["name"]["familyName"]
                param["first_name"]=w["name"]["givenName"]
            if w.has_key('gender'):
                param['gender']=w['gender']
            if w.has_key('image'):
                param['image_url']=w['image']['url']
                param["image_is_default"]=w['image']['isDefault']
            if w.has_key('birthday'):
                param["birthday"]=w['birthday']
            if w.has_key('about_me'):
                param["about_me"]=w['aboutMe']
            if w.has_key('relationshipStatus'):
                param["relationship"]=w['relationshipStatus']
            if w.has_key('organizations'):
                param["org"]=w['organizations']
            if w.has_key('placesLived'):
                param["places"]=w['placesLived']
            if w.has_key('ageRange'):
                param["age_min"]=w['ageRange']['min']
                param["age_max"]=w['ageRange']['max']
            if w.has_key('language'):
                param['language']=w['language']
            if w.has_key('emails'):
                param['emails']=w['emails']
            if w.has_key('occupations'):
                param['occupations']=w['occupations']
            if w.has_key('skills'):
                param['skills']=w['skills']
            # print param
            content=""
            for i in sorted(param.keys()):
                content=content+str(param[i])+","
            wr.write(content+"\n")
        else:
            print r
    f.close()
    wr.close()
if __name__ == '__main__':
    generateCSV()