def double():
    user_num = int(input("enter yur number:"))
    while True:
        result =  user_num*2
        print(result)
        user_num = result
        if result >= 100:
            break
double()
    