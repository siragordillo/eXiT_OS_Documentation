# GENERAL (sqlDB)

### `vacuum` {: #vacuum }
Allibera l'espai no utilitzat i reconstrueix el fitxer de la base de dades.

Aquest mètode executa la comanda VACUUM per defragmentar la base de dades, reduir-ne la mida al disc i optimitzar el rendiment de les consultes futures.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.vacuum()
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `clean_database_hourly_average` {: #clean_database_hourly_average }
Agrupa i compacta les dades històriques (últims 21 dies) per hores.
Calcula la mitjana aritmètica per a valors numèrics o la moda per a valors de text, substituint els registres originals per un únic resum horari per optimitzar l'espai.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.clean_database_hourly_average(sensor_id=..., all_sensors=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: Identificador del sensor si es processa de forma individual.
- `all_sensors`: Si és True, ignora sensor_id i processa tota la base de dades.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection), [`vacuum`](../../SqlDB/sqlDB/GENERAL.md#vacuum)



---

### `get_lat_long` {: #get_lat_long }
Obté les coordenades geogràfiques de la configuració de Home Assistant.

Realitza una petició a l'endpoint de configuració i n'extreu la latitud i la longitud.
En cas d'error o de no trobar les claus necessàries, registra la incidència.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_lat_long()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla "latitude, longitude" si té èxit, un enter -1 si no troba les columnes, o un string amb el missatge d'error en cas d'excepció.



---

