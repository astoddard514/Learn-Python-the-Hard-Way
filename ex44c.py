# Alter Before or After

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # call super with arguments 'Child' and 'self', then call the function 'altered' on whatever it runs.
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# python ex44c.py
# PARENT altered()
# CHILD, BEFORE PARENT altered()
# PARENT altered()
# CHILD, AFTER PARENT altered()