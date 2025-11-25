1. postgres database lack role assignment
2. postgres database url points to a different entry point instead of localhost
3. AttributeError: 'str' object has no attribute 'model_dump' 

    __tablename__ = "items"

solution:
- add type hint to table name
    __tablename__: str = "items"



