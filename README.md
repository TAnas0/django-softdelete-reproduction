## Setup

virtualenv --python 3.9 .venv
source .venv/bin/activate

pip install django
pip install djangorestframework

django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart


## Bug reproductions

In Django shell:

```bash
from tutorial.models import Company, Employee
c = Company(name="C1")
Employee(name="E1", company=Company.objects.get())
c.delete()
```

The expected behaviour in this case is that the company is deleted, and the `company` attribute on the `Employee` instance is set to `None`.
What actually happens is that the Employee instance is deleted, as if the on-delete behaviour was set to `Cascade`.