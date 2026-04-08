import json
import os
from datetime import datetime
 
notes_db = "notes_db.json"
 
 
def load_db():
    if os.path.exists(notes_db):
        with open(notes_db, "r") as f:
            notes =  json.load(f)
            return notes
    return []
 
 
def get_all_notes():
    print(load_db())
 
 
def save_db(notes):
    with open(notes_db, "w") as fh:
        json.dump(notes, fh, indent=2)
    print("Notes saved successfully! ")
 
 
def add_note():
    notes = load_db()
    title = input("Enter title: ")
    content = input("Enter the content: ")
    tag_input = input("Enter tags with comma: ")
    if tag_input:
        tag = tag_input.split(",")
    else:
        tag = []
 
    new_note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "tags": tag,
        "created": datetime.now().isoformat(),
    }
 
    notes.append(new_note)
    save_db(notes)
 
 
def search_by_tag():
    notes = load_db()
    search_tag = input("Enter the tag: ")
    result = []
    for t in notes:
        if search_tag in t["tags"]:
            result.append((t["title"],search_tag))
 
    if result:
        print(result)
    else:
        print("Tag not found")
 
while True:
    print("1.Get all DB \n2.Add DB \n3.Search by Tag \n4.Quit ")
    choice = int(input("Enter choice: "))
    if choice == 1:
        get_all_notes()
    elif choice == 2:
        add_note()
    elif choice == 3:
        search_by_tag()
    elif choice == 4:
        print("Program Exited Successfully !")
        break
    else:
        print("Invalid Key! ")