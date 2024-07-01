from ._anvil_designer import dashbord_oneTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class dashbord_one(dashbord_oneTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_2_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    # Make text_box_2 invisible and text_box_1 visible
    self.text_box_2.visible = False
    self.text_box_1.visible = True
