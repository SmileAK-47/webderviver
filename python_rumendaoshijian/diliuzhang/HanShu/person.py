'''

def build_person(first_name,last_name):
    person = {'farst':first_name,'last':last_name}
    return person
musician = build_person('jimi','lll')
print(musician)
'''
def build_person(first_name,last_name,age =''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']= age
    return person
musician = build_person('jimi','hendirx',age =27)
print(musician)