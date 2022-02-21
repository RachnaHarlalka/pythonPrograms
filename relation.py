def getSet():
    x=set()
    setElementCount = int(input("Enter the cardinality of the set : "))
    for i in range(setElementCount):
        element=int(input("Enter the "+ str(i) + " element : "))
        x.add(element)
    return x

def getRelation(X):
    r=set()
    orderPairCount = int(input("Enter the number of order pairs you will enter in the relation : "))
    # print(setElementCount)
    for i in range(orderPairCount):
        print("Enter the " + str(i) + " ordered pair : ")
        x=int(input("Enter the first element of the pair :"))
        y=int(input("Enter the second element of the pair : "))

        if x in X:
            if y in X:
                r.add((x,y))
        else:
            print("Element you entered does not exists in th given set, please enter properly !")
          
    return r 

def reflexive(X,R):
    for a in X:
        if(a,a) not in R:
            return False

    return True

def irreflexive(X,R):
    for a in X:
        if(a,a) in R:
            return False

    return True

def symmetric(R):
    for element in R:
        a,b = element
        if a != b:
            if (b,a) not in R:
                return False
    return True


def antiSymmetric(R):
    for element in R:
        a,b = element
        if(b,a) in R:
            if a!=b:
                return False
    return True

def transitive(R):
    for element in R:
        a, b = element
        for op in R:
            c, d = op
            if b == c:
                if (a, d) not in R:
                    return False
    return True
            
def equivalence(X,R):
    if reflexive(X,R):
        if symmetric(R):
            if transitive(R):
                return True
    return False

def PartialOrder(X,R):
    if reflexive(X,R):
        if antiSymmetric(R):
            if transitive(R):
                return True
    return False


def main():
    X = set()
    R = set()
    choice = -1
    while choice != 0:
        print("\t.................Main Menu..................\t")
        print("\t1. Enter the set X")
        print("\t2.Enter the relation R on set X")
        print("\t3.Check if reflexive or not reflexive")
        print("\t4.Check if irreflexive")
        print("\t5.Check if symmetric or not symmetric")
        print("\t6.Check if antiSymmetric")
        print("\t7.Check if transitive or not transitive")
        print("\t8.Check if equivalence relation")
        print("\t9.Check if partial order")
        print("\t0.Exit")
        choice = int(input("Enter your option : "))
        if choice == 0:
            exit()
        if choice == 1:
            X=getSet()
        if choice == 2:
            R=getRelation(X)
        if choice == 3:
            status = reflexive(X,R)
            if status == True:
                print("Given Relation is reflexive")
            else:
                print("Given Relation is not reflexive")
        if choice == 4:
            status = irreflexive(X,R)
            if status == True:
                print("Given Relation is irreflexive")
            else:
                print("Given Relation is not irreflexive")
        if choice == 5:
            status = symmetric(R)
            if status == True:
                print("Given Relation is symmetric")
            else:
                print("Given Relation is not symmetric")
        if choice == 6:
            status = antiSymmetric(R)
            if status == True:
                print("Given Relation is antiSymmetric")
            else:
                print("Given Relation is not antiSymmetric")
        if choice == 7:
            status = transitive(R)
            if status == True:
                print("Given Relation is transitive")
            else:
                print("Given Relation is not transitive")
        if choice == 8:
            status = equivalence(X,R)
            if status == True:
                print("Given Relation is equivalence")
            else:
                print("Given Relation is not equivalence")
        if choice == 9:
            status = PartialOrder(X,R)
            if status == True:
                print("Given Relation is PartialOrder")
            else:
                print("Given Relation is not PartialOrder")
        

if __name__=='__main__':
    main()
        

        
