import tomllib
import logging
import src.constants as constants
from src.commit_extractor import CommitExtractor

if __name__ == '__main__':
    # Initialize logger
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize config
    logging.info("Loading config...")
    with open(constants.CONFIG_FILE, "rb") as file:
        config = tomllib.load(file)
    logging.info("Config loaded")
    logging.info(f"Config content: '{config}'")

    app_config = config[constants.CONFIG_APP_KEY]
    commit_extractor = CommitExtractor(app_config[constants.CONFIG_REPO_PATHS_KEY], user_names=app_config[constants.CONFIG_USER_NAMES_KEY])
    commit_extractor.load_commits()

    commit_extractor.save_commits(app_config[constants.CONFIG_OUTPUT_PATH_KEY])
