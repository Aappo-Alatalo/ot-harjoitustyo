# Ohjelmistotekniikka, harjoitustyö

Aion toteuttaa kurssilla _Osake- ja kryptomarkkina pelin_, jossa pelaaja kisaa **kuukausittain** suurimmasta salkusta yhdessä muiden pelaajien kanssa.

# Dokumentaatio

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)

# Asennus

> [!IMPORTANT]  
> Ohjelma vaatii vähintään Pythonin version 3.10

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

# Muut komentorivitoiminnot

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon ja raporttia voi tarkastella selaimella.
