"#django-polls" 
"#django-polls" 
Após clonar o repositório 

No terminl:

    python -m venv venv
    .\venv\Scripts\activate.bat
    pip install django

     pip install -r requirements.txt

verificar: 
    python manage.py runserver

Para cancelar servidor:
    CTRL + C

Criar 1º app (módulo) Django
    django-admin startapp polls

    alt + shift + f = formatar

exclui as tabelas do banco de dados:
    python manage.py migrate contenttypes zero