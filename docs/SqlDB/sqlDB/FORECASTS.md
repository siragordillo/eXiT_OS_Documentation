# FORECASTS (sqlDB)

### `get_forecasts_name` {: #get_forecasts_name }
Obté el nom de tots els forecastings guardats a la base de dades.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_forecasts_name()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
[('forecasting1',), ('forecasting2',)]
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_data_from_forecast_from_date` {: #get_data_from_forecast_from_date }
Obté les dades (temps de realització del forecast, temps predit, valor predit i valor real) del forecast indicat per a la data desitjada.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_data_from_forecast_from_date(forecast_id=..., date=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `forecast_id`: ID del forecast del qual es volen obtenir les dades.
- `date`: Data de la qual es volen obtenir les dades ('%d-%m-%Y')


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Data Frame

```python
['run_date', 'timestamp', 'value', 'real_value']
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `get_data_from_forecast_from_date_and_sensorID` {: #get_data_from_forecast_from_date_and_sensorID }
Obté el forecast realitzat per a un sensor concret en la data indicada.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_data_from_forecast_from_date_and_sensorID(sensor_id=..., date=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: ID del sensor del qual es volen trobar forecastings
- `date`: Data sobre la qual es vol trobar forecasting


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Data Frame

```python
['run_date', 'timestmap', 'value', 'real_value']
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `remove_forecast` {: #remove_forecast }
Elimina el forecasting amb ID indicat de la base de dades, eliminant totes les entrades amb aquell ID


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.remove_forecast(forecast_id=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `forecast_id`: ID del forecast que es vol eliminar.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

### `save_forecast` {: #save_forecast }
Guarda el forecasting realitzat a la base de daes. En cas que existeixi un forecasting realitzat a la mateixa data el substitueix eliminant l'antic.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.save_forecast(data=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: dades del forecating, han d'incloure (forecast_name, sensor_forecasted, forecast_run_time, forecasted_time,
predicted_value, real_value)


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_connection`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#_get_connection)



---

