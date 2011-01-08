def flames_count(male_name, female_name):
    male_name_list = list(male_name)
    female_name_list = list(female_name)
    for letter in male_name_list[:]:
        if female_name_list.count(letter) > 0:
            female_name_list.remove(letter)
            male_name_list.remove(letter)
    return len(female_name_list) + len(male_name_list)     
    
def flames_result(count):
    flames_list = ['F','L','A','M','E','S']
    while len(flames_list) > 1:
        remove_count = count
        if count > len(flames_list):
            remove_count = count % len(flames_list)
            if remove_count == 0:
                remove_count = len(flames_list)
        flames_list.remove(flames_list[remove_count - 1])
        flames_list = flames_list[remove_count - 1:] + flames_list[:remove_count - 1]
    return flames_list[0]

def calculate(male_name, female_name):
    count = flames_count(male_name, female_name)
    result = flames_result(count)
    if result == 'F':
        return "Friend"
    elif result == 'L':
        return "Love"
    elif result == 'A':
        return "Angry"
    elif result == 'M':
        return "Marriage"
    elif result == 'E':
        return "Enemy"
    elif result == 'S':
        return "Sister"
        
    

    
