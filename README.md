# Instrucciones para ejecutar este proyecto de CODERHOUSE
### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix` y clonar el proyecto.

```bash
git clone https://github.com/sofiagt0413/familyApp.git \
cd familyApp
```

### 2. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv \
source venv/bin/activate
```

### 3. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 4. Crear las migraciones si hay algún cambio o un nuevo modelo
```bash
python manage.py makemigrations
```

### 5. Correr las migraciones para que cree todo lo necesario en la base de datos
```bash
python manage.py migrate
```
### 6. Levantar el servidor de Django que expone el servicio en el puerto por defecto 8000
```bash
python manage.py runserver
```

- Es hora de ir al navegador y en una pestaña nueva navegar hacia `http://127.0.0.1:8000/` o `http://localhost:8000/` para visualizar la paguina principal en esta encontara un menu lateral para navegar por las diferentes funcionalidades