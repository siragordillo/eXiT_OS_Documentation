# Control energètic eXIT (`sensors.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#onlySavedSwitch`
    - `#saveBtn`
    - `#selectAllBtn`
    - `#deselectAllBtn`
    - `#devices-form`
    - `#devices-table`
    - `#devices-table-body`
    - `#saveResult`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-anchor" style="color: #990033;"></i> Constants Globals
    - **`ENTITY_TYPES`**: comentari Entity_Types
    - **`devicesTableBody`**: comentari devicesTableBody
    - **`onlySavedSwitch`**: comentari onlySavedSwitch

    #### <i class="fa-solid fa-network-wired" style="color: #990033;"></i> Dependències API (Pàgina)
    [`get_sensors`](../Server/server/General.md#get_sensors), [`update_sensors`](../Server/server/General.md#update_sensors)

    ### `LoadDevices`
    Carrega dispositius amb un fetch i els renderitza en pantalla. Assumim que fetch retorna format { "<device name>": [ {entity_id, friendly_name}, ... ], ... }

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    LoadDevices()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_sensors`](../Server/server/General.md#get_sensors)

    ---

    ### `RenderDevices`
    Renderitza creant una fila per a cada dispositiu i una subtaula per les entitats.

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    RenderDevices()
    ```

    ---

    ### `CreateDeviceRow`
    Crea una fila per a cada dispositiu + files per a la subtaula d'entitats

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    CreateDeviceRow(index=..., deviceName=..., entities=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `index`: -
    - `deviceName`: -
    - `entities`: -

    ---

    ### `CreateEntityRow`
    Crea la fila per a cada entitat

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    CreateEntityRow(ent=..., entIdx=..., devCheckbox=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `ent`: -
    - `entIdx`: -
    - `devCheckbox`: -

    ---

    ### `ToggleAll`
    Marca o desmarca totes les entitats i dispositius

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    ToggleAll(select=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `select`: -

    ---

    ### `ToggleOnlySaved`
    Alterna la vista entre tots els dispositius o només aquells guardats.

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    ToggleOnlySaved()
    ```

    ---

    ### `SaveDevices`
    Envia les dades seleccionades al backend per a guardar-les a la base de dades

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    SaveDevices()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`update_sensors`](../Server/server/General.md#update_sensors)

    ---

    ### `ScrollToTop`
    Petita funcionalitat per retornar la pàgina a la part superior en premer el botó

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    ScrollToTop()
    ```

    ---

