Feature: A kuka lista megjelenítése, sorba állítása, hova dobta létrehozása



 Scenario: Hova dobta bejegyzés létrehozása 
  Given Egy hulladék bejegyzéslapján vagyok
  And tudom hogy hova dobtam a hulladékot
  When rákattintok a hova dobjam szekcióban arra a kukára ahová dobtam a hulladékot
  Then létrejön az adatbázisban egy bejegyzés arról hogy hova dobtam a hulladékot
  And az alkalmazás megköszöni hogy kidobtam a hulladékot
  And visszakerülök a kezdő oldalra
 
