class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("이름:", self.name)
        print("급여:", self.salary)


class Manager:
    def __init__(self):
        self.team_members = []

    def add_team_member(self, employee):
        self.team_members.append(employee)

    def display_team(self):
        print("팀원 목록:")
        for member in self.team_members:
            member.display_info()



manager = Manager()

employee1 = Employee("김철수", 5000)
employee2 = Employee("이영희", 7000)
employee3 = Employee("박지민", 6000)

manager.add_team_member(employee1)
manager.add_team_member(employee2)
manager.add_team_member(employee3)


manager.display_team()