import faker

fake = faker.Faker()


transactions = []
for _ in range(10):
    transaction = {
        "transaction_id": fake.uuid4().replace("-", ""),
        "transaction_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "amount": round(fake.random_int(min=100, max=5000, step=1) / 100, 2)
    }
    transactions.append(transaction)


for transaction in transactions:
    print(f"Transaction ID: {transaction['transaction_id']}, Date: {transaction['transaction_date']}, Amount: {transaction['amount']}")