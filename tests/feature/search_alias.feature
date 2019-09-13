
Feature: Hulladék keresése név alapján
  Regisztrált vagy nem regisztrált felhasználóként,
  Szeretnék rákeresni a hulladékra,
  Hogy megtudjam hova kell kidobni,
  
  Scenario: Keresés névvel.
    Given a Hova Dobjam kezdő oldalán vagyok
    When rákeresek a "krumpli"-ra
    Then a "krumpli" adatlapot jeleníti meg az oldal
    
