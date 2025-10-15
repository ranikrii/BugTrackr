from sqlalchemy.orm import Session
from app import models, schemas
from app.db import get_db

# user 

def create_user(db: Session, user_in: schemas.UserCreate):
    from app.auth import get_password_hash 
    hashed = get_password_hash(user_in.password)
    user = models.User(username=user_in.username, hashed_password=hashed, role=user_in.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).get(user_id)


# project CRUD


def create_project(db: Session, project_in: schemas.ProjectCreate):
    p = models.Project(name=project_in.name, description=project_in.description)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p




def list_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()




def get_project(db: Session, project_id: int):
    return db.query(models.Project).get(project_id)


# issue CRUD


def create_issue(db: Session, issue_in: schemas.IssueCreate, reporter_id: int):
    issue = models.Issue(title=issue_in.title, description=issue_in.description, project_id=issue_in.project_id, reporter_id=reporter_id)
    db.add(issue)
    db.commit()
    db.refresh(issue)
    return issue




def list_issues(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Issue).offset(skip).limit(limit).all()




def get_issue(db: Session, issue_id: int):
    return db.query(models.Issue).get(issue_id)




def update_issue_status(db: Session, issue_id: int, status: str):
    issue = get_issue(db, issue_id)
    if not issue:
        return None
    issue.status = status
    db.add(issue)
    db.commit()
    db.refresh(issue)
    return issue