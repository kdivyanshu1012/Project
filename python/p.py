# a = input("data1: ").split(",")
# b = input("data2: ").split(",")
# f,l = '{','}'
# result=""
# if(len(a) == len(b)):
#     z = 0
#     for i in a:
#         for j in range(z,z+2):
#             k = b[j]
#             result = result+ "'" + i + "'"+":"+"'"+k +"'"
#             if z < len(a) -1:
#                 result += ","
#             break
#         z = z+1
#     result = f + result + l
#     print(result)
# else:
#     print("Lists are different lengths")
a = input("data1: ").split(",")
b = input("data2: ").split(",")
result = {}

if len(a) == len(b):
    for i in range(len(a)):
        result[a[i]] = b[i]

    print(result)
else:
    print("Lists are different lengths")
