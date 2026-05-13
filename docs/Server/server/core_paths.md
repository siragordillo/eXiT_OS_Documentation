# core_paths (server)

## `serve_static` {: #serve_static }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /static/<filepath:path></small>

retorna la imatge sol·licitada del path /images/


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = serve_static(filepath=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `filepath`: path de la imatge desitjada


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

static_file

```python
(filepath, root='./images/')
```



---

## `serve_resources` {: #serve_resources }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /resources/<filepath:path></small>

retorna el resource sol·licitada del path /resources/


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = serve_resources(filepath=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `filepath`: path del resource desitjat


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

static_file

```python
(filepath, root='./resources/')
```



---

## `serve_models` {: #serve_models }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: models/<filepath:path></small>

retorna el model sol·licitat del path /models/


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = serve_models(filepath=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `filepath`: path del model


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

static_file

```python
(filepath, root='./models/')
```



---

## `get_page` {: #get_page }
<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">Route: /<page></small>

Retorna la pàgina HTML sol·licitada


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = get_page(page=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres d'entrada

- `page`: pàgina HTML a servir


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

pàgina

```python
(static file)
```

si existeix, HTTPError 404 en cas contrari



---

