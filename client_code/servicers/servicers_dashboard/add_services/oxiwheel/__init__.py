from ._anvil_designer import oxiwheelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class oxiwheel(oxiwheelTemplate):
  def __init__(self, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = user_id

    # Any code you write here will run before the form opens.
  def next_button_1_click(self, **event_args):
    vehicle_no = self.vehicle_no.text
    model_year = self.model_year.date
    state = self.state.text
    district = self.district.text
    pincode = self.pincode.text
    address = self.address.text
    capsules = self.capsules.text

    if (
      not vehicle_no
      and not address
      and not capsules
      and not district
      and not model_year
      and not pincode
      and not state
    ):
      Notification("All fields are required.").show()
    else:
      print(self.item)
      oxiwheel_details = [
        vehicle_no,
        model_year,
        state,
        district,
        pincode,
        address,
        capsules,
      ]
      print(oxiwheel_details)

      open_form(
        "servicers_registration_form.oxiwheel_documents",
        oxiwheel_details=oxiwheel_details,
        user_id=self.user_id,
      )
