# Tankegang og prosess for "JSON gruppetime" teknisk oppgave:

### før implementering
- aldri jobbet med json objekt, så må bare finne ut hvilken egenskaper den har og hvordan man behandler det. 
- første tanke gikk til å kanskje dele alt opp og legge det i objekter. Mest med tanke på at det er litt naturlig å lage objekter når man har slike type egenskaper som id, navn, bookinginfo osv.
- begynner også å tenke på hvordan man skal gjøre ting robust og en liten baktanke på sikkerhet, må id være sterkt beskyttet eller ikke? må navn være skjult?
- det ser ut som alle "objektene" jeg kan lage har samme egenskaper, men hvis jeg treffer på noen objekter som plutselig har flere egenskaper hmmmm.
  
### i implementering
- startet med kun en klasse. så splittet det ut til en klasse for å holde på flere resultater, også ha en klasse som bare har egenskapene til et søkeresultat. 
- virket naturlig å holde på resultatene en plass
- underveis tenker jeg på hvor jeg skal formatere ting, i resultat klassen eller resultatholdern.
- i searchResult klassen tenke jeg først på en switch case for å tildele alle verdiene til instansvariablene fra json informasjonen, men tenke at det kanskje blir litt vel lite fleksibelt og som en hardkodet løsning, dritt å endre på i ettertid.
- løsning til dette^^, ha en slags mapping til egenskapene, så legger bare til egenskapene som er i mappingen, så hvis json informasjonen plutselig har noen andre nye egenskaper så kræsjer ikke hele greia. Informasjon blir jo på en måte "borte" da, men da er det mye enklere å vedlikeholde med tanke på man bare trenger å endre på mappingen, og ikke alt annet. Fant ut at python har en setattribute funksjon, sjekket litt hva den gjør og syns den funket fint der. 
- lager en __repr__ metode bare for å representere dataen i et første utkast. mens jeg lager denne tenker jeg at kanskje noe av denne infoen ikke er særlig viktig, og kan kanskje legges i noe "ekstra info" opplegg i et senere brukergrensesnitt
- ser når __repr__ er ferdig at det er kanskje ikke en brukervennlig måte å se resultatene på, men mere en informatikervennlig måte. Kanskje prøve å putte det i et lite brukergrensesnitt som viser enkelt bare hva de forskjellige tingene er. Konseptet å putte det i objekter tror jeg fortsatt er en god ide.
- Lar __repr__ være som den er, kan muligens brukes som debugging verktøy senere. Lagde __str__ som den "endelige" brukervennlige representasjonen. Viser infoen jeg tror er mest nyttig. Etter det var gjort spurte jeg GPT om å legge til grønn, rød/grønn og blå på de forskjellige tingene bare for å skille de litt bedre. 
- Lagde en veldig enkel klasse som kan la deg velge mellom __Str__ og __repr__

