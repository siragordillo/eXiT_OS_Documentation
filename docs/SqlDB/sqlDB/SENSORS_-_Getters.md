# SENSORS - Getters (sqlDB)

### `get_all_sensors` {: #get_all_sensors }
Obté una llista amb el ID i Friendly Name de tots els sensors


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_all_sensors()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
[[ID, FriendlyName], [ID, FriendlyName], ...]
```

- **None** si no troba l'API



---

### `get_current_sensor_state` {: #get_current_sensor_state }
Obté l'estat actual del sensor indicat (valor actual)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_current_sensor_state(sensor_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: ID del sensor que volem obtenir


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Valor actual del sensor que marca l'API



---

### `get_all_sensors_data` {: #get_all_sensors_data }
Obté informació de tots els devices i entitats guardats a la base de dades.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_all_sensors_data()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{"device_name": ,"entities": {{"entity_id","entity_name","save","type"},...}}
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_data_from_sensor` {: #get_data_from_sensor }
Obté tots els valors guardats del sensor indicat juntament amb el seu timestamp, ordenats per Timestamp.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_data_from_sensor(sensor_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: ID del sensor del qual es volen obtenir les dades


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Pandas DataFrame

```python
[timestamp, value]
```

- *Exemple de Valors*: [2025-11-24 03:00:00+00:00, 621.06893]


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_all_saved_sensors_data` {: #get_all_saved_sensors_data }
Obté totes les dades guardades dins un rang de dades per tots els sensors indicats.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_all_saved_sensors_data(sensors_saved=..., start_date=..., end_date=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensors_saved`: ID dels sensors dels quals es volen obtenir les dades
- `start_date`: Data d'inici de les dades
- `end_date`: Data final per a les dades


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb les dades per a cada sensor

```python
{ ID_sensor_1: [(timestamp, value), (timestamp,value)], ID_sensor_2: ... }
```

- *Exemple de Valors*: ('2026-04-22T12:00:00', 2727.2727272727275)


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_all_saved_sensors_id` {: #get_all_saved_sensors_id }
Obté el ID de tots els sensors marcats per a guardar.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_all_saved_sensors_id(kw=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `kw`: Si és true, retorna només aquells sensors que usen KW com a unitat de mesura. En cas que no s'indiqui és False, mostrarà tots els ID guardats


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
['ID_sensor1', 'ID_sensor2']
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_sensor_active` {: #get_sensor_active }
Obté 0 o 1 segons si el sensor indicat es troba actiu o no (és a dir que està marcat per a guardar dades)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_sensor_active(sensor=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor`: ID del sensor a obtenir


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

0 si no està actiu, 1 en cas contrari

```python
(actiu = guarda dades)
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_latest_data_from_sensor` {: #get_latest_data_from_sensor }
Obté l'última dada guardada, juntament amb el timestamp, del sensor indicat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_latest_data_from_sensor(sensor_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: ID del sensor del qual es vol obtenir la dada.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
('timestamp', 'value')
```

- *Exemple de Valors*: ('2026-04-29T07:00:00', 411.07975460122697)


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

