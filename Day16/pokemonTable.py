from prettytable import PrettyTable, from_csv

''' 
    First Form Creating the Table
'''
myTable = PrettyTable()
myTable.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
myTable.add_column("Type", ["Electric", "Water", "Fire"])
print(myTable)


''' 
    Second Form Creating the Table
'''
myTable2 = PrettyTable()
myTable2.field_names = ["Pokemon Name" , "Type"]
myTable2.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)
print(myTable2)


''' 
    My Personal Pokemon Database 
'''
with open("C:\\Users\\Usuario\\pokemon.csv") as fp:
    myTable3 = from_csv(fp)
    print(myTable3)