

class searchResult:
    # en enkel klasse for å holde på egenskaper til et søkeresultat. et enkelt søkeresultat
    # tilsvarer til et objekt
    #objektet tar inn en dictionary som har egenskapene til det søkeresultatet
    #og fordeler egenskapene funnet inni
    def __init__(self, result: dict):
        #alle egenskapene til et searchResult objekt
        self.id: str
        self.durationInMinutes: float
        self.instructor: str
        self.clubName: str
        self.name: str
        self.bookingInfo: dict
        self.followingBookingCount: int
        self.followingBookings: list
        self.zonedStartTime: dict

        self.__format_result(result)#tar argumentet result og fordeler det ut på instansvariablene våre


    def __format_result(self, unformatted_result: dict) -> None:
        #tar informasjonen fra unformatted_result og fordeler det på instansvariablene
        # til klassen basert på mappingen den får fra __get_mapping 
        mapping = self.__get_mapping()#mapping er en dict

        for key, value in unformatted_result.items():
            if key in mapping:
                setattr(self, mapping[key], value)


    def __get_mapping(self) -> dict:
        #mapping for å gjøre det lettere og mer fleksibelt å tildele egenskaper til klassen
        #hvis json formatet eller objektet endrer seg på noen måte er det lettere å endre
        #mappingen istedenfor en switch case for eksempel.
        return {
            "id": "id",
            "durationInMinutes": "durationInMinutes",
            "instructor": "instructor",
            "clubName": "clubName",
            "name": "name",
            "bookingInfo": "bookingInfo",
            "followingBookingCount": "followingBookingCount",
            "followingBookings": "followingBookings",
            "zonedStartTime": "zonedStartTime",  
        }
    

    def __str__(self):
        #representasjon av objektet på et "uformelt" vis, for bruk og visning til bruker
        return (f"\033[93m{self.name}\033[0m"  #gul for gruppetimenavn og tid
                f"\n\033[93m{self.durationInMinutes} min\033[0m"
                f"{'\n\033[92mBooket\033[0m' if self.bookingInfo['memberBookingInfo']['bookingState'] == 'Booked' else '\n\033[91mBook gruppetime\033[0m'}" #grønn hvis booket, rød hvis ikke booket
                f"\n\033[91m{self.bookingInfo['capacity']-self.bookingInfo['bookedCount']} plasser igjen\033[0m"
                f"\n\033[94m{self.clubName} med {self.instructor.split()[0]}\033[0m")  #blå for sted og instruktør fornavn


    def __repr__(self): 
        #representasjon av objektet på et formelt vis. Viser alt av informasjon. Kan brukes til debugging eller utvikler bruk

        return (f"|----------------Result object:---------------|\n"
                f"id: {self.id}\n"
                f"duration in minutes: {self.durationInMinutes}\n"
                f"instructor: {self.instructor}\n"
                f"club name: {self.clubName}\n"
                f"name: {self.name}\n"
                f"\nbooking info:\n"
                f"\tcapacity: {self.bookingInfo["capacity"]}\n"
                f"\tbooked count: {self.bookingInfo["bookedCount"]}\n"
                f"\twaiting list count: {self.bookingInfo["waitingListCount"]}\n"
                f"\nmember booking info:\n"
                f"\tparticipation id: {self.bookingInfo["memberBookingInfo"]["participationId"]}\n"
                f"\tbooking state: {self.bookingInfo["memberBookingInfo"]["bookingState"]}\n"
                f"\nfollowing booking count: {self.followingBookingCount}\n"
                f"following bookings {self.followingBookings}\n"#dette er en liste, vurdere å repr på en annen måte
                f"\nzoned start time: \n"
                f"\ttime zone: {self.zonedStartTime["timeZone"]}\n"
                f"\tdate time: {self.zonedStartTime["dateTime"]}"
                f"\n|---------------------End---------------------|")
    
    
    