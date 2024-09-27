from model.user import User
from data import database_interface as dbi
import uuid, json

i = str(uuid.uuid4())

data = {
    "user_id": i,
    "sent_feedback_ids": [],
    "recieved_feedback_ids":[]
}
u1 = User(data)
data = u1.to_dict()

dbi.add_user_by_id(u1.user_id, u1.to_dict())

print(json.dumps(dbi.get_user_by_id(i)))

data_to_modify:dict = u1.to_dict()
list_to_modify:list = data_to_modify["sent_feedback_ids"]
list_to_modify.append("1234567")
data_to_modify["sent_feedback_ids"] = list_to_modify
dbi.modify_user_by_id(i, data_to_modify)

print(json.dumps(dbi.get_user_by_id(i)))