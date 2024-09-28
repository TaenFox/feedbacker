import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 

from model.user import User
from model.feedback import Feedback
from data.database_interface import FeedbackDTO, UserDTO
import uuid

def save_feedback(author_id:str,
            reciever_id:str,
            feedback_context:str,
            feedback_id:str = "",
            test_path = ""):
    if feedback_id == "": feedback_id = str(uuid.uuid4())
    feedback_data = {
        "feedback_id": feedback_id,
        "content": feedback_context,
        "author_id": author_id,
        "reciever_id": reciever_id
    }
    
    path = "" #стандартный путь к хранилищу
    if test_path != "": path = test_path

    saved_data = FeedbackDTO(path).add_feedback_by_id(feedback_id, feedback_data)
    return saved_data