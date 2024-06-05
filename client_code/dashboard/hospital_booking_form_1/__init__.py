from ._anvil_designer import hospital_booking_form_1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class hospital_booking_form_1(hospital_booking_form_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def servicers_next_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.services_register_add_service')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('slot_book')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard')
