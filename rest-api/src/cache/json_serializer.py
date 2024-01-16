import json


# определяет методы для сериализации (то есть преобразование в формат легкий для сохранения и передачи) и десериализации данных в JSON-формат
class JsonSerializer(object):
    def serialize(self, key, value):
        # если значение уже является строкой, возвращает её без изменений и флаг 1
        if isinstance(value, str):
            return value, 1
        # проверка на базовый тип языка (int, str, float и тд)
        if type(value).__module__ != "__builtin__":
            value = dict(value)
        # снова сериализация. Преобразует значение в JSON-строку с помощью json.dumps и возвращает её вместе с флагом 2
        return json.dumps(value), 2

    def deserialize(self, key, value, flags):
        # если флаг равен 1, значит значение не было сериализовано и возвращается без изменений
        if flags == 1:
            return value
        # если флаг равен 2, десериализует значение из JSON-строки с помощью json.loads и возвращает полученный объект
        if flags == 2:
            return json.loads(value)
        # если условия выше не выполнены, то генерирует исключение, сигнализируя об ошибке
        raise Exception("Unknown serialization format")
       
