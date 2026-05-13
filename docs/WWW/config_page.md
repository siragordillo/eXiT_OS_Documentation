# Control energètic eXIT (`config_page.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#user-name`
    - `#global-consumption`
    - `#global-generation`
    - `#map`
    - `#info`
    - `#address`
    - `#lockBtn`
    - `#unlockBtn`
    - `#last-link-div`
    - `#certificates-container`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-anchor" style="color: #990033;"></i> Constants Globals
    - **`form`**: #region Map
  var lat = {{ location['lat']}};
  var lon = {{ location['lon']}};


  var map = L.map('map').setView([lat, lon], 15); // Coordenades per centrar el mapa

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
  }).addTo(map);
  var marker = L.marker([lat, lon]).addTo(map);

  //obtenir direcció
  fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json`)
    .then(response => response.json())
    .then(data => {
      if (data.display_name) {
        document.getElementById('address').innerHTML += data.display_name;
        document.getElementById('info').style.display = 'block';
      }
    });
  //#endregion

  function setFormLock(locked) {
    - **`consumption`**: El botó d'unir sempre ha de quedar bloquejat si ja estem bloquejats
    if (locked) document.getElementById('lockBtn').disabled = true;
  }

  function lockForm() {
    setFormLock(true);

    #### <i class="fa-solid fa-network-wired" style="color: #990033;"></i> Dependències API (Pàgina)
    [`save_config`](../../Server/server/General.md#save_config), [`delete_config`](../../Server/server/General.md#delete_config), [`get_res_certify_data`](../../Server/server/General.md#get_res_certify_data)

