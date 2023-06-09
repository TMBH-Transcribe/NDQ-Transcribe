import json
from lunr import lunr
from tqdm import tqdm
import os

def main():
  documents = []
  files = []
  for filename in tqdm(os.listdir("Data")):

    files.append(os.path.splitext(filename)[0])
    doc = {}
    with open(f"Data/{filename}", "r") as f:
      data = json.loads(f.read())
    doc["id"] = os.path.splitext(filename)[0]
    doc["episode_num"] = os.path.splitext(filename)[0]
    doc["title"] = data["meta_data"]["title"]
    doc["description"] = data["meta_data"]["description"]
    doc["body"] = data["transcription_data"]["text"]
    documents.append(doc)
  idx = lunr(ref="id", fields=("episode_num", "title", "description", "body"), documents=documents )
  files.sort()
  return idx, files
    

if __name__ == "__main__":
  idx, files = main()
  with open("index.json", "w") as f:
    json.dump(idx.serialize(), f)
  with open("files.json", "w") as f:
    json.dump({"files":files}, f)
  


