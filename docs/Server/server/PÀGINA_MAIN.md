# PÀGINA MAIN (server)

## `get_scheduler_data` {: #get_scheduler_data }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_scheduler_data</small>

Obté les dades de l'optimització del dia actual per tal de generar una gràfica amb Plotly
on mostri el consum general previst per a cada hora segons l'optimització.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_scheduler_data()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

figura Plotly codificada en json.dumps


#### <i class="fa-solid fa-link"></i> Depèn de:
[`optimize`](../../Server/server/PÀGINA_OPTIMITZACIÓ.md#optimize)



---

## `get_global_flexi_data` {: #get_global_flexi_data }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_flexi_data</small>

Obté les dades de la flexibilitat del dia actual per tal de generar una gràfica amb Plotly on mostri
la flexibilitat global disponible per a cada hora.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_global_flexi_data()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

figura Plotly codificada en json.dumps


#### <i class="fa-solid fa-link"></i> Depèn de:
[`optimize`](../../Server/server/PÀGINA_OPTIMITZACIÓ.md#optimize)



---

## `get_device_config_and_state` {: #get_device_config_and_state }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_device_config_and_state/<file_name></small>

Mètode provisional amb únic proposit de debugar l'estat actual de la Sonnen vs el que hauria de fer segons l'optimització


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_device_config_and_state(file_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `file_name`: nom del fitxer de configuració de la Sonnen


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Configuració del dispositiu


#### <i class="fa-solid fa-link"></i> Depèn de:
[`clean_database_hourly_average`](../../SqlDB/sqlDB/GENERAL.md#clean_database_hourly_average), [`get_all_saved_sensors_data`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_saved_sensors_data), [`get_device_config_data`](../../Server/server/PÀGINA_OPTIMITZACIÓ.md#get_device_config_data), [`update_database`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_database)



---

