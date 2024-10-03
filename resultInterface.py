import sys
import json
from searchResultHolder import searchResultHolder 

class resultInterface:

    def __init__(self, results: json):
        self.search_result_holder = searchResultHolder()
        self.search_result_holder.add_results(results)

    def display_results(self):
        for result in self.search_result_holder.get_results():
            print(f"{result}\n") #__str__ som brukes her

    def display_detailed_results(self):
        for detailed_result in self.search_result_holder.get_results():
            print(f"{detailed_result.__repr__()}\n") 

    def user_prompt(self):
        print("\nVelg et alternativ:")
        print("\n1. Vis informasjon om alle resultat")
        print("\n2. Vis detaljert informasjon om alle resultat")
        print("\n3. Avslutt")
        return int(input("\nSkriv inn valget ditt: "))


def main():
    results = sys.argv[1]
    interface = resultInterface(results)

    while True:
        choice = interface.user_prompt()
        
        match choice:
            
            case 1:
                interface.display_results()

            case 2:
                interface.display_detailed_results()

            case 3:
                break

if __name__ == "__main__":
    main()