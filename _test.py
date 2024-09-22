import data.file_database as db
import data.database_interface as dbi
import uuid, json

d = db.FileDataBase("feedback")
i = str(uuid.uuid4())
print(f"./data/feedback/{i}.json")
data = {
    "1":1,
    "2":2
}
dbi.addFeedbackById(i, data)

print(json.dumps(dbi.getFeedbackById(i)))