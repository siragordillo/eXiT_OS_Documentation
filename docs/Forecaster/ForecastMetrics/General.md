# General (ForecastMetrics)

### `__init__` {: #__init__ }
Constructor de la classe ForecastMetrics per a la gestió de validacions i informes.

Inicialitza el sistema de seguiment de mètriques, configurant el mode de depuració,
el comptador de passos del pipeline i carregant les traduccions corresponents
per als missatges de validació en l'idioma seleccionat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__init__(debug=..., lang=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `debug`: Booleà per activar la traçabilitat detallada del procés.
- `lang`: Codi d'idioma ('ca', 'es', 'en') per a les traduccions.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`load_locale`](../../Forecaster/ForecastMetrics/General.md#load_locale)



---

### `load_locale` {: #load_locale }
Carrega el fitxer de traduccions per als missatges de validació del mòdul de mètriques.

Busca un fitxer JSON a la carpeta de recursos segons el codi d'idioma proporcionat.
Si el troba, extreu la secció específica de mètriques; en cas contrari, retorna un
diccionari buit i manté l'execució amb els valors per defecte.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.load_locale(lang=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `lang`: Codi de l'idioma (ex: 'ca', 'es', 'en') que determina el nom del fitxer.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb les claus i traduccions de text per a la interfície o informes.

```python
{ "step_1_title": str, "validation_error": str, "metric_label": str }
```



---

### `get_text` {: #get_text }
Recupera una cadena de text traduïda a partir d'una clau jeràrquica i hi aplica format.

Utilitza la notació de punts per navegar pel diccionari de traduccions fins a trobar
el valor corresponent. Si es proporcionen arguments addicionals, s'injecten en els
marcadors de posició del text (tipus str.format).


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_text(key=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `key`: Clau de traducció en format de punts (ex: 'errors.nan_found').
- `args`: Valors variables per emplenar els buits del text traduït.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

El text formatat si existeix, o la mateixa clau si no es troba la traducció.



---

### `log_step` {: #log_step }
Registra i emmagatzema les mètriques i l'estat d'un pas concret del pipeline.

Incrementa el comptador de passos, genera un registre amb la marca de temps,
l'identificador de l'etapa i els indicadors de validesa, i finalment imprimeix
un resum visual per la consola segons el nivell de log especificat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.log_step(
    step_name=...,
    metrics_dict=...,
    level=...,
    step_id=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `step_name`: Nom descriptiu del pas executat.
- `metrics_dict`: Diccionari amb els valors numèrics o booleans de control.
- `level`: Nivell de severitat del registre ("INFO", "WARNING", "ERROR").
- `step_id`: Identificador estable utilitzat per a la integració amb el frontend.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_print_step_metrics`](../../Forecaster/ForecastMetrics/General.md#_print_step_metrics)



---

### `_print_step_metrics` {: #_print_step_metrics }
Genera una sortida visual per consola amb el resum detallat de les mètriques d'un pas.

Dibuixa una capçalera estructurada amb el nom del pas i el seu número d'ordre,
formata els valors numèrics per a una lectura òptima (control de decimals i milers)
i etiqueta cada mètrica segons la seva categoria funcional. Finalment, mostra un
indicador d'estat (èxit o advertència) basat en la validesa del pas.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj._print_step_metrics(step_name=..., metrics=..., level=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `step_name`: Títol o descripció de l'etapa del pipeline que s'està mostrant.
- `metrics`: Diccionari de dades tècniques i indicadors de control.
- `level`: Nivell de log utilitzat per a la impressió (per defecte "INFO").


#### <i class="fa-solid fa-link"></i> Depèn de:
[`_get_metric_category`](../../Forecaster/ForecastMetrics/General.md#_get_metric_category)



---

### `_get_metric_category` {: #_get_metric_category }
Classifica una mètrica específica en una categoria funcional per facilitar-ne la lectura.

Compara el nom de la mètrica amb un mapa de paraules clau predefinit i retorna la
traducció de la categoria corresponent (com ara 'Files', 'Columnes', 'Mètriques d'error', etc.).
Si no troba cap coincidència, assigna una categoria genèrica.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj._get_metric_category(metric_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `metric_name`: Nom tècnic de la mètrica que s'ha d'avaluar.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

El nom de la categoria traduït segons el fitxer de localització.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text)



---

### `validate_dataframe_preparation` {: #validate_dataframe_preparation }
Avalua la integritat i la qualitat de les dades després de la fase d'unificació (Pas 0).

Calcula estadístiques clau sobre el volum de dades (files i columnes), el percentatge de
valors nuls i la cobertura temporal en dies. Verifica que no s'hagi produït una pèrdua
excessiva de dades durant el remostreig horari i que la densitat de la informació sigui
suficient per a l'entrenament del model.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_dataframe_preparation(
    sensor_df=...,
    meteo_df=...,
    extra_sensors=...,
    merged_df=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_df`: DataFrame original del sensor objectiu.
- `meteo_df`: DataFrame amb les dades meteorològiques utilitzades.
- `extra_sensors`: Diccionari o conjunt de sensors addicionals integrats.
- `merged_df`: DataFrame resultant després de la fusió i el resample.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb les mètriques de volum, cobertura i el flag de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_windowing` {: #validate_windowing }
Verifica la correcta transformació del dataset després d'aplicar la tècnica de finestra temporal (Pas 1).

Calcula el nombre de noves característiques (lags) generades i les compara amb el valor
teòric esperat segons la configuració de 'look_back'. També analitza la quantitat de valors
nuls (NaN) introduïts per l'efecte de desplaçament de la finestra, especialment a l'inici
del dataset, per assegurar que no es comprometi la densitat de dades útil.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_windowing(original_df=..., windowed_df=..., look_back=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `original_df`: DataFrame abans d'expandir les columnes temporals.
- `windowed_df`: DataFrame resultant amb les noves columnes de retard (lags).
- `look_back`: Diccionari de configuració que defineix els intervals de la finestra.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb les mètriques de característiques creades, nuls introduïts i estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_temporal_features` {: #validate_temporal_features }
Comprova la correcta generació i els rangs de les variables temporals i de calendari (Pas 2).

Valida que les noves columnes (Dia, Hora, Mes) s'hagin afegit correctament i que els seus
valors estiguin dins dels rangs lògics (0-6 per a dies, 0-23 per a hores, 1-12 per a mesos).
Així mateix, analitza la proporció de dies festius detectats per assegurar que la distribució
és coherent i no presenta anomalies en el calendari aplicat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_temporal_features(df_with_temporal=..., extra_vars=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `df_with_temporal`: DataFrame que inclou les noves característiques exògenes.
- `extra_vars`: Configuració que especifica quines variables i festius s'havien de crear.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb el recompte de característiques afegides, els rangs detectats i l'estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_colinearity_removal` {: #validate_colinearity_removal }
Supervisa el procés de filtratge de variables redundants o altament correlacionades (Pas 3).

Calcula la matriu de correlació restant per assegurar que cap parell de variables superi
el llindar establert i verifica que la variable objectiu (target) no hagi estat eliminada
per error. També controla el percentatge de reducció del dataset per evitar una pèrdua
excessiva d'informació que pugui afectar la capacitat predictiva del model.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_colinearity_removal(
    df_before=...,
    df_after=...,
    removed_cols=...,
    y_col=...,
    threshold=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `df_before`: DataFrame previ a l'eliminació de col·linearitats.
- `df_after`: DataFrame resultant amb les variables seleccionades.
- `removed_cols`: Llista de noms de les columnes que han estat descartades.
- `y_col`: Nom de la variable objectiu que s'ha de preservar.
- `threshold`: Llindar de correlació (0 a 1) utilitzat per al filtratge.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb les mètriques de reducció, correlació màxima restant i estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_nan_handling` {: #validate_nan_handling }
Verifica l'eficàcia de la neteja de valors nuls i l'impacte en el volum del dataset (Pas 4).

Compara la quantitat de valors nuls abans i després de l'aplicació de mètodes d'interpolació
i imputació. Controla estrictament el percentatge de files eliminades durant aquest procés
per evitar una pèrdua d'informació crítica i assegura que el dataset final estigui
completament lliure de valors nuls abans d'entrar a la fase d'entrenament.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_nan_handling(df_before=..., df_after=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `df_before`: DataFrame que conté els valors nuls originals o introduïts pel windowing.
- `df_after`: DataFrame net després de la interpolació i l'eliminació de files incompletes.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb el recompte de valors nuls eliminats, files perdudes i estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_scaling` {: #validate_scaling }
Avalua la correcta normalització de les característiques del dataset (Pas 6).

Calcula estadístiques descriptives (mitjana, desviació estàndard, mínim i màxim) sobre
les dades transformades per verificar que el mètode d'escalat s'ha aplicat correctament.
Per al mètode 'minmax', comprova que els valors estiguin continguts entre 0 i 1, mentre
que per a l'escalat 'standard' (StandardScaler), valida que la mitjana sigui propera
a 0 i la desviació estàndard propera a 1.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_scaling(df_before=..., df_after=..., scaler_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `df_before`: DataFrame o array abans de realitzar l'escalat.
- `df_after`: DataFrame o array amb les dades ja transformades.
- `scaler_name`: Nom del mètode utilitzat ('minmax', 'standard', 'robust' o None).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb les estadístiques de l'escalat, el tipus de transformació i l'estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_feature_selection` {: #validate_feature_selection }
Analitza l'eficàcia del procés de selecció d'atributs i el seu impacte en el dataset (Pas 7).

Compara la quantitat de característiques abans i després de l'aplicació de l'algorisme de
selecció (com 'Tree' o 'ANOVA'). Verifica que no s'hagi buidat el dataset per complet,
que s'hagi mantingut un nombre mínim de variables per a la predicció i que la reducció
no sigui excessivament agressiva, la qual cosa podria indicar una pèrdua de senyal rellevant.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_feature_selection(X_before=..., X_after=..., method=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `X_before`: Matriu de dades d'entrada abans de la selecció.
- `X_after`: Matriu de dades d'entrada amb només els atributs seleccionats.
- `method`: Nom del mètode de selecció utilitzat.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb el recompte de variables, el percentatge de reducció i l'estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_model_training` {: #validate_model_training }
Avalua el rendiment del model entrenat mitjançant el càlcul de mètriques d'error i bondat d'ajust (Pas 8).

Calcula indicadors clau com el MAE, RMSE i R², així com el MAPE i WAPE per mesurar l'error
percentual de forma robusta. També analitza el biaix (Bias) per detectar si el model
tendeix a sobreestimar o infraestimar sistemàticament els valors. Realitza validacions
crítiques sobre el coeficient de determinació i la magnitud de l'error per garantir
que el model sigui estadísticament significatiu.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_model_training(
    X=...,
    y=...,
    y_pred=...,
    algorithm=...,
    score=...,
    training_time=...,
    iterations=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `X`: Matriu de característiques del conjunt de test.
- `y`: Valors reals (ground truth) del conjunt de test.
- `y_pred`: Valors predits pel model per al mateix conjunt.
- `algorithm`: Nom de l'algorisme utilitzat.
- `score`: Puntuació obtinguda durant la fase d'entrenament/optimització.
- `training_time`: Temps total invertit en l'entrenament en segons.
- `iterations`: Nombre de configuracions provades (en cas d'AutoML).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb el resum de mètriques d'error, temps d'execució i estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_feature_target_correlation` {: #validate_feature_target_correlation }
Analitza el poder predictiu de les variables independents respecte a la variable objectiu.

Calcula el coeficient de correlació de Pearson per a cada columna del dataset en relació
amb el target. Identifica les 10 característiques amb més influència i verifica si existeix
un llindar mínim de senyal (0.1) per garantir que el model tingui una base estadística
sòlida sobre la qual aprendre. Si la correlació màxima és massa baixa, emet una advertència
sobre la probable falta de capacitat predictiva del futur model.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_feature_target_correlation(df=..., y_col=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `df`: DataFrame que conté tant les característiques com la variable objectiu.
- `y_col`: Nom de la columna que es vol predir (target).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb la correlació màxima, les variables més rellevants i l'estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `validate_forecast_output` {: #validate_forecast_output }
Verifica la coherència i la qualitat de les prediccions generades pel model.

Comprova que el nombre de passos predits coincideixi amb l'horitzó de previsió sol·licitat
i analitza la distribució estadística dels valors resultants en comparació amb les dades
originals. Detecta possibles valors atípics (outliers) que s'allunyin més de tres desviacions
estàndard de la mitjana històrica i assegura l'absència de valors nuls en la sortida final.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.validate_forecast_output(forecast_df=..., original_df=..., future_steps=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `forecast_df`: DataFrame que conté els valors predits pel model.
- `original_df`: Sèrie o DataFrame amb les dades històriques de referència.
- `future_steps`: Nombre de passos (horitzó temporal) que s'esperava predir.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb estadístiques de la predicció, recompte d'outliers i estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

### `get_summary` {: #get_summary }
Genera un informe consolidat de totes les validacions realitzades durant l'execució.

Calcula estadístiques globals com el percentatge d'èxit del pipeline, el recompte total de
passos completats i el nombre d'advertències detectades. A més, imprimeix un resum
executiu per consola i retorna l'historial complet de mètriques emmagatzemades al log
per a la seva posterior anàlisi o visualització.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_summary()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb el resum estadístic de l'execució i el llistat detallat de cada pas.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text)



---

### `export_metrics` {: #export_metrics }
Persisteix l'historial complet de mètriques i validacions en un fitxer de dades extern.

Escriu el contingut de l'atribut 'metrics_log' en format JSON amb sagnat per facilitar-ne
la lectura humana. Un cop finalitzada l'escriptura, notifica la ubicació del fitxer
generat a través del logger.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.export_metrics(filename=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `filename`: Nom o ruta del fitxer on s'emmagatzemaran les dades (per defecte "metrics_log.json").


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text)



---

### `compare_with_baseline` {: #compare_with_baseline }
Compara el rendiment del model entrenat respecte a models de referència (baselines) simplificats.

Calcula l'error (MAE) de dos mètodes base: la persistència (utilitzar l'últim valor conegut
com a predicció) i la mitjana mòbil. Determina el percentatge de millora del model
respecte a aquests mètodes i valida si el model és realment útil; si el model no
supera els baselines simples, es considera que no està aportant valor predictiu real.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.compare_with_baseline(y_true=..., y_pred_model=..., last_history_value=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `y_true`: Valors reals del conjunt de dades.
- `y_pred_model`: Valors predits pel model d'aprenentatge automàtic.
- `last_history_value`: Últim valor real conegut abans del set de test per al càlcul de persistència.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb els MAE de cada mètode, els percentatges de millora i l'estat de validesa.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_text`](../../Forecaster/ForecastMetrics/General.md#get_text), [`log_step`](../../Forecaster/ForecastMetrics/General.md#log_step)



---

