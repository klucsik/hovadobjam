Feature: 
 
 Scenario: Helyette hozzászólás
  Given Egy hulladék bejegyzéslapjának helyette szekciójában vagyok 
  And Bejelentkezett felhasználó vagyok
  When Rá kattintok a hozzászólás funkcióra
  And Hozzá szólást írok
  And rá kattintok a hozzászolás beküldése funkcióra
  Then a hozzászólás megjelenik a hovadobjam szekcióban
 
