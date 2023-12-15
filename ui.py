import panel as pn
import obd

# Initialize variables to control the gauge movement and setup OBD commands
def init_vars():
    global current_value, increment, max_value, min_value
    global connection, rpm, boost, mph, oil, coolant, intake
    global rpmResponse, boostResponse, mphResponse, oilResponse, coolantResponse, intakeResponse

    current_value = 0
    increment = 1
    max_value = 100
    min_value = 0

    connection = obd.OBD()  # auto-connects to USB or RF port

    # OBD commands
    rpm = obd.commands.RPM
    boost = obd.commands.INTAKE_PRESSURE
    mph = obd.commands.SPEED
    oil = obd.commands.OIL_TEMP
    coolant = obd.commands.COOLANT_TEMP
    intake = obd.commands.INTAKE_TEMP

    # Initialize response variables with dummy values
    rpmResponse = obd.Response()
    boostResponse = obd.Response()
    mphResponse = obd.Response()
    oilResponse = obd.Response()
    coolantResponse = obd.Response()
    intakeResponse = obd.Response()

def update_gauge():
    global rpmResponse, boostResponse, mphResponse, oilResponse, coolantResponse, intakeResponse

    # Query the OBD-II interface
    rpmResponse = connection.query(rpm)
    boostResponse = connection.query(boost)
    mphResponse = connection.query(mph)
    oilResponse = connection.query(oil)
    coolantResponse = connection.query(coolant)
    intakeResponse = connection.query(intake)

def init_gauges():
    global rpmGauge, boostGauge, mphGauge, oilGauge, coolantGauge, intakeGauge

    # Initialize the gauges with dummy values, to be updated by update_gauge()
    rpmGauge = pn.indicators.Number(name='RPM', value=0, format='{value}', height=160, width=160, colors=[(33, 'green'), (66, 'gold'), (100, 'red')])
    boostGauge = pn.indicators.Number(name='BOOST', value=0, format='{value}', height=160, width=160, colors=[(33, 'green'), (66, 'gold'), (100, 'red')])
    mphGauge = pn.indicators.Number(name='MPH', value=0, format='{value}', height=160, width=160, colors=[(33, 'green'), (66, 'gold'), (100, 'red')])
    oilGauge = pn.indicators.Number(name='OIL', value=0, format='{value}', height=160, width=160, colors=[(33, 'green'), (66, 'gold'), (100, 'red')])
    coolantGauge = pn.indicators.Number(name='Coolant', value=0, format='{value}', height=160, width=160, colors=[(33, 'green'), (66, 'gold'), (100, 'red')])  # Added missing comma
    intakeGauge = pn.indicators.Number(name='Intake', value=0, format='{value}', height=160, width=160, colors=[(33, 'green'), (66, 'gold'), (100, 'red')])

def layout_gauges():
    global row1, row2
    row1 = pn.Row(mphGauge, rpmGauge, boostGauge)
    row2 = pn.Row(oilGauge, coolantGauge, intakeGauge)

def callback_gauges():
    global callback_id
    callback_id = pn.state.add_periodic_callback(update_gauge, period=1000, count=None)  # Adjusted to 1000 ms (1 second)

def main():
    init_vars()
    init_gauges()
    layout_gauges()
    callback_gauges()
    row1.servable()
    row2.servable()

if __name__ == "__main__":
    main()
