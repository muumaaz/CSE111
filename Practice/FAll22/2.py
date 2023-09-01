class Mobile:
    countryCodes = {"880": "Bangladesh", "966": "India", "455": "USA"}
    def __init__(self, model, simCardStatus):
        self.model = model
        self.__simCardStatus = simCardStatus
        print(f"Model {model} is manufactured.")
    def setSimCardStatus(self,status):
        self.__simCardStatus = status
        print("SIM card status updated successfully.")
    def getSimCardStatus(self):
        return self.__simCardStatus
    def __str__(self):
        return f"Mobile Phone Detail:\nModel: {self.model}\nSIM Card Status: {self.__simCardStatus}"

#Write your code here
class Nokia(Mobile):
    dialCallHistory = []
    def __init__(self, model, simstatus, balance = 0):
        super().__init__(model, simstatus)
        self.bal = balance

    def __str__(self):
        return f"Mobile Phone Detail:\nModel: {self.model}\nSIM Card Status: {super().getSimCardStatus()}\nBalance: {self.bal} Tk"

    def changeSIMCardStatus(self):
        super().setSimCardStatus(True)

    def rechargeSIMCard(self, tk):
        self.bal = tk
        print(f"Recharge successful! Current balance {self.bal}")
    
    def dialCall(self, number):
        code = number[:3]
        if super().getSimCardStatus() == True:
            if self.bal > 0:
                if code in Mobile.countryCodes:
                    self.dialCallHistory.append(number)
                    return f"Dialing the number {number} to {Mobile.countryCodes[code]} region."
                else:
                    return "Dialing is not allowed in this region."
            else:
                return "Insufficient balance!"
        else:
            return "No Sim card available!"


N3110 = Nokia("N3110", False)
print("#######################################")
print(N3110)
print("1======================================")
N1100 = Nokia("N1100", True,100)
print("#######################################")
print(N1100)
print("2======================================")
print(N3110.dialCall("88017196xxxx"))
print("3======================================")
N3110.changeSIMCardStatus()
print("4======================================")
print(N3110.dialCall("88017196xxxx"))
print("5======================================")
N3110.rechargeSIMCard(200)
print("6======================================")
print(N3110.dialCall("88017196xxxx"))
print("7======================================")
print(N1100.dialCall("45617196xxxx"))
print("8======================================")
print(N1100.dialCall("45517196xxxx"))
print(N1100.dialCall("96617196xxxx"))
print("9======================================")
print(f"Dial call history for {N1100.model}: {N1100.dialCallHistory}")
print(f"Dial call history for {N3110.model}: {N3110.dialCallHistory}") 