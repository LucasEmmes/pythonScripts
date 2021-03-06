fd = [] # Functional Dependencies
tables = []

class dependency():
    def __init__(self, symbol, choses):
        self.symbol = symbol
        self.choses = choses
        fd.append(self)
        
    def __repr__(self):
        return "".join(self.symbol) + " -> " + "".join(self.choses)

    def derives_to(self, depB):
        for k in depB.symbol:
            if k not in self.choses:
                return False
        return True

    def derives_from(self, attributes):
        for s in self.symbol:
            if s not in attributes:
                return False
        return True

        
class table():
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        tables.append(self)
    def __repr__(self):
        return f"{self.name}"

def derivate_attributes(attributes):
    pot = fd.copy()
    atts = []
    for i in range(len(attributes)):
        atts.append(attributes[i])
    
    while len(pot) > 0:
        t = False
        for dep in pot:
            if dep.derives_from(atts):
                t = True
                atts += dep.choses
                pot.remove(dep)
        if not t:
            break
        
    if len(tables) > 0:
        for a in tables[0].attributes:
            if a not in atts:
                return list(dict.fromkeys(atts))
        return tables[0].name
    
    return list(dict.fromkeys(atts))
                
def remove_spaces(string):
    result = ""
    for c in string:
        if c != " ":
            result += c
    return result

def parse_table(string):
    string = string.split("(")
    name = string[0]
    attributes = string[1][:-1].split(",")
    table(name, attributes)

def parse_dependencies(string):
    string = remove_spaces(string)
    string = string[3:-1]
    dependencies = string.split(";")
    for i in range(len(dependencies)):
        dependencies[i] = dependencies[i].split("->")
        x = []
        y = []
        for j in range(len(dependencies[i][0])):
            x.append(dependencies[i][0][j])
        for j in range(len(dependencies[i][1])):
            y.append(dependencies[i][1][j])
        dependency(x, y)

F = "F = { B -> A; CD -> E; E -> B; A -> C }"
T = "R(A,B,C,D,E)"

parse_dependencies(F)
parse_table(T)


# Coded by Lucas Emmes 03/03/21-05/03/21
# Made this to double-check my test answers
# Chill it's only during home exams and is -technically- allowed
