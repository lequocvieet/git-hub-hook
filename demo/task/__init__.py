from demo import celery
from demo.git_hub import *
from flask import json
from demo.telegram_bot import Send_Message


@celery.task
def get_all_repo():
    res=Github_Load_Repositories()
    return json.dumps(res)

@celery.task
def get_all_hook(OWNER, REPO_NAME):
    res=Get_All_Hook(OWNER,REPO_NAME)
    return json.dumps(res)

@celery.task
def delete_hook(owner,repo_name,hook_id):
    res=Delete_Hook(owner,repo_name,hook_id)
    return json.dumps(res)

@celery.task
def hook(owner,repo_name,host,endpoint):
    res=Github_Hook_Repository(owner,repo_name,host,endpoint)
    print(res)
    return json.dumps(res)

@celery.task
def trigger_event(data):
    res=Send_Message(data)
    return json.dumps(res)