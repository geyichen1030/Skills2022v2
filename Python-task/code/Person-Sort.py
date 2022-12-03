class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
def person_sort(person_list, sort_key):
    person_list.sort(key=lambda p: getattr(p, sort_key))
    return person_list
if __name__ == '__main__':
    p1 = Person("Michael", "smith", 40)
    p2 = Person("Alice", "Waters", 21)
    p3 = Person("Zone", "Jones", 29)
    p_list = person_sort([p1, p2, p3], "firstname")
    for p in p_list:
        print(getattr(p, "firstname"))
    print()
    p_list = person_sort([p1, p2, p3], "lastname")
    for p in p_list:
        print(getattr(p, "lastname"))
    print()
    p_list = person_sort([p1, p2, p3], "age")
    for p in p_list:
        print(getattr(p, "age"))
    print()