from .store import get_latlng
from .store import get_latlng2

from .google_style_example import function_with_types_in_docstring
from .google_style_example import ExampleError

from .functions import x_cubed
from .functions import x_squared



__all__ = [
    get_latlng,
    get_latlng2,

    x_cubed,
    x_squared,

    ExampleError,
    function_with_types_in_docstring
]