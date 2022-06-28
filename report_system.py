target_money = int(input())
payment_counter = 0
cash_pay_sum = 0
cash_pay_counter = 0
card_pay_sum = 0
card_pay_counter = 0
user_input = input()
while not user_input == "End":
    transaction = int(user_input)
    payment_counter += 1
    if not payment_counter % 2 == 0 and transaction <= 100:
        cash_pay_counter += 1
        cash_pay_sum += transaction
        print("Product sold!")
    elif payment_counter % 2 == 0 and transaction >= 10:
        card_pay_sum += transaction
        card_pay_counter += 1
        print("Product sold!")
    else:
        print("Error in transaction!")
    if cash_pay_sum + card_pay_sum >= target_money:
        break
    user_input = input()
if cash_pay_sum + card_pay_sum >= target_money:
    print(f"Average CS: {cash_pay_sum / cash_pay_counter:.2f}")
    print(f"Average CC: {card_pay_sum / card_pay_counter:.2f}")
else:
    print("Failed to collect required money for charity.")