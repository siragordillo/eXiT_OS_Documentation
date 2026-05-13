# General (OptimalScheduler)

### `__init__` {: #__init__ }
Controlador central per a l'optimització de recursos energètics en una xarxa local.

Aquesta classe s'encarrega de gestionar la programació òptima (scheduling) de consumidors,
generadors i sistemes d'emmagatzematge d'energia (bateries). Utilitza dades de previsió
de consum i generació, així com els preus de l'electricitat, per resoldre un problema
d'optimització que minimitzi el cost o maximitzi l'autoconsum en un horitzó temporal definit.

Atributs principals:
    database: Connexió amb la base de dades o el sistema (e.g., Home Assistant).
    horizon: Finestra temporal de planificació (per defecte 24 hores).
    horizon_min: Resolució temporal de cada interval (pas de temps).
    maxiter: Límit d'iteracions per a l'algorisme d'optimització (ajustat segons l'entorn).
    energy_storages: Diccionari de bateries disponibles per a la gestió de càrrega/descàrrega.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__init__(database=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `database`: Referencia a la classe SqlDB


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_lat_long`](../../SqlDB/sqlDB/GENERAL.md#get_lat_long)



---

### `start_optimization` {: #start_optimization }
Inicia i coordina el procés d'optimització energètica per a un període determinat.

Aquest mètode actua com a orquestrador principal: prepara les dades d'entrada, obté les
previsions de consum i generació per als sensors especificats, configura els límits de les
variables de decisió (varbounds) i recupera els preus de l'electricitat. Finalment, executa
l'algorisme d'optimització per trobar la configuració de dispositius que minimitzi el cost,
calculant el balanç energètic resultant.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.start_optimization(
    consumer_id=...,
    generator_id=...,
    horizon=...,
    horizon_min=...,
    today=...
)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `consumer_id`: Identificador del sensor de consum global.
- `generator_id`: Identificador del sensor de generació (e.g., plaques solars).
- `horizon`: Nombre d'hores de la finestra de planificació.
- `horizon_min`: Resolució temporal (intervals per hora).
- `today`: Data de referència per a l'optimització.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla amb:

```python
(èxit del procés, configuració per dispositiu, costos, balanç total)
```

.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`__calc_total_balance`](../../Optimizer/OptimalScheduler/General.md#__calc_total_balance), [`__optimize`](../../Optimizer/OptimalScheduler/General.md#__optimize), [`configure_varbounds`](../../Optimizer/OptimalScheduler/General.md#configure_varbounds), [`get_hourly_config_for_device`](../../Optimizer/OptimalScheduler/General.md#get_hourly_config_for_device), [`get_hourly_electric_prices`](../../Optimizer/OptimalScheduler/General.md#get_hourly_electric_prices), [`get_sensor_forecast_data`](../../Optimizer/OptimalScheduler/General.md#get_sensor_forecast_data), [`prepare_data_for_optimization`](../../Optimizer/OptimalScheduler/General.md#prepare_data_for_optimization)



---

### `prepare_data_for_optimization` {: #prepare_data_for_optimization }
Carrega i inicialitza els dispositius des de fitxers de configuració per preparar l'entorn d'optimització.

Escaneja el directori de configuracions desades, llegeix els fitxers JSON corresponents
i instancia cada dispositiu utilitzant una fàbrica (factory). Els objectes resultants
s'organitzen en diccionaris segons la seva categoria funcional (Generadors, Consumidors
o Sistemes d'Emmagatzematge) per ser utilitzats posteriorment en el càlcul del balanç energètic.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.prepare_data_for_optimization()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

True si s'han trobat i carregat configuracions amb èxit; False si no hi ha cap fitxer de configuració disponible.



---

### `get_sensor_forecast_data` {: #get_sensor_forecast_data }
Recupera la predicció de dades d'un sensor específic per a un dia determinat i l'alinea temporalment.

Aquest mètode obté les dades de forecast des de la base de dades, calcula el rang de temps
pertinent segons l'horitzó d'optimització (avui o demà) i reconstrueix una sèrie temporal
completa. En cas que falten dades per a hores específiques dins de la finestra temporal
definida, s'omplen amb zeros.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_sensor_forecast_data(sensor_id=..., today=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `sensor_id`: Identificador únic del sensor en el sistema.
- `today`: Booleà que indica si es volen les dades del dia actual (True) o de l'endemà (False).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla que conté:

```python
([1.2, 0.5, 0.0, . . . ], ['2026-05-13 00:00', '2026-05-13 01:00', . . .])
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`get_data_from_forecast_from_date_and_sensorID`](../../SqlDB/sqlDB/FORECASTS.md#get_data_from_forecast_from_date_and_sensorID)



---

### `configure_varbounds` {: #configure_varbounds }
Estableix els límits inferiors i superiors (*constraints*) per a les variables del problema d'optimització.

Aquest mètode defineix l'espai de cerca per a l'algorisme mapejant cada dispositiu (consumidors,
generadors i bateries) a un rang d'índexs dins d'un vector global. Per a cada dispositiu, es
calculen els límits de potència mínima i màxima per a cada interval de temps de l'horitzó.
Aquests índexs (`vbound_start` i `vbound_end`) s'emmagatzemen en els objectes de dispositiu
per permetre la reconstrucció posterior de la solució.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.configure_varbounds()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

**scipy.optimize.Bounds** -> Objecte de restriccions que conté els vectors de límits
inferiors i superiors per a totes les variables de decisió.

```python
( lb=[0.0, 0.0, ..., -3000.0, -3000.0], ub=[1500.0, 1500.0, ..., 3000.0, 3000.0], keep_feasible=True )
```



---

### `__optimize` {: #__optimize }
Executa l'algorisme d'optimització d'Evolució Diferencial (DE) per trobar la millor configuració energètica.

Aquest mètode privat configura i llança un procés d'optimització estocàstica global basat en
poblacions. L'objectiu és minimitzar la funció de cost (`self.cost_DE`) dins dels límits
establerts (`self.varbound`), forçant la integritat de les variables per a una gestió
discreta (ON/OFF o potència entera). Utilitza una estratègia 'best1bin' amb inicialització
'halton' per assegurar una bona cobertura de l'espai de cerca.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.__optimize()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla que conté:

- np.ndarray: Vector de solució òptima amb els valors per a cada variable de decisió.

- float: El valor de la funció de cost per a la millor solució trobada.

```python
([1500, 0, 3000, 1, . . .], -12.45)
```



---

### `cost_DE` {: #cost_DE }
Funció objectiu per a l'algorisme d'optimització.
Aquest mètode actua com a interfície entre l'algorisme de cerca global i el motor de càlcul
energètic. Rep una configuració candidata generada per l'optimitzador i retorna el cost
associat invocant el mètode intern de balanç total. És la funció que l'algorisme intentarà
minimitzar iteració rere iteració.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.cost_DE(config=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: Vector de variables de decisió generat per l'algorisme d'optimització.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

El cost econòmic o penalització energètica de la configuració enviada.
Exemple:  **4.25** --> cost positiu ||   **-1.12** -> benefici/estalvi.


#### <i class="fa-solid fa-link"></i> Depèn de:
[`__calc_total_balance`](../../Optimizer/OptimalScheduler/General.md#__calc_total_balance)



---

### `__update_DE_step` {: #__update_DE_step }
Sense descripció.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
obj.__update_DE_step(bounds=..., convergence=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `bounds`: -
- `convergence`: -



---

### `__calc_total_balance` {: #__calc_total_balance }
Calcula el balanç energètic net i el cost econòmic total d'una configuració específica.

Aquest mètode és el nucli del simulador energètic. Combina les previsions globals de consum i
generació amb el comportament dels dispositius individuals (consumidors actius, generadors
i bateries). Calcula el flux d'energia hora a hora i hi aplica els preus de mercat de
l'electricitat per determinar el cost operatiu total. Si el paràmetre `total` és cert,
actualitza l'estat actual de la millor solució trobada.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.__calc_total_balance(config=..., total=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: Vector de dades amb la configuració candidata per a tots els dispositius.
- `total`: Booleà; si és True, retorna el cost total (float). Si és False, retorna el
vector de balanç detallat (list).


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Depenent del paràmetre 'total':
--> Si True: El cost econòmic total en unitats monetàries
--> Si False: Llista del balanç net per interval


#### <i class="fa-solid fa-link"></i> Depèn de:
[`__calc_total_balance_consumer`](../../Optimizer/OptimalScheduler/General.md#__calc_total_balance_consumer), [`__calc_total_balance_energy`](../../Optimizer/OptimalScheduler/General.md#__calc_total_balance_energy), [`__calc_total_balance_generator`](../../Optimizer/OptimalScheduler/General.md#__calc_total_balance_generator)



---

### `__calc_total_balance_consumer` {: #__calc_total_balance_consumer }
Simula el comportament de tots els dispositius consumidors segons una configuració donada.

Itera sobre la col·lecció de consumidors (com electrodomèstics intel·ligents o càrregues
programables), extraient del vector global la part de la configuració que correspon a
cadascun mitjançant els seus índexs de vinculació (`vbound_start` i `vbound_end`).
Executa la simulació individual de cada dispositiu per obtenir-ne el perfil de consum
temporal i els costos operatius interns.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.__calc_total_balance_consumer(config=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: Vector global de variables de decisió de l'optimitzador.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla que conté:
- llista de floats: Perfil de consum agregat per a tots els consumidors
- float: Suma dels costos operatius propis de tots els consumidors

```python
([float, float, . . .], float)
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`simula`](../../Assets/SonnenBattery/General.md#simula)



---

### `__calc_total_balance_generator` {: #__calc_total_balance_generator }
To Do


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.__calc_total_balance_generator(config=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: 



---

### `__calc_total_balance_energy` {: #__calc_total_balance_energy }
Simula l'impacte dels sistemes d'emmagatzematge (bateries) sobre el balanç energètic net.

Aquest mètode integra l'activitat de les bateries en el balanç prèviament calculat entre
consumidors i generadors. Per a cada sistema d'emmagatzematge, extreu la seva part
corresponent del vector de configuració i executa la seva simulació (càrrega o descàrrega).
Els valors resultants s'afegeixen al balanç global, modificant la corba d'energia final
que s'haurà d'importar o exportar a la xarxa elèctrica.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.__calc_total_balance_energy(config=..., total_balance=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: Vector global de variables de decisió de l'optimitzador.
- `total_balance`: Llista amb el balanç net actual (Consum - Generació) abans de bateries.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una tupla que conté el balanç energètic final després de l'efecte de les bateries i la suma dels costos operatius o degradació dels sistemes d'emmagatzematge.

```python
([float, float, . . .], float)
```


#### <i class="fa-solid fa-link"></i> Depèn de:
[`simula`](../../Assets/SonnenBattery/General.md#simula)



---

### `get_hourly_electric_prices` {: #get_hourly_electric_prices }
Descarrega i processa els preus del mercat elèctric marginal (OMIE) per a l'horitzó d'optimització.

Es connecta al portal d'OMIE per obtenir el fitxer de preus horaris del dia actual. El mètode
descarrega un fitxer CSV temporal, n'extreu els preus de la darrera columna i els adapta a la
resolució temporal definida pel sistema (`horizon_min`). Si l'horitzó d'optimització supera
les 24 hores, el mètode reinicia el cicle de preus per cobrir tot el període.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_hourly_electric_prices()
```


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Una llista amb el preu de l'energia per a cada interval de l'optimització.
Retorna -1 en cas de fallada en la descàrrega.

```python
[45.12, 45.12, 42.05, 42.05, 38.90, 38.90, . . .]
```



---

### `get_hourly_config_for_device` {: #get_hourly_config_for_device }
Descodifica el vector de solució de l'optimitzador en un format llegible per dispositiu.

Aquest mètode rep el vector numèric pla generat per l'algorisme d'Evolució Diferencial
i el fragmenta segons els índexs de vinculació (`vbound_start` i `vbound_end`) de cada
actuador. El resultat és un diccionari on cada clau és el nom del dispositiu i el valor
és la seva seqüència de consignes d'activació o potència per a tot l'horitzó.


#### <i class="fa-solid fa-laptop-code"></i> Exemple d'ús

```python
resultat = obj.get_hourly_config_for_device(config=...)
```


#### <i class="fa-solid fa-arrow-right-to-bracket"></i> Paràmetres

- `config`: Array de variables de decisió resultant de l'optimització.


#### <i class="fa-solid fa-arrow-right-from-bracket"></i> Valor de retorn

Diccionari amb la planificació detallada per a cada dispositiu.

```python
{
    'Rentadora': [0.0, 1.0, 1.0, 0.0, . . .],
    'Bateria_Sonnen': [-1500, -1500, 2000, . . .],
    'Escalfador': [1200, 1200, 0, 0, . . .] 
}
```



---

