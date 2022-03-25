import subprocess
from flask import Flask, request, Response
import json
from function.LocalRepository import getRepositoryAndBranch, pullCommits

from function.checkSender import checkSenders
from function.log import GenerateLog

app_settings = ""
with open("settings.json", "r") as f:
    app_settings = json.loads(f.read());

app = Flask(__name__)


@app.route("/newCommit", methods=["POST"])
def newCommit():
    try:
        checkSenders(request, app_settings["GitLabToken"]);
        repBranch = getRepositoryAndBranch(request.json)
        pullCommits(repBranch, app_settings["rootDirectory"])
        subprocess.Popen([app_settings["scriptAfterCommit"], f'{app_settings["rootDirectory"]}{repBranch["repository"]}'], shell=False)
        return Response(status=200)
    except Exception as ex:
        GenerateLog(ex, "newCommit endpoint")
        print(ex)
        return Response(status=401)


@app.route("/test", methods=["GET"])
def testGet():
    return "hello World"




@app.before_request
def logStartRequest():
    GenerateLog("Starting request", request.endpoint)


@app.after_request
def logEndRequest(response):
    GenerateLog(f"Ended request with status: {response.status_code}", request.endpoint)
    return response


app.run(host="0.0.0.0", port=7050, debug=True)