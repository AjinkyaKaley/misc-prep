
class Employee:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def __lt__(self, other):
        if self.first == other.first:
            return self.last < other.last
        return self.first < other.first

    def __str__(self):
        return self.first + " " + self.last + " " + self.email


class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def __eq__()
class Solution:

    def __init__(self,data):
        self.data = data

    def sortByFirstName(self):
        items = [Employee(item['first'], item['last'], item['email']) for item in self.data]
        ans = sorted(items)
        for i in ans:
            print(i)

people = [
    {'first': 'Barack', 'last': 'Obama', 'email': 'president@whitehouse.gov'},
    {'first': 'Barack', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
    {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.kremlin.ru'}
    ]

sln = Solution(people)
sln.sortByFirstName()
