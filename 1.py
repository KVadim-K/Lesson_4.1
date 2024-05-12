from datetime import datetime

class Task:
    def __init__(self, name, description, due_date):  # Добавляем аргумент name
        self.name = name  # Сохраняем имя задачи
        self.description = description # Описание задачи
        self.due_date = due_date  # Срок выполнения задачи
        self.completed = False  # Задача не выполнена по умолчанию

    def mark_as_completed(self):  # Метод для отметки задачи как выполненной
        self.completed = True  # Задача выполнена

    def __str__(self): # Метод для создания строкового представления объекта
        status = "Выполнено" if self.completed else "Не выполнено"  # Статус задачи (выполнена или не выполнена)
        return f"Задача: {self.name}, Описание: {self.description}, Срок: {self.due_date}, Статус: {status}" # Возвращаем строку с информацией о задачеё

class TaskManager:  # Класс для управления задачами
    def __init__(self): # Конструктор класса TaskManager
        self.tasks = []  # Список задач по умолчанию пустый

    def add_task(self, name, description, due_date):  # Метод для добавления новой задачи
        if isinstance(due_date, datetime):  # Проверяем, является ли due_date объектом datetime
            new_task = Task(name, description, due_date.strftime("%d.%m.%Y"))  # Если да, формируем новую задачу
        else:
            new_task = Task(name, description, due_date)  # Если нет, формируем новую задачу без даты выполнения
        self.tasks.append(new_task)  # Добавляем задачу в список

    def mark_completed(self, name):  # Метод для отметки задачи как выполненной
        for task in self.tasks:  # Перебираем все задачи в списке
            if task.name == name and not task.completed:  # Если задача с заданным именем и не выполнена
                task.mark_as_completed()  # Отмечаем задачу как выполненную
                return True  # Возвращаем True, если задача отмечена
        return False  # Возвращаем False, если задача не отмечена

    def show_all_tasks(self):  # Метод для вывода всех задач
        if not self.tasks:  # Если список задач пуст
            print("Нет задач.")  # Выводим соответствующее сообщение
        else:
            for task in self.tasks:
                print(task)  # Выводим информацию о каждой задаче

# Пример использования
manager = TaskManager()
manager.add_task("Покупки", "Купить бананы и яблоки", "18.05.2024")
manager.add_task("Оплата кредита", "Кредит на покупку автомобиля", datetime(2024, 1, 2))
manager.add_task("Отчет", "Подготовить отчет о продажах", "03-01-2024")

manager.mark_completed("Оплата кредита")
manager.mark_completed("Отчет")
manager.show_all_tasks()  # Вывод всех задач, включая выполненные