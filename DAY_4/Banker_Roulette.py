import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

## Method - 1
random_index = random.randint(0,4)
print(f"The bill will be paid by: {friends[random_index]}")

## Method - 2
print(f"The bill will be paid by: {random.choice(friends)}")