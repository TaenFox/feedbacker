
class User():
    userId: str
    sentFeedbackIds = []
    recievedFeedbackIds = []

    def __init__(self, data: dict) -> None:
        '''
        Объект пользователя. В аргументе передаётся словарь с ключами (значения в них строковые):
        - userId - идентификатор пользователя
        - sentFeedbackIds - список идентификаторов отправленных сообщений с фидбеком
        - recievedFeedbackIds - список идентификаторов полученных сообщений с фидбеком
        '''
        #TODO добавить проверку на строковые данные
        #TODO добавить проверку на списки
        try:
            if "userId" not in data: raise Exception("No 'userId' in 'data'")
            if "sentFeedbackIds" not in data: raise Exception("No 'sentFeedbackIds' in 'data'")
            if "recievedFeedbackIds" not in data: raise Exception("No 'recievedFeedbackIds' in 'data'")
        except Exception as e:
            print(e)
            return None
        
        try:
            self.userId = data["userId"]
            self.sentFeedbackIds = data["sentFeedbackIds"]
            self.recievedFeedbackIds = data["recievedFeedbackIds"]
        except Exception as e:
            print(f"Can't use 'data' dictionary: {e}")
        return
    
    def toDict(self):
        '''Возвращает словарь с полями пользователя'''

        try:
            data = {
                "userId": self.userId,
                "sentFeedbackIds": self.sentFeedbackIds,
                "recievedFeedbackIds": self.recievedFeedbackIds
            }
            return data
        except Exception as e:
            print(f"Can't construct dictionary for user id={self.userId}: {e}")