Exercices OpenAPI avec Enoncés et Solutions YAML

Exercice 1 : API de gestion de livres

```yaml
# Énoncé :
# Crée une spécification OpenAPI pour une API de gestion de livres :
# - GET /books → Liste de tous les livres
# - POST /books → Ajout d’un livre
# - GET /books/{id} → Détail d’un livre par ID
#
# Modèle Book :
# {
#   "id": 1,
#   "title": "Le Petit Prince",
#   "author": "Antoine de Saint-Exupéry",
#   "published_year": 1943
# }

openapi: 3.0.0
info:
  title: Books API
  version: 1.0.0
paths:
  /books:
    get:
      summary: Get all books
      responses:
        '200':
          description: List of books
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Book'
    post:
      summary: Add a new book
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Book'
      responses:
        '201':
          description: Book created
  /books/{id}:
    get:
      summary: Get book by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Book details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Book'
        '404':
          description: Book not found
components:
  schemas:
    Book:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        author:
          type: string
        published_year:
          type: integer
```

Énoncé :
Crée une API qui :
 GET /movies → Liste des films avec paramètres `limit` et `q`

 Modèle Movie :
 {
   "id": 1,
   "title": "Inception",
   "director": "Christopher Nolan",
   "year": 2010
 }

 ```yaml
 openapi: 3.0.0
info:
  title: Movies API
  version: 1.0.0
paths:
  /movies:
    get:
      summary: Get all movies
      parameters:
        - $ref: '#/components/parameters/limit'
        - $ref: '#/components/parameters/q'
      responses:
        '200':
          description: List of movies
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Movie'
components:
  parameters:
    limit:
      name: limit
      in: query
      schema:
        type: integer
      required: false
    q:
      name: q
      in: query
      schema:
        type: string
      required: false
  schemas:
    Movie:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        director:
          type: string
        year:
          type: integer
 ```

Énoncé :
Crée une API pour gérer des comptes utilisateurs :
POST /login → Authentification avec Basic Auth
GET /users → Liste des utilisateurs protégée par authentification

```yaml
openapi: 3.0.0
info:
  title: Auth Users API
  version: 1.0.0
paths:
  /login:
    post:
      summary: Login user
      security:
        - basicAuth: []
      responses:
        '200':
          description: Login successful
  /users:
    get:
      summary: Get all users
      security:
        - basicAuth: []
      responses:
        '200':
          description: List of users
components:
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(firstname: str, lastname: str):
    return {"message": f"Bonjour {firstname} {lastname}"}

```
```python
@app.get("/status")
def status(is_online: bool | None = None):
    if is_online is True:
        return {"status": "L’utilisateur est en ligne"}
    elif is_online is False:
        return {"status": "L’utilisateur est hors ligne"}
    return {"status": "Statut inconnu"}

```
```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.get("/secure-data")
def secure_data(request: Request):
    token = request.headers.get("X-Token")
    if token != "abc123":
        return JSONResponse(content={"error": "Accès refusé"}, status_code=403)
    return {"data": "Accès autorisé"}

```
```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"message": f"Utilisateur {user.username} enregistré avec succès"}

```
```python
from typing import List

class Task(BaseModel):
    title: str
    done: bool

tasks_store: List[Task] = []

@app.get("/tasks")
def list_tasks():
    return {"tasks": [task.dict() for task in tasks_store]}

@app.post("/tasks")
def add_task(task: Task):
    tasks_store.append(task)
    return {"tasks": [t.dict() for t in tasks_store]}

```
```python
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if 0 <= task_id < len(tasks_store):
        tasks_store[task_id] = task
        return {"tasks": [t.dict() for t in tasks_store]}
    return JSONResponse(content={"error": "Tâche non trouvée"}, status_code=404)

```

```python
@app.get("/tasks/paginated")
def paginated_tasks(page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    end = start + limit
    return {"tasks": [t.dict() for t in tasks_store[start:end]]}

```
```python
@app.get("/profile")
def profile(token: str):
    if token == "secret123":
        return {"user": "admin", "role": "superuser"}
    return JSONResponse(content={"error": "Non autorisé"}, status_code=401)

```


```python
from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse


app = FastAPI()

@app.get("/hello")
def read_hello(request: Request):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)
    return JSONResponse(content="Hello world", status_code=200)


class WelcomeRequest(BaseModel):
    name: str

@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}
def read_hello(name: str, is_teacher: bool):
    if is_teacher:
        return f"Hello Teacher {name}!"
    return f"Hello {name}!"


•	/hello?name=Ryan&is_teacher=true → Hello Teacher Ryan!
•	/hello?name=Rakoto&is_teacher=false → Hello Rakoto!

@app.get("/hello")
def read_hello(name: str = None, is_teacher: bool = None):
    if name is None and is_teacher is None:
        return "Hello world"
    if name is None:
        name = "Non fourni"
    if is_teacher is None:
        is_teacher = False
    if is_teacher:
        return f"Hello Teacher {name}!"
    return f"Hello {name}!"

•	/hello → Hello world
•	/hello?name=Ryan → Hello Ryan!
•	/hello?is_teacher=true → Hello Teacher Non fourni!


app = FastAPI()

class SecretModel(BaseModel):
    secret_code: int

@app.put("/top-secret")
def top_secret(request: Request, payload: SecretModel):
    auth = request.headers.get("Authorization")
    if auth != "my-secret-key":
        raise HTTPException(status_code=403, detail=f"Unauthorized: {auth}")

    code_str = str(payload.secret_code)
    if len(code_str) != 4:
        raise HTTPException(status_code=400, detail="Code must be 4 digits")

    return {"code": payload.secret_code}



•	En-tête Authorization: my-secret-key et JSON {"secret_code": 1234} → ✅ OK
•	Sinon → 403 ou 400


app = FastAPI()

@app.get("/")
def root(request: Request):
    accept = request.headers.get("Accept")
    if accept not in ["text/html", "text/plain"]:
        raise HTTPException(status_code=400, detail="Only text/html or text/plain supported")

    api_key = request.headers.get("x-api-key")
    if api_key != "12345678":
        raise HTTPException(status_code=403, detail="Invalid API key")

    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("404.html", "r", encoding="utf-8") as f:
        content = f.read()
    return Response(content=content, status_code=404, media_type="text/html")

gerer les evenements
class EventModel(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str

events_store: List[EventModel] = []

def serialized_stored_events():
    return [event.model_dump() for event in events_store]

@app.get("/events")
def list_events():
    return {"events": serialized_stored_events()}

@app.post("/events")
def add_events(new_events: List[EventModel]):
    events_store.extend(new_events)
    return {"events": serialized_stored_events()}

@app.put("/events")
def update_events(updated_events: List[EventModel]):
    for updated in updated_events:
        for i, existing in enumerate(events_store):
            if existing.name == updated.name:
                events_store[i] = updated
                break
        else:
            events_store.append(updated)  # si pas trouvé, on ajoute
    return {"events": serialized_stored_events()}

```