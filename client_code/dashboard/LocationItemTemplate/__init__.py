from ._anvil_designer import LocationItemTemplateTemplate
from anvil import *

class LocationItemTemplate(LocationItemTemplateTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        # Set the text of the link to the formatted address
        self.link_location.text = self.item['formatted']
        # Set up the event handler for the link's click event
        self.link_location.set_event_handler('click', self.link_location_click)

    def link_location_click(self, **event_args):
        # Update text_box_2 in the main form directly
        main_form = get_open_form()
        main_form.update_text_boxes(self.item['formatted'])
       
