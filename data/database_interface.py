from data.file_database import FileDataBase as db_class
import os

def get_feedback_by_id(feedbackId:str)-> dict:
    '''Получает словарь значений, соответствующих фидбеку с id={feedbackId}'''
    try:
        db = db_class(f"{os.curdir}/data/feedback")
        data = db.get_by_id(feedbackId)
        return data
    except Exception as e:
        print(f"Can't get feedback by id = {feedbackId}: {e}")
        return None

def add_feedback_by_id(feedbackId:str, data:dict)-> dict:
    '''Сохраняет словарь значений, переданных в словаре data. 
    Сохраняется с id={feedbackId}. Возвращает результат сохранения'''
    try:
        db = db_class(f"{os.curdir}/data/feedback")
        db.add_by_id(feedbackId, data)
        data = db.get_by_id(feedbackId)
        return data
    except Exception as e:
        print(f"Can't add feedback by id = {feedbackId}: {e}")
        return None

def modify_feedback_by_id(feedbackId:str, data:dict)-> dict:
    '''Заменяет словарь значений, переданных в словаре data в файле
    с id={feedbackId}. Возвращает результат сохранения'''
    try:
        db = db_class(f"{os.curdir}/data/feedback")
        db.modify_by_id(feedbackId, data)
        data = db.get_by_id(feedbackId)
        return data
    except Exception as e:
        print(f"Can't modify feedback by id = {feedbackId}: {e}")
        return None
    
def get_user_by_id(userId:str)-> dict:
    '''Получает словарь значений, соответствующих пользователю с id={userId}'''
    try:
        db = db_class(f"{os.curdir}/data/user")
        data = db.get_by_id(userId)
        return data
    except Exception as e:
        print(f"Can't get user by id = {userId}: {e}")
        return None

def add_user_by_id(userId:str, data:dict)-> dict:
    '''Сохраняет словарь значений, переданных в словаре data. 
    Сохраняется с id={userId}. Возвращает результат сохранения'''
    try:
        db = db_class(f"{os.curdir}/data/user")
        db.add_by_id(userId, data)
        data = db.get_by_id(userId)
        return data
    except Exception as e:
        print(f"Can't add user by id = {userId}: {e}")
        return None
    
def modify_user_by_id(userId:str, data:dict)-> dict:
    '''Заменяет словарь значений, переданных в словаре data в файле
    с id={userId}. Возвращает результат сохранения'''
    try:
        db = db_class(f"{os.curdir}/data/user")
        db.modify_by_id(userId, data)
        data = db.get_by_id(userId)
        return data
    except Exception as e:
        print(f"Can't modify user by id = {userId}: {e}")
        return None