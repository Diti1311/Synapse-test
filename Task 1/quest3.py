def total_spending(request_spending, account_id: str, category:str):
    account = request_spending[account_id]
    for transaction in account["transactions"]:
        if transaction["category"] == category:
            amount = transaction["amount"]
    return amount

def account_balance(request_spending, account_id: str):
    account = request_spending[account_id]
    balance = account["balance"]
    total_amount = 0
    for transaction in account["transactions"]:
        amount = transaction["amount"]
        total_amount += amount
    total_balance = balance + total_amount
    return total_balance

def money_owed(request_spending, account_id: str):
    account = request_spending[account_id]
    money = 0
    for transaction in account["transactions"]:
        if transaction["amount"]< 0:
            money += transaction["amount"]
    return money


request_spending = {
    "Mahek":{
        "balance": 3000.00,
        "transactions":[
            {"amount":-9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category":"Sponsor"},
            {"amount":-2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham":{
        "balance": 5000.00,
        "transactions":[
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "Unnati":{
        "balance": 3500.00,
        "transactions":[
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2000.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang":{
        "balance": 2000.00,
        "transactions":[
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    },
}
account_id = input("Enter the account to check:")
category = input("Enter the category to check:")
total_spent = total_spending(request_spending, account_id, category)
balance = account_balance(request_spending, account_id)
money = money_owed(request_spending, account_id)
print(f'The total amount spent by {account_id} in {category} is {total_spent}')
print('The balance of the given account is: ',balance)
print('The amount of moneny owed is: ',money)
