domaci_zvirata = ["pes","kočka","králík","had"]
domaci_zvirata_2 = []

for zvire in domaci_zvirata:
    if len(zvire) < 5:
        domaci_zvirata_2.append(zvire)

print("Jména domácích zvířat, která jsou kratší než 5 písmen:", domaci_zvirata_2)
