Feature: Hulladék bejegyzés létrehozása
Felhasználóként, ha még nincs az általam keresett hulladék az adatbázisban,
Szeretném felvinni.

Scenario: Új bejegyzés létrehozása sikertelen keresés esetén
Given A kezdőoldalon vagyok
And rákeresek egy olyan névre amire nincs találat az adatbázisban
When az alkalmazás üres találati listával térne vissza
Then hozzon létre egy üres bejegyzést, az általam megadott névvel

Scenario: Új bejegyzés létrehozása sikeres keresés esetén
Given A kezdőoldalon vagyok
And rákeresek egy olyan névre melyre vannak találatok (de ezek nem a nekem megfelelőek)
When rákattintok az új bejegyzés létrehozása funkcióra
Then Az alkalmazás létrehoz egy üres bejegyzést az általam megadott névvel
