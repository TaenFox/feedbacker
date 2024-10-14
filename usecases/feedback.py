import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 

from model.user import User
from model.feedback import Feedback
from data.database_interface import FeedbackDTO
from usecases import user as uc_user
import uuid

def save(author_id:str,
            receiver_id:str,
            feedback_context:str,
            feedback_id:str = "",
            test_path_feedback = "",
            test_path_user = ""):
    if feedback_id == "": feedback_id = str(uuid.uuid4())
    feedback_obj = Feedback()

    feedback_data = {
        "feedback_id": feedback_id,
        "content": feedback_context,
        "author_id": author_id,
        "receiver_id": receiver_id
    }
    
    path_feedback = "" #стандартный путь к хранилищу фидбеков
    if test_path_feedback != "": path_feedback = test_path_feedback

    path_user = "" #стандартный путь к хранилищу пользователей
    if test_path_user != "": path_user = test_path_user

    #проверяем существование автора и если отсутствует - стопаем
    if not uc_user.is_exist(author_id, path_user):
        print(f"Отправитель с ID={author_id} не добавлен в систему")
        return None
    
    #проверяем существование получателся и если отсутствует - стопаем
    if not uc_user.is_exist(receiver_id, path_user):
        print(f"Получатель с ID={receiver_id} не добавлен в систему")
        return None
    
    #добавляем запись с фидбеком
    feedback_obj.from_dict(feedback_data)
    saved_data = FeedbackDTO(path_feedback).add_feedback_by_id(feedback_id, feedback_obj.to_dict())

    #добавляем запись о фидбеке в объект автора
    author = uc_user.get(author_id, path_user)
    author.sent_feedback_ids.append(feedback_id)
    uc_user.modify(author, path_user)

    #добавляем запись о фидбеке в объект получателя
    receiver = uc_user.get(receiver_id, path_user)
    receiver.recieved_feedback_ids.append(feedback_id)
    uc_user.modify(receiver, path_user)

    return saved_data