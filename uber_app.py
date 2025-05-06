 # Uber CLI-applicatie

# Pseudocode:
# 1. Toon een menu met drie Uber-diensten (via een dictionary)
# 2. Vraag de gebruiker of hij zijn voorkeursdienst wil gebruiken of een andere kiezen
# 3. Laat de gebruiker het aantal kilometers invoeren (valideer invoer)
# 4. Bereken de ritkosten
# 5. Toon het resultaat
# 6. Voeg de rit toe aan de geschiedenis
# 7. Geef extra opties in het menu voor het aanpassen van voorkeur en het bekijken van geschiedenis


# 1. Definieer een dictionary met de Uber-diensten en hun prijs per kilometer

UBER_SERVICES = {
    "1": {"name": "Uber Black", "price_per_km": 2.00},
    "2": {"name": "Uber Van", "price_per_km": 3.50},
    "3": {"name": "Uber X", "price_per_km": 1.50}
}
# 2. Maak een USER-dictionary aan om voorkeur en ritgeschiedenis bij te houden
USER = {
    "preference": None,
    "history": []
}
# Functie: get_user_choice()
def get_user_choice():
  
#   - Toon de lijst met Uber-diensten
    
#   - Vraag de gebruiker om een geldige keuze (1, 2 of 3)
   
#   - Valideer invoer met een while-loop
    
    

# Functie: get_distance()
def get_distance():
#   - Vraag het aantal kilometers
#   - Controleer of het een positief getal is
#   - Gebruik try-except voor invoerfouten
    
          

# Functie: calculate_cost(service_key, distance)
def calculate_cost(service_key, distance):
#   - Haal de prijs per km op uit de dictionary
    price = UBER_SERVICES[service_key]["price_per_km"]
#   - Vermenigvuldig met het aantal kilometers
#   - Rond af op 2 decimalen
    return round(price * distance, 2)

# Functie: show_history()
#   - Toon de opgeslagen ritten met service, kilometers en kosten
def show_history():
    if not USER["history"]:
        print("Geen ritgeschiedenis gevonden.")
#   - Als er geen geschiedenis is, meld dat dan
    else:
        print("\n--- Ritgeschiedenis ---")
        for i, ride in enumerate(USER["history"], 1):
            print(f"{i}. {ride['service']} - {ride['km']} km - €{ride['cost']:.2f}")

# Functie: set_preference()
#   - Laat gebruiker een dienst kiezen
def set_preference():
    print("\n--- Stel uw voorkeursdienst in ---")
    choice = get_user_choice()
#   - Sla deze op in USER['preference']
    USER["preference"] = choice
    print(f"Voorkeursdienst ingesteld op: {UBER_SERVICES[choice]['name']}")

# Functie: main_menu()
#   - Toon hoofdmenu: rit boeken, voorkeur instellen, geschiedenis bekijken, afsluiten
def main_menu():
    while True:
        print("\n--- Uber CLI Applicatie ---")
        print("1. Boek een rit")
        print("2. Stel voorkeursdienst in")
        print("3. Bekijk ritgeschiedenis")
        print("4. Afsluiten")
        optie = input("Kies een optie: ").strip()
#   - Bij rit boeken:
#       - Vraag of voorkeur gebruikt moet worden
#       - Vraag anders opnieuw naar keuze
#       - Vraag om kilometers
#       - Bereken en toon kosten
#       - Sla rit op in geschiedenis
#   - Bij optie 2: voorkeur instellen
#   - Bij optie 3: ritgeschiedenis tonen
#   - Bij optie 4: programma afsluiten
        if optie == "1":
            if USER["preference"]:
                use_pref = input(f"Wilt u uw voorkeursdienst ({UBER_SERVICES[USER['preference']]['name']}) gebruiken? (j/n): ").strip().lower()
                if use_pref == 'j':
                    service_choice = USER["preference"]
                else:
                    service_choice = get_user_choice()
            else:
                service_choice = get_user_choice()

            km = get_distance()
            cost = calculate_cost(service_choice, km)
            print(f"U heeft gekozen voor {UBER_SERVICES[service_choice]['name']}. De kosten voor uw rit van {km} kilometer(s) zijn €{cost:.2f}.")

            USER["history"].append({
                "service": UBER_SERVICES[service_choice]['name'],
                "km": km,
                "cost": cost
            })

        elif optie == "2":
            set_preference()

        elif optie == "3":
            show_history()

        elif optie == "4":
            print("Bedankt voor het gebruiken van Uber CLI!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

# Start de applicatie alleen als dit script direct wordt uitgevoerd
if __name__ == "__main__":
    main_menu()


# Start main_menu() als script direct wordt uitgevoerd

