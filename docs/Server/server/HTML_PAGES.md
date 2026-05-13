# HTML PAGES (server)

## `get_init` {: #get_init }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /</small>

Obté la pàgina inicial del programa (main.html) i la retorna en format *template* juntament amb la llista de sensors actius.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_init()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Retorna la pàgina inicial del programa en format *template*


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_forecasts_name`](../../SqlDB/sqlDB/FORECASTS.md#get_forecasts_name)



---

## `sensors_page` {: #sensors_page }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /sensors</small>

Obté la pàgina HTML sensors.html


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = sensors_page()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

pàgina sensors.html en format template



---

## `database_graph_page` {: #database_graph_page }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /databaseView</small>

Obté tots els sensors guardats (ID) i prepara la *template* de graphs.html amb aquesta informació


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = database_graph_page()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Retorna la pàgina graphs.html en format *template*.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_all_saved_sensors_id`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_saved_sensors_id)



---

## `create_model_page` {: #create_model_page }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /model</small>

Prepara el *template* per a la pàgina model.html obtenint diferents dades que necessita la pàgina per a funcionar:

- **sensors_input**: llista de ID de tots els sensors guardats.

- **models_input**: llista de tots els models guardats en format .pkl a la carpeta forecastings del programa.

- **forecasts_id**: llista de ID dels forecasts guardats a la base de dades.

- **active_model**: nom del model actiu a la pàgina de model.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = create_model_page(active_model=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `active_model`: model de forecasting actiu a la pàgina model.html


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

pàgina model.html en format *template* juntament amb sensors_id, els models guardats,
els id dels forecastings guardats i el model actiu.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_all_saved_sensors_id`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_saved_sensors_id), [`get_forecasts_name`](../../SqlDB/sqlDB/FORECASTS.md#get_forecasts_name)



---

## `config_page` {: #config_page }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /config_page</small>

Prepara el template per a la pàgina config.html obtenint diferents dades que necessita la pàgina per a funcionar:

- **Sensors**: Llista de ID dels sensors guardats a la base de dades.

- **Location**: Diccionari amb Latitut i Longitud de l'ubicació del Home Asistant.

- **User_data**: Configuració guardada de l'usuari.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = config_page()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Pàgina config_page.html en format *template*.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_all_saved_sensors_id`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_saved_sensors_id), [`get_user_configuration_data`](../../Server/server/PÀGINA_CONFIGURACIÓ.md#get_user_configuration_data)



---

## `optimization_page` {: #optimization_page }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /optimization</small>

Prepara el *template* per a la pàgina optimization.html obtenint diferents dades que necessita la pàgina per a funcionar:

- **Current_date**: data actual en format 'd-m-Y'

- **Device_entities**: Informació sobre els dispositius i entitats filles que conté Home Asistant vinculats.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = optimization_page()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Pàgina optimization_page.html en format *template*.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_devices_info`](../../SqlDB/sqlDB/DEVICES.md#get_devices_info)



---

