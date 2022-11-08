import sys


class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages


    def print_information(self):
        print('%s\n%s\n%s'%(self.name, self.author, self.pages))


class Magazine(Publication):
    def __init__(self, name, editor, pages):
        super().__init__(name)
        self.editor = editor
        self.pages = pages

    def print_information(self):
        print('%s\n%s\n%s'%(self.name, self.editor, self.pages))

book = Book('Compartment No. 6', 'Rosa Liksom', 192)
mag = Magazine('Donald Duck', 'Aki Hyyppa', 35)

book.print_information()
mag.print_information()

sys.exit(0)