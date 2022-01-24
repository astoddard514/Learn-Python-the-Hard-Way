# Implicit Inheritence

class Parent(object):

    def implicit(self):
        print("PARENT FEATURES/implicit()")

class Child(Parent):
    pass # this Child block is empty, so we can observe that it inherits behavior from the Parent block

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# python ex44.py
# PARENT FEATURES/implicit()
# PARENT FEATURES/implicit()