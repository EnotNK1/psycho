from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Demo</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style>
        body {
            background-color: #f8f9fa;
        }
        h1 {
            color: #343a40;
        }
        ul#messages {
            list-style-type: none;
            padding: 0;
            max-height: 300px;
            overflow-y: auto;
        }
        ul#messages li {
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
        }
        ul#messages li:nth-child(odd) {
            background-color: #e9ecef;
        }
        ul#messages li:nth-child(even) {
            background-color: #dee2e6;
        }
    </style>
</head>
<body>
<div class="container mt-5">
    <div class="card shadow">
        <div class="card-header text-center">
            <h1>FastAPI WebSocket Chat</h1>
        </div>
        <div class="card-body">
            <h2>Your ID: <span id="ws-id"></span></h2>
            <form action="" onsubmit="sendMessage(event)">
                <div class="input-group mb-3">
                    <input type="text" class="form-control" id="messageText" placeholder="Type your message here..." autocomplete="off" />
                    <button class="btn btn-primary" type="submit">Send</button>
                </div>
            </form>
            <ul id="messages" class="border p-3"></ul>
        </div>
    </div>
</div>
<script>
    var client_id = Date.now();
    document.querySelector("#ws-id").textContent = client_id;
    var ws = new WebSocket(`ws://localhost:8080/ws/${client_id}`);
    ws.onmessage = function(event) {
        var messages = document.getElementById('messages');
        var message = document.createElement('li');
        var content = document.createTextNode(event.data);
        message.appendChild(content);
        messages.appendChild(message);
        messages.scrollTop = messages.scrollHeight; // Auto-scroll to the latest message
    };
    function sendMessage(event) {
        var input = document.getElementById("messageText");
        if (input.value.trim() !== "") { // Prevent sending empty messages
            ws.send(input.value.trim());
            input.value = '';
        }
        event.preventDefault();
    }
</script>
</body>
</html>

"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} has left the chat")


