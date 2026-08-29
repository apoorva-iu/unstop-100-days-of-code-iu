# Unstop 100 Days of Code
# Day 5
# Chocolate STore

def process_queries(q, queries):
    # Placeholder function for user logic

    stock = {}

    for query in queries:
        typ = int(query[0])
        name = query[1]
        quantity = int(query[2])

        if typ == 1:
            # Add chocolates
            if name in stock:
                stock[name] += quantity
            else:
                stock[name] = quantity

        else:
            # Sell chocolates
            available = stock.get(name, 0)

            sold = min(available, quantity)

            print(sold)

            stock[name] = available - sold


if __name__ == "__main__":
    q = int(input())
    queries = [input().split() for _ in range(q)]
    process_queries(q, queries)