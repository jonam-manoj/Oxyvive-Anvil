from ._anvil_designer import servicers_navigation_barTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class servicers_navigation_bar(servicers_navigation_barTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def servicers_home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
