class ToDoItem:

    def __init__(self, name, is_done=False):
        self.name = name
        self.is_done = is_done

    def mark(self):
        self.is_done = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        text = ' {}'.format(self.name)
        if self.is_done is True:
            message = '[X]' + text
        else:
            message = '[ ]' + text

        return message



