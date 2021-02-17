# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
#extra = 1000
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

# while month <= 12:
#     principal = principal * (1+rate/12) - (payment+extra)
#     total_paid = total_paid + payment + extra
#     month = month + 1
   

while principal > payment:

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        print(month, round(total_paid,2), round(principal,2))
        month = month + 1

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        print(month, round(total_paid,2), round(principal,2))
        month = month + 1

total_paid = total_paid + principal
principal = 0
print(month, round(total_paid,2), round(principal,2))

        

print('Total paid:', round(total_paid,2))
print("In months:", round(month,2))

