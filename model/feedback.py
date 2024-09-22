
class Feedback():
    feedbackId: str
    content: str
    authorId: str
    receiverId: str

    def __init__(self, data: dict) -> None:
        '''
        Объект фидбека. В аргументы передаётся словарь с ключами (значения в них строковые):
        - feedbackId - идентификатор фидбека
        - content - сообщение фидбека
        - authorId - идентификатор автора фидбека
        - receiverId - идентификатор получателя фидбека
        '''
        #TODO добавить проверку на строковые данные
        try:
            if "feedbackId" not in data: raise Exception("No 'feedbackId' in 'data'")
            if "content" not in data: raise Exception("No 'content' in 'data'")
            if "authorId" not in data: raise Exception("No 'authorId' in 'data'")
            if "receiverId" not in data: raise Exception("No 'receiverId' in 'data'")
        except Exception as e:
            print(e)
            return None
        
        try:
            self.feedbackId = data['feedbackId']
            self.content = data['content']
            self.authorId = data['authorId']
            self.receiverId = data['receiverId']
        except Exception as e:
            print(f"Can't use 'data' dictionary: {e}")
        return

    def toDict(self):
        '''Возвращает словарь с полями фидбека'''
        try:
            data = {
                "feedbackId": self.feedbackId,
                "content": self.content,
                "authorId": self.authorId,
                "receiverId": self.receiverId
            }
            return data
        except Exception as e:
            print(f"Can't construct dictionary for feedback id={self.feedbackId}: {e}")