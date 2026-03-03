
steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk

for stad in steden:
    print(stad, end= ', ')

# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple
print('\n---------------')
tuple3= tuple1 + tuple2
print(tuple3)

# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)
gegevens = (3, 'biggetjes', ['hebben', 'een'], 'huis', True)

# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element

print('---------')
print(gegevens[0])
print(gegevens[2:5])
print(gegevens[-1])

# --------------------------------------------------------------------------------------------
print('-----------')

# Maak een tuple met een naam en een leeftijd

persoon = ('Lana', 25)

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)
naam, leeftijd = persoon

# Print de uitgepakte variabelen
print(naam)
print(leeftijd)