# DEVICES (sqlDB)

### `get_devices_info` {: #get_devices_info }
Recupera l'estructura completa de dispositius i entitats de Home Assistant.

Envia un template de Jinja2 a l'API per agrupar les entitats segons el seu
dispositiu associat, incloent-hi els atributs 'friendly_name' i gestionant
les entitats sense dispositiu assignat sota un grup especial anomenat '0rphans'.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_devices_info()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una llista de diccionaris amb el nom del dispositiu i les seves entitats,
o un diccionari buit en cas d'error en la petició.

```python
[
    {
        "device_name": "Sensor Temperatura",
        "entities": [
            {
                "entity_id": "sensor.temp_living",
                "entity_name": "Temperatura Salo"
            }
        ]
    },
    {
        "device_name": "0rphans",
        "entities": [
            {
                "entity_id": "sun.sun",
                "entity_name": "Sol"
            }
        ]
    }
]
```



---

### `get_parent_device_from_sensor_id` {: #get_parent_device_from_sensor_id }
Cerca el nom del dispositiu pare al qual pertany una entitat concreta.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_parent_device_from_sensor_id(sensor_id=..., devices_dict=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: L'identificador de l'entitat a cercar.
- `devices_dict`: El diccionari de dispositius obtingut amb 'get_devices_info'.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

El nom del dispositiu pare o "None" si no es troba la coincidència.



---

