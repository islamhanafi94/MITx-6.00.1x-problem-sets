# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def calcPayment(balance,annualInterestRate,monthlyPaymentRate):
    for i in range(12):
        balance = (balance - (balance * monthlyPaymentRate)) * (1 + annualInterestRate/12)

    return balance


print(round(calcPayment(balance, annualInterestRate, monthlyPaymentRate), 2))

