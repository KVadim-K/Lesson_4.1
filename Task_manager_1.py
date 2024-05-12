from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        if isinstance(due_date, datetime):
            new_task = Task(description, due_date.strftime("%d.%m.%Y"))
        else:
            new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.mark_as_completed()
                return True
        return False

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Все задачи выполнены.")
        else:
            for task in current_tasks:
                print(task)

# Пример использования
manager = TaskManager()
manager.add_task("Задача 1", "01-01-2024")
manager.add_task("Задача 2", datetime(2024, 1, 2))
manager.add_task("Задача 3", "03-01-2024")
manager.add_task("Задача 4", "04-05-2024")

manager.mark_completed("Задача 1")
manager.show_current_tasks()