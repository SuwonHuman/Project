def login(name):
    with open(f"./Human_project.txt", mode="a", encoding="utf-8") as f:
    # with open(f"C:/project/{name}.txt", mode="wt", encoding="utf-8") as f:
        f.write(f"{name}님 반갑습니다.\n")
