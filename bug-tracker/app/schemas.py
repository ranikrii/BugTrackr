from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum as PyEnum
from app.db import Base


class RoleEnum(str, PyEnum):
    admin = "admin"
    user = "user"


class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[RoleEnum] = RoleEnum.user
    
    model_config = ConfigDict(arbitrary_types_allowed=True)


class UserOut(BaseModel):
    id: int
    username: str
    role: RoleEnum
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProjectBase(BaseModel):
    name: str
    description: Optional[str]


class ProjectCreate(ProjectBase):
    pass


class ProjectOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    model_config = ConfigDict(from_attributes=True)


class IssueBase(BaseModel):
    title: str
    description: Optional[str] = None


class IssueCreate(IssueBase):
    project_id: int


class IssueOut(IssueBase):
    id: int
    status: str
    project_id: int
    reporter_id: int
    model_config = ConfigDict(from_attributes=True)