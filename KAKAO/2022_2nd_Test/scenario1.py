import urllib.request
import urllib.parse
import json

x_auth_token="47780eac56cde9f856dbfa569f1aaa70"
base_url = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

#start api 출처https://gist.github.com/Nesffer/e658fe491fd01842e760
url=base_url+"/start"
values = {'problem': 1}
headers = {'X-Auth-Token': x_auth_token}
data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
response_message = response.read().decode('utf8')
auth_key = json.loads(response_message).get('auth_key')

def waitingline_api():
    url=base_url+"/waiting_line"
    hdr = {'Authorization': auth_key}  
    req = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(req)
    response_message = response.read().decode('utf8')
    wating_line = json.loads(response_message).get('waiting_line')
    return wating_line

def gameresult_api():
    url=base_url+"/game_result"
    headers = {'Authorization': auth_key}   
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    response_message = response.read().decode('utf8')
    game_result = json.loads(response_message).get('game_result')
    return game_result

def userinfo_api():
    url=base_url+"/user_info"
    headers = {'Authorization': auth_key}   
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    response_message = response.read().decode('utf8')
    user_info = json.loads(response_message).get('user_info')
    return user_info
#출처:https://dev.to/ultrainstinct05/using-the-python-urllib-module-for-making-web-requests-5hkm
def match_api(pairs):
    url = base_url + "/match"
    headers = {'Authorization': auth_key,'Content-Type': 'application/json'}  
    values = {"pairs":pairs}
    data = json.dumps(values)
    req = urllib.request.Request(url,data = bytes(data.encode("utf-8")),headers=headers,method='PUT')
    res = urllib.request.urlopen(req)
    response_message = res.read().decode('utf8')
    status = json.loads(response_message).get('status')
    time = json.loads(response_message).get('time')
    return status,time

def changegrade_api(commands):
    url=base_url + "/change_grade"
    headers = {'Authorization': auth_key,'Content-Type': 'application/json'}  
    values = {'commands':commands}
    data = json.dumps(values)
    req = urllib.request.Request(url,data = bytes(data.encode("utf-8")),headers=headers,method='PUT')
    res = urllib.request.urlopen(req)
    response_message = res.read().decode('utf8')
    status = json.loads(response_message).get('status')
    return status

def score_api():
    url=base_url+"/score"
    headers = {'Authorization': auth_key}   
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    response_message = response.read().decode('utf8')
    return response_message

time=0
status='ready'
user_dic={}

def make_pairs(waiting_line):
    pairs=[]
    r=list(range(9000,-1000,-1000))#기준
    grades=[[] for _ in range(len(r))]
    if len(waiting_line)>=2:
        waiting_ids=[0 for _ in range(len(waiting_line))]
        for i in range(len(waiting_ids)):
            waiting_ids[i]=waiting_line[i]['id']
        for i in waiting_ids:
            grade=user_dic[i]
            for j in range(len(r)):
                if grade>=r[j]:
                    grades[j].append(i)
                    break
            for k in range(len(grades)):
                if len(grades[k])==2:
                    pairs.append([grades[k][0],grades[k][1]])
                    del grades[k][0]
                    del grades[k][0]
    return pairs

while time<596:
    print(time)
    user_info=userinfo_api()
    for i in user_info:
        user_dic[i['id']]=i['grade']
    waiting_line=waitingline_api()
    pairs=make_pairs(waiting_line)
    if time<595:
        status,time=match_api(pairs)
    else:
        time+=1
    game_result=gameresult_api()
    commands=[]
    for i in game_result:
        win_score=user_dic[i['win']]+int(3000/i['taken'])
        lose_score=user_dic[i['win']]-int(3000/i['taken'])
        if lose_score<0:
            lose_score=0
        commands.append({'id':i['win'],'grade':win_score})
        commands.append({'id':i['lose'],'grade':lose_score})
    changegrade_api(commands)

status,time=match_api(pairs)
print(status,time)
print(score_api())




