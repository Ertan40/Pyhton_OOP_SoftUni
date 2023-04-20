# dict = {'cheese': 2, 'tomatoes': 1}
#
# result = []
# for key, value in dict.items():
#     result.append(f"{key}: {value}")
#
# print(', '.join(result))

my_list = ["ertan", "Meryem"]

num = 3
for i in range(len(my_list)):

    if i == num:
        my_list.remove(my_list[i])
        my_list.insert(i, "Ani")
    elif num >= len(my_list):
        raise IndexError("Cannot find comment.")

    # except IndexError:
    #     print("Cannot find comment.")

print(my_list)