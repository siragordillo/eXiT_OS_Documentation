# SENSORS - Home Asistant (sqlDB)

### `set_sensor_value_HA` {: #set_sensor_value_HA }
Força l'estat indicat a value, al dispositiu **sensor_id** a través de l'API de Home Assistant.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.set_sensor_value_HA(sensor_mode=..., sensor_id=..., value=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_mode`: Tipus de sensor que es vol modificar (select, number, button, switch).
- `sensor_id`: ID del sensor que es vol controlar.
- `value`: Nou valor a aplicar al sensor.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None



---

