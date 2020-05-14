from django.db import models

# Create your models here.

class projects:
    id=int
    name:str
    dec: str
    date:str
    image:str
    
class education:
    year=str
    study=str
    college=str
    branch=str
    branchIs=bool
    cgpa=float