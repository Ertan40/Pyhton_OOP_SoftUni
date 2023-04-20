class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number >= len(self.comments):
        # if not 0 <= comment_number < len(self.comments):
            return "Cannot find comment."
        else:
            for i in range(len(self.comments)):
                if i == comment_number:
                    self.comments.remove(self.comments[comment_number])
                    self.comments.insert(comment_number, new_comment)
            # self.comments[comment_number] = new_comment
            return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

