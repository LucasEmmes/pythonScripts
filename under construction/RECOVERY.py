transactions = []

def get_trans(trans_id):
    global transactions
    for trans in transactions:
        if trans.id == trans_id:
            return trans
    
    return False


def test_recoverable(story):
    has_written = {}
    has_read = {}
    has_commited = []

    is_recoverable = True
    for i in range(len(story)):
        act = story[i]

        # if it wants to commit
        if act.action == "c":
            has_commited.append(act.transaction.id)
            # check who it has read from
            # check that all have commited
            if act.transaction.id in has_read.keys():
                for trans in has_read[act.transaction.id]:
                    if trans not in has_commited:
                        # print(f"UNRECOVERABLE: action number {i} - {act.transaction.id} tries to read {act.value} from {get_trans(id).id} before it has been commited")
                        print(f"UNRECOVERABLE: action number {i} - {act.transaction.id} tried to read from {get_trans(trans).id} before it has been commited")
                        is_recoverable = False

        elif act.action == "w":
            if act.value not in has_written.keys():
                has_written[act.value] = [act.transaction.id]
            else:
                has_written[act.value].append(act.transaction.id)
        
        elif act.action == "r":
            if act.value in has_written.keys():
                if act.transaction.id not in has_read.keys():
                    has_read[act.transaction.id] = []

                for trans in has_written[act.value]:
                    has_read[act.transaction.id].append(trans)
    

    return is_recoverable


def test_aca(story):
    has_commited = []
    has_written = {}
    is_aca = True

    for i in range(len(story)):
        act = story[i]

        if act.action == "r":
            if act.value in has_written.keys():
                for trans in has_written[act.value]:
                    if trans not in has_commited:
                        print(f"NOT ACA - action {i} tried to read from {act.value} before transaction {trans} had commited")
                        is_aca = False
        
        elif act.action == "w":
            if act.value not in has_written.keys():
                has_written[act.value] = [act.transaction.id]
            else:
                has_written[act.value].append(act.transaction.id)
        
        elif act.action == "c":
            has_commited.append(act.transaction.id)

    return is_aca


def test_strict(story):
    has_commited = []
    has_written = {}
    is_strict = True

    for i in range(len(story)):
        act = story[i]

        if act.action == "r":
            if act.value in has_written.keys():
                for trans in has_written[act.value]:
                    if trans not in has_commited:
                        print(f"NOT STRICT - action {i} tried to read from {act.value} before transaction {trans} had commited")
                        is_strict = False
        
        elif act.action == "w":
            if act.value in has_written.keys():
                for trans in has_written[act.value]:
                    if trans not in has_commited:
                        print(f"NOT STRICT - action {i} tried to write to {act.value} before transaction {trans} had commited")
                        is_strict = False

            if act.value not in has_written.keys():
                has_written[act.value] = [act.transaction.id]
            else:
                has_written[act.value].append(act.transaction.id)
        
        elif act.action == "c":
            has_commited.append(act.transaction.id)

    return is_strict

class action:
    def __init__(self, code):
        code = code.lower()
        self.action = code[0]

        t = get_trans(code[1])
        if t:
            self.transaction = t
        else:
            self.transaction = transaction(code[1])
            transactions.append(self.transaction)
        self.value = None

        if self.action != "c":
            self.value = code[3]

class transaction:
    def __init__(self, id):
        self.id = id

def test(story):
    actions = story.split("; ")

    story_array = []

    for act in actions:
        if len(act) > 0:
            a = action(act)
            story_array.append(a)

    #debug
    # for ac in story_array:
    #     print(f"{ac.action}, {ac.transaction.id}, {ac.value}")
    if not test_recoverable(story_array):
        print("NOT RECOVERABLE")
    elif not test_aca(story_array):
        print("RECOVERABLE")
    elif not test_strict(story_array):
        print("ACA")
    else:
        print("STRICT")






# test("w1(X); r2(X); w1(Y); w2(Y); c2;")
#print("-----------------------")
#test("w1(X); r2(X); w1(Y); w2(Y); c1; c2;")
#print("-----------------------")
#test("w1(X); r2(Y); w1(Y); c1; r2(X); c2;")
#print("-----------------------")
#test("w1(X); w2(X); w1(Y); w2(Y); c1; C2;")
#print("-----------------------")
