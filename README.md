# Ohjelmistotekniikka, harjoitustyö

Aion toteuttaa kurssilla _Osake- ja kryptomarkkina pelin_, jossa pelaaja kisaa **kuukausittain** suurimmasta salkusta yhdessä muiden pelaajien kanssa.

# Dokumentaatio

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

# Asennus

> [!IMPORTANT]  
> Ohjelma vaatii vähintään Pythonin version 3.10

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Luo ympäristömuuttujatiedostot seuraavasti:

- **`.env`**: Lisää SQLite-tietokantatiedoston nimi (nimet esimerkkejä).

  ```env
  DATABASE_FILENAME=database.sqlite
  ```

- **`.env.test`**: Lisää testitietokantatiedoston nimi (oleellinen vain, jos suoritat testejä).
  ```env
  DATABASE_FILENAME=test-database.sql
  ```

3. Luo tietokanta komennolla:

```bash
poetry run invoke build-db
```

4. Käynnistä sovellus komennolla:

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
