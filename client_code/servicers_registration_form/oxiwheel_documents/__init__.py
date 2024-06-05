from ._anvil_designer import oxiwheel_documentsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string

class oxiwheel_documents(oxiwheel_documentsTemplate):
  def __init__(self, oxiwheel_details, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id =user_id
    self.oxiwheel_details=oxiwheel_details

    # Any code you write here will run before the form opens.
  first_file_name = None
  second_file_name = None
  def back_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiwheel',user_id=self.user_id)

  def Submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.first_file_name and not self.second_file_name:
      Notification('Upload Documents.' ).show()
    else:
      user_details = app_tables.users.get(id=self.user_id)
      print(user_details)
      oxiwheel_details = self.oxiwheel_details
      print(oxiwheel_details)
      app_tables.oxiwheels.add_row(id=str(user_details['id']),
                                   name=user_details['username'],
                                   email=user_details['email'],
                                   password=user_details['password'],
                                   phone=int(user_details['phone']),
                                   pincode=int(oxiwheel_details[4]),
                                   Oxiwheels_Name=oxiwheel_details[0],
                                   model_year=str(oxiwheel_details[1]),
                                   State=oxiwheel_details[2],
                                   District=oxiwheel_details[3],
                                   address_2=oxiwheel_details[5],
                                   capsules=int(oxiwheel_details[6]),
                                   vehicle_rc=oxiwheel_details[7],
                                   driving_licence=oxiwheel_details[8],
                                  oxywheel_id=self.generate_unique_random_code())
                                  
      alert("You added oxiwheel successfully.")
      open_form('servicers_registration_form.services_register_add_service',id=self.user_id)

  def medical_file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name =file.get_name()
    self.file_name_1.text = self.first_file_name
    self.oxiwheel_details.append(file)

  def building_file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name =file.get_name()
    self.file_name_2.text = self.second_file_name
    self.oxiwheel_details.append(file)

  def generate_unique_random_code(self):
    prefix = "OW"
    while True:
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        code = prefix + random_numbers
        
        # Check if the code already exists in the data table
        existing_rows = app_tables.oxiwheels.get(oxywheel_id=code)
        if not existing_rows:
            # If the code does not exist, return it
            return code

