from ._anvil_designer import slot_bookTemplate
from anvil import *
import anvil.server
from datetime import datetime, timedelta

class slot_book(slot_bookTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.set_button_date()
        
        # Add click handlers to time buttons
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.set_event_handler('click', self.time_button_click)
    
    def set_button_date(self):
        current_date = datetime.now()
        for i in range(1, 5):  # Assuming you have 4 buttons named button_1, button_2, ..., button_4
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i-1)
            # Format the date as "Day" (e.g., "Tue") and day number (e.g., "17")
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date
    
    def update_timing_buttons(self, day_offset):
        self.primary_color_1.visible = True
        selected_date = datetime.now() + timedelta(days=day_offset)
        current_time = datetime.now().time()
        times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
        
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            if i - 5 < len(times):
                button.text = times[i - 5]
                button_time = datetime.strptime(button.text, "%I:%M %p").time()
                if selected_date.date() == datetime.now().date():
                    button.enabled = current_time <= button_time
                else:
                    button.enabled = True
                button.background = "white"  # Reset background color to default
                button.visible = True
            else:
                button.text = "No Time"
                button.enabled = False
                button.visible = True
    
    def button_1_click(self, **event_args):
        """This method is called when button_1 is clicked"""
        self.update_timing_buttons(day_offset=0)

    def button_2_click(self, **event_args):
        """This method is called when button_2 is clicked"""
        self.update_timing_buttons(day_offset=1)

    def button_3_click(self, **event_args):
        """This method is called when button_3 is clicked"""
        self.update_timing_buttons(day_offset=2)

    def button_4_click(self, **event_args):
        """This method is called when button_4 is clicked"""
        self.update_timing_buttons(day_offset=3)
    
    def time_button_click(self, **event_args):
        """Change the button color to light green when a timing button is clicked"""
        button = event_args['sender']
        button.background = "lightgreen"
    
    def primary_color_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('wallet')
