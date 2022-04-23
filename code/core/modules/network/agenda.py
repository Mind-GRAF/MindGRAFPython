import enum


class agenda(enum.Enum):
    start = 1
    find_plan = 2
    find_preconditions = 3
    test_precondition = 4
    find_effects = 5
    execute = 6
    done = 7