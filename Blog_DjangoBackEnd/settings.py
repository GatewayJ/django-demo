import os
 
# Default settings between dev and prd
 
if os.environ.get('ENV', None) == 'PRODUCT':
    from .product import *
else:
    from .dev import *