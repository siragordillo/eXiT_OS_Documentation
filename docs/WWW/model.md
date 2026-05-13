# Control energètic eXIT (`model.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#lang-input`
    - `#models`
    - `#modelName`
    - `#sensorsId`
    - `#sensor-data`
    - `#selected-sensors`
    - `#sensor-search`
    - `#sensor-list`
    - `#sensors-input`
    - `#modelSelect`
    - `#modelConfig`
    - `#scaled`
    - `#windowingOption`
    - `#customWindowingInputs`
    - `#windowStart`
    - `#windowEnd`
    - `#meteoData`
    - `#create-model-button`
    - `#fetch-data`
    - `#delete-forecast`
    - `#forecast-chart-container`
    - `#forecast-title`
    - `#forecast-chart`
    - `#metrics-section`
    - `#main-metrics`
    - `#metrics-table-body`
    - `#dataset-info`
    - `#dataset-info-content`
    - `#validation-warnings`
    - `#warnings-content`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-network-wired" style="color: #990033;"></i> Dependències API (Pàgina)
    [`get_model_config/`](../../Server/server/General.md#get_model_config/), [`get_forecast_data/`](../../Server/server/General.md#get_forecast_data/), [`get_model_metrics/`](../../Server/server/General.md#get_model_metrics/)

    ### `updateSensorsHiddenInput`
    Funció per a actualitzar el hidden input field*

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    updateSensorsHiddenInput()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_model_config/`](../../Server/server/General.md#get_model_config/), [`get_forecast_data/`](../../Server/server/General.md#get_forecast_data/), [`get_model_metrics/`](../../Server/server/General.md#get_model_metrics/)

    ---

