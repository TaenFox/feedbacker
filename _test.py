import data.file_database as db
import uuid

db.addById(str(uuid.uuid4()), {"1":1})