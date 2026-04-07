import os
import json

NOTES_DIR = "notes"
try:
    with open("config.json") as f:
        config = json.load(f)
        print(f"\nWelcome To {config['app_name']} V {config['version']}")
except FileNotFoundError:
    print("Config File not found")


def list_note():
    files = os.listdir(NOTES_DIR)
    for i, f in enumerate(files, 1):
        with open(os.path.join(NOTES_DIR, f)) as fh:
            content = fh.read().strip()
            print(f"{i}.{f} - {content}")


def add_note():
    title = input("Enter the title of the file: ")
    content = input("Enter the contents: ")
    filename = title.lower().replace(" ", "_") + ".txt"
    path = os.path.join(NOTES_DIR, filename)
    with open(path, "w") as a:
        a.write(content)
    print(f"saved : {filename} successfully!!")


def search_note():
    result = []
    keyword = input("Enter the keyword: ")
    for f in os.listdir(NOTES_DIR):
        with open(os.path.join(NOTES_DIR, f)) as fh:
            text = fh.read()
            if keyword.lower() in text.lower():
                result.append((f, text.strip()))
                print(result)


while True:
    print("\n1.List the contents\n2.Add new notes\n3.Search in notes\n4.Quit")
    choice = int(input("Enter the choice :"))
    if choice == 1:
        list_note()
    elif choice == 2:
        add_note()
    elif choice == 3:
        search_note()
    elif choice == 4:
        break
    else:
        print("invalid choice")
