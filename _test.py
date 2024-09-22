import data.file_database as db
import data.database_interface as dbi
import uuid, json

d = db.FileDataBase("feedback")
i = str(uuid.uuid4())
d.addById(i, {"1":1})

d.modifyById(i, {"1":2})

i = "36d1395b-c0a5-4a11-a0d1-eddcf1408862"

print(json.dumps(dbi.getFeedbackById(i)))