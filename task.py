class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # По умолчанию задача не выполнена

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"Описание задачи: {self.description}nСрок выполнения: {self.deadline}nСтатус: {'Выполнено' if self.status else 'Не выполнено'}"

    