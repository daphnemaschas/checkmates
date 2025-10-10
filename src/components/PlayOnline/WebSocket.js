// WebSocket.js

class WebSocketInstance {
    constructor() {
      this.socket = null;
    }
  
    connect(gameNumber) {
      this.socket = new WebSocket(`ws://localhost:8000/ws/game/${gameNumber}/`);
      this.socket.onopen = () => {
        console.log('WebSocket connected');
      };
  
      this.socket.onmessage = (event) => {
        console.log('Received message:', event.data);
        // Traitement des messages reçus du serveur WebSocket
      };
  
      this.socket.onclose = () => {
        console.log('WebSocket closed');
      };
    }
  
    sendMessage(message) {
      this.socket.send(JSON.stringify(message));
    }
  }
  
  const webSocketInstance = new WebSocketInstance();
  export default webSocketInstance;
  