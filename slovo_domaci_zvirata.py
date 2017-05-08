domaci_zvirata = ["pes","kočka","králík","had"]
slovo=input("Napiš_slovo:")

if slovo in domaci_zvirata:
    print(slovo," se nachází v seznamu domácích zvířat.")
else:
    print(slovo," se nenachází v seznamu domácích zvířat.")
