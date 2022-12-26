import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

GITHUB_ACCESSS_TOKEN = os.getenv('GITHUB_ACCESSS_TOKEN')
print(GITHUB_ACCESSS_TOKEN)


def Github_Load_Repositories():
    print(GITHUB_ACCESSS_TOKEN)
    gh = Github(GITHUB_ACCESSS_TOKEN)

    # Then play with your Github objects:
    repos = []
    for repo in gh.get_user().get_repos():
        print(repo.name)
        repos.append(repo.name)
    return repos


def Get_All_Hook(OWNER, REPO_NAME):
    gh = Github(GITHUB_ACCESSS_TOKEN)
    repo = gh.get_repo(
        "{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
    for hook in repo.get_hooks():
        print("response", hook.config)
    return (repo.get_hooks.__name__)


def Delete_Hook(OWNER, REPO_NAME, HOOK_ID):
    gh = Github(GITHUB_ACCESSS_TOKEN)
    repo = gh.get_repo(
        "{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
    repo.get_hook(HOOK_ID).delete()
    return


def Github_Hook_Repository(OWNER, REPO_NAME, HOST, ENDPOINT):
    gh = Github(GITHUB_ACCESSS_TOKEN)
    config = {
        "url": "https://{host}/{endpoint}".format(host=HOST, endpoint=ENDPOINT),
        "content_type": "json",
        "insecure_ssl": 0
    }
    EVENTS = ["push", "pull_request"]
    repo = gh.get_repo(
        "{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
    res = repo.create_hook("web", config, EVENTS, active=True)
    response={
        "hook repo url": res.url
    }
    return response
