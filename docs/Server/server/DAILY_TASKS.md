# DAILY TASKS (server)

## `daily_task` {: #daily_task }
Funció que s'executa diariament per tal de realitzar els Forecasts i l'optimització.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = daily_task()
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`clean_database_hourly_average`](../../SqlDB/sqlDB/GENERAL.md#clean_database_hourly_average), [`daily_forecast_task`](../../Server/server/DAILY_TASKS.md#daily_forecast_task), [`optimize`](../../Server/server/PÀGINA_OPTIMITZACIÓ.md#optimize), [`update_database`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_database)



---

## `daily_database_clean` {: #daily_database_clean }
Funció que s'executa cada nit per tal de netejar la base de dades. 

Elimina de la base de dades *dades* tots aquells senosrs que tingui guardats però ja no estiguin marcats per a guardar.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = daily_database_clean()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_all_sensors`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_sensors), [`get_data_from_sensor`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_data_from_sensor), [`get_sensor_active`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_sensor_active), [`remove_sensor_data`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#remove_sensor_data)



---

## `daily_forecast_task` {: #daily_forecast_task }
Funció que es crida diariament a la nit per tal de realitzar els forecastings de tots els models guardats.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = daily_forecast_task(today=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `today`: True si es vol fer el forecasting a data d'avui, False en cas que sigui per l'endamà


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`forecast_model`](../../Forecaster/ForecasterManager/General.md#forecast_model)



---

## `certificate_hourly_task` {: #certificate_hourly_task }
Funció que es crida horariament. Envia amb Blockchain el consum i la generació de l'usuari d'aquella hora al sevidor de la comunitat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = certificate_hourly_task()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`clean_database_hourly_average`](../../SqlDB/sqlDB/GENERAL.md#clean_database_hourly_average), [`get_latest_data_from_sensor`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_latest_data_from_sensor), [`get_sensor_active`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_sensor_active), [`update_database`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_database)



---

## `config_optimized_devices_HA` {: #config_optimized_devices_HA }
Configura els dispositius que han estat optimitzats al valor que tocaria cada hora per tal que segueixin el planing de l'optimització.

S'executa cada hora.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = config_optimized_devices_HA()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`controla`](../../Assets/SonnenBattery/General.md#controla), [`optimize`](../../Server/server/PÀGINA_OPTIMITZACIÓ.md#optimize), [`prepare_data_for_optimization`](../../Optimizer/OptimalScheduler/General.md#prepare_data_for_optimization), [`set_sensor_value_HA`](../../SqlDB/sqlDB/SENSORS_-_Home_Asistant.md#set_sensor_value_HA)



---

## `run_threaded` {: #run_threaded }
Executa un thread secundari per no parar el programa en cas de fallada.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
run_threaded(job_func=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `job_func`: -



---

## `run_scheduled_tasks` {: #run_scheduled_tasks }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
run_scheduled_tasks()
```



---

