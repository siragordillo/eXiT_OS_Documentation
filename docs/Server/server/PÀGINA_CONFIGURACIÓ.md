# PÀGINA CONFIGURACIÓ (server)

## `save_config` {: #save_config }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /save_config</small>

Guarda la configuració d'usuari entrat al formulari. Generant claus privades per al Blockchain.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = save_config()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

"OK"


#### <i class="fa-solid fa-link"></i> Depèn de:
[`certificate_hourly_task`](../../Server/server/DAILY_TASKS.md#certificate_hourly_task), [`update_sensor_active`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_sensor_active)



---

## `delete_config` {: #delete_config }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /delete_config</small>

Elimina l'arxiu de configuració d'usuari guardat a /config/user.config"


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = delete_config()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

String amb l'estat


#### <i class="fa-solid fa-link"></i> Depèn de:
[`update_sensor_active`](../../SqlDB/sqlDB/SENSORS_-_Setters.md#update_sensor_active)



---

## `get_res_certify_data` {: #get_res_certify_data }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /get_res_certify_data</small>

Obté el document .pkl on es guarden els últim 10 missatges enviats al Blockchain.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_res_certify_data()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb status "OK / Error" i data que es troba dins el fitxer *res_certify.pkl*



---

## `get_user_configuration_data` {: #get_user_configuration_data }
Obté la configuració de l'usuari guardada al document *config/user.config*


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_user_configuration_data()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Informació guardada de l'usuari

```python
(nom, variable consum, variable generació, formulari bloquejat)
```

.



---

