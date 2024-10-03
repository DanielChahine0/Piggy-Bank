n = int(input())
list1 = input().split(" ")
fishy = False
# print(list1)
for i in range(n):
    if list1[i] == "mumble" or str(i + 1) == list1[i]:
        continue
    else:
        fishy = True
if not fishy:
    print("makes sense")
else:
    print("something is fishy")
