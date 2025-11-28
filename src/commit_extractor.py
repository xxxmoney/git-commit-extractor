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
        logging.info("Initializing commit extractor...")

        logging.debug(f"Initializing commit extractor with repo_paths: '{repo_paths}', branch: '{branch}', user_names: {user_names}")
        self.repo_paths = repo_paths
        self.branch = branch
        self.user_names = user_names

        if user_names is None:
            logging.debug(f"Supplied user names list empty, initializing from current git user...")
            self.user_names = [CommitExtractor._get_current_git_user()]
            logging.debug(f"Initialized user names from current git user")

        logging.info("Initialized commit extractor")

    def load_commits (self) -> None:
        logging.info("Loading commits...")

        self.commits = {}

        for repo_path in self.repo_paths:
            self.commits[repo_path] = self._get_commits(repo_path)

        logging.info(f"Loaded commits for {len(self.commits)} repositories")

    def _get_commits(self, repo_path) -> list[CommitInfo]:
        logging.info(f"Getting commits for '{repo_path}'...")

        repo = Repo(repo_path)

        commits: list[Commit] = []
        for commit in repo.iter_commits(self.branch):
            logging.debug(f"Got commit info for '{commit.hexsha}' by '{commit.author}'")
            if commit.author.name in self.user_names:
                logging.debug(f"Username '{commit.author.name}' found in commit, adding to commits")
                commits.append(commit)

        logging.info(f"Got {len(commits)} commits for '{repo_path}'")
        return [CommitInfo(commit) for commit in commits]

    def serialize_commits(self) -> str:
        return jsonpickle.encode(self.commits, indent=4, unpicklable=False)

    def save_commits(self, file_path: str) -> None:
        logging.info(f"Making sure directory for path '{file_path}' exists...")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Directory for path '{file_path}' now surely exists")

        logging.info(f"Saving commits to '{file_path}'...")
        with open(file_path, 'w') as file:
            logging.debug(f"Serializing commits for file '{file_path}'...")
            serialized = self.serialize_commits()
            logging.debug(f"Serialized commits for file '{file_path}': \n'{serialized}'")

            file.write(serialized)
        logging.info(f"Saved commits to '{file_path}'")

    @staticmethod
    def _get_current_git_user():
        logging.info("Getting current git user...")
        result = delegator.run("git config user.name")
        logging.debug(f"Got current git user name: '{result}'")

        return result.out


