import os


def getRepositoryAndBranch(jsonData, onlyMain: bool = False, branchName: str = ""):  
    if ("repository" not in jsonData): 
        raise Exception("Json is missing repository")
    repository = jsonData["repository"]["name"]
    
    if ("ref" not in jsonData):
        raise Exception("Json is missing in ref(branch)")
    if (onlyMain):
        branch = "main"
    else:
        if (branchName != jsonData["ref"].replace("refs/heads/", "")):
            raise Exception("Not the Correct branch")
        branch = branchName

    return {"repository" : repository, "branch": branch}

def pullCommits(repBranch: dict, baseDir):
    if (not os.path.isdir(baseDir)):
        os.mkdir(baseDir)
    repository = repBranch["repository"]
    branch = repBranch["branch"]
    os.system(f"git -C {baseDir}\\{repository.lower()} pull origin {branch.lower()}")


