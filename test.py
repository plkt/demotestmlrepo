from jupextdemo.utils import *
from jupextdemo.azaks_deploy import *
from jupextdemo.gitHubManager import GithubManager
from jupextdemo.const import *


def _test_accounts():
    pass


replyObject = {}
if __name__ == "__main__":
    # STEP 1 : take the AKS and ACR details
    # STEP 2 : Configure the Workflow files if they don't exist
    # STEP 3:  Check-In the Workflow files to Github Repo
    # if aks_dep.IsUserLoggedIn():
    #     replyObject["DefaultSubscription"] = aks_dep.getDefaultSubscription()
    # else:
    #     aks_dep.loginUserFlow()
    #     replyObject["DefaultSubscription"] = aks_dep.getDefaultSubscription()

    # # get ACR details
    # replyObject["ACRAccount"] = aks_dep.getACRDetails()

    # # get AKS details
    # replyObject["AKSCluster"] = aks_dep.getAKSDetails()

    # now use this object and pass it to Github manager to implement

    gm = GithubManager("abfcf1bf051a01c1ddec427de9bb047182ed02ab")
    repo = gm.getRepo()

    # gm.pushFiles(repo)
    gm.pushDeployFilestoRepo(
        {"name": "aaaaaaa", "resourceGroup": "shpraka"}, {"name": "aaaaaademo"})
    # add Az credentials to github

    # akscluster = replyObject["AKSCluster"][0] if len(
    #     replyObject["AKSCluster"]) > 0 else None
    # acrAccount = replyObject["ACRAccount"][0] if len(
    #     replyObject["ACRAccount"]) > 0 else None
    # gm.pushDeployFilestoRepo(akscluster, acrAccount)

    # # print(files)
    # newFile = "charts/Chart.yml"
    # content = "Hello world".encode()
    # repos.create_file(
    #     path=newFile,
    #     message="Create file for testCreateFile",
    #     content="this is the file content",
    #     branch="master",
    # )
