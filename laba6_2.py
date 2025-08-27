import multiprocessing

def worker(shared_dict, key, value):
    """Функция для обновления общего словаря."""
    shared_dict[key] = value

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()  # Создаем общий словарь

        processes = []
        data = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]  # Данные для загрузки

        # Создаем и запускаем процессы
        for key, value in data:
            a = multiprocessing.Process(target=worker, args=(shared_dict, key, value))
            processes.append(a)
            a.start()

        # Ожидаем завершения всех процессов
        for a in processes:
            a.join()

        # Выводим итоговый общий словарь
        print("Общий словарь:", dict(shared_dict))