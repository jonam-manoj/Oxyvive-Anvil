from ._anvil_designer import slot_bookTemplate
from anvil import *
import anvil.server
from datetime import datetime, timedelta

class slot_book(slot_bookTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.set_button_texts()
   
    def set_button_texts(self):
        current_date = datetime.now()
        for i in range(1, 5):  # Assuming you have 4 buttons named button_1, button_2, ..., button_4
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i-1)
            # Format the date as "Day" (e.g., "Tue") and day number (e.g., "17")
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date

    def button_1_click(self, **event_args):
        pass

    def button_5_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass
