
def calculateElectronicsGST(a, b):
    amount = a + b
    return amount + (amount * 18 / 100)


def calculateFashionGST(c, d):
    amount = c + d
    return amount + (amount * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    return (
        calculateElectronicsGST(a, b)
        + calculateFashionGST(c, d)
        + calculateFoodGST(e)
    )


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


total = totalBill(100, 100, 100, 100, 100)
discount = total * 20 / 100
payable = calculateDiscountedBill(100, 100, 100, 100, 100)

print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {payable:.2f}")
