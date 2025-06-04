# 📚 BookSwap - Sistema de Intercambio de Libros

BookSwap es una plataforma web que permite a los usuarios registrarse, publicar libros físicos disponibles para intercambio y buscar libros de otros usuarios según la ubicación y autor. Está desarrollado con Django para la lógica de servidor y frontend, y preparado para integraciones con FastAPI.

## 🚀 Tecnologías utilizadas

- Python 3.13
- Django 5.x
- FastAPI (API REST para calificaciones)
- TailwindCSS (CDN)
- HTML5, CSS3
- SQLite (modo desarrollo)
- Docker (opcional)
- Git (versionado)
- Render (para deploy futuro)

## 📂 Estructura del proyecto

```bash
bookswap_project/
├── backend/                # Proyecto principal de Django
│   └── settings.py
├── api/                    # FastAPI: calificaciones, usuarios, solicitudes
│   ├── database.py         # Conexión con SQLite
│   ├── models.py           # Modelos SQLAlchemy
│   ├── exchange            # Endpoints de intercambio
│   │── books               # Endpoints de libros
│   │── history             # Endpoints de historial de intercambios
│   │── ratings             # Endpoints de calificaciones
│   │── users               # Endpoints de usuarios
│   └── main.py             # Instancia de FastAPI
├── users/                  # App para registro, login y modelo CustomUser
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── books/                  # App para publicar e intercambiar libros
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/              # Templates HTML organizados por módulo
│   ├── products/           # base.html y home.html
│   ├── users/              # login.html y register.html
│   └── books/              # create_book.html, my_books.html, exchange_books.html
├── static/                 # Archivos estáticos (opcional)
├── manage.py               # Comando principal de Django
└── requirements.txt        # Requisitos de Python
```

## ⚙️ Instrucciones de instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Jeff-Deck/bookswap.git
cd bookswap
```

2. Crea un entorno virtual e instálalo:
```bash
python -m venv env
env\Scripts\activate  # En Windows
pip install -r requirements.txt
```

3. Aplica las migraciones y crea superusuario:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Ejecuta el servidor de Django:
```bash
python manage.py runserver
```

5. Ejecuta FastAPI (en otra terminal y otro puerto):
```bash
uvicorn api.main:app --reload --port 8001
```

6. Accede desde el navegador a:
- Registro/Login: http://localhost:8000/users/
- Publicar libro: http://localhost:8000/books/crear/
- Intercambiar libros: http://localhost:8000/books/intercambiar/
- Admin: http://localhost:8000/admin/

## 📩 Notas adicionales

- Las calificaciones entre usuarios se gestionan exclusivamente desde FastAPI.
- El chat entre usuarios solo se activa si ambas partes han aceptado e iniciado el intercambio (`initiated = True`).
- El proyecto está listo para ser desplegado en Render u otras plataformas.

## 🧾 Autor

- Jefferson Ruiz - [UDLA - Ingeniería de Software]
- Contacto personal: je1400r@gmail.com
