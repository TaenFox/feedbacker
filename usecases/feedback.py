import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 

from model.user import User
from model.feedback import Feedback
from data.database_interface import FeedbackDTO, UserDTO
import uuid

def save_feedback(author_id:str,
            receiver_id:str,
            feedback_context:str,
            feedback_id:str = "",
            test_path = ""):
    if feedback_id == "": feedback_id = str(uuid.uuid4())
    feedback_obj = Feedback()

    feedback_data = {
        "feedback_id": feedback_id,
        "content": feedback_context,
        "author_id": author_id,
        "receiver_id": receiver_id
    }
    
    path = "" #стандартный путь к хранилищу
    if test_path != "": path = test_path

    feedback_obj.from_dict(feedback_data)

    saved_data = FeedbackDTO(path).add_feedback_by_id(feedback_id, feedback_obj.to_dict())
    return saved_data