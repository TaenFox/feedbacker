import json, os

class FileDataBase():
    def __init__(self, catalog:str) -> None:
        self.catalog = f"{os.curdir}/data/{catalog}"

    def getById(self, id:str)-> dict:
        '''Извлекает информацию из json-файла в указанной директории, 
        название которого соответствует маске `{id}.json`. 
        Возвращает словарь'''
        #TODO обработать ситуации, когда файл не существует
        try:
            with open(f"{self.catalog}/{id}.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                return data
        except Exception as e:
            print(f"Can't read file {id}.json: {e}")

    def addById(self, id:str, data:dict)-> dict:
        '''Сохраняет информацию в json-файл в указанной директории, 
        название которого соответствует маске `{id}.json`.
        В случае успеха возвращает сохранённый словарь значений'''
        try:
            json_file = open(f"{self.catalog}/{id}.json", "x", encoding="utf-8")
            json_file.write(json.dumps(data))
            json_file.close()
        except Exception as e:
            print(f"Can't create file {id}.json: {e}")
            return None
        
        try:
            savedData = self.getById(id=id)
            if data != savedData: raise Exception("Input data doesn't match with saved data")
            return savedData
        except Exception as e:
            print(f"Error creating file {id}.json: {e}")
            return None
        
    def modifyById(self, id:str, data:dict):
        '''Изменяет информацию в json-файл в указанной директории, 
        название которого соответствует маске `{id}.json`.
        В случае успеха возвращает сохранённый словарь значений'''
        try:
            json_file = open(f"{self.catalog}/{id}.json", "w", encoding="utf-8")
            json_file.write(json.dumps(data))
            json_file.close()
        except Exception as e:
            print(f"Can't modify file {id}.json: {e}")

        try:
            savedData = self.getById(id=id)
            if data != savedData: raise Exception("Input data doesn't match with saved data")
            return savedData
        except Exception as e:
            print(f"Error creating file {id}.json: {e}")
            return None