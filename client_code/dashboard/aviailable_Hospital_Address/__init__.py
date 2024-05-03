from ._anvil_designer import aviailable_Hospital_AddressTemplate
from anvil import *
import anvil.server


class aviailable_Hospital_Address(aviailable_Hospital_AddressTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
