# General (ForecasterManager)

## `get_meteodata` {: #get_meteodata }
Consulta i combina la previsió meteorològica d'Open-Meteo amb l'històric existent.

Realitza una petició a l'API per obtenir múltiples variables horàries des d'avui
fins al nombre de dies especificat, i les concatena amb un DataFrame d'arxiu.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_meteodata(
    latitude=...,
    longitude=...,
    archive_meteo=...,
    days_foreward=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `latitude`: Latitud per a la consulta meteorològica.
- `longitude`: Longitud per a la consulta meteorològica.
- `archive_meteo`: DataFrame amb dades meteorològiques prèvies o None.
- `days_foreward`: Nombre de dies de previsió a recuperar a partir d'avui.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

DataFrame fusionat amb les dades històriques i la nova previsió.
pd.DataFrame

```python
({
        "timestamp": [datetime, ...],
        "temperature_2m": [float, ...],
        "relativehumidity_2m": [int, ...],
        "cloudcover": [int, ...],
        "windspeed_10m": [float, ...] 
    })
```



---

## `predict_consumption_production` {: #predict_consumption_production }
Genera una predicció de consum o producció energètica utilitzant un model entrenat.

Carrega la configuració del model, recupera les dades actualitzades dels sensors
pertinents i de l'API meteorològica (si s'escau), i executa el pronòstic per a
les properes 48 hores.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = predict_consumption_production(model_name=..., database=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `model_name`: Nom del fitxer del model a carregar.
- `database`: Instància de la base de dades per recuperar les dades recents.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla que conté la predicció, els valors reals ,si n'hi ha, i l'ID del sensor.

```python
( pd.Series([float, ...], index=[datetime, ...]), pd.Series([float, ...], index=[datetime, ...]), str )
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`Forecaster`](../../Forecaster/Forecaster/General.md#Forecaster), [`forecast`](../../Forecaster/Forecaster/General.md#forecast), [`get_data_from_sensor`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_data_from_sensor), [`get_meteodata`](../../Forecaster/ForecasterManager/General.md#get_meteodata), [`load_model`](../../Forecaster/Forecaster/General.md#load_model), [`prepare_dataframes`](../../Forecaster/Forecaster/General.md#prepare_dataframes)



---

## `train_model` {: #train_model }
Configura, processa les dades i entrena un nou model de predicció.

Extrau els paràmetres del formulari, gestiona la finestra temporal (windowing),
recupera les dades històriques dels sensors (principal i addicionals) i de
l'API meteorològica, per finalment delegar la creació del model a l'objecte forecaster.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = train_model(
    form_data=...,
    database=...,
    forecaster=...,
    lat=...,
    lon=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `form_data`: Diccionari amb les claus i valors del formulari de la interfície.
- `database`: Instància de la base de dades per obtenir l'històric de sensors.
- `forecaster`: Instància del motor de predicció per entrenar el model.
- `lat`: Latitud per a la integració de dades meteorològiques.
- `lon`: Longitud per a la integració de dades meteorològiques.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

El nom del model creat que s'ha utilitzat per desar el fitxer.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`create_model`](../../Forecaster/Forecaster/General.md#create_model), [`get_data_from_sensor`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_data_from_sensor)



---

## `forecast_model` {: #forecast_model }
Executa la predicció d'un model específic i emmagatzema els resultats a la base de dades.

Crida la funció de predicció per obtenir els valors estimats i reals, filtra les
dades per mantenir només els últims 14 dies (més la previsió futura) i desa el
conjunt resultant amb la marca de temps de l'execució.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
forecast_model(
    selected_forecast=...,
    database=...,
    models_filepath=...,
    today=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `selected_forecast`: Nom del fitxer del model (.pkl) a utilitzar.
- `database`: Instància de la base de dades on es guardaran els resultats.
- `models_filepath`: Ruta on s'allotgen els fitxers dels models.
- `today`: Booleà que defineix si la data objectiu és avui o demà.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`predict_consumption_production`](../../Forecaster/ForecasterManager/General.md#predict_consumption_production), [`save_forecast`](../../SqlDB/sqlDB/FORECASTS.md#save_forecast)



---

## `delete_model` {: #delete_model }
Elimina un model del sistema, tant de la base de dades com del disc físic.

Esborra totes les dades de predicció associades al model a la base de dades i,
posteriorment, elimina el fitxer binari (.pkl) de la carpeta de magatzem.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
delete_model(model_name=..., database=..., models_filepath=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `model_name`: Nom del fitxer del model a eliminar (incloent l'extensió).
- `database`: Instància de la base de dades per executar la neteja de registres.
- `models_filepath`: Ruta arrel on s'ubiquen els fitxers de predicció.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`remove_forecast`](../../SqlDB/sqlDB/FORECASTS.md#remove_forecast)



---

