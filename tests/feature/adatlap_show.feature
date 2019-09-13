Feature: Hulladék bejegyzés megjelenítése, interakciók
  Felhasználóként,
  Szeretném látni a hulladék bejegyzéslapját,
  Hogy el tudjam dönteni hova és hogyan dobjam
  -
  Az adatlapra lépve az egyes szekciókat látom a következő sorrendben:
  Hova dobjam - Az első 3 ajánlott kuka. 
  hogyan dobjam - Az első 3 legnépszerűbb komment
  helyette - Az első 3 legnépszerűbb komment
  -
  Minden szekcióból csak egy részletet látok a legfontosabb információkkal,
  hogy a teljes bejegyzés könnyen áttekinthető legyen, de a egy kattintásra
  a teljes szekciót minden funkcióval el lehet érni.
 
 
Scenario: Hova dobjam szekció megjelenése
  Given Egy hulladék bejegyzéslapján vagyok
  When rákattintok a hovadobjam szekció bővebben funkcióra
  Then megjelenik az összes kuka, a hova dobta gyakoriság szerint rendezve
  
 Scenario: Hogyan dobjam szekció megjelenése
  Given Egy hulladék bejegyzéslapján vagyok
  When rákattintok a hogyan szekció bővebben funkcióra
  Then népszerűség szerint sorbarendezve látom az összes hogyan kommentet
  
 Scenario: Helyette szekció megjelenése
  Given Egy hulladék bejegyzéslapján vagyok
  When rákattintok a helyette szekció bővebben funkcióra
  Then népszerűség szerint sorbarendezve látom az összes helyette kommentet
  
 Scenario: Hova dobta bejegyzés létrehozása 
  Given Egy hulladék bejegyzéslapján vagyok
  And tudom hogy hova dobtam a hulladékot
  When rákattintok a hova dobjam kimutatásban arra a kukára ahová dobtam a hulladékot
  Then létrejön az adatbázisban egy bejegyzés arról hogy hova dobtam a hulladékot
  And az alkalmazás megköszöni hogy kidobtam a hulladékot
  And visszakerülök a kezdő oldalra
 

  
 Scenario: Hogyan dobjam hozzászólás
  Given Egy hulladék bejegyzéslapján vagyok 
  And Bejelentkezett felhasználó vagyok
  When Rá kattintok a hozzászólás funkcióra
  And 
  Then 


 Scenario: 
  Given 
  When 
  Then 

 Scenario: 
  Given 
  When 
  Then 

 Scenario: 
  Given 
  When 
  Then 
