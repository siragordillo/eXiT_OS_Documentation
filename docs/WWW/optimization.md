# Control energètic eXIT (`optimization.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#test-optimization`
    - `#new-device-config`
    - `#scheduler-grid`
    - `#global-flexi-grid`
    - `#optimization-graphs-container`
    - `#new-optimization-modal`
    - `#device-type`
    - `#device-name`
    - `#restrictionsContainer`
    - `#vars-config-section`
    - `#control-vars-config-section`
    - `#${restriction.id}`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-anchor" style="color: #990033;"></i> Constants Globals
    - **`parent_config_div`**: Reload configurations when language changes
    I18n.onLanguageChange(async function (newLocale) {

        // Reload device types for the new language
        await loadDeviceTypes(newLocale);

        // Reload saved configurations with new translations

    #### <i class="fa-solid fa-network-wired" style="color: #990033;"></i> Dependències API (Pàgina)
    [`run_optimization`](../../Server/server/General.md#run_optimization), [`get_scheduler_data`](../../Server/server/General.md#get_scheduler_data), [`get_flexi_data`](../../Server/server/General.md#get_flexi_data), [`save_optimization_config`](../../Server/server/General.md#save_optimization_config), [`get_config_file_names`](../../Server/server/General.md#get_config_file_names), [`get_device_config_data/`](../../Server/server/General.md#get_device_config_data/), [`update_device_config`](../../Server/server/General.md#update_device_config), [`delete_optimization_config/`](../../Server/server/General.md#delete_optimization_config/)

    ### `loadDeviceTypes`
    Carrega les configuracions dels dispositius segons l'idioma seleccionat

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    loadDeviceTypes(locale=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `locale`: -

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`run_optimization`](../../Server/server/General.md#run_optimization)

    ---

    ### `onLoadPage`
    Funció que es crida en carregar la pàgina. Genera la gràfica d'optimització i crida la funció per a mostrar les configuracions guardades

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    onLoadPage()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_scheduler_data`](../../Server/server/General.md#get_scheduler_data), [`get_flexi_data`](../../Server/server/General.md#get_flexi_data)

    ---

    ### `NewDeviceConfig`
    Obre el formulari per a crear una nova configuració i l'omple dinàmicament.

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    NewDeviceConfig()
    ```

    ---

    ### `UpdateRestrictions`
    Modifica les restriccions segons el tipus de device seleccionat al formulari

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    UpdateRestrictions()
    ```

    ---

    ### `CreateSelectOption`
    Crea select i option per als paràmetres entrats

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    CreateSelectOption(container=..., varId=..., varName=..., dev=..., isControllVar=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `container`: -
    - `varId`: -
    - `varName`: -
    - `dev`: -
    - `isControllVar`: -

    ---

    ### `UpdateAssociatedVariables`
    Modifica els inputs per a les variables associades segons el tipus de dispositiu i entitats d'aquest

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    UpdateAssociatedVariables()
    ```

    ---

    ### `GetSelectedVariables`
    Retorna totes les variables seleccionades dins el div #vars-config-section. Busca tots els <select> dins aquest div, i per a cadascun recull totes les opcions seleccionades (amb id i friendly_name).

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    GetSelectedVariables()
    ```

    ---

    ### `showErroratSubmit`
    Mostra un missatge d'error sota un element concret si aquyest esta buit al moment de guardar.

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    showErroratSubmit(element=..., message=...)
    ```

    #### <i class="fa-solid fa-arrow-right-to-bracket" style="color: #990033;"></i> Paràmetres

    - `element`: element html que està buit al moment de guardar
    - `message`: Missatge que es mostrarà sota l'element

    ---

    ### `SubmitOptimization`
    Elimina els missatges d'error si l'usuari canvia el valor

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    SubmitOptimization()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`save_optimization_config`](../../Server/server/General.md#save_optimization_config)

    ---

    ### `CloseModal`
    Tanca el formulari

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    CloseModal()
    ```

    ---

    ### `LoadDevicesEntities`
    Omple el select amb els dispositius

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    LoadDevicesEntities()
    ```

    ---

    ### `LoadConfigsSaved`
    Carrega des del back-end les configuracions guardades

    #### <i class="fa-solid fa-laptop-code" style="color: #990033;"></i> Exemple de crida

    ```javascript
    LoadConfigsSaved()
    ```

    #### <i class="fa-solid fa-link" style="color: #990033;"></i> Dependències API
    [`get_config_file_names`](../../Server/server/General.md#get_config_file_names), [`get_device_config_data/`](../../Server/server/General.md#get_device_config_data/), [`update_device_config`](../../Server/server/General.md#update_device_config), [`delete_optimization_config/`](../../Server/server/General.md#delete_optimization_config/)

    #### <i class="fa-solid fa-arrow-right-from-bracket" style="color: #990033;"></i> Valor de retorn

    s {Promise<void>} Si les obté correctament les mostra a la pàgina.

    ---

