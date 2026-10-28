# Electricity Billing System
def calculate_bill(consumed_units):
    bill_amount = 0
    if consumed_units <= 100:
        bill_amount = consumed_units * 1.50
    elif consumed_units <= 200:
        bill_amount = 100 * 1.50 + (consumed_units - 100) * 2.50
    elif consumed_units <= 500:
        bill_amount = (100 * 1.50) + (100 * 2.50) + (consumed_units - 200) * 4.00
    else:
        bill_amount = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (consumed_units - 500) * 6.00
    return bill_amount

num_customers = int(input("Enter number of customers: "))
for customer_num in range(1, num_customers + 1):
    print(f"\nCustomer {customer_num}")
    customer_name = input("Enter customer name: ")
    units_consumed = float(input("Enter units consumed: "))
    bill_amount = calculate_bill(units_consumed)

    print("Customer Name :", customer_name)
    print("Units :", units_consumed)
    print("Bill Amount : Rs.", round(bill_amount, 2))