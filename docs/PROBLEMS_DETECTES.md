1. 🎨 **Catégorie Formatage**

- curl -X POST http://localhost:8000/items

It is not the correct endpoing as the prefix is rightly appeneded but the endpoint has an extra /, so the endpoint shoduld be `/items/` and not `/items``

- very_long_variable_name_that_exceeds_line_length in main

2. 🔒 **Catégorie Sécurité**

- postgres database lack role assignment

- env.example exposes complete database URL instead of using a placeholder string.

- postgres database url points to a different entry point instead of localhost

- DEBUG_MODE exposed in main.py

- secret and API_KEY defined in main.py and not in .env

3. 📦 **Catégorie Imports** :

- from typing import Generator, import sys in database.py (unused import)

- import datetime in route/items (unused import)

- from typing import Optional (unused import) in schemas/item

- import json (unused in main)

- from typing import Dict, Any (unused in main)

- import sys (unused in main)

- UNUSED_VAR (unused .env variable)

4. 📦 🏷️ **Types** :

- from typing import List but "list" used in @router.get("/", response_model=list[ItemResponse]) instead of "List". (bad naming)

- Type "Literal['items']" is not assignable to declared type "declared_attr[Unknown]"
  "Literal['items']" is not assignable to "declared_attr[Unknown]" in model item

    __tablename__ = "items"

solution:
- add type hint to table name
    __tablename__: str = "items"

- Route for items POST and item_id endpoint had type hint issues. Needed to specify the data models for the parameters accepted.

AttributeError: 'str' object has no attribute 'model_dump' in items_service

E.g: def create_item(item_data, db: Session)

should be

def create_item(item_data: ItemCreate, db: Session = Depends(get_db)):

This way, item_data is processed as a data model and not just a request string.

5. 📝 **Documentation** :

- docstring missing in all but one of the endpoints

6. **Code mort** : dans route/items

- def _old_helper_function(data):
    """Cette fonction n'est plus utilisée mais n'a pas été supprimée."""
    return data.upper()

-   in modesl/items

    def _legacy_method(self):
      pass
