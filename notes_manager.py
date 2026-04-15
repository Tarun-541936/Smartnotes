import json
import os
from datetime import datetime


class NotesManager:
    def __init__(self, db_file, notes_folder):
        self.db_file = db_file
        self.notes_folder = notes_folder

    def load_db(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                return json.load(f)
        return []

    def save_db(self, notes):
        with open(self.db_file, "w") as f:
            json.dump(notes, f, indent=2)

    def get_all_notes(self):
        return self.load_db()

    def add_note(self, title, content, tags=None):
        notes = self.load_db()
        if tags is None:
            tags = []

        new_note = {
            "id": len(notes) + 1,
            "title": title,
            "content": content,
            "tags": tags,
            "created": datetime.now().isoformat()
        }

        notes.append(new_note)
        self.save_db(notes)
        return new_note

    def search_by_tag(self, tag):
        notes = self.load_db()
        return [n for n in notes if tag in n.get("tags", [])]