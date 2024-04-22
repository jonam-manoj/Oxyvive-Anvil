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
    rows =app_tables.oxigyms.search(id=self.user_id)
    rows =app_tables.oxiwheels.search(id=self.user_id)
    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}
      
      # Assign data to dictionary keys
      user_info['serial_no'] = i  # Assuming you want to include a serial number
      user_info['Oxiclinics_Name'] = row['Oxiclinics_Name']
      user_info['State'] = row['State']
      
      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics
    
      

    # Any code you write here will run before the form opens.
