from ._anvil_designer import available_zym_addressTemplate
from anvil import *
import anvil.users
import anvil.server


class available_zym_address(available_zym_addressTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
