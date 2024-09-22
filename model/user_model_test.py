from user import User
import uuid, json

i = str(uuid.uuid4())

data = {
    "userId": i,
    "sentFeedbackIds": [],
    "recievedFeedbackIds":[]
}

u1 = User(data)

print(json.dumps(u1.toDict()))