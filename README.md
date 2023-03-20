# my-movie-fastAPI

# Pasos

Para ejecutar la API debes seguir las siguentes instrucciones en una terminal:

# Windows
```sh
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

# Linux
```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
uvicorn main:app --reload
```

# Documentación
Ejemplo para ver la documentación con Swagger: http://127.0.0.1:8000/docs