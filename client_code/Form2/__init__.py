from ._anvil_designer import Form2Template
import anvil.server
from datetime import datetime, timedelta

class Form2(Form2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.set_button_date()
        
        # Initialize the booked slots list
        self.booked_slots = []

    def set_button_date(self):
        current_date = datetime.now()
        for i in range(1, 5):  # Assuming you have 4 buttons named button_1, button_2, ..., button_4
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i-1)
            # Format the date as "Day" (e.g., "Tue") and day number (e.g., "17")
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date
            button.tag.days_offset = i - 1  # Store the days_offset in the tag

    def button_1_click(self, **event_args):
        self.update_time_buttons(days_offset=0)

    def button_2_click(self, **event_args):
        self.update_time_buttons(days_offset=1)

    def button_3_click(self, **event_args):
        self.update_time_buttons(days_offset=2)

    def button_4_click(self, **event_args):
        self.update_time_buttons(days_offset=3)

    def update_time_buttons(self, days_offset):
        # Get the current date and time
        current_datetime = datetime.now()
        target_datetime = current_datetime + timedelta(days=days_offset)
        
        # Define the times for the buttons
        times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
        
        # Loop over buttons 5 to 10 and set their texts and visibility
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            if i - 5 < len(times):
                # Set the text to the appropriate time
                button.text = times[i - 5]
                button.tag.days_offset = days_offset  # Store the current days_offset
                
                # Convert the button text time to a datetime object for comparison
                button_time_str = button.text
                button_time = datetime.strptime(button_time_str, "%I:%M %p").time()
                
                # Combine target date with button time for accurate comparison
                button_datetime = datetime.combine(target_datetime.date(), button_time)
                
                # Enable or disable the button based on the target date and time and if it's booked
                button.enabled = current_datetime <= button_datetime and button_datetime not in self.booked_slots
            else:
                # If no time available, set text to "No Time" and disable the button
                button.text = "No Time"
                button.enabled = False
            
            # Make the button visible
            button.visible = True

    def book_slot(self, button):
        # Get the days_offset from the button's tag
        days_offset = button.tag.days_offset if hasattr(button.tag, 'days_offset') else 0

        # Get the current date and time
        current_datetime = datetime.now()
        target_datetime = current_datetime + timedelta(days=days_offset)
        
        button_time_str = button.text
        button_time = datetime.strptime(button_time_str, "%I:%M %p").time()
        button_datetime = datetime.combine(target_datetime.date(), button_time)

        # Add the booked slot to the booked slots list
        self.booked_slots.append(button_datetime)
        
        # Update buttons to reflect the booked slot
        self.update_time_buttons(days_offset)

    def button_5_click(self, **event_args):
        self.book_slot(self.button_5)

    def button_6_click(self, **event_args):
        self.book_slot(self.button_6)

    def button_7_click(self, **event_args):
        self.book_slot(self.button_7)

    def button_8_click(self, **event_args):
        self.book_slot(self.button_8)

    def button_9_click(self, **event_args):
        self.book_slot(self.button_9)

    def button_10_click(self, **event_args):
        self.book_slot(self.button_10)
