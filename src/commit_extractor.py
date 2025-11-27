from git import Repo, Commit
import delegator

def get_commits(repo_path, branch = "master", user_names=None):
    if user_names is None:
        user_names = [_get_current_git_user()]
        
    repo = Repo(repo_path)
 
    commits: list[Commit] = []
    for commit in repo.iter_commits(branch):
        if commit.author.name in user_names:
            commits.append(commit)
        
    return commits

def _get_current_git_user(): 
    result = delegator.run("git config user.name")
    
    return result.out
