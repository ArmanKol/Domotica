# Domotica
Voor het project moesten we een domotica systeem ontwerpen voor mensen met een lichtversandelijke beperking waarmee je de lampen, camera en de noodknop op afstand kon besturen. Per kamer heb je een camera, lampen en een noodknop. Via de centrale moest gezien kunnen worden of ze aan/uit stonden. Ook moest je via de centrale de lampen, camera of de noodknop kunnen in of uitschakelen.

Het eindproduct is dus de domotica systeem voor mensen met een lichtverstandelijke beperking. We hebben een syseem gemaakt die de lampen, camera en de noodknop per kamer in de gaten houdt. De kameractiviteiten worden in de database opgeslagen en communiceert met de gui. Zo hebben verschillende bewoners hun eigen gegevens in de database staan, maar ook de noodcontactgegevens van die bewoner. In geval van nood is dan mogelijk om die noodcontact te bellen.

We hebben verschillende bestanden in de github staan: guinew, rpi-gpio en rpi-gpio2. rpi-gpio is voor kamer1 en rpi-gpio2 is voor kamer2.

1. map IMG: Is een map waar de foto's voor de gui in staan.

2.guinew (Gemaakt door: Bart, Teun en Arman): Is een programma die op de centrale draait. Een scherm waarop je alle statussen van de verschillende kamers kunt zien. De statussen worden live in de gui ververst. Ook kun je de bewoners per kamer zien en de noodcontactgegevens van die bewoner. Verder kunnen we de laatste kamer activiteiten in de gui zien. Als laatst hebben we nog een functie om personen aan de database toe te voegen of juist te verwijderen. Daarnaast kun je ook bewoners uit de kamer zetten of juist erin.

3.rpi-gpio en rpi-gpio2 (Gemaakt door: Lars en Bart): Dit is een programma die op de raspberry pi draait. Het houdt de kameractiviteiten in de gaten en stuurt vervolgens die informatie door naar de gui.
