input_name = input("Enter your product name:")
key = len(input_name) + 0xCA 
key = key ^ 0x3D8D40F
print(key)
input()