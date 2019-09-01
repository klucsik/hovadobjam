# hovadobjam [![Build Status](https://travis-ci.org/klucsik/hovadobjam.svg?branch=master)](https://travis-ci.org/klucsik/hovadobjam)

Az alkalmazás elsődleges célja választ adni a nagy kérdésre: "Hát ezt meg mégis hova dobjam?"
A szelektív gyűjtés nem olyan egyszerű mint elsőnek tűnik, de az lesz!

A másodlagos cél a tanulás!
* Contious Integration Travissal
* Continoius Deployment Herokuval
* Python programozás fejlesztése: Flask, SQLAlchemy, Pytest

Alkalmazás elérhetősége: https://hovadobjam.herokuapp.com/
Slack szerver: https://hovadobjamdev.slack.com/

Pipeline:
A masterbe küldött pull requesteken a travis futtatja a pytestet (szóval ami nálad terminálban pytest paranccsal lefut, nála is az fog).
A masterbe ekrülő összes push után a heroku deployolja az alkalmazást, az pár percen belül elérhető is lesz.

A bare minimum milestone tartalma:

Grafikai kinézet és user auth nélkül. Egyszerű html formátumban lehessen feltölteni hull_info bejegyzéseket, ezekhez aliasokat. Ezeket lehessen szerkeszteni és lekérni html formmal és apival. Szintén lehessen feltölteni és lekérni hova_dobta bejegyzéseket, lehessen lokációkat megadni irányítószám alapján. Kukak tábla feltöltése 4-5 fajtával. hova-dobjam report lekérdezhető legyen lokáció, anév segítségével. Ebből egyenesen lehessen feltölteni a hova_dobta táblába
