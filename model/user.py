
class User():
    user_id: str
    sent_feedback_ids = list
    recieved_feedback_ids = list

    def from_dict(self, data: dict) -> None:
        '''
        Объект пользователя. В аргументе передаётся словарь с ключами (значения в них строковые):
        - user_id - идентификатор пользователя
        - sent_feedback_ids - список идентификаторов отправленных сообщений с фидбеком
        - recieved_feedback_ids - список идентификаторов полученных сообщений с фидбеком
        '''
        if "user_id" not in data: raise ImportWarning("No 'user_id' in 'data'")
        if type(data["user_id"]) is not str: raise TypeError("Field 'user_id' should be string")
        if len(data["user_id"]) == 0: raise ImportWarning("Field 'user_id' must not be empty")
        if "sent_feedback_ids" not in data: raise ImportWarning("No 'sent_feedback_ids' in 'data'")
        if type(data["sent_feedback_ids"]) is not list: raise TypeError("Field 'sent_feedback_ids' should be list")
        if "recieved_feedback_ids" not in data: raise ImportWarning("No 'recieved_feedback_ids' in 'data'")
        if type(data["recieved_feedback_ids"]) is not list: raise TypeError("Field 'recieved_feedback_ids' should be list")
        
        try:
            self.user_id = data["user_id"]
            self.sent_feedback_ids = data["sent_feedback_ids"]
            self.recieved_feedback_ids = data["recieved_feedback_ids"]
        except Exception as e:
            print(f"Can't use 'data' dictionary: {e}")
        return
    
    def to_dict(self):
        '''Возвращает словарь с полями пользователя'''

        try:
            data = {
                "user_id": self.user_id,
                "sent_feedback_ids": self.sent_feedback_ids,
                "recieved_feedback_ids": self.recieved_feedback_ids
            }
            return data
        except Exception as e:
            print(f"Can't construct dictionary for user id={self.user_id}: {e}")