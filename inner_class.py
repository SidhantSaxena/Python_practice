class University:
    name = 'Geetanjali University'
    def __init__(self):
        print('University Created !!!')

    class Department:
        dept_name = 'Computer Science !! '

        def __init__(self):
            print('Computer Science !!! ')

    class Sport:
        sport_name = "football"
        print(University.Department.dept_name)         






u = University()
d = u.Department()
s = u.Sport()