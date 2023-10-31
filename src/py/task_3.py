def transform_number(a, b):
    transformations = [a]
    current_number = a

    while current_number < b:
       
        multiplied_number = current_number * 2

        if multiplied_number <= b:
            transformations.append(multiplied_number)
            current_number = multiplied_number
        else:
           
            appended_number = int(str(current_number) + '1')
            transformations.append(appended_number)
            current_number = appended_number

    if current_number == b:
        print("YES")
        print(len(transformations))
        print(*transformations)
    else:
        print("NO")


a, b = map(int, input().split())


transform_number(a, b)
