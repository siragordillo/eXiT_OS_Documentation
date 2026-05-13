# Control energètic eXIT (`databaseView.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#graphs-form`
    - `#sensor-data`
    - `#selected-sensors`
    - `#sensor-search`
    - `#sensor-list`
    - `#sensors-input`
    - `#fetch-data`
    - `#update-database`
    - `#delete-database`
    - `#graph-container`
    - `#self-destruct-modal`
    - `#modal-box`
    - `#modal-title`
    - `#modal-text`
    - `#btn-yes`
    - `#btn-no`
    - `#explosion-container`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-anchor" style="color: #990033;"></i> Constants Globals
    - **`selectedSensors`**: #region select sensors
    let sensors = document.getElementById("sensor-data").getAttribute("data-sensors").split(",");
    sensors = sensors.map(sensor => sensor.replace(/['\[\]]/g, ''));
    - **`li`**: Funció per actualitzar el hidden input field
    function updateSensorsHiddenInput() {
        sensorsInput.value = Array.from(selectedSensors).join(",");
    }

    //Funció per actualitzar els sensors del Dropdown
    function updateSensorList(filteredSensors) {
        sensorList.innerHTML = "";
        if (filteredSensors.length > 0) {
            sensorList.style.display = "block";
            filteredSensors.forEach(sensor => {
    - **`query`**: Mostra la llista completa de sensors
    sensorSearch.addEventListener("focus", () => {
        updateSensorList(sensors);
    });

    //Filtra dinamicament mentre s'escriu
    sensorSearch.addEventListener("input", () => {
    - **`tag`**: selecciona sensor i afageix com a tag
    function selectSensor(sensor) {
        if (!selectedSensors.has(sensor)) {
            selectedSensors.add(sensor);
    - **`sensors`**: Eliminar tag de sensor
    function removeSensor(event, sensor) {
        selectedSensors.delete(sensor);

        //elimina només el sensor clicat
        event.target.parentElement.remove();
        updateSensorsHiddenInput()
    }

    //amaga la llista al fer clic a fora
    document.addEventListener("click", (event) => {
        if (!event.target.closest(".dropdown")) {
            sensorList.style.display = "none";
        }
    });

    //#endregion select sensors

    //#region graph generation
    function FetchGraph() {
    - **`modal`**: #endregion graph generation

    //#region SELF DESTRUCT BUTTON

    #### <i class="fa-solid fa-network-wired" style="color: #990033;"></i> Dependències API (Pàgina)
    [`get_graph_info`](../../Server/server/General.md#get_graph_info), [`force_update_database`](../../Server/server/General.md#force_update_database), [`self_destruct`](../../Server/server/General.md#self_destruct)

