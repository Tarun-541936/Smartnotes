import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def run_clustering():
    with open("notes_db.json", "r") as f:
        notes_data = json.load(f)

    texts = [note["content"] for note in notes_data]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(X)

    for i, note in enumerate(notes_data):
        note["cluster"] = int(kmeans.labels_[i])

    # save back
    with open("notes_db.json", "w") as f:
        json.dump(notes_data, f, indent=2)

    return notes_data