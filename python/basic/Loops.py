# for i in range(5):  # 0 to 4
#     print(i, end=" ")  # 0 1 2 3 4


# count = 0
# while count < 3:
#     print("Count:", count)
#     count += 1


for i in range(10):
    if i == 5:
        break    # Stops at 5
    if i % 2 == 0:
        continue # Skips even numbers
    print(i)     # 1 3