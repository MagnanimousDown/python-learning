# Why do we write "auth" or "products" in Blueprint() class?

Example:
```py
auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)
```

The first argument:
```
"auth"
```

is the **blueprint name.**

Think of it as an internal identifier.

Flask uses it internally for things like:
- URL generation
- Debugging
- Distinguishing blueprints


## Doubt 2: Why do we write __name__? 

__name__ tells Flask: \
"Where is this file located?"

Flask uses it to find:
- templates
- static files
- resources


## Doubt 3: Why is __pycache__ getting created?

This is actually a Python thing, not a Flask thing.

When Python executes:
```py
from routes.auth import auth_bp
```

Python compiles:
```py
auth.py
```
into bytecode.

Bytecode files look like:
```py
auth.cpython-311.pyc
```

and are stored in:
```py
__pycache__/
```

Why? \
Because bytecode runs faster than reparsing .py files every time.