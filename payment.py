def process_payment(amount):

    if amount is None:
        return "Invalid payment amount"

    if amount <= 0:
        return "Payment amount must be positive"

    return "Payment processed successfully"


print(process_payment(500))
print(process_payment(None))
print(process_payment(-10))