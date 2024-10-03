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
        for result in self.__retrive_results(result):
            formatted_result = searchResult(result)
            self.results.append(formatted_result)


    def __retrive_results(self, results: json) -> Iterable[dict]:
        #tar filen og yielder/"returerer" tilbake noe itererbart
        with open(results, "r") as file:
            data = json.load(file)
        results_iterable = data["results"]#litt hardkodet muligens, enn hvis json filen har noe annet enn "results"
        
        yield from results_iterable


    def get_results(self) -> Iterable[searchResult]:
        yield from self.results

