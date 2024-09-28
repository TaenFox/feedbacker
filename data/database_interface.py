from data.file_database import FileDataBase
# import os

class FeedbackDTO():
    path: str
    db: FileDataBase

    def __init__(self, path:str = "") -> None:
        if path == "":
            path = "./data/feedback"

        self.db = FileDataBase(path)

    def get_feedback_by_id(self, feedback_id:str)-> dict:
        '''Получает словарь значений, соответствующих фидбеку с id={feedback_id}'''
        try:
            data = self.db.get_by_id(feedback_id)
            return data
        except Exception as e:
            print(f"Can't get feedback by id = {feedback_id}: {e}")
            return None

    def add_feedback_by_id(self, feedback_id:str, data:dict)-> dict:
        '''Сохраняет словарь значений, переданных в словаре data. 
        Сохраняется с id={feedback_id}. Возвращает результат сохранения'''
        try:
            self.db.add_by_id(feedback_id, data)
            data = self.db.get_by_id(feedback_id)
            return data
        except Exception as e:
            print(f"Can't add feedback by id = {feedback_id}: {e}")
            return None

    def modify_feedback_by_id(self, feedback_id:str, data:dict)-> dict:
        '''Заменяет словарь значений, переданных в словаре data в файле
        с id={feedback_id}. Возвращает результат сохранения'''
        try:
            self.db.modify_by_id(feedback_id, data)
            data = self.db.get_by_id(feedback_id)
            return data
        except Exception as e:
            print(f"Can't modify feedback by id = {feedback_id}: {e}")
            return None

class UserDTO():
    path: str
    db: FileDataBase

    def __init__(self, path:str = "") -> None:
        if path == "":
            path = "./data/user"

        self.db = FileDataBase(path)
        
    def get_user_by_id(self, userId:str)-> dict:
        '''Получает словарь значений, соответствующих пользователю с id={userId}'''
        try:
            data = self.db.get_by_id(userId)
            return data
        except Exception as e:
            print(f"Can't get user by id = {userId}: {e}")
            return None

    def add_user_by_id(self, userId:str, data:dict)-> dict:
        '''Сохраняет словарь значений, переданных в словаре data. 
        Сохраняется с id={userId}. Возвращает результат сохранения'''
        try:
            self.db.add_by_id(userId, data)
            data = self.db.get_by_id(userId)
            return data
        except Exception as e:
            print(f"Can't add user by id = {userId}: {e}")
            return None
        
    def modify_user_by_id(self, userId:str, data:dict)-> dict:
        '''Заменяет словарь значений, переданных в словаре data в файле
        с id={userId}. Возвращает результат сохранения'''
        try:
            self.db.modify_by_id(userId, data)
            data = self.db.get_by_id(userId)
            return data
        except Exception as e:
            print(f"Can't modify user by id = {userId}: {e}")
            return None