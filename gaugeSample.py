import panel as pn

# Initialize variables to control the gauge movement
current_value = 0
increment = 10
max_value = 8000
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
    rpm.value = current_value
    cir.value = current_value
    boost.value = current_value
    dial.value = current_value

cir = pn.indicators.Gauge(
    name="Engine2", value=current_value, bounds=(min_value, max_value), format='{value}',
    colors=[(0.2, 'green'), (0.8, 'gold'), (1, 'red')],
    custom_opts={"pointer": {"itemStyle": {"color": 'red'}}}
)

# Create the gauge
rpm = pn.indicators.LinearGauge(
    name='Engine', value=current_value, bounds=(min_value, max_value), format='{value:.0f} rpm',
    colors=['green', 'gold', 'red'], horizontal=True, width=125, height=160
)

speed = pn.indicators.Number(name='RPM', value=current_value, format='{value}', height=160, width=160)
boost = pn.indicators.Number(name='BOOST',value=current_value, format='{value}', height=160, width=160)

dial = pn.indicators.Dial(
    name='Engine', value=current_value, bounds=(min_value, max_value), format='{value} rpm',
    colors=[(0.2, 'green'), (0.8, 'gold'), (1, 'red')], width=120, height=120
)


#####################################
#              RPM                  #
#   MPH                  BOOST      #
#                                   #
# OIL       Coolant        Intake   #
##################################### 
# Create the layout with the gauge
gspec = pn.GridSpec(sizing_mode='scale_both', width=800, height=480)

#gspec[:,   0 ] = pn.Spacer(styles=dict(background='red'))
gspec[0,   0:5] = rpm
gspec[1,   1:2] = speed
gspec[1,   3:4] = boost
gspec[2,   0:1] = dial
gspec[2,   2:3] = dial
gspec[2,   4:5] = dial
#gspec[0:1, 3:4] = pn.Spacer(styles=dict(background='purple'))

# Schedule the periodic callback to update the gauge
callback_id = pn.state.add_periodic_callback(update_gauge, period=10, count=None)

# Make the layout servable
gspec.servable()
