# PÀGINA OPTIMITZACIÓ (server)

## `run_optimization` {: #run_optimization }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /run_optimization</small>

Funció filtre que crida optimize amb paràmetre fixe de *today = True*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = run_optimization()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`optimize`](../../Server/server/PÀGINA_OPTIMITZACIÓ.md#optimize)



---

## `optimize` {: #optimize }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /optimize</small>

Realitza l'optimització per a la data indicada (Avui o demà).
En cas que funcioni correctament guarda timestamps, balanç total, preu total i configuració dels dispositius a un document .pkl
a amb nom *%d-%m-%YY* a la carpeta *share/exitos/optimizations/*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = optimize(today=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `today`: Booleana. True si l'optimització és del dia d'avui, False en cas que sigui per l'endemà.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`flexibility`](../../Server/server/FLEXIBILITY.md#flexibility), [`get_user_configuration_data`](../../Server/server/PÀGINA_CONFIGURACIÓ.md#get_user_configuration_data), [`start_optimization`](../../Optimizer/OptimalScheduler/General.md#start_optimization)



---

## `get_config_file_names` {: #get_config_file_names }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_config_file_names</small>

Obté els noms de tots els documents de configuració de dispositius guardats a *share/exitos/optimizations/configs/*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_config_file_names()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari

```python
{Status: ok / error, "names": [noms dels documents]}
```



---

## `save_optimization_config` {: #save_optimization_config }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /save_optimization_config</small>

Guarda la configuració entrada al formulari (optimization page -> New Device) com a arxiu .json a la carpeta */share/exitos/optimizations/configs/* 

El nom de l'arxiu és el nom del dispositiu introduit. 

En cas que ja existeixi una configuració amb el mateix nom elimina la config existent i guarda la nova.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = save_optimization_config()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{
    "status": "ok / error",
    "msg": "info de l'estat en format string"
}
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`update_sensor_active`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_sensor_active)



---

## `delete_optimization_config` {: #delete_optimization_config }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /delete_optimization_config/<file_name></small>

Elimina l'arxiu de configuració del device indicat per paràmetre.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = delete_optimization_config(file_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `file_name`: nom de l'arxiu que es vol eliminar.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{status: ok / error}
```



---

## `get_device_config_data` {: #get_device_config_data }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_device_config_data/<file_name></small>

Obté la configuració guardada al document indicat per paràmetre, guardat a */share/exitos/optimizations/configs/*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_device_config_data(file_name=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `file_name`: Nom de l'arxiu que es vol obtenir.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{status: ok , device_config: { }}
```

si ha anat bé, {status: error, msg: ""} en cas contrari



---

## `get_device_types` {: #get_device_types }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_device_types/<locale></small>

Obté els tipus de Device del programa configurats a l'arxiu *optimization_devices.conf*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_device_types(locale=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `locale`: idioma del programa, per trobar l'arxiu en l'idioma configurat actualment.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{Tipus de dispositius guardats}
```



---

## `update_device_config` {: #update_device_config }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /update_device_config</small>

Actualitza la configuració del dispositiu amb les noves dades entrades al formulari (només el paràmetre que indica si controlem o no el dispositiu)


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = update_device_config()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

```python
{status: success / error}
```



---

