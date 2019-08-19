# hovadobjam [![Build Status](https://travis-ci.org/klucsik/hovadobjam.svg?branch=master)](https://travis-ci.org/klucsik/hovadobjam)

Az alkalmazás elsődleges célja választ adni a nagy kérdésre: "Hát ezt meg mégis hova dobjam?"
A szelektív gyűjtés nem olyan egyszerű mint elsőnek tűnik, de az lesz!

A másodlagos cél a tanulás!
* Contious Integration Travissal
* Continoius Deployment Herokuval
* Python programozás fejlesztése: Flask, SQLAlchemy, Pytest

Alkalmazás elérhetősége: https://hovadobjam.herokuapp.com/

Pipeline:
A masterbe küldött pull requesteken a travis futtatja a pytestet (szóval ami nálad terminálban pytest paranccsal lefut, nála is az fog).
A masterbe ekrülő összes push után a heroku deployolja az alkalmazást, az pár percen belül elérhető is lesz.

