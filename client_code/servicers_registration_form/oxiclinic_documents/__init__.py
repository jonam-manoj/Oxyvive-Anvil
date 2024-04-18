from ._anvil_designer import oxiclinic_documentsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class oxiclinic_documents(oxiclinic_documentsTemplate):
  def __init__(self, oxiclinc_details, **properties):
    self.oxiclinc_details=oxiclinc_details
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  first_file_name = None
  second_file_name = None
  def back_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiclinic')

  def Submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.file_name_1 and not self.file_name_2:
      pass
    else:
      print(self.oxiclinc_details)
      oxiclinc_details = self.oxiclinc_details
      open_form('servicers_registration_form.services_register_add_service', oxiclinc_details = oxiclinc_details)

  def medical_file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name =file.get_name()
    self.file_name_1.text = self.first_file_name
    self.oxiclinc_details.append(file)

  def building_file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name =file.get_name()
    self.file_name_2.text = self.second_file_name
    self.oxiclinc_details.append(file)
