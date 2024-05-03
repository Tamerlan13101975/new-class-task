class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # По умолчанию задача не выполнена

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"Описание задачи: {self.description}nСрок выполнения: {self.deadline}nСтатус: {'Выполнено' if self.status else 'Не выполнено'}"

# Создаем несколько задач
tasks = [Task("Помыть посуду", "Сегодня"),
         Task("Сделать домашнее задание", "Завтра"),
         Task("Купить продукты", "Послезавтра")]

# Добавляем задачи
tasks.append(Task("Погулять с собакой", "Вечером"))
tasks.append(Task("Успеть на тренеровку", "Вечером"))


# Отмечаем выполненные задачи
tasks[0].mark_as_done()
tasks[2].mark_as_done()


# Выводим список не выполненных задач
print("Список не выполненных задач:")
for task in tasks:
    if not task.status:
        print(task)