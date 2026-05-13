# General (ShellyPlus1pm)

### `__init__` {: #__init__ }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__init__(config=..., database=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: -
- `database`: -


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_consumption_when_ON`](../../Assets/ShellyPlus1pm/General.md#get_consumption_when_ON), [`get_data_from_sensor`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_data_from_sensor)



---

### `simula` {: #simula }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.simula(config=..., horizon=..., horizon_min=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: -
- `horizon`: -
- `horizon_min`: -



---

### `controla` {: #controla }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.controla(config=..., current_hour=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: -
- `current_hour`: -


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_current_sensor_state`](../../SqlDB/sqlDB/SENSORS_-_Getters.md#get_current_sensor_state)



---

### `get_consumption_when_ON` {: #get_consumption_when_ON }
Calcula la mitjana de consum quan l'interruptor està encés. Mira un màxi mde 500 valors


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_consumption_when_ON(data=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `data`: -



---

### `get_flexibility` {: #get_flexibility }
Calcula la flexibilitat del dispositiu Shelly.
Flexibilitat es basa en si està ON o OFF.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_flexibility(optimization_data=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `optimization_data`: -



---

### `initialize_flex_tracker` {: #initialize_flex_tracker }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.initialize_flex_tracker(baseline_plan=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `baseline_plan`: -



---

### `reserve_flexibility` {: #reserve_flexibility }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.reserve_flexibility(hour=..., requested_power=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `hour`: -
- `requested_power`: -



---

