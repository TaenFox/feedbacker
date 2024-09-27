
class Feedback():
    feedback_id: str
    content: str
    author_id: str
    receiver_id: str

    def __init__(self, data: dict) -> None:
        '''
        Объект фидбека. В аргументы передаётся словарь с ключами (значения в них строковые):
        - feedback_id - идентификатор фидбека
        - content - сообщение фидбека
        - author_id - идентификатор автора фидбека
        - receiver_id - идентификатор получателя фидбека
        '''
        #TODO добавить проверку на строковые данные
        if "feedback_id" not in data: raise Exception("No 'feedback_id' in 'data'")
        if "content" not in data: raise Exception("No 'content' in 'data'")
        if "author_id" not in data: raise Exception("No 'author_id' in 'data'")
        if "receiver_id" not in data: raise Exception("No 'receiver_id' in 'data'")
        
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