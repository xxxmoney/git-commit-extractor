from pathlib import Path
import jsonpickle
from git import Repo, Commit
import delegator
import logging
from src.commit_info import CommitInfo

class CommitExtractor:
    repo_paths: list[str]
    branch: str
    user_names: list[str]
    commits: dict[str, list[CommitInfo]]

    def __init__(self, repo_paths: list[str], branch ="master", user_names=None):
        self.repo_paths = repo_paths
        self.branch = branch
        self.user_names = user_names

        if user_names is None:
            self.user_names = [CommitExtractor._get_current_git_user()]

    def load_commits (self) -> None:
        self.commits = {}

        for repo_path in self.repo_paths:
            self.commits[repo_path] = self._get_commits(repo_path)

    def _get_commits(self, repo_path) -> list[CommitInfo]:
        repo = Repo(repo_path)

        commits: list[Commit] = []
        for commit in repo.iter_commits(self.branch):
            if commit.author.name in self.user_names:
                commits.append(commit)

        return [CommitInfo(commit) for commit in commits]

    def serialize_commits(self) -> str:
        return jsonpickle.encode(self.commits, indent=4, unpicklable=False)

    def save_commits(self, file_path: str) -> None:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(self.serialize_commits())

    @staticmethod
    def _get_current_git_user():
        result = delegator.run("git config user.name")

        return result.out


