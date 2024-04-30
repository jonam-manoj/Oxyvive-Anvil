from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta
import time


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    while True:
      self.text_box_1.text=  datetime.now().time()
      time.sleep(1)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers.servicers_dashboard.customer_report')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    pass
