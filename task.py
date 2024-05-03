class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # По умолчанию задача не выполнена

    def mark_as_done(self):
        self.status = True