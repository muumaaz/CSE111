#1

# Subtask 1: Write the CellPackage Class
class CellPackage:
    def __init__(self, price, data, talk_time, messages, cashback, validity):
        self.price = price

        data = data.split()
        gb = int(data[0])
        self.data = gb * 1024

        self.talk_time = talk_time
        self.messages = messages
        self.cashback = round(price * int(cashback.strip('%')) / 100)
        self.validity = validity




pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
# Subtask 2: Check each attribute and print
print(f"Data = {pkg.data} MB") if pkg.data > 0 else None
print(f"Talktime = {pkg.talk_time} Minutes") #if pkg.talk_time > 0 else None
print(f"SMS/MMS = {pkg.messages}") if pkg.messages > 0 else None
print(f"Validity = {pkg.validity} Days") #if pkg.validity > 0 else None
print(f"--> Price = {pkg.price} tk") if pkg.price > 0 else None
print(f"Buy now to get {pkg.cashback} tk cashback.") if pkg.cashback > 0 else None


pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
# Subtask 3: Check each attribute and print
print(f"Data = {pkg2.data} MB") if pkg2.data > 0 else None
print(f"Talktime = {pkg2.talk_time} Minutes") #if pkg2.talk_time > 0 else None
print(f"SMS/MMS = {pkg2.messages}") if pkg2.messages > 0 else None
print(f"Validity = {pkg2.validity} Days") #if pkg2.validity > 0 else None
print(f"--> Price = {pkg2.price} tk") if pkg2.price > 0 else None
print(f"Buy now to get {pkg2.cashback} tk cashback.") if pkg2.cashback > 0 else None

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
# Subtask 4: Check each attribute and print
print(f"Data = {pkg4.data} MB") if pkg4.data > 0 else None
print(f"Talktime = {pkg4.talk_time} Minutes") #if pkg4.talk_time > 0 else None
print(f"SMS/MMS = {pkg4.messages}") if pkg4.messages > 0 else None
print(f"Validity = {pkg4.validity} Days") #if pkg4.validity > 0 else None
print(f"--> Price = {pkg4.price} tk") if pkg4.price > 0 else None
print(f"Buy now to get {pkg4.cashback} tk cashback.") if pkg4.cashback > 0 else None