import json
import sys
from typing import Iterable, List
from searchResult import searchResult

class searchResultHolder:
    # en klasse for å holde på resultater, siden vi ofte har mange søkeresultater
    # så virker det lurt å ha noe for å holde på alle disse resultatene
    def __init__(self):
        self.results: List[searchResult] = [] #holder på resultat objekter
    
    def add_results(self, result: Iterable[dict]) -> None:
        #tar inn et hashmap og lager formaterte resultat objekter fra hashmappet
        #og legger det inn i results listen
        for result in self.__get_results(result):
            formatted_result = searchResult(result)
            self.results.append(formatted_result)


    def __get_results(self, results: json) -> Iterable[dict]:
        #tar filen og yielder/"returerer" tilbake noe itererbart
        with open(results, "r") as file:
            data = json.load(file)
        results_iterable = data["results"]#litt hardkodet muligens, enn hvis json filen har noe annet enn "results"
        
        yield from results_iterable
        



#teste litt
def main():
    result_holder = searchResultHolder()
    result_holder.add_results(sys.argv[1])
    for i, result in enumerate(result_holder.results):
        print(f"{i+1}")
        print(result)
        print("\n\n")
    
if __name__ == "__main__":
    main()