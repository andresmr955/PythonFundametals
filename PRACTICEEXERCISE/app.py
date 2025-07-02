from aiohttp import web

# Lista en memoria para almacenar tareas
tasks = []

# Manejador para GET /tasks
async def get_tasks(request):
    return web.json_response(tasks)

# Manejador para POST /tasks
async def create_task(request):
    data = await request.json()
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Sin título"),
        "done": False
    }
    tasks.append(task)
    return web.json_response(task, status=201)

# Crear app y registrar rutas
app = web.Application()
app.add_routes([
    web.get('/tasks', get_tasks),
    web.post('/tasks', create_task)
])

# Ejecutar servidor
if __name__ == '__main__':
    web.run_app(app, port=8000)
