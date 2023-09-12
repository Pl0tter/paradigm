# Задача 2
# Мы разрабатываем систему управления ресурсами в офисе. У нас есть несколько комнат, в каждой из которых размещены разные устройства (компьютеры, принтеры, лампы и т. д.).
# Каждое устройство имеет следующие характеристики: тип (компьютер, принтер, лампа и т. д.), статус (включено или выключено), идентификатор.
# Мы хотим выполнить следующие операции:
# __
# Добавить новое устройство в комнату.
# Включить или выключить устройство в комнате.
# Поиск устройства по типу и статусу.
# Получить список всех устройств в конкретной комнате.
# Подсчитать общее количество устройств каждого типа в офисе.

office = {}


def append_room(room_number: int):
    '''Добавить комнату'''
    office[room_number] = []


def append_device(place: int, type: str, statusOn: bool, id: int):
    '''Добавить новое устройство в комнату'''
    office[place].append({'id': id, 'type': type, 'statusOn': statusOn})


def change_statusOn(place: int, id: int, statusOn: bool):
    '''Включить или выключить устройство в комнате'''
    for item in office[place]:
        if (item['id'] == id):
            item['statusOn'] = statusOn


def find_device(type: str, statusOn: bool):
    '''Поиск устройства по типу и статусу'''
    for room in office:
        for device in office[room]:
            if (device['type'] == type and device['statusOn'] == statusOn):
                print(f'Комната: {room}, устройство: {device}')


def devices_room(room: int):
    '''Получить список всех устройств в конкретной комнате'''
    print(f'Список устройств в комнате {room}:')
    for device in office[room]:
        print(f"\t {device}")


def print_all_devices():
    '''Вывод всех устройств'''
    for room in office:
        devices_room(room)


def count_devices():
    '''Подсчитать общее количество устройств каждого типа в офисе'''
    summary = {}
    for room in office:
        for device in office[room]:
            if (device['type'] in summary):
                summary[device['type']] += 1
            else:
                summary[device['type']] = 1
            device['type']
    print(summary)


append_room(101)
append_room(102)

append_device(101, 'PC', True, 1)
append_device(101, 'PC', False, 2)
append_device(101, 'Printer', True, 3)
append_device(101, 'Lamp', False, 4)
append_device(102, 'PC', True, 1)
append_device(102, 'Printer', True, 2)
append_device(102, 'Printer', False, 3)
append_device(102, 'Lamp', True, 4)

change_statusOn(101, 1, False)
find_device('PC', True)

print_all_devices()
devices_room(101)
count_devices()
