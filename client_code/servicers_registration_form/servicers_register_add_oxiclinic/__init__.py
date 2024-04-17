from ._anvil_designer import servicers_register_add_oxiclinicTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class servicers_register_add_oxiclinic(servicers_register_add_oxiclinicTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

  def back_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.services_register_add_service')
