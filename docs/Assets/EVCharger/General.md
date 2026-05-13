# General (EVCharger)

### `__init__` {: #__init__ }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__init__(config=..., database=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: -
- `database`: -



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
obj.controla(config=..., current_hour=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: -
- `current_hour`: -



---

### `get_flexibility` {: #get_flexibility }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.get_flexibility(optimization_data=...)
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
De moment el EVCharger no aporta flexibilitat fins que definim un comportament.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.reserve_flexibility(hour=..., requested_power=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `hour`: -
- `requested_power`: -



---

