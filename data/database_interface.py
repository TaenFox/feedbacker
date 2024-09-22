from data.file_database import FileDataBase as db_interface

def getFeedbackById(feedbackId:str)-> dict:
    '''Получает словарь значений, соответствующих фидбеку с id={feedbackId}'''
    try:
        db = db_interface("feedback")
        data = db.getById(feedbackId)
        return data
    except Exception as e:
        print(f"Can't get feedback by id = {feedbackId}: {e}")
        return None

def addFeedbackById(feedbackId:str, data:dict)-> dict:
    '''Сохраняет словарь значений, переданных в словаре data. 
    Сохраняется с id={feedbackId}. Возвращает результат сохранения'''
    try:
        db = db_interface("feedback")
        db.addById(feedbackId, data)
        data = db.getById(feedbackId)
        return data
    except Exception as e:
        print(f"Can't add feedback by id = {feedbackId}: {e}")
        return None

def modifyFeedbackById(feedbackId:str, data:dict)-> dict:
    '''Заменяет словарь значений, переданных в словаре data в файле
    с id={feedbackId}. Возвращает результат сохранения'''
    try:
        db = db_interface("feedback")
        db.modifyById(feedbackId, data)
        data = db.getById(feedbackId)
        return data
    except Exception as e:
        print(f"Can't modify feedback by id = {feedbackId}: {e}")
        return None
    
def getUserById(userId:str)-> dict:
    '''Получает словарь значений, соответствующих пользователю с id={userId}'''
    try:
        db = db_interface("user")
        data = db.getById(userId)
        return data
    except Exception as e:
        print(f"Can't get user by id = {userId}: {e}")
        return None

def addUserById(userId:str, data:dict)-> dict:
    '''Сохраняет словарь значений, переданных в словаре data. 
    Сохраняется с id={userId}. Возвращает результат сохранения'''
    try:
        db = db_interface("user")
        db.addById(userId, data)
        data = db.getById(userId)
        return data
    except Exception as e:
        print(f"Can't add user by id = {userId}: {e}")
        return None
    
def modifyUserById(userId:str, data:dict)-> dict:
    '''Заменяет словарь значений, переданных в словаре data в файле
    с id={userId}. Возвращает результат сохранения'''
    try:
        db = db_interface("user")
        db.modifyById(userId, data)
        data = db.getById(userId)
        return data
    except Exception as e:
        print(f"Can't modify user by id = {userId}: {e}")
        return None