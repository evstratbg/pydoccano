# Doccano Client

Simple classes for doccano rest api


## Usage

```python
from pydoccano import Doccano

doccano = Doccano(
    'http://localhost:8000',
    'admin ',
    'password'
)

my_user = doccano.get_me()
print(my_user)

projects_list = doccano.projects.list()
print(projects_list)