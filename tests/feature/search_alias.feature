
Feature: Hulladék keresése név alapján
  Regisztrált vagy nem regisztrált felhasználóként,
  Szeretnék rákeresni a hulladékra,
  Hogy megtudjam hova kell kidobni,
  
  Scenario: Keresés névvel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "krumpli"-ra
    Then a "krumpli" adatlapot jeleníti meg az oldal
    
 Scenario: Keresés névrészlettel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "zacskó"-ra
    Then az összes "zacskó" szót tartalmazó hulladék bejegyzésből alkotott listát jeleníti meg az oldal.
