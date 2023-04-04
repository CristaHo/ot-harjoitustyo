# Budjettisovellus

Sovellus jolla voit laskea itsellesi budjetin ja pitää kirjaa kuinka budjetissa pysyminen sujuu.

## Dokumentaatio:

- [Vaatimusmäärittely](https://github.com/CristaHo/ot-harjoitustyo/blob/master/dokumentaatio/vatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/CristaHo/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/CristaHo/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

- Kloonaa repositorio komennolla git clone https://github.com/CristaHo/ot-harjoitustyo.git
- Asenna riippuvuudet komennolla poetry install
- Käynnistä sovellus komennolla poetry run invoke start

- HUOM, jos jollakin komennolla tulee ongelmia, kokeile lisätä komennon eteen PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

## Testaus

- Testit saa tehtyä komennolla poetry run invoke test
- Testikattavuusraportin saa generoitua komennolla poetry run invoke coverage-report

