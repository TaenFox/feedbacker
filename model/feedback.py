
class Feedback():
    feedback_id: str
    content: str
    author_id: str
    receiver_id: str

    def from_dict(self, data: dict) -> None:
        '''
        Объект фидбека. В аргументы передаётся словарь с ключами (значения в них строковые):
        - feedback_id - идентификатор фидбека
        - content - сообщение фидбека
        - author_id - идентификатор автора фидбека
        - receiver_id - идентификатор получателя фидбека
        '''
        
        if "feedback_id" not in data: raise ImportWarning("No 'feedback_id' in 'data'")
        if type(data["feedback_id"]) is not str: raise TypeError("Field 'feedback_id' should be string")
        if "content" not in data: raise ImportWarning("No 'content' in 'data'")
        if type(data["content"]) is not str: raise TypeError("Field 'content' should be string")
        if "author_id" not in data: raise ImportWarning("No 'author_id' in 'data'")
        if type(data["author_id"]) is not str: raise TypeError("Field 'author_id' should be string")
        if "receiver_id" not in data: raise ImportWarning("No 'receiver_id' in 'data'")
        if type(data["receiver_id"]) is not str: raise TypeError("Field 'receiver_id' should be string")
        
        try:
            self.feedback_id = data['feedback_id']
            self.content = data['content']
            self.author_id = data['author_id']
            self.receiver_id = data['receiver_id']
        except Exception as e:
            print(f"Can't use 'data' dictionary: {e}")
        return

    def to_dict(self):
        '''Возвращает словарь с полями фидбека'''
        try:
            data = {
                "feedback_id": self.feedback_id,
                "content": self.content,
                "author_id": self.author_id,
                "receiver_id": self.receiver_id
            }
            return data
        except Exception as e:
            print(f"Can't construct dictionary for feedback id={self.feedback_id}: {e}")