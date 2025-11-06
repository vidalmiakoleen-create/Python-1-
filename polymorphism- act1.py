class InkPrinter:
    def print_document(self):
        return "Printing using ink..."

class LaserPrinter:
    def print_document(self):
        return "Printing using laser..."

printers = [InkPrinter(), LaserPrinter()]
for p in printers:
    print(p.print_document()
