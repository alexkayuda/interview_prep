# For loops

# How many characters in each word?
words = ['cat', 'window', 'defenestrate']

for word in words:
    print(f"{word} has {len(word)} characters")

print("---" * 20)


for i in range(0,100, 5): # from 0 to 100 with a step 5 -> 0, 5, 10
     print(i, end=" ")

print("---" * 20)



print("---" * 20)

# Find all active users
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.items():      # user.items()
    # print(f"Processing user {user} with status {status}")
    if status == 'active':
            active_users[user] = status
        
print(active_users)