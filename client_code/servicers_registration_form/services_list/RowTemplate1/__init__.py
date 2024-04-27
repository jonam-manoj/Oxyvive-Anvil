from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    id = self.label_4.text
    oxiclinic = app_tables.oxiclinics.get(oxiclinic_id=id)
    oxigym = app_tables.oxigyms.get(oxigym_id=id)
    oxiwheel = app_tables.oxiwheels.get(oxywheel_id=id)
    if oxiclinic:
      oxiclinic.delete()
    elif oxigym:
      oxigym.delete()
    elif oxiwheel:
      oxiwheel.delete()
    alert('You delete this service')
