"""
If we do not know the number of arguments we pass to our function,
we can create a function which can take arbitrary number of arguments by adding * before the parameter name
"""


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob')


