class TestCase:
    functions=[]
    name=""
    def __add__(self, other):
        self.functions.append(other)
    def get_functions(self):
        return  self.functions

class Functions:

    functionName=""
    packageName=""
    def __init__(self,fname,packageName,pre,post):
        self.functionName=fname
        self.packageName=packageName
        self.precondition=pre
        self.postcondition=post

    def add_precondition(self, other):
        self.precondition.append(other)

    def add_postcondition(self, other):
        self.postcondition.append(other)

    def get_precondition(self):
        return self.precondition

    def get_postcondition(self):
        return self.postcondition

class ProgramInvariant:
        invariant=[]

        def add_invariant(self, other):
            self.invariant.append(other)
