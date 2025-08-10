
class PDF:
    def generate_pdf(self):
        print("PDF generated")

class Save:
    def save_to_file(self, filename):
        print(f"Saved {filename}")

class Report(PDF, Save):
    def __init__(self, title, content):
        self.title = title
        self.content = content

r = Report('ABC', 'asdasdadssdf')
print(r.__dict__)
r.generate_pdf()
r.save_to_file(r.title)

