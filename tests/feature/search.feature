
Feature: Hulladék keresése név alapján
  Felhasználóként,
  Szeretnék rákeresni a hulladékra,
  Hogy megtudjam nézni az bejegyzéslapját. 
  
  Scenario: Keresés álnévvel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "krumpli"-ra
    Then a "burgonya" bejegyzéslapjot jeleníti meg az oldal
    
 Scenario: Keresés névrészlettel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "zacskó"-ra
    Then az összes "zacskó" szót tartalmazó hulladék bejegyzésből alkotott listát jeleníti meg az oldal.

  Scenario: Keresés névvel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "burgonya"-ra
    Then a "burgonya" bejegyzéslapjot jeleníti meg az oldal
  
  Scenario: Nem létező név/álnév keresése.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "ilyenmincs"-re
    Then Bejegyzés nem található hibaüzenetet ad az oldal
    And Az új bejegyzés létrehozás oldal jelenik meg. 
   