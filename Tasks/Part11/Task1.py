class Publication:
    def __init__(self, name):
        self.name = name
class Book(Publication):
    def __init__(self, name, writer, pagecount):
        self.writer = writer
        self.pagecount = pagecount
        super().__init__(name)
#    def print_info(self):
#        print(self.name, self.writer, self.pagecount)
    # Alternative answer
    def __str__(self): return(self.name + " " + self.writer + " " + str(self.pagecount))
class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    def print_info(self):
        print(self.name, self.editor)

B = Book("Hytti no.6", "Rosa Liksom", 200)
M = Magazine("Aku Ankka", "Aki Hyyppä")
print(B)
M.print_info()
