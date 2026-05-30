from fastapi import FastAPI
from models import Developer,Projects

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message":"Developer created successfully","developer":developer}

@app.post("/projects/")
def create_project(project: Projects):
    return {"message":"Project created successfully","project":project}

@app.get("/projects/")
def get_projects():
    sample_project = Projects(
        title = "Sample Project",
        description= "This is a sample project",
        language=["HTML","CSS","JavaScript"],
        lead_developer= Developer(name="John Doe",experience=5)
    )

    return{"projects":[sample_project]}