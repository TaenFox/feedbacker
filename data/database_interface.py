from data.file_database import FileDataBase as db_interface

def getFeedbackById(feedbackId:str)-> dict:
    '''Получает словарь значений, соответствующих фидбеку с id={feedbackId}'''
    try:
        db_feedback = db_interface("feedback")
        data = db_feedback.getById(feedbackId)
        if data == None: raise Exception("No data has been read")
        return data
    except Exception as e:
        print(f"Can't get feedback by id = {feedbackId}: {e}")
        return None

def modifyFeedbackById(feedback:str, data:dict)-> dict:
    pass