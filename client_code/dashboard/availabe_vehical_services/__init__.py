from ._anvil_designer import availabe_vehical_servicesTemplate
from anvil import *
import anvil.users
import anvil.server


class availabe_vehical_services(availabe_vehical_servicesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
