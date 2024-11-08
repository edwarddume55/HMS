from django import forms


# ROOM_CATEGORIES =  (
#         ('YAC', 'AC'),
#         ('DEL', 'DELUXE'),
#         ('KIN', 'KING'),
#         ('QUE', 'QUEEN'),
#     )
class AvailabilityForm(forms.Form):
    # room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])

