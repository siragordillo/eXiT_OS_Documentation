# llmChat.html (`llmChat.html`)

=== "<i class=\"fa-solid fa-eye\"></i> Vista (HTML)"

    #### <i class="fa-solid fa-fingerprint" style="color: #990033;"></i> Elements Identificats (IDs)
    - `#clearBtn`
    - `#deleteBtn`
    - `#chatMessages`
    - `#loadingIndicator`
    - `#userInput`
    - `#sendBtn`
    - `#delete-conversation-modal`
    - `#confirmDeleteBtn`

=== "<i class=\"fa-solid fa-brain\"></i> Lògica (JavaScript)"

    #### <i class="fa-solid fa-anchor" style="color: #990033;"></i> Constants Globals
    - **`SERVER_BASE_URL`**: URL base del servidor eXiT (sempre port 55023, independentment d'on s'accedeixi)
    - **`chatMessages`**: Neteja visual del xat (no borra l'historial del servidor)
    function clearChatVisual() {
    - **`modal`**: Elimina tota la conversa: obre el modal de confirmació
    function deleteConversation() {
    - **`modal`**: Tanca el modal de confirmació
    function closeDeleteModal() {
    - **`res`**: Confirma i executa l'eliminació (crida l'API)
    async function confirmDeleteConversation() {
        closeDeleteModal();
        try {
    - **`res`**: Carrega l'historial de conversa del servidor en entrar a la pàgina
    async function loadChatHistory() {
        try {

