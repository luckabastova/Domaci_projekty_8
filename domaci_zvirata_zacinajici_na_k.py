domaci_zvirata = ["pes","kočka","králík","had"]
domaci_zvirata_2 = []

for zvire in domaci_zvirata:
    if zvire[0] == "k":
        domaci_zvirata_2.append(zvire)

print("Jména domácích zvířat, která začínají na písmeno k:", domaci_zvirata_2)
