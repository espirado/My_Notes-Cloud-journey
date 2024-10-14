class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email


class EmailService:
    def send_email(self,customer,message):
        pass
class Ordering_Service:
    def place_order(self,customer,order):
      pass

class InvoiceService:
    def generate_invoice(self,customer,invoice):
      pass