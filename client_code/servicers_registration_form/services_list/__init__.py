from ._anvil_designer import services_listTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class services_list(services_listTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = '4'
    rows = app_tables.oxiclinics.search(id=self.user_id)
    i= 1
    List_oxiclinics = []
    for row in rows:
      if row is not None:
      # Initialize list
        user_info = []
      # Append data to the list
        user_info.append(i)  # Assuming the serial number column is named 'serial_number'
        user_info.append(row['Oxiclinics_Name'])
        user_info.append(row['State'])
        List_oxiclinics.append(user_info)
      i=i+1

    self.repeating_panel_1.items=List_oxiclinics
    
      

    # Any code you write here will run before the form opens.
