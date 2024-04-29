from fastapi import FastAPI

# uvicorn main:app To run the app
# --reload to reload the app when you make changes
# --port 8000 to run the app on a specific port
# --host 0.0.0.0 to run the app on all the network interfaces

# /docs and /redoc to acces to the documentation by FastAPI


app = FastAPI()

app.title = "NotesAPI"

users = [
    {
        "username": "usuario1",
        "email": "usuario1@example.com",
        "password": "contraseña1"
    },
    {
        "username": "usuario2",
        "email": "usuario2@example.com",
        "password": "contraseña2"
    }
]

@app.get("/")
def get_users():
    return users
