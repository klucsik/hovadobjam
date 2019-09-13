
Feature: Hulladék keresése név alapján
  Felhasználóként,
  Szeretnék rákeresni a hulladékra,
  Hogy megtudjam nézni az bejegyzéslapját. 
  
  Scenario: Keresés névvel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "krumpli"-ra
    Then a "krumpli" bejegyzéslapjot jeleníti meg az oldal
    
 Scenario: Keresés névrészlettel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "zacskó"-ra
    Then az összes "zacskó" szót tartalmazó hulladék bejegyzésből alkotott listát jeleníti meg az oldal.
