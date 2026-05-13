# General (Forecaster)

### `__init__` {: #__init__ }
Inicialitza una nova instància de la classe Forecaster i configura l'entorn de treball.

Estableix les rutes dels fitxers de configuració i el directori de magatzem dels models
en funció de si l'execució es realitza dins d'un entorn Hass.io o en local. També
inicialitza el diccionari de metadades de la base de dades i el mòdul de mètriques.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__init__(debug=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `debug`: Booleà per activar o desactivar els missatges de depuració.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`ForecastMetrics`](../../Forecaster/ForecastMetrics/General.md#ForecastMetrics)



---

### `windowing_group` {: #windowing_group }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Funció per crear les variables del windowing. 

Treballa sobre un dataset i inclou la variable objectiu. 

Les variables creades es diràn com les originals (legacy) i s'afagirà '_' amb el número de desplaçament. 

Es tindràn en compte les hores en el rang [ini,fi)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.windowing_group(dataset=..., look_back_start=..., look_back_end=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `dataset`: Dataframe amb datetime com a índex
- `look_back_start`: On comença la finestra ( 24 -> el dia anterior si és horari)
- `look_back_end`: On acaba el número d'observacions (48 -> el dia anterior si és horari)


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Dataset amb les cariables desplaçades en columnes noves



---

### `windowing_univariant` {: #windowing_univariant }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Funció per crear les variables del windowing. 

Treballa sobre un dataset i inclou la variable objectiu. 

Les variables creades es diràn com les originals (legacy) i s'afagirà '_' amb el número de desplaçament. 

Es tindràn en compte les hores en el rang [ini,fi)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.windowing_univariant(
    dataset=...,
    look_back_start=...,
    look_back_end=...,
    variable=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `dataset`: Dataframe amb datetime com a índex
- `look_back_start`: On comença la finestra ( 24 -> el dia anterior si és horari)
- `look_back_end`: On acaba el número d'observacions (48 -> el dia anterior si és horari)
- `variable`: Variable a transformar en variables del windowing.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Dataset amb les variables desplaçades en columnes noves



---

### `do_windowing` {: #do_windowing }
Aplica el Windowing en consequencia al look_back indicat.

- None -> no aplica el windowing 

- Diccionari on la clau és la variable a fer windowing i el valor la finestra que s'ha d'aplicar 

- Les claus son Strings, indicant el nom de la columna a aplicar windowing
- Si com a clau es dona -1, la finestra aplicara a totes les variables NO especificades individualment.
- Els valors són els que defineixen la finestra a aplicar, i poden ser:
    - [ini, fi]
    - [ini, fi, salt]


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.do_windowing(data=..., look_back=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: dataframe de dades
- `look_back`: Windowing a aplicar


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

dataframe de dades preparades per el model de forecasting.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`windowing_group`](../../Forecaster/Forecaster/General.md#windowing_group), [`windowing_univariant`](../../Forecaster/Forecaster/General.md#windowing_univariant)



---

### `timestamp_to_attrs` {: #timestamp_to_attrs }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Afageix columnes derivades de l'índex temporal al DataFreame 'dad' segons les opcions indicades en 'extra_vars'. 
'


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.timestamp_to_attrs(dad=..., extra_vars=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `dad`: Dataframe amb un índex timestamp
- `extra_vars`: Diccionari amb opcions per a generar columnes adicionals ('variables', 'festius')


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

El mateix DataFrame amb les noves columnes afegides.



---

### `colinearity_remove` {: #colinearity_remove }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Elimina les colinearitats entre les variables segons el nivell indicat


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.colinearity_remove(data=..., y=..., level=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: Dataframe amb datetime com a índex
- `y`: Variable objectiu (per mirar que no la eliminem!)
- `level`: el percentatge de correlació de pearson per eliminar variables. None per no fer res


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

- dataset - Dataset amb les variables eliminades
- to_drop - Les variables que ha eliminat



---

### `scalate_data` {: #scalate_data }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Aplica una normalització o estandardització a les columnes del dataset.

Utilitza diferents mètodes de la llibreria *scikit-learn* per transformar les dades
segons el tipus d'escalador seleccionat (MinMaxScaler, RobustScaler o StandardScaler),
mantenint l'índex i els noms de les columnes originals.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.scalate_data(data=..., input_scaler=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: DataFrame original amb les dades numèriques a transformar.
- `input_scaler`: String que defineix el mètode ('minmax', 'robust', 'standard' o None).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una llista que conté el DataFrame escalat i l'objecte scaler utilitzat.

```python
( pd.DataFrame([[float, ...], ...]), <sklearn.preprocessing.scaler_object> or None )
```



---

### `get_attribs` {: #get_attribs }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Realitza una selecció o reducció de característiques (features) del dataset.

Segons el mètode escollit, pot mantenir totes les variables, seleccionar les més
importants mitjançant un arbre de decisió (ExtraTreesRegressor) o escollir les
'k' millors basant-se en proves estadístiques univariants.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_attribs(X=..., y=..., method=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `X`: Matriu de característiques d'entrada (features).
- `y`: Vector de la variable objectiu (target).
- `method`: Mètode de selecció (None, 'Tree' o un enter per a SelectKBest).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una llista que conté el model de selecció aplicat, la nova matriu X reduïda i la y original.

```python
[ <sklearn.feature_selection_object> or [], np.array([[float, ...], ...]), np.array([float, ...]) ]
```



---

### `Model` {: #Model }
Entrena o cerca la millor configuració d'un algorisme de predicció.

Si es proporcionen paràmetres, entrena el model directament. Si no, realitza una
cerca aleatòria (Randomized Search) sobre l'espai definit al fitxer de configuració,
avalua els models amb MAE (Mean Absolute Error) i selecciona el millor dins dels
límit de temps establerts.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.Model(
    X=...,
    y=...,
    algorithm=...,
    params=...,
    max_time=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `X`: Matriu de característiques d'entrada.
- `y`: Vector de la variable objectiu.
- `algorithm`: Nom o llista d'algorismes a utilitzar (si és None, es proven tots).
- `params`: Diccionari de paràmetres concrets o None per activar la cerca automàtica.
- `max_time`: Temps màxim d'execució en segons per a l'optimització de cada algorisme.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una llista que conté el model entrenat i la seva puntuació -> MAE o 'none'.

```python
[ <sklearn.model_object>, float # (Puntuació MAE o 'none') ]
```



---

### `prepare_dataframes` {: #prepare_dataframes }
<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">Mètode Estàtic</small>

Consolida les dades del sensor principal, meteorologia i sensors extra en un únic dataset.

Normalitza tots els conjunts de dades eliminant les zones horàries i aplicant un
remostreig (resample) horari basat en la mitjana. Finalment, fusiona les dades
mitjançant un 'outer join' per l'índex temporal.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.prepare_dataframes(sensor=..., meteo=..., extra_sensors=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor`: DataFrame del sensor objectiu (target).
- `meteo`: DataFrame amb dades meteorològiques o None.
- `extra_sensors`: Diccionari de DataFrames amb sensors addicionals.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

DataFrame unificat amb el timestamp com a columna i valors agregats per hores.

```python
{
    "timestamp": [datetime, ...],
    "value": [float, ...],
    "temperature_2m": [float, ...],
    "extra_sensor_col": [float, ...] 
}
```



---

### `create_model` {: #create_model }
Orquestra el cicle complet de creació, entrenament i validació d'un model de forecasting.

Aquesta funció executa tot el pipeline de Machine Learning: descarrega dades meteorològiques històriques,
prepara i fusiona datasets, aplica tècniques de finestra temporal (windowing), gestiona col·linearitats
i valors nuls, escala les dades, selecciona les millors característiques i, finalment, entrena el model
dividint les dades en conjunts de train, validació i test (60/20/20). Finalment, desa el model i
les seves mètriques de rendiment.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.create_model(
    data=...,
    sensors_id=...,
    y=...,
    lat=...,
    lon=...,
    algorithm=...,
    params=...,
    escalat=...,
    max_time=...,
    filename=...,
    meteo_data=...,
    extra_sensors_df=...,
    look_back=...,
    lang=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: DataFrame original amb les dades del sensor principal.
- `sensors_id`: Identificador del sensor a predir.
- `y`: Nom de la columna objectiu (target).
- `lat`: Latitud per a dades meteorològiques.
- `lon`: Longitud per a dades meteorològiques.
- `algorithm`: Algorisme específic o None per a mode automàtic (AutoML).
- `params`: Paràmetres de l'algorisme o None.
- `escalat`: Mètode d'escalat ('minmax', 'robust', 'standard' o None).
- `max_time`: Temps límit per a la cerca d'hiperparàmetres.
- `filename`: Nom del fitxer on es desarà el model .pkl final.
- `meteo_data`: DataFrame previ de meteo o None per descarregar automàticament.
- `extra_sensors_df`: Diccionari amb dades de sensors addicionals.
- `look_back`: Configuració de la finestra temporal (lags).
- `lang`: Idioma per a les notificacions i informes de mètriques.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None

Exemple d'estat final de self.db -> dades guardades:

```python
{
    "model": <sklearn.model_object>,
    "scaler": <sklearn.scaler_object>,
    "metrics": {
        "mae": float,
        "mse": float,
        "r2": float,
        "validation_score": float 
    },
    "algorithm": str,
    "look_back": {
        -1: [int, int]
    },
    "sensors_id": str 
}
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`ForecastMetrics`](../../Forecaster/ForecastMetrics/General.md#ForecastMetrics), [`Model`](../../Forecaster/Forecaster/General.md#Model), [`colinearity_remove`](../../Forecaster/Forecaster/General.md#colinearity_remove), [`compare_with_baseline`](../../Forecaster/ForecastMetrics/General.md#compare_with_baseline), [`do_windowing`](../../Forecaster/Forecaster/General.md#do_windowing), [`get_attribs`](../../Forecaster/Forecaster/General.md#get_attribs), [`get_summary`](../../Forecaster/ForecastMetrics/General.md#get_summary), [`prepare_dataframes`](../../Forecaster/Forecaster/General.md#prepare_dataframes), [`save_model`](../../Forecaster/Forecaster/General.md#save_model), [`scalate_data`](../../Forecaster/Forecaster/General.md#scalate_data), [`timestamp_to_attrs`](../../Forecaster/Forecaster/General.md#timestamp_to_attrs), [`validate_colinearity_removal`](../../Forecaster/ForecastMetrics/General.md#validate_colinearity_removal), [`validate_dataframe_preparation`](../../Forecaster/ForecastMetrics/General.md#validate_dataframe_preparation), [`validate_feature_selection`](../../Forecaster/ForecastMetrics/General.md#validate_feature_selection), [`validate_feature_target_correlation`](../../Forecaster/ForecastMetrics/General.md#validate_feature_target_correlation), [`validate_model_training`](../../Forecaster/ForecastMetrics/General.md#validate_model_training), [`validate_nan_handling`](../../Forecaster/ForecastMetrics/General.md#validate_nan_handling), [`validate_scaling`](../../Forecaster/ForecastMetrics/General.md#validate_scaling), [`validate_temporal_features`](../../Forecaster/ForecastMetrics/General.md#validate_temporal_features), [`validate_windowing`](../../Forecaster/ForecastMetrics/General.md#validate_windowing)



---

### `forecast` {: #forecast }
Genera prediccions futures de manera recursiva i calcula l'ajust sobre dades històriques.

Aquesta funció implementa un bucle recursiu on cada predicció s'utilitza com a entrada (lag)
per a la següent hora. Aplica tot el pipeline de transformació (windowing, atributs
temporals, eliminació de colinearitats, escalat i selecció) a cada iteració. A més,
calcula la predicció sobre el conjunt de test actual per permetre la comparació visual.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.forecast(
    data=...,
    y=...,
    model=...,
    future_steps=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: DataFrame amb les dades històriques recents (llavor per a la recursivitat).
- `y`: Nom de la variable objectiu a predir.
- `model`: Objecte del model entrenat per realitzar les inferències.
- `future_steps`: Nombre de passos (hores) a predir cap al futur.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla amb el DataFrame de prediccions, passades i futures, els valors reals de test i l'ID del sensor.

```python
( pd.DataFrame({
            "value": [float, ...]
        }, index=[datetime, ...]), pd.Series([float, ...], index=[datetime, ...]), str )
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`do_windowing`](../../Forecaster/Forecaster/General.md#do_windowing), [`timestamp_to_attrs`](../../Forecaster/Forecaster/General.md#timestamp_to_attrs)



---

### `save_model` {: #save_model }
Serialitza l'estat actual del model i la seva configuració en un fitxer binari.

Crea el directori de destinació si no existeix, guarda el diccionari intern 'self.db'
(que conté el model, escaladors, mètriques i metadades) utilitzant joblib i,
finalment, buida la memòria temporal de l'objecte per alliberar recursos.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.save_model(model_filename=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `model_filename`: Nom del fitxer (sense extensió) on es desarà el model.



---

### `load_model` {: #load_model }
Carrega un model prèviament entrenat i la seva configuració des d'un fitxer físic.

Restaura el diccionari intern 'self.db' amb tota la informació necessària per realitzar
prediccions: l'algorisme entrenat, els escaladors, els paràmetres de finestra temporal
i les metadades dels sensors associats.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.load_model(model_filename=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `model_filename`: Nom del fitxer .pkl (incloent l'extensió) a carregar.



---

