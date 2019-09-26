 Feature: Hogyan dobjam információk megjelenítése
 Felhasználóként szeretném tudni hogy mit tegyek a hulladékkal mielőtt a kukába teszem,
 ha már tudom szeretném ezt az infromációt átadni a többi felhasználónak.
 
 Scenario: Hogyan dobjam hozzászólás
  Given Egy hulladék bejegyzéslapján a hogyan dobjam szekcióban vagyok vagyok 
  And Bejelentkezett felhasználó vagyok
  When Rá kattintok a hozzászólás funkcióra
  And Hozzá szólást írok
  And rá kattintok a hozzászolás beküldése funkcióra
  Then a hozzászólás megjelenik a hogyan dobjam szekcióban
 
