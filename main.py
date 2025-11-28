from pathlib import Path
import logging
import src.constants as constants
from src.commit_extractor import CommitExtractor

if __name__ == '__main__':
    repos = [
        r"C:\Users\xxxmo\source\repos\restaurants-dashboard"
    ]
    user_names = [
        "Jakub Hana, "
        "Jakub Hána, "
        "Hána Jakub",
        "Hana Jakub",
        "jakub.hana"
    ]

    commit_extractor = CommitExtractor(repos, user_names=user_names)
    commit_extractor.load_commits()

    commit_extractor.save_commits(constants.OUTPUT_FILE_PATH)
