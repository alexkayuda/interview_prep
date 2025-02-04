# For loops

# How many characters in each word?
words = ['cat', 'window', 'defenestrate']

print("---" * 20)

for i in range(len(words)):
    print(i)

print("---" * 20)

for word in words:
    print(f"{word} has {len(word)} characters")

print("---" * 20)


for i in range(0,100, 5): # from 0 to 100 with a step 5 -> 0, 5, 10
     print(i, end=" ")

print("\n" + "---" * 20)

# Find all active users
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.items():      # user.items()
    # print(f"Processing user {user} with status {status}")
    if status == 'active':
            active_users[user] = status
        
print(active_users)

print("---" * 20)

# In a for loop, the else clause is executed after the loop finishes its final iteration, that is, if no break occurred.
#
# In a while loop, it’s executed after the loop’s condition becomes false.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')