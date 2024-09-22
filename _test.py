import data.file_database as db
import data.database_interface as dbi
import uuid, json
from model.feedback import Feedback as fb

# d = db.FileDataBase("feedback")
i = str(uuid.uuid4())
# print(f"./data/feedback/{i}.json")
data = {
    "feedbackId":i,
    "content": "Some message",
    "authorId": "123456",
    "receiverId": "1234"
}
mes = fb(data)
dbi.addFeedbackById(i, mes.toDict())
print(json.dumps(mes.toDict()))

mes.content = "more info"

dbi.modifyFeedbackById(i, data)

print(json.dumps(mes.toDict()))