from dataclasses import dataclass
from git import Commit

class CommitInfo:
    author_name: str
    date: int
    message: str
    files: list[str]

    def __init__(self, commit: Commit):
        self.author_name = commit.author.name
        self.date = commit.committed_date
        self.message = commit.message
        self.files = list(commit.stats.files.keys())
