from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app import crud, schemas, models, auth
from app.db import get_db

router = APIRouter()

# --- PATCH schema ---
class IssueStatusUpdate(BaseModel):
    status: str

# --- User routes ---
@router.post('/users/', response_model=schemas.UserOut)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user_in.username)
    if existing:
        raise HTTPException(status_code=400, detail='Username already exists')
    return crud.create_user(db, user_in)

@router.post('/token', response_model=schemas.Token)
def login_for_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect username or password')
    access_token = auth.create_access_token({'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}

# --- Project routes ---
@router.post("/projects/", response_model=schemas.ProjectOut)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get('/projects/', response_model=list[schemas.ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return crud.list_projects(db)

@router.get('/projects/{project_id}', response_model=schemas.ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(404, 'Not found')
    return project

# --- Issue routes ---
@router.post('/issues/', response_model=schemas.IssueOut)
def create_issue(
    issue_in: schemas.IssueCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user)
):
    return crud.create_issue(db, issue_in, reporter_id=user.id)

@router.get('/issues/', response_model=list[schemas.IssueOut])
def list_issues(db: Session = Depends(get_db)):
    return crud.list_issues(db)

@router.patch('/issues/{issue_id}/status', response_model=schemas.IssueOut)
def update_status(
    issue_id: int,
    status_in: IssueStatusUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user)
):
    issue = crud.get_issue(db, issue_id)
    if not issue:
        raise HTTPException(404, 'Not found')
    if user.role != models.RoleEnum.admin and issue.reporter_id != user.id:
        raise HTTPException(403, 'Forbidden')
    return crud.update_issue_status(db, issue_id, status_in.status)

@router.get("/debug-sentry")
async def trigger_error():
    division_by_zero = 1 / 0

