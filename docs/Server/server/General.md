# General (server)

## `convert_to_json_serializable` {: #convert_to_json_serializable }
Converteix recursivament objectes amb tipus NumPy/Pandas a tipus natius de Python
per permetre la serialització JSON.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = convert_to_json_serializable(obj=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `obj`: obj que volem convertir de NumPy/Pandas a tipus natiu de Python.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Retorna l'objecte convertit a tipus Python.



---

## `main` {: #main }
Funció main que encén el servidor web.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = main()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

None


#### <i class="fa-solid fa-link"></i> Depèn de:
[`run`](../../Server/server/Threading.md#run)



---

