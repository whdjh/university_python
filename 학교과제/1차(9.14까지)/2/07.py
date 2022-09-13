def zip_strings(str1, str2, str3):
    if len(str1) == len(str2):
        list_str3 = list(str3)
        list_str1 = list(str1)
        list_str2 = list(str2)
        odd_str3 = list_str3[1::2]
        even_str3 = list_str3[0::2]
        if odd_str3 == list_str1 and even_str3 == list_str2:
            result = True
        elif even_str3 == list_str1 and odd_str3 == list_str2:
            result = True
        else:
            result = False
    
    else:
        if len(str1) > len(str2):
            list_str3 = list(str3)
            list_str1 = list(str1)
            list_str2 = list(str2)
            even_str3 = list_str3[1:(len(str2) * 2) + 1:2]
            odd_str3 = list_str3[0:(len(str2) * 2) + 1:2] + list_str3[(len(str2) * 2) + 1:]
            print(even_str3)
            print(odd_str3)
            if odd_str3 == list_str1 and even_str3 == list_str2:
                result = True
            elif even_str3 == list_str1 and odd_str3 == list_str2:
                result = True
            else:
                result = False
        else:
            list_str3 = list(str3)
            list_str1 = list(str1)
            list_str2 = list(str2)
            even_str3 = list_str3[1:(len(str1) * 2) + 1:2]
            odd_str3 = list_str3[0:(len(str1) * 2) + 1:2] + list_str3[(len(str1) * 2) + 1:]
            print(odd_str3)
            print(even_str3)
            if odd_str3 == list_str1 and even_str3 == list_str2:
                result = True
            elif even_str3 == list_str1 and odd_str3 == list_str2:
                result = True
            else:
                result = False
    return result
print(zip_strings(str1, str2, str3))