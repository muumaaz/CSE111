class Ticket:
    route_distance = {"Route A":400, "Route B":425, "Route C":350}
    fare_per_km = 20
    def __init__(self, route, journeyDate, price = 0):
        self.route = route
        self.journeyDate = journeyDate
        self.__price = price
    def setPrice(self, price):
        self.__price = price
    def getPrice(self):
        return self.__price
    def ticket_details(self):
        return f"Route: {self.route}\nJourney Date: {self.journeyDate}"

class BusTicket(Ticket):
    total_tickets = 0
    bus = {}
    def __init__(self, route, date, busname, seat):
        super().__init__(route, date)
        self.busname = busname
        self.seat = seat
        BusTicket.total_tickets += 1
        self.ticket_id = f"{self.busname}-{BusTicket.total_tickets}"
        self.status = "Not paid"

    def calculate_fare(self):
        super().setPrice(Ticket.route_distance[self.route])
        self.fare = super().getPrice() * Ticket.fare_per_km
        print("Ticket fare is calculated succesfully")

    def ticket_details(self):
        print(f"Ticket ID: {self.ticket_id}")
        super().ticket_details()
        print(f"Bus name: {self.busname}")
        print(f"Seat No: {self.seat}")
        print(f"Price: {self.fare}")
        print(f"Status: {self.status}")
    
    def make_payment(self):
        self.status = "Paid"


ticket1 = BusTicket("Route A", "30 April, 2023", "Nabil Enterprise", "F2")
print("Total ticket(s):", BusTicket.total_tickets)
print("1============================")
ticket1.calculate_fare()
print("2============================")
ticket1.ticket_details()
print("3============================")
ticket1.make_payment()
print("4============================")
ticket1.ticket_details()
print("5============================")
ticket2 = BusTicket("Route C", "26 April, 2023", "Hanif Enterprise", "A2")
print("Total ticket(s):", BusTicket.total_tickets)
print("6============================")
ticket2.calculate_fare()
print("7============================")
ticket2.make_payment()
print("8============================")
ticket2.ticket_details()