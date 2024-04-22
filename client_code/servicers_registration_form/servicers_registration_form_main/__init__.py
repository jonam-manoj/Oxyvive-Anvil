from ._anvil_designer import servicers_registration_form_mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

# import bcrypt

class servicers_registration_form_main(servicers_registration_form_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.
  
  def servicers_next_button_1_click(self, **event_args):
    name = self.servicers_name_text_box.text
    email = self.servicers_email_text_box.text
    phone =self.servicers_phone_text_box.text
    password = self.servicers_password_text_box.text
    address = self.servicers_address_text_box.text
  
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid_password, password_error_message = self.validate_password(password)
    if not name:
      self.servicers_name_text_box_change()
    elif not email or not re.match(email_regex, email):
      self.servicers_email_text_box_change()  
    elif not is_valid_password:
      print(password_error_message)
      self.servicers_password_text_box_change()
    elif not phone or len(phone) != 10:
      self.servicers_phone_text_box_change()
    elif not address:
      self.servicers_address_text_box_change()
    else:

      # hash_pashword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
      # hash_pashword = hash_pashword.decode('utf-8')
      try: 
        # If not present, proceed to insert the new user
        rows = app_tables.users.search()
        id = f"SP{len(rows):04d}"
        app_tables.users.add_row(id = id, username = name, email = email, password = password, phone = int(phone),address=address)
        """This method is called when the button is clicked"""
        open_form('servicers_registration_form.services_register_add_service',id=id)
      except Exception as e:
        print(e)
        pass
      
      # service_register_data = {'name': name, 'email': email,
      #                             'phone': phone, 'address': address,
      #                             'password': password, }
      
    
    # password validation
  def validate_password(self, password):
      # Check if the password is not empty
    special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
    if not password:
      return False, "Password cannot be empty"
      # Check if the password has at least 8 characters
    elif len(password) < 6:
      return False, "Password must have at least 6 characters"
      # Check if the password contains both uppercase and lowercase letters
    elif not any(c.isupper() for c in password) or not any(c.islower() for c in password):
      return False, "Password must contain uppercase, lowercase"
      # Check if the password contains at least one digit
    elif not any(c.isdigit() for c in password):
      return False, "Password must contain at least one digit"
      # Check if the password contains at least one special character
    elif not re.search(special_characters, password):
      return False, "Password must contain a special character"
    else :
      # All checks passed; the password is valid
      return True, "Valid password"

  def show_password_check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    checked = self.show_password_check_box.checked
    if not  checked:
      self.servicers_password_text_box.hide_text = True
    else:
      self.servicers_password_text_box.hide_text = False
      

  def servicers_name_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    name = self.servicers_name_text_box.text
    if not name:
      self.name_hint.text = 'please enter the name '
    else:
      self.name_hint.text = ''

  def servicers_email_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    email = self.servicers_email_text_box.text
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    existing_email = app_tables.users.get(email=email)
    if not email or not re.match(email_regex, email):
      self.email_hint.text = 'Invalid email format. '
    else:
      self.email_hint.text = ''
    if existing_email:
      self.email_hint.text = "Email already registered"

  def servicers_password_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    password = self.servicers_password_text_box.text
    is_valid_password, password_error_message = self.validate_password(password)
    if not is_valid_password:
      self.hint_text.text = password_error_message
    else:
      self.hint_text.foreground ='#05d628'
      self.hint_text.text = 'Strong password'

  def servicers_phone_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    phone = self.servicers_phone_text_box.text
    existing_phone = app_tables.users.get(phone=float(phone))
    if not phone or len(phone) != 10:
      self.phone_hint.text = 'Invalid Phone number.'
    else:
      self.phone_hint.text = ''
    if existing_phone:
      self.phone_hint.text = "Phone number already registered"

  def servicers_address_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    address = self.servicers_address_text_box.text
    if not address:
      self.address_hint.text ='Fill the address field'
    else:
      self.address_hint.text =''

  def have_account_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('login')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
      
  
      
    
      

 
