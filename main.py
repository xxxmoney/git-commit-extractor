from src.commit_extractor import get_commits

if __name__ == '__main__':
    result = get_commits(r"C:\Users\jakub.hana\Source\Repos\Newton.N2",  user_names=["Jakub Hana, Jakub Hána, Hána Jakub", "jakub.hana"])
    
    print([item.repo for item in result])
