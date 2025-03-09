years = int(input("Enter your age: "))
# DRIVE
if years >= 16:
    can_drive = True
else:
    can_drive = false

if can_drive:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")
# VOTE
if years >= 18:
    can_vote = True
else:
    can_vote = False

if can_vote:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")
    # DRINKING
if years >= 21:
    can_buy_alcohol = True
else:
    can_buy_alcohol = False

if can_buy_alcohol:
    print("You are old enough to buy alcohol.")
else:
    print("You are not old enough to buy alcohol.")
# OLD PPL
if years >= 62:
    eligible_for_senior_discount = True
else:
    eligible_for_senior_discount = False

if eligible_for_senior_discount:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")
