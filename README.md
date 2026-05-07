# LogiMath 📚

**Plataforma educativa integral** para estudiantes: Logic, Matemáticas, Química, Física y Programación en una sola app.

**Arquitectura:**
- **Backend:** FastAPI + PostgreSQL (REST API)
- **Frontend:** Kivy (Python) → APK Android
--lo hara angel esta parte, no toquen--
- **DevOps:** Docker + Docker Compose (desarrollo local), Render.com (producción **FUTURO**)
- **CI/CD:** GitHub Actions (próximamente), DevSecOps (SAST scanning)

---

## 📋 Tabla de Contenidos

1. [Inicio Rápido](#inicio-rápido)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Requisitos Previos](#requisitos-previos)
4. [Setup Local (Docker)](#setup-local-docker)
5. [Desarrollo sin Docker](#desarrollo-sin-docker)
6. [APIs y Endpoints](#apis-y-endpoints)
7. [Features Principales](#features-principales)
8. [Despliegue en Render.com](#despliegue-en-rendercom)
9. [Workflow de Equipo](#workflow-de-equipo)
10. [Troubleshooting](#troubleshooting)

---

## 🚀 Inicio Rápido

### Con Docker (Recomendado para desarrollo en equipo)

```bash
# Clonar el repo
git clone https://github.com/StrawBerryNode/LogiMath.git
cd LogiMath

# Construir las imágenes
docker-compose build

# Ejecutar servicios (backend + frontend + db)
docker-compose up --build
```

**URLs locales:**
- Backend: `http://localhost:8000`
- Docs interactivos: `http://localhost:8000/docs`
- Frontend Kivy: Se ejecuta en contenedor, acceso via `localhost:5000` si está configurado

**Base de datos:** PostgreSQL corre automáticamente en `localhost:5432`

### Sin Docker (Desarrollo rápido individual)

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (en otra terminal)
cd frontend
pip install -r requirements.txt
python main.py
```

---

## 📁 Estructura del Proyecto
**A FUTURO SE PLANEA SER ASi**
```
LogiMath/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Punto de entrada FastAPI
│   │   ├── models/              # Modelos SQLAlchemy (User, Course, Quiz, etc)
│   │   ├── schemas/             # Schemas Pydantic (request/response)
│   │   ├── routes/              # Blueprints de rutas (auth, courses, quizzes)
│   │   ├── database.py          # Conexión PostgreSQL + SessionLocal
│   │   └── config.py            # Variables de entorno
│   ├── requirements.txt          # pip freeze output
│   ├── Dockerfile               # Imagen Docker del backend
│   └── .env.example             # Variables de entorno (renombrar a .env)
├── frontend/
│   ├── main.py                  # Entry point Kivy
│   ├── screens/                 # Pantallas Kivy (Home, Quiz, Results, etc)
│   ├── services/                # Clientes HTTP (APIClient, AuthService)
│   ├── assets/                  # Imágenes, fuentes, estilos
│   ├── requirements.txt
│   ├── Dockerfile               # Imagen Docker del frontend
│   └── buildozer.spec           # Config para compilar APK
├── docker-compose.yml           # Orquestación: backend + frontend + db
├── render.yaml                  # Deploy en Render (auto-detectado)
├── .gitignore
├── .env                         # NO COMMITEAR (local solo)
└── README.md                    # Este archivo
```

---

## 📦 Requisitos Previos

### Instalación de Docker y Docker Compose

**En Windows:**
1. Descargar [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Instalar y reiniciar
3. Verificar: `docker --version && docker-compose --version`


### Verificación
```bash
docker --version
# Docker version 24.x.x

docker-compose --version
# Docker Compose version 2.x.x
```

### Otros requisitos

- **Git** para clonar el repo
- **Python 3.9+** (si desarrollas sin Docker)
- **Node.js** 

---

## 🐳 Setup Local (Docker)

### 1. Clonar y configurar variables de entorno

```bash
git clone https://github.com/StrawBerryNode/LogiMath.git
cd LogiMath

# Crear archivo .env en raíz (NO SE COMMITEA)
cat > .env << EOF
# Backend
DATABASE_URL=postgresql://logimath_user:logimath_pass@db:5432/logimath_db
SECRET_KEY=tu-clave-secreta-aqui-cambiar-en-produccion
DEBUG=True
ENVIRONMENT=development

# Base de datos
POSTGRES_USER=logimath_user
POSTGRES_PASSWORD=logimath_pass
POSTGRES_DB=logimath_db
EOF
```

### 2. Construir servicios

```bash
docker-compose build
```

Esto:
- Construye la imagen del backend desde `backend/Dockerfile`
- Construye la imagen del frontend desde `frontend/Dockerfile`
- Descarga imagen oficial de PostgreSQL

### 3. Levantar servicios

```bash
docker-compose up --build
```

**Salida esperada:**
```
backend_1  | INFO: Started server process
db_1       | LOG: database system is ready to accept connections
frontend_1 | [INFO] Kivy app started
```

### 4. Verificar servicios

En otra terminal:
```bash
# Ver contenedores corriendo
docker-compose ps

# Ver logs del backend
docker-compose logs backend

# Ver logs de la base de datos
docker-compose logs db
```

### 5. Detener servicios

```bash
docker-compose down

# O con -v para limpiar volúmenes (SQL se borra)
docker-compose down -v
```

---


### Backend (FastAPI)

```bash
cd backend

# Crear entorno virtual 
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear base de datos PostgreSQL local (o usar Docker solo para DB)
# Opción A: Usar PostgreSQL nativo
createdb logimath_db
# Opción B: Docker solo para DB
docker run --name logimath_db -e POSTGRES_PASSWORD=logimath_pass -e POSTGRES_DB=logimath_db -p 5432:5432 -d postgres:15

# Variables de entorno
export DATABASE_URL=postgresql://logimath_user:logimath_pass@localhost:5432/logimath_db
export SECRET_KEY=dev-key-cambiar-en-prod
export DEBUG=True

# Ejecutar servidor (auto-reload en cambios)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Acceso a la API:**
- Base: `http://localhost:8000`
- Docs Swagger: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Frontend (Kivy)

```bash
cd frontend

# Entorno virtual
python -m venv venv
source venv/bin/activate

# Dependencias
pip install -r requirements.txt

# Ejecutar app
python main.py
```

---

## 🔌 APIs y Endpoints

### Estructura de rutas

```
backend/app/routes/
├── auth.py          # POST /api/auth/login, /api/auth/register
├── users.py         # GET/PUT /api/users/{id}
├── courses.py       # GET /api/courses, POST /api/courses/{id}/enroll
├── quizzes.py       # GET /api/quizzes, POST /api/quizzes/{id}/submit
└── results.py       # GET /api/results, GET /api/results/{user_id}
```

### Ejemplos principales

#### Autenticación
**TODAVIA NO HAY XD**
**gran parte de aca no existe o no funciona**
```bash
# Registro
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "password": "password123",
    "full_name": "Juan Pérez"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "password": "password123"
  }'
# Retorna: { "access_token": "...", "token_type": "bearer" }
```

#### Cursos

```bash
# Listar cursos
curl -X GET http://localhost:8000/api/courses \
  -H "Authorization: Bearer {token}"

# Inscribirse en un curso
curl -X POST http://localhost:8000/api/courses/1/enroll \
  -H "Authorization: Bearer {token}"
```

#### Quizzes

```bash
# Obtener quiz
curl -X GET http://localhost:8000/api/quizzes/1 \
  -H "Authorization: Bearer {token}"

# Enviar respuestas
curl -X POST http://localhost:8000/api/quizzes/1/submit \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "answers": [
      {"question_id": 1, "answer": "A"},
      {"question_id": 2, "answer": "C"}
    ]
  }'
```

#### Resultados

```bash
# Mis resultados
curl -X GET http://localhost:8000/api/results \
  -H "Authorization: Bearer {token}"

# Resultados de usuario específico (admin)
curl -X GET http://localhost:8000/api/results/user/5 \
  -H "Authorization: Bearer {token}"
```

**Para explorar interactivamente:** Abre `http://localhost:8000/docs` en el navegador

---

## ✨ Features Principales

### Materias soportadas

- **Lógica:** Tablas de verdad, silogismos, razonamientos
- **Matemáticas:** Álgebra, geometría, cálculo (según nivel)
- **Física:** Cinemática, dinámica, termodinámica, ondas
- **Química:** Estequiometría, enlaces, reacciones
- **Programación:** Python, Java, C++ (conceptos básicos)

### Funcionalidades

✅ Autenticación JWT + sesiones seguras  
✅ Registro y perfil de usuario  
✅ Catálogo de cursos por materia  
✅ Quizzes interactivos con retroalimentación inmediata  
✅ Seguimiento de progreso  
✅ Leaderboard 
✅ Historial de resultados  
✅ Roles (student, instructor, admin)  
falta lo de tete/logi (mascota) todavia sin definir con disfraces y todo

---

## 🚢 Despliegue en Render.com

### Proceso automático

1. **Push a GitHub**
   ```bash
   git add .
   git commit -m "Update features"
   git push origin main
   ```

2. **Render detecta cambios** (Esta parte tovia es innecesaria)
   - Lee `render.yaml` automáticamente
   - Construye imágenes Docker
   - Crea/actualiza servicios
   - Ejecuta migraciones (si las hay)

3. **Resultado**
   - Backend: `https://logimath-backend.onrender.com` (o tu nombre)
   - DB: PostgreSQL privada en Render

### Archivo render.yaml

```yaml
services:
  - type: web
    name: logimath-backend
    env: docker
    dockerfilePath: backend/Dockerfile
    envVars:
      - key: DATABASE_URL
        scope: run
        value: ${DATABASE_URL}
      - key: SECRET_KEY
        scope: run
        value: ${SECRET_KEY}
      - key: ENVIRONMENT
        scope: run
        value: production
    healthCheckPath: /health
    
  - type: pserv
    name: logimath-db
    ipAllowList: []  # Abierto solo a los servicios web
    plan: free
    postgresVersion: 15
```

### Setup inicial en Render

1. Crear cuenta en [Render.com](https://render.com)
2. Conectar repositorio GitHub
3. Crear nuevo "Web Service":
   - Apuntar a repo LogiMath
   - Seleccionar `main` branch
   - Environment: Docker
4. Crear PostgreSQL Database (puede ser free tier por todo el año)
5. Copiar `DATABASE_URL` a variables de entorno del Web Service
6. Deploy

**Nota:** Free tier de Render duerme después de 15 min sin tráfico, perfecto para desarrollo.

---

## 👥 Workflow de Equipo

### Antes de empezar

```bash
# Clonar repo
git clone https://github.com/StrawBerryNode/LogiMath.git
cd LogiMath

# Crear rama personal
git checkout -b feature/mi-feature
```

### Durante desarrollo (con Docker)

```bash
# Terminal 1: Servicios corriendo
docker-compose up --build

# Terminal 2: Cambios en código (hot reload automático)
# Editar archivos en backend/ o frontend/
# Docker recompila automáticamente por volúmenes montados
```

### Para hacer commit

```bash
# Ver cambios
git status

# Agregar cambios
git add .

# Commit descriptivo
git commit -m "feat: agregar validación en quiz submit

- Validar que todas las respuestas estén presentes
- Calcular puntaje correctamente
- Retornar detalles en response"

# Push a tu rama
git push origin feature/mi-feature
```

### Pull Request

1. Abre PR en GitHub con descripción clara
2. Otros revisan código
3. Merge a `main` cuando esté aprobado
4. Render despliega automáticamente

### Commits atómicos

Cada commit debe:
- Hacer UNA cosa (no mezclar features)
- Ser testeable por sí solo
- Tener mensaje descriptivo

Ejemplo malo:
```
git commit -m "stuff" ❌
```

Ejemplo bueno:
```
git commit -m "fix: corregir cálculo de puntaje en quizzes

- Usar división float en lugar de int
- Agregar validación de preguntas respondidas
- Tests agregados" ✅
```

---

## 🛠️ Troubleshooting

### Docker no inicia

**Error:** `docker: command not found`
```bash
# Solución: Instalar Docker Desktop o docker.io
# Ver sección "Requisitos Previos"
```

### Volúmenes no se sincronizan (cambios no aparecen)

```bash
# Solución: Reconstruir
docker-compose down -v
docker-compose up --build

# O: Limpiar caché de Docker
docker system prune -a
```

### Puerto 5432 ya en uso (PostgreSQL)

```bash
# Cambiar puerto en docker-compose.yml
ports:
  - "5433:5432"  # Host:Container

# Actualizar DATABASE_URL
DATABASE_URL=postgresql://user:pass@db:5432/db  # Interno
# (El puerto interno siempre es 5432 en el contenedor)
```

### Backend no conecta a BD

**Error:** `psycopg2.OperationalError: could not translate host name "db" to address`

```bash
# Verificar que db está corriendo
docker-compose ps

# Ver logs de la BD
docker-compose logs db

# Verificar DATABASE_URL en .env
cat .env | grep DATABASE_URL
```

### Kivy no carga en contenedor

**Error:** `DISPLAY not set`

```bash
# Esto es normal en Docker headless
# Usa archivo .kv o API headless para testing
# Para desarrollo visual, ejecuta Kivy sin Docker:
cd frontend && python main.py
```

### Git no deja hacer push (permisos)

```bash
# Verificar que tienes acceso al repo
git remote -v

# Si es problema de SSH
ssh -T git@github.com  # Debe mostrar tu username

# Si falla, agregar clave SSH
# Ver: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

---

## 📚 Recursos Adicionales

- **FastAPI Docs:** https://fastapi.tiangolo.com
- **Kivy Tutorial:** https://kivy.org/doc/stable/gettingstarted/intro.html
- **PostgreSQL + SQLAlchemy:** https://docs.sqlalchemy.org/en/20/orm/
- **Docker Compose:** https://docs.docker.com/compose/
- **Render Docs:** https://render.com/docs

---

## 📝 Licencia

LogiMath © 2024 StrawBerryNode. Todos los derechos reservados.

--