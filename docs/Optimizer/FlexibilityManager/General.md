# General (FlexibilityManager)

## `convert_to_json_serializable` {: #convert_to_json_serializable }
Converteix recursivament objectes amb tipus NumPy/Pandas a tipus natius de Python
per permetre la serialització JSON.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = convert_to_json_serializable(obj=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `obj`: -



---

## `get_flexibility` {: #get_flexibility }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
get_flexibility(
    device_flex=...,
    base_file_path=...,
    total_fup=...,
    total_fdown=...,
    device_name=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `device_flex`: -
- `base_file_path`: -
- `total_fup`: -
- `total_fdown`: -
- `device_name`: -


#### <i class="fa-solid fa-link"></i> Depèn de:
[`convert_to_json_serializable`](../../Optimizer/FlexibilityManager/General.md#convert_to_json_serializable)



---

## `send_flexibility` {: #send_flexibility }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = send_flexibility(base_file_path=..., today=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `base_file_path`: -
- `today`: -



---

## `generate_fake_response` {: #generate_fake_response }
Simula el servidor central. Retorna UNA sola instrucció al dia,
aplicada a un RANG horari continu (ex: de 11h a 14h).


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = generate_fake_response(flexi_data=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `flexi_data`: -



---

## `load_flexibility_data` {: #load_flexibility_data }
Llegeix tots els fitxers JSON de la carpeta especificada i crea un diccionari
amb la flexibilitat de tots els dispositius.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = load_flexibility_data(folder_path=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `folder_path`: -



---

## `dispatch_local_devices` {: #dispatch_local_devices }
Intenta complir la petició del servidor combinant dispositius hora a hora.
Calcula si hem aconseguit l'objectiu o ens hem quedat curts.
Ara evalua els límits globals seqüencials utilitzant l'estat intern seqüencial
dels dispositius.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = dispatch_local_devices(requested_flex=..., folder_path=..., optimal_scheduler=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `requested_flex`: -
- `folder_path`: -
- `optimal_scheduler`: -


#### <i class="fa-solid fa-link"></i> Depèn de:
[`initialize_flex_tracker`](../../Assets/SonnenBattery/General.md#initialize_flex_tracker), [`reserve_flexibility`](../../Assets/SonnenBattery/General.md#reserve_flexibility)



---

