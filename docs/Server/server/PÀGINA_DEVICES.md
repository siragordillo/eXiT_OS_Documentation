# PÀGINA DEVICES (server)

## `get_sensors` {: #get_sensors }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_sensors</small>

Obté tota la informació disponible a la base de dades sobre cada un dels sensors.
Separant la informació entre dispositiu pare i entitats fills.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_sensors()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

diccionari amb dispositius pare i les seves entitats filles


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_all_sensors_data`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_all_sensors_data)



---

## `update_sensors` {: #update_sensors }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /update_sensors</small>

Actualitza les variables *save* i *type* de tots els sensors que han estat modificats al formulari.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = update_sensors()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Status: ok si tot ha anat bé, error en cas contrari.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`reset_all_sensors_save`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#reset_all_sensors_save), [`update_sensor_active`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_sensor_active)



---

## `self_destruct_database` {: #self_destruct_database }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /self_destruct</small>

Elimina completament la base de dades SQL del programa


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = self_destruct_database()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

status: ok


#### <i class="fa-solid fa-link"></i> Depèn de:
[`self_destruct`](../../SqlDB/sqlDB/PRIVATE_METHODS.md#self_destruct)



---

