dna = input()
veikur = False
for i in range (len(dna)):
    if dna[i] == 'C' and i < len(dna)-2:
        if dna[i+1] == 'O':
            if dna[i+2] == 'V':
                veikur = True
                print("Veikur!")
                break
if veikur == False:
    print("Ekki veikur!")