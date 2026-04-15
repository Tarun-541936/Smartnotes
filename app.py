from flask import Flask, jsonify, request, render_template
import json
from notes_manager import NotesManager

app = Flask(__name__)

with open("config.json", "r") as f:
    config = json.load(f)

manager = NotesManager(
    config["data_file"],
    config["notes_dir"]
)

@app.route("/")
def home():
    return render_template("index.html", notes=manager.get_all_notes())


@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify(manager.get_all_notes())


@app.route("/api/notes", methods=["POST"])
def create_note():
    data = request.json

    return jsonify(manager.add_note(
        data["title"],
        data.get("content", ""),
        data.get("tags", [])
    )), 201


@app.route("/api/search")
def search():
    tag = request.args.get("tag")
    return jsonify(manager.search_by_tag(tag))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.get("port", 5000), debug=True)