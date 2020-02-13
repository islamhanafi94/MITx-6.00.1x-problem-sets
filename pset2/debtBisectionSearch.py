from math import *

def calc(initialBalance, annualInterestRate, monthlyPayment):
    for i in range(12):
        initialBalance = (initialBalance - monthlyPayment) * \
            (1 + annualInterestRate/12)
    return initialBalance


def calcPayment(balance, annualInterestRate):
    lowerLimit = round(balance / 12,2)
    upperLimit = round((balance * (1 + (annualInterestRate/12))**12) / 12.0,2)
    # approximate
    monthlyPayment = round((lowerLimit + upperLimit) / 2,2)

    # test our value and deside to recalculate upper or lower limit
    initialBalance = round(calc(balance, annualInterestRate, monthlyPayment), 2)

    while abs(initialBalance) > 0.1 :
        if initialBalance < 0 :
            upperLimit = monthlyPayment
            monthlyPayment = round((lowerLimit + upperLimit) / 2, 2)
            initialBalance = round(calc(balance, annualInterestRate, monthlyPayment), 2)
        elif initialBalance > 0 :
            lowerLimit = monthlyPayment
            monthlyPayment = round((lowerLimit + upperLimit) / 2, 2)
            initialBalance = round(calc(balance, annualInterestRate, monthlyPayment), 2)

    return monthlyPayment

balance = 999999
annualInterestRate = 0.18

print(calcPayment(balance, annualInterestRate))
