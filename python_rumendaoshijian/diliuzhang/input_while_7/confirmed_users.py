unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verifying user:"+current_user.title())
    confirmed_users.append(current_user)
print("\n the following users have been confiremd:")
for confirmed_users in confirmed_users:
    print(confirmed_users)