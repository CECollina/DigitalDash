import panel as pn

# Initialize variables to control the gauge movement
current_value = 0
increment = 100
max_value = 3000
min_value = 0

# Callback to update the gauge
def update_gauge():
    global current_value, increment

    # Update the current value
    current_value += increment

    # Reverse the direction of the gauge movement at the bounds
    if current_value >= max_value or current_value <= min_value:
        increment = -increment

    # Set the gauge value
    gauge.value = current_value

# Create the gauge
gauge = pn.indicators.LinearGauge(
    name='Engine', value=current_value, bounds=(min_value, max_value), format='{value:.0f} rpm',
    colors=['green', 'gold', 'red'], horizontal=True, width=125
)

# Create the layout with the gauge
layout = pn.Column(gauge)

# Schedule the periodic callback to update the gauge
callback_id = pn.state.add_periodic_callback(update_gauge, period=50, count=None)

# Make the layout servable
layout.servable()
