from ._anvil_designer import loginTemplate
from anvil import *

from anvil import alert, open_form, server

class login(loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.text_box_1.text
    password = self.text_box_2.text
    
    try:
        # Call the server function to check login credentials
        user = server.call('login_user', email, password)
        
        if user:
            # If a user with the provided credentials exists, open the database
            open_form('dashboard')
        else:
            # If no user found, display a message indicating that the user does not have an account
            alert("You don't have an account. Please sign up first.")
    
    except Exception as e:
        # Handle any errors that occur during the login process
        alert(f"Error: {e}")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("signup")


