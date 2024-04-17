from ._anvil_designer import servicers_registration_form_mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import re

class servicers_registration_form_main(servicers_registration_form_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.auto_validate()
  
    # Any code you write here will run before the form opens.
  
  def servicers_next_button_1_click(self, **event_args):
    name = self.servicers_name_text_box.text
    email = self.servicers_email_text_box.text
    phone =self.servicers_phone_text_box.text
    password = self.servicers_password_text_box.text
    address = self.servicers_address_text_box.text
  
    # random_code = self.generate_random_code()
    # print(random_code)

    # Validation logic
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid_password, password_error_message = self.validate_password(password)
    if not name:
      self.servicers_name_text_box.hint_text = 'please enter the name '
    elif not email or not re.match(email_regex, email):
      self.servicers_email_text_box.placeholder = 'please enter the name '  
    elif not is_valid_password:
      self.servicers_password_text_box.placeholder = password_error_message 
    elif not phone or len(phone) != 10:
      self.servicers_phone_text_box.placeholder = 'Please enter correct Phone number'
    elif not address:
      self.servicers_address_text_box.placeholder ='Fill this field'
    else:
      service_register_data = {'name': name, 'email': email,
                                  'phone': phone, 'address': address,
                                  'password': password, }
      """This method is called when the button is clicked"""
      open_form('servicers_registration_form.services_register_add_service')
      
        
  def auto_validate(self, *args):
    self.password_valid = bool(
        self.servicers_password_text_box.text and self.validate_password(self.servicers_password_text_box.text)[
            0])
    # password validation
  def validate_password(self, password):
      # Check if the password is not empty
    if not password:
      return False, "Password cannot be empty"

      # Check if the password has at least 8 characters
    if len(password) < 6:
      return False, "Password must have at least 6 characters"

      # Check if the password contains both uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
      return False, "Password must contain uppercase, lowercase"

      # Check if the password contains at least one digit
    if not any(c.isdigit() for c in password):
      return False, "Password must contain at least one digit"

      # Check if the password contains at least one special character
    special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_characters, password):
      return False, "Password must contain a special character"

      # All checks passed; the password is valid
    return True, "Password is valid"

  # def generate_random_code(self):
  #   prefix = "SP"
  #   random_numbers = ''.join(random.choices(string.digits, k=5))
  #   code = prefix + random_numbers

    # return code

  def show_password_check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.servicers_password_text_box.hide_text

 
