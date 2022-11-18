
f = open("base.txt", "r")
s = f.readlines()
f.close()

base_dict = {}

for i in range(len(s)):
    k = str(s[i].split()[0])
    v = int(s[i].split()[1])
    base_dict[k] = v  # from file to dictionary

print("Our dictionary with names and balances")
print(base_dict)

print("Enter sender's name, recipient's name and transfer amount (Example) Max Vlad 20")
user_input = input("Enter: ")


def bank(user_input):
    u = user_input.split()
    if len(u) == 3:
        user_1 = str(user_input.split()[0])  # sender
        user_2 = str(user_input.split()[1])  # recipient
        amount = int(user_input.split()[2])  # amount

        """Our sender and recipient are in the dictionary 'base_dict' """
        if amount <= base_dict[user_1]:
            if user_1 in base_dict.keys() and user_2 in base_dict.keys():
                base_dict[user_2] += amount  # recipient get his money
                base_dict[user_1] -= amount  # sender gave his money
                f_1 = open('new_data.txt', 'w')
                l = 0

                """ Search for the maximum length key """
                for key, value in base_dict.items():
                    if len(key) > l:
                        l = len(key)

                """ Enter new data to the file 'new_data.txt' """
                for key, value in base_dict.items():
                    f_1.write("User: {0}".format(key) + ' '*(l-len(key)+1) + "| Balance: {0} \n".format(value))

                return base_dict  # new dictionary

            else:
                return "UserDoesNotExist or The"
        else:
            return "There is not enough money on the balance sheet"
    else:
        return "InCorrectInputError"

if __name__ == "__main__":
    print(bank(user_input))