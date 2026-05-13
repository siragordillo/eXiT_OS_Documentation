# DEFINICIÓ EINES LLM (server)

## `tool_get_current_time` {: #tool_get_current_time }
Retorna l'hora actual del servidor


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_current_time()
```



---

## `tool_get_current_day` {: #tool_get_current_day }
Retorna la data actual (dia, mes i any)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_current_day()
```



---

## `tool_get_current_year` {: #tool_get_current_year }
Retorna l'any actual


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_current_year()
```



---

## `tool_get_sensor_value` {: #tool_get_sensor_value }
Retorna l'últim valor conegut d'un sensor específic


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_sensor_value(sensor_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `sensor_id`: -


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_current_sensor_state`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_current_sensor_state), [`get_latest_data_from_sensor`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_latest_data_from_sensor)



---

## `tool_get_optimization_configs` {: #tool_get_optimization_configs }
Retorna totes les configuracions d'optimització guardades per l'usuari


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_optimization_configs(config_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `config_name`: -



---

## `tool_get_available_device_types` {: #tool_get_available_device_types }
Retorna tots els tipus de dispositius disponibles per configurar a l'optimitzador, amb les seves restriccions i variables


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_available_device_types(device_type_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `device_type_id`: -



---

## `tool_get_system_entities` {: #tool_get_system_entities }
Retorna la llista de dispositius i entitats (sensors/actuadors) reals del sistema.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = tool_get_system_entities(query=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `query`: -


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_devices_info`](../../SqlDB/sqlDB/DEVICES.md#get_devices_info)



---

