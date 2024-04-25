from ._anvil_designer import servicers_dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import user_id


class servicers_dashboard(servicers_dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.id = user_id.user_id 
    print("sd user id",self.id,user_id.user_id)
    
 
    # Any code you write here will run before the form opens.
