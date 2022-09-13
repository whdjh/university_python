def phone_book(name, phone):
    if len(name) == 2 or len(name) == 3 or len(name) == 4:
        name = list(name)
        name[1] = '*'
        result = ''.join(s for s in name)

    for i in phone:
        if i == '-':
            if len(phone) == 11:
                phone = phone[6:11]
            if len(phone) == 12:
                phone = (phone[8:12])
            if len(phone) == 13:
                phone = phone[9:13]
        if i == '.':
            if len(phone) == 11:
                phone = phone[6:11]
            if len(phone) == 12:
                phone = phone[8:12]
            if len(phone) == 13:
                phone = phone[9:13]
        if len(phone) == 10:
            phone = phone[6:10]
        if len(phone) == 11:
            phone = phone[7:11]
        if len(phone) == 12:
            phone = phone[8:12]
    return (result, int(phone))

print(phone_book(name, phone))

assert phone_book('강현', '01012345678') == ('강*', 5678)