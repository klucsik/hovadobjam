Feature: Hulladék bejegyzés megjelenítése, alap adatokkal való interakciók
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
  hogy a teljes bejegyzés könnyen áttekinthető legyen, de egy kattintásra
  a teljes szekciót minden funkcióval el lehet érni.
  Az egyes szekciók külön featureként vannak megfogalmazva.
 
 
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
  
 Scenario: Álnév hozzáadása
  Given Egy hulladék bejegyzéslapján vagyok
  And be jelentkezett felhasználó vagyok
  When álnév hozzá adása funkcióra kattintok
  And megadok egy vagy több új álnevet
  And rá kattintok az álnév be küldése funkcióra
  Then az álnév a hulladékhoz kapcsolódik

 Scenario: Fénykép feltöltése
  Given Egy hulladék bejegyzéslapján vagyok
  And rendelkezek a hulladékomról egy fotóval
  When A Fotó hozzáadása funkcióra kattintok
  And Kiválasztom a feltöltendő fájlt
  And a feltöltésre kattintok
  Then A kép feltöltődik az adatábzisba, a hulladék adatlapjához rendelve
  And Az alkalmazás megköszöni a hozzáadott információt
