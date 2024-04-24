from ._anvil_designer import loginTemplate
from anvil import alert, open_form
from anvil.tables import app_tables

class login(loginTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def primary_color_1_click(self, **event_args):
        email = self.text_box_1.text
        password = self.text_box_2.text
        
        try:
            # Search for the user in the Data Table
            users_table = app_tables.users
            user = users_table.get(email=email, password=password)
            
            if user:
                open_form('dashboard')
            else:
                alert("Invalid email or password. Please try again.")
        
        except Exception as e:
            alert(f"Error: {e}")

    def link_2_click(self, **event_args):
        open_form("signup")
