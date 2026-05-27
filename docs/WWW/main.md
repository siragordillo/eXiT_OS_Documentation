# Control energètic eXIT (`main.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#scheduler-grid`
    - `#forecast-grid`
    - `#device-config-grid`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-network-wired" style="color: #990033;"></i> Dependències API (Pàgina)
    [`panik_function`](../Server/server/General.md#panik_function), [`get_forecast_data/`](../Server/server/General.md#get_forecast_data/), [`get_scheduler_data`](../Server/server/General.md#get_scheduler_data), [`get_config_file_names`](../Server/server/General.md#get_config_file_names), [`get_device_config_and_state/`](../Server/server/General.md#get_device_config_and_state/), [`get_device_config_data/`](../Server/server/General.md#get_device_config_data/)

    ### `panikButtonTest`
    Funció purament per testejar. ELIMINAR QUAN ACABI DE DEBUGAR *

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    panikButtonTest()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`panik_function`](../Server/server/General.md#panik_function)

    ---

    ### `onLoadPage`
    Obté amb 2 fetch els forecastings guardats i el graph d'optimització

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    onLoadPage()
    ```

    ---

    ### `loadForecastsData`
    Carrega des del Backend el forecast per al sensor indicat i genera el plotly *

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    loadForecastsData(sensor_id=..., parent_div_forecast=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `sensor_id`: -
    - `parent_div_forecast`: -

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_forecast_data/`](../Server/server/General.md#get_forecast_data/)

    ---

    ### `loadSchedulerData`
    Carrega la gràfica de consum general del dia i genera el plotly (gràfica resultat de l'optimització) *

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    loadSchedulerData(parent_div_scheduler=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `parent_div_scheduler`: -

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_scheduler_data`](../Server/server/General.md#get_scheduler_data)

    ---

    ### `loadDevicesConfigData`
    Carrega les gràfiques de configuració horàries dels dispositius optimitzats *

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    loadDevicesConfigData(parent_div_config=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `parent_div_config`: -

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_config_file_names`](../Server/server/General.md#get_config_file_names), [`get_device_config_and_state/`](../Server/server/General.md#get_device_config_and_state/), [`get_device_config_data/`](../Server/server/General.md#get_device_config_data/)

    ---

