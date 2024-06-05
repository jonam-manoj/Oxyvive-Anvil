from ._anvil_designer import oxiclinicTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string


class oxiclinic(oxiclinicTemplate):
  def __init__(self, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = user_id
    self.first_file_name = None
    self.second_file_name = None
    self.file1 = None
    self.file2 = None 

    # Any code you write here will run before the form opens

  def back_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(
      "servicers_registration_form.services_register_add_service", id=self.user_id
    )

  def next_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    hospital_name = self.hospital_name.text
    establised_year = self.oxiclini_established_year.date
    state = self.state.text
    district = self.district.text
    pincode = self.oxiclinic_pincode.text
    address = self.oxiclinic_address.text
    capsule = self.oxiclinic_capsules.text
    

    if (
      not hospital_name
      and not address
      and not capsule
      and not district
      and not establised_year
      and not pincode
      and not state
      and not self.first_file_name
      and not self.second_file_name
    ):
      Notification('All "Fields" and "Documents"  are required.').show()
    else:
      user_details = app_tables.users.get(id=self.user_id)
      print(user_details)
      app_tables.oxiclinics.add_row(id=str(user_details['id']),
                                   name=user_details['username'],
                                   email=user_details['email'],
                                   password=user_details['password'],
                                   phone=int(user_details['phone']),
                                   pincode=int(pincode),
                                   Oxiclinics_Name=hospital_name,
                                   established_year=str(establised_year),
                                   State=state,
                                   District=district,
                                   address_2=address,
                                   capsules=int(capsule),
                                   medical_licence=self.file1,
                                   building_licence=self.file2,
                                   oxiclinic_id=self.generate_unique_random_code())
                                   

                                  
      alert("You added oxiclinic successfully.")

      open_form("servicers.servicers_dashboard.add_services", id = self.user_id )

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name =file.get_name()
    self.file_name_1.text = self.first_file_name
    self.file1 = file
    self.file_loader_1.text ="Selected"

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name =file.get_name()
    self.file_name_2.text = self.second_file_name
    self.file2 = file
    self.file_loader_2.text ="Selected"


  def generate_unique_random_code(self):
    prefix = "OC"
    while True:
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        code = prefix + random_numbers
        
        # Check if the code already exists in the data table
        existing_rows = app_tables.oxiclinics.get(oxiclinic_id=code)
        if not existing_rows:
            # If the code does not exist, return it
            return code

