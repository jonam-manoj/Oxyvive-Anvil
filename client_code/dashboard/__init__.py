from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
from ..Form2 import Form2

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.aviailable_Hospital_Address')

  def primary_color_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.availabe_vehical_services')

  def primary_color_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    # open_form('dashboard.available_zym_address')   
    self.content_panel.add_component(Form2())
    

