import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 

from model.user import User
from data.database_interface import UserDTO
import uuid

def new(test_path = ""):
    user_id = str(uuid.uuid4())
    user_data = {
        "user_id":user_id,
        "sent_feedback_ids":[],
        "recieved_feedback_ids":[]}
    
    path = "" #стандартный путь к хранилищу
    if test_path != "": path = test_path
    
    user_obj = User()
    user_obj.from_dict(user_data)

    saved_data = UserDTO(path).add_user_by_id(user_id, user_obj.to_dict())
    return saved_data