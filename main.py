from pathlib import Path

import jsonpickle

from src.commit_extractor import get_commits
import src.constants as constants

if __name__ == '__main__':
    print("Getting commits ...")
    result = get_commits(r"C:\Users\xxxmo\source\repos\restaurants-dashboard", user_names=["Jakub Hana, Jakub Hána, Hána Jakub", "Hana Jakub", "jakub.hana"])
    print(f"Got commits, count: {len(result)}")
    
    file_path = Path(constants.OUTPUT_FILE_PATH)
    # Create directory if not exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Serializing commit info...")
    serialized = jsonpickle.encode(result, indent=4, unpicklable=False)
    print(f"Serialized commit info")

    print(f"Saving to file: '{file_path}'...")
    with open(file_path, 'w') as file:
        file.write(serialized)
    print(f"Saved to file: '{file_path}'")
