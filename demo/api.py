
from flask import Flask, request, json, jsonify
from demo.git_hub import *
from demo.task import *
from celery.result import AsyncResult


app = Flask(__name__)


@app.route('/result/<task_name>/<task_id>', methods=['GET'])
def taskstatus(task_name,task_id):
    if task_name=="get-all-repo":
        result=get_all_repo.AsyncResult(task_id)
    if task_name=="get-all-hook":
        result=get_all_hook.AsyncResult(task_id)
    if task_name=="trigger-event":
        result=trigger_event.AsyncResult(task_id)
    if task_name=="hook-repo":
        result=hook.AsyncResult(task_id)
    return jsonify(result.get())


@app.route('/get-all-repo', methods=['GET'])
def getAllRepo():
    res = get_all_repo.delay()
    response={
        "task_id": res.id,
        "status":res.status
    }
    return jsonify(response)


@app.route('/get-all-hook/<owner>/<repo_name>', methods=['GET'])
def getAllHooks(owner, repo_name):
    res = get_all_hook.delay(owner, repo_name)
    response={
        "task_id": res.id,
        "status":res.status
    }
    return jsonify(response)


@app.route('/delete-hook', methods=['POST'])
def deleteHook():
    # res=Delete_Hook("lequocvieet","booking-chain",393297938)
    data = json.loads(request.data)
    res = delete_hook.delay(data["owner"], data["repo_name"], data["hook_id"])
    response={
        "task_id": res.id,
        "status":res.status
    }
    return jsonify(response)


@app.route('/hook-repo', methods=['POST'])
def hookRepo():
    #Todo: catch exception if hook already exist
    data = json.loads(request.data)
    res = hook.delay(data["owner"], data["repo_name"],
                     data["host"], data["endpoint"])
    response={
        "task_id": res.id,
        "status":res.status
    }
    return jsonify(response)


@app.route('/trigger-event', methods=['POST'])
def triggerEvent():
    if(request.headers["X-GitHub-Event"]=="ping"):
        return jsonify("ping success!")
    data = {
        "time stamp":request.json["head_commit"]["timestamp"],
        "name": request.json["pusher"]["name"],
        "commit": request.json["head_commit"]["message"],
        "added":request.json["head_commit"]["added"],
        "removed":request.json["head_commit"]["removed"],
        "modified":request.json["head_commit"]["modified"],

    }
    res = trigger_event.delay(data)
    response={
        "task_id": res.id,
        "status":res.status
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
