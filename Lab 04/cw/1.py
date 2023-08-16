#1
class Customer:
    def __init__(self):
        self.ticket_count = 0
        self.total_price = 0

        print("Welcome to ABC Memorial Park")

    def buyTicket(self, name, age):
        if self.ticket_count == 3:
            print("You can't buy more than 3 tickets")
            return

        if age > 10:
            ticket_price = 100
        else:
            ticket_price = 50
        self.ticket_count += 1
        self.total_price += ticket_price

        print(f"Successfully purchased a ticket for {name}!")

    def showDetails(self):
        print(f"Amount of tickets: {self.ticket_count}")
        print(f"Total price: {self.total_price}")

print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()