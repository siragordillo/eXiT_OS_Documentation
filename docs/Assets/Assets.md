# Gestió d'Actius (Assets)

<div class="hero-container">
    <div class="card-icon"><i class="fa-solid fa-microchip"></i></div>
    <h1 class="hero-title">Gestió d'Actius</h1>
    <p class="hero-subtitle">
        Documentació detallada de tots els actius físics i sensors integrats en el sistema eXiT OS. 
        Aquí trobaràs la lògica de control, simulació i gestió de flexibilitat per a cada dispositiu.
    </p>
</div>

## 🔌 Actius Disponibles

<div class="card-grid">
    <a href="EVCharger/General/" class="custom-card centered">
        <div class="card-icon"><i class="fa-solid fa-bolt"></i></div>
        <div class="card-title">Carregador VE</div>
        <div class="card-description">
            Lògica de control per a carregadors de vehicles elèctrics, incloent simulació de càrrega i gestió de la flexibilitat.
        </div>
        <div class="card-footer">Veure mètodes ➔</div>
    </a>
    
    <a href="ShellyPlus1pm/General/" class="custom-card centered">
        <div class="card-icon"><i class="fa-solid fa-toggle-on"></i></div>
        <div class="card-title">Shelly Plus 1PM</div>
        <div class="card-description">
            Integració amb relés Shelly per al monitoratge de potència i control remot de càrregues individuals.
        </div>
        <div class="card-footer">Veure mètodes ➔</div>
    </a>
    
    <a href="SonnenBattery/General/" class="custom-card centered">
        <div class="card-icon"><i class="fa-solid fa-car-battery"></i></div>
        <div class="card-title">Bateria Sonnen</div>
        <div class="card-description">
            Control i monitoratge de sistemes d'emmagatzematge d'energia Sonnen, gestionant estats de càrrega i descàrrega.
        </div>
        <div class="card-footer">Veure mètodes ➔</div>
    </a>
</div>

---

> [!NOTE]
> Cada actiu hereta de la classe base `Asset` per garantir una interfície unificada amb l'optimitzador i el servidor central.
