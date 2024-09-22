import data.file_database as db
import uuid

d = db.FileDataBase("feedback")
i = str(uuid.uuid4())
d.addById(i, {"1":1})

d.modifyById(i, {"1":2})