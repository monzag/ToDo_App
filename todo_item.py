class ToDoItem:

    def __init__(self, name):
        self.name = name
        self.is_done = False

    def mark(self):
        self.is_done = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    

