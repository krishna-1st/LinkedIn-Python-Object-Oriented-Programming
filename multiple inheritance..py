

# HERE WE WILL BE DEMOSTRATING THE CONCEPT OF MULTIPLE INHERTITANCE AND THE PROBLEM THAT ARISES WHILE INHERITING THE CLASS 



class a :
    def __init__(self,name, title) -> None:
        self.name=name
        self.title=title
        
class b:
    def __init__(self,name,author) -> None:
        self.name=name
        self.author=author
        
        
class c(a,b):
    def __init__(self) -> None:
        
        super().__init__()
        
A=a('abc','krishna')
B=b('qwe','rty')

C=c()

print(C)

