import data.file_database as db
import uuid

d = db.FileDataBase("feedback")
d.addById(str(uuid.uuid4()), {"1":1})