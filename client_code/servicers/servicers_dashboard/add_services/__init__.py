from ._anvil_designer import add_servicesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class add_services(add_servicesTemplate):
  def __init__(self, id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = id

    # Any code you write here will run before the form opens.

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("servicers_registration_form.servicers_registration_form_main")

  def add_oxiclinic_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(
      "servicers_registration_form.servicers_register_add_oxiclinic",
      user_id=self.user_id,
    )

  def add_oxiwheel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(
      "servicers_registration_form.servicers_register_add_oxiwheel",
      user_id=self.user_id,
    )

  def add_oxigym_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(
      "servicers_registration_form.servicers_register_add_oxigym", user_id=self.user_id
    )

  def services_list_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("servicers_registration_form.services_list", user_id=self.user_id)

  def servicers_confirm_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    oxiclinic = app_tables.oxiclinics.search(id=str(self.user_id))
    oxiwheel = app_tables.oxiwheels.search(id=str(self.user_id))
    oxigym = app_tables.oxigyms.search(id=str(self.user_id))

    if oxiclinic or oxiwheel or oxigym:
      

      open_form("servicers.servicers_dashboard")
    else:
      alert("Services are empty , please add at least one service")
