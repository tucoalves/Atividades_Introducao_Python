palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

if sorted(palavra1) == sorted(palavra2):
    print(f'"{palavra1}" e "{palavra2}" são anagramas.')
else:
    print(f'"{palavra1}" e "{palavra2}" não são anagramas.')