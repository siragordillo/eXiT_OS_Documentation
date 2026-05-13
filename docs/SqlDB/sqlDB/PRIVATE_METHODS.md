# PRIVATE METHODS (sqlDB)

### `__init__` {: #__init__ }
Constructor de la classe SqlDB. 

Inicialitza les variables necessàries de la classe i crea la Base de dades en cas que aquesta no existeixi.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__init__()
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_init_db`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_init_db), [`get_devices_info`](../../SqlDB/sqlDB/DEVICES.md#get_devices_info)



---

### `_init_db` {: #_init_db }
Crea les taules de la base de dades 

- DADES: conté els valors i timestamps de les dades 

- SENSORS: conté la info dels sensors
- FORECASTS: conté les dades i timestamps de les prediccions realitzades per a cada model


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj._init_db()
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`clean_database_hourly_average`](../../SqlDB/sqlDB/GENERAL.md#clean_database_hourly_average), [`update_database`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_database)



---

### `_get_connection` {: #_get_connection }
Crea una connexió amb la base de dades indicada a la varaible *self.database_file*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj._get_connection()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Connexió amb la base de dades



---

### `self_destruct` {: #self_destruct }
Elimina completament tota la base de dades


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.self_destruct()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_init_db`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_init_db)



---

### `query_select` {: #query_select }
Executa un query SQL bàsic a la base de dades


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.query_select(
    table=...,
    column=...,
    sensor_id=...,
    con=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `table`: nom de la taula a la que es vol accedir
- `column`: nom de la columna a la qual es col accedir
- `sensor_id`: nom del sensor concret que es vol buscar
- `con`: connexió amb la base de dades creada


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

