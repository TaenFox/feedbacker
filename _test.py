import data.file_database as db
import data.database_interface as dbi
import uuid, json

d = db.FileDataBase("feedback")
i = str(uuid.uuid4())
d.addById(i, {"1":1})

d.modifyById(i, {"1":2})

print(json.dumps(dbi.getFeedbackById(i)))