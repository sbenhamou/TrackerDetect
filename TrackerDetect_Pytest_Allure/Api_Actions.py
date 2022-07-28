# coding=utf-8
import requests
import json

url = 'https://l761dniu80.execute-api.us-east-2.amazonaws.com/default/exercise_api'
payload = {'main_key': '', 'value': ''}

def get_method():
    with requests.Session() as client:
        response = client.get(url, allow_redirects=False,verify = False)

def get_method_getInfos():
    with requests.Session() as client:
        response = client.get(url, allow_redirects=False,verify = False) 
        return {'status': response.status_code, 'reason': response.reason, 'content': response.content}        

def post_method(main_key, value):
    with requests.Session() as client:
        payload['main_key'] = main_key
        payload['value'] = value
        headers = {'content-type': 'application/json'}
        response = client.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)              

def post_method_getInfos(main_key, value):
    with requests.Session() as client:
        payload['main_key'] = main_key
        payload['value'] = value
        headers = {'content-type': 'application/json'}
        response = client.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False) 
        return {'status': response.status_code, 'reason': response.reason, 'content': response.content}

def put_method(main_key, value):
    with requests.Session() as client:
        payload['main_key'] = main_key
        payload['value'] = value
        headers = {'content-type': 'application/json'}
        response = client.put(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)        

def put_method_getInfos(main_key, value):
    with requests.Session() as client:
        payload['main_key'] = main_key
        payload['value'] = value
        headers = {'content-type': 'application/json'}
        response = client.put(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)
        return {'status': response.status_code, 'reason': response.reason, 'content': response.content}

def delete_method(main_key):
    with requests.Session() as client:
        headers = {'content-type': 'application/json'}
        payload['main_key'] = main_key
        response = client.delete(url, headers=headers, data=json.dumps(payload),allow_redirects=False,verify = False)     

def delete_method_getInfos(main_key):
    with requests.Session() as client:
        headers = {'content-type': 'application/json'}
        payload['main_key'] = main_key
        response = client.delete(url, headers=headers, data=json.dumps(payload),allow_redirects=False,verify = False)
        return {'status': response.status_code, 'reason': response.reason, 'content': response.content}

'''Business Flow: put method missing one parameter'''
def put_method_without_parameter(parameter1, vparameter1):
    payload={}
    with requests.Session() as client:
        payload[parameter1] = vparameter1
        headers = {'content-type': 'application/json'}
        response = client.put(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)

'''Business Flow: put method missing one parameter: get status_code, reason and content'''
def put_method_getInfos_without_parameter(parameter1, vparameter1):
    payload={}
    with requests.Session() as client:
        payload[parameter1] = vparameter1
        headers = {'content-type': 'application/json'}
        response = client.put(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)
        return {'status': response.status_code, 'reason': response.reason, 'content': response.content}

'''Business Flow: post method missing one parameter'''
def post_method_without_parameter(parameter1, vparameter1):
    payload={}
    with requests.Session() as client:
        payload[parameter1] = vparameter1
        headers = {'content-type': 'application/json'}
        response = client.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)

'''Business Flow: post method missing one parameter: get status_code, reason and content'''
def post_method_getInfos_without_parameter(parameter1, vparameter1):
    payload={}
    print(payload)
    with requests.Session() as client:
        payload[parameter1] = vparameter1
        print(payload)
        headers = {'content-type': 'application/json'}
        response = client.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False,verify = False)
        return {'status': response.status_code, 'reason': response.reason, 'content': response.content}        

'''Business Flow: put method ten times'''
def put_method_several_times(num):
    for i in range (num):
        put_method(str(i), str(i)) 

'''Business Flow: delete method ten times'''
def delete_method_several_times(num):
    for i in range (num):
        delete_method(str(i))