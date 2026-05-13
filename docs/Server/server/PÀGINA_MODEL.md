# PÀGINA MODEL (server)

## `get_model_config` {: #get_model_config }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_model_config/<model_name></small>

Obté la configuració del model indicat


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_model_config(model_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `model_name`: Nom del model a obtenir


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

configuració del model *model_name* en format string.



---

## `get_model_metrics` {: #get_model_metrics }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_model_metrics/<model_name></small>

Obté les mètriques del model indicat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_model_metrics(model_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `model_name`: nom del model a obtenir


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb Status "ok/error", metrics "mètriques del model" i train_val_test_split


#### <i class="fa-solid fa-link"></i> Depèn de:
[`convert_to_json_serializable`](../../Optimizer/FlexibilityManager/General.md#convert_to_json_serializable)



---

## `train_model` {: #train_model }
Entrena el model per a forecastings futurs


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = train_model()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Model entrenat



---

## `forecast_model` {: #forecast_model }
Realitza forecast a partir d'un model entrenat.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = forecast_model(selected_forecast=..., today=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `selected_forecast`: forecast a realitzar (model)
- `today`: True si realitzem un forecast a data d'avui, False si el realitzem amb data de demà


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Forecasting realitzat.



---

## `delete_model` {: #delete_model }
Elimina el model indicat al formulari.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = delete_model()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None



---

## `submit_model` {: #submit_model }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /submit-model</small>

Actua com a pont entre el frontent (HTML) de model.html i el backend.
 Cridant a la funció indicada segons el que ha seleccionat l'usuari (Entrentar, Forecasting o Eliminar model)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = submit_model()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Pàgina model.html actualitzada.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`create_model_page`](../../Server/server/HTML_PAGES.md#create_model_page), [`delete_model`](../../Forecaster/ForecasterManager/General.md#delete_model), [`forecast_model`](../../Forecaster/ForecasterManager/General.md#forecast_model), [`train_model`](../../Forecaster/ForecasterManager/General.md#train_model)



---

## `get_forecast_data` {: #get_forecast_data }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_forecast_data/<model_name></small>

Obté les dades del forecasting indicat *model_name*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_forecast_data(model_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `model_name`: nom del model de forecasting del qual obtenir les dades.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{
    Status,
    Timestamps,
    Predictions,
    Valors reals,
    Timestamps dels valors reals,
    Predicció del dia anterior,
    Timestamps de la predicció del dia anterior,
    Timestamp inicial,
    Timestamp final 
}
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_data_from_forecast_from_date`](../../SqlDB/sqlDB/FORECASTS.md#get_data_from_forecast_from_date)



---

