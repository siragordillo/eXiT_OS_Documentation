# SENSORS - Setters (sqlDB)

### `reset_all_sensors_save` {: #reset_all_sensors_save }
Reinicia el paràmetre *save_sensor* de tots els sensors, posant-lo a 0


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.reset_all_sensors_save()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `update_sensor_active` {: #update_sensor_active }
Actualitza la variable *save_sensor* del sensor indicat


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.update_sensor_active(sensor=..., active=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor`: ID del sensor que es vol modificar
- `active`: nou estat a guardar (Boolean)


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `remove_sensor_data` {: #remove_sensor_data }
Elimina totes les entrades d'un sensor de la taula *dades* de la base de dades


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.remove_sensor_data(sensor_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: ID del sensor que es vol eliminar.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `update_database` {: #update_database }
Actualitza la taula *dades* de la base de dades, posant totes les noves dades dels sensors marcats ocm actius. En cas que s'indiqui un sensor només s'actualitzarà aquest.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.update_database(sensor_to_update=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_to_update`: "all" si es vol actualitzar tota la base de dades, sensor_id en cas que es vulgui actualitzar només un sensor concret


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection), [`get_devices_info`](../../SqlDB/sqlDB/DEVICES.md#get_devices_info), [`get_parent_device_from_sensor_id`](../../SqlDB/sqlDB/DEVICES.md#get_parent_device_from_sensor_id), [`query_select`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#query_select)



---

