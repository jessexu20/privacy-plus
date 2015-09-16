import json
import requests
import os
def generateCSV():
    f=open("input.txt",'r')
    wr=open("output.csv",'w')
    API_KEY=os.environ.get("GOOGLE_API_KEY")
    for line in f:
        print line
        userid=line
        # userid="114382286519521947458"
        url = "https://www.googleapis.com/plus/v1/people/"+userid+"?key="+API_KEY
        r = requests.get(url)
        if r.status_code == 200 :
            w=r.json()
            param={}
            if w.has_key('birthday'):
                param.put("birthday",w['birthday'],)
            if w.has_key('about_me'):
                param.put("about_me",w['aboutMe'])
            if w.has_key('relationshipStatus'):
                param.put("relationship",w['relationshipStatus'])
            if w.has_key('organizations'):
                param.put("org",w['organizations'])
            if w.has_key('organizations'):
                param.put("org",w['organizations'])
            if w.has_key('placesLived'):
                param.put("places",w['placesLived'])
            if w.has_key('ageRange'):
                param.put("age_min",w['ageRange']['min'])
                param.put("age_max",w['ageRange']['max'])
            if w.has_key('language'):
                param.put('language',w['language'])
            if w.has_key('emails'):
                param.put('emails',w['emails'])
            if w.has_key('occupations'):
                param.put('occupations',w['occupations'])
            if w.has_key('skills'):
                param.put('skills',w['skills'])    
            param={
                "user_id":w['id'],
                "url":w["url"],
                "display_name":w['displayName'],
                "last_name": w["name"]["familyName"],
                "first_name": w["name"]["givenName"],
                "gender":w['gender'],
                "image_url":w['image']['url'],
                "image_is_default":w['image']['isDefault'],
            }
            print param
            title=""
            content=""
            for i in sorted(param.keys()):
                title=title+i+","
            for i in sorted(param.keys()):
                content=content+str(param[i])+","
            wr.write(title+"\n")
            wr.write(content+"\n")
    else:
        print r
if __name__ == '__main__':
    generateCSV()