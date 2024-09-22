import json

def getById(id:str)-> dict:
    '''Извлекает информацию из json-файла в текущей директории, 
    название которого соответствует маске `{id}.json`. 
    Возвращает словарь'''
    try:
        with open(f"{id}.json","r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(f"Can't read file {id}.json: {e}")

        