
def calc(initialBalance, annualInterestRate, monthlyPayment):
    for i in range(12):
        initialBalance = (initialBalance - monthlyPayment) * \
        (1 + annualInterestRate/12)
    return initialBalance

def calcPayment(balance, annualInterestRate):
    # initialBalance = balance
    monthlyPayment = 10
    initialBalance = calc(balance, annualInterestRate, monthlyPayment)
    while initialBalance > 0:
        monthlyPayment += 10
        initialBalance = calc(balance, annualInterestRate, monthlyPayment)

    return monthlyPayment


print(calcPayment(320000, 0.2))
