def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('cyril','guo')
print(musician)

def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician2 = build_person('cyril','guo','26')
print(musician2)