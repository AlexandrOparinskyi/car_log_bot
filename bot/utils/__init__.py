from .database import *
from .general import *
from .car import *
from .refuel_record import *
from .home import *
from .service_record import *

__all__ = ["get_button_for_add_components",
           "get_text_for_select_part",
           "replace_dot_at_comma",
           "get_paginator_buttons",
           database.__all__,
           car.__all__,
           refuel_record.__all__,
           home.__all__,
           service_record.__all__]
