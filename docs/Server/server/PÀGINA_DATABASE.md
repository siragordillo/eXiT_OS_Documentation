# PÀGINA DATABASE (server)

## `graphs_view` {: #graphs_view }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_graph_info</small>

Genera un diccionari amb les dates d'inici i final indicades per l'usuari i les dades
dels sensors per a enviar al frontend i poder generar un plotly.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = graphs_view()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari

```python
{Status, Range{Start, End,Label}, Graphs{...,...,}}
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_all_saved_sensors_data`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_saved_sensors_data)



---

## `force_update_database` {: #force_update_database }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /force_update_database/<use_clean></small>

Actua com a connexió entre en frontend (HTML) i la base de dades,
 cridant al mètode per a actualitzar les dades dels sensors.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = force_update_database(use_clean=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `use_clean`: -


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

"ok"


#### <i class="fa-solid fa-link"></i> Depèn de:
[`clean_database_hourly_average`](../../SqlDB/sqlDB/GENERAL.md#clean_database_hourly_average), [`update_database`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_database)



---

