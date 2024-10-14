import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 

from model.user import User
from data.database_interface import UserDTO
import uuid

def new(test_path = ""):
    '''Функция создаёт нового пользователя и возвращает его объект'''
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
    user_obj.from_dict(saved_data)
    return user_obj

def is_exist(user_id:str, test_path = "") -> bool:
    '''Функция проверяет существование в системе пользователя
    с указанным ID. Возвращает True или False'''
    try:
        path = "" #стандартный путь к хранилищу
        if test_path != "": path = test_path

        result_user_data = UserDTO(path).get_user_by_id(user_id)
        if result_user_data==None: return False
        else: return True
    except Exception as e:
        print(f"Can't check is user user_id={user_id} exist: {e}")
        return False