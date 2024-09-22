from model.user import User
from data import database_interface as dbi
import uuid, json

i = str(uuid.uuid4())

data = {
    "userId": i,
    "sentFeedbackIds": [],
    "recievedFeedbackIds":[]
}
u1 = User(data)
data = u1.toDict()

dbi.addUserById(u1.userId, u1.toDict())

print(json.dumps(dbi.getUserById(i)))