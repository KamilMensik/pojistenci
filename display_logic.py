help_file = open('hint.txt').read()

def show_all(hash: dict) -> None:
    clear_screen()
    for i in hash:
        print(hash[i])

def show_one(hash: dict, key: str) -> None:
    clear_screen()
    print(hash.get(key))

def clear_screen() -> None:
    for i in range(30):
        print('\n')

def show_hint() -> None:
    print(help_file)
