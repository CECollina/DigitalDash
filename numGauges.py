import obd
import panel as pn
from gpiozero import LED
from time import sleep

# Connect to OBD-II adapter
connection = obd.OBD()

# leds
green1 = LED(4)
green2 = LED(17)
green3 = LED(27)
green4 = LED(22)
green5 = LED(5)
yellow1 = LED(6)
yellow2 = LED(13)
yellow3 = LED(19)
yellow4 = LED(26)
red1 = LED(21)
red2 = LED(20)
red3 = LED(16)


# Commands
cmd_rpm = obd.commands.RPM
cmd_speed = obd.commands.SPEED
cmd_oil = obd.commands.OIL_TEMP
cmd_coolant = obd.commands.COOLANT_TEMP
cmd_intake = obd.commands.INTAKE_PESSURE
cmd_baro = obd.commands.BAROMETRIC_PRESSURE
cmd_pedalPos = obd.commands.RELATIVE_ACCEL_POS

# Create the RPM gauge
rpmGauge = pn.indicators.Number(
    name='RPM', value=0, format='{value}', height=160, width=160,
    colors=[(3000, 'green'), (5000, 'gold'), (6100, 'red')]
)

# Create the Speed gauge
speedGauge = pn.indicators.Number(
    name='Speed (MPH)', value=0, format='{value}', height=160, width=160,
    #colors=[(33, 'green'), (66, 'gold'), (100, 'red')]
)

# Create the Boost gauge
boostGauge = pn.indicators.Number(
    name='BOOST', value=0, format='{value}', height=160, width=160,
    colors=[(0, 'blue'), (20, 'green'), (23, 'red')]
)

# Create the Oil temp gauge
oilGauge = pn.indicators.Number(
    name='OIL', value=0, format='{value}', height=160, width=160,
    colors=[(120, 'blue'), (175, 'gold'), (2000, 'green')]
)

# Create the Coolant temp gauge
coolantGauge = pn.indicators.Number(
    name='Coolant', value=0, format='{value}', height=160, width=160,
    colors=[(170, 'blue'), (220, 'green'), (230, 'red')]
)

# Create throttle position gauge
throttleGauge = pn.indicators.Number(
    name='Throttle', value=0, format='{value}', height=160, width=160,
    #colors=[(0, 'blue'), (50, 'green'), (100, 'red')]
)


# Function to update the gauges
def update_gaugesFAST():
    # Update RPM
    response_rpm = connection.query(cmd_rpm)
    if response_rpm.value is not None:
        rpm = response_rpm.value.magnitude
        rpmGauge.value = rpm

        #Shift lights
        if rpm < 900:
            green1.on()
            green2.off()
            green3.off()
            green4.off()
            green5.off()
            yellow1.off()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 1700:
            green1.on()
            green2.on()
            green3.off()
            green4.off()
            green5.off()
            yellow1.off()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 2200:
            green1.on()
            green2.on()
            green3.on()
            green4.off()
            green5.off()
            yellow1.off()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 2700:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.off()
            yellow1.off()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 3100:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.off()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        #yellow lights
        elif rpm < 3500:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 4200:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 4700:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.on()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
        elif rpm < 5100:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.on()
            yellow4.on()
            red1.off()
            red2.off()
            red3.off()
        
        #red lights
        elif rpm < 5500:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.on()
            yellow4.on()
            red1.on()
            red2.off()
            red3.off()
        elif rpm < 6000:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.on()
            yellow4.on()
            red1.on()
            red2.on()
            red3.off()
        elif rpm < 6300:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.on()
            yellow4.on()
            red1.on()
            red2.on()
            red3.on()
        elif rpm > 6300:
            green1.on()
            green2.on()
            green3.on()
            green4.on()
            green5.on()
            yellow1.on()
            yellow2.on()
            yellow3.on()
            yellow4.on()
            red1.on()
            red2.on()
            red3.on()
            sleep(.2)
            green1.off()
            green2.off()
            green3.off()
            green4.off()
            green5.off()
            yellow1.off()
            yellow2.off()
            yellow3.off()
            yellow4.off()
            red1.off()
            red2.off()
            red3.off()
            sleep(.2)
        

    # Update Speed
    response_speed = connection.query(cmd_speed)
    if response_speed.value is not None:
        speed_mph = response_speed.value.to("mph").magnitude
        speedGauge.value = speed_mph
    
    # Update Boost
    response_baro = connection.query(cmd_baro)
    response_intake = connection.query(cmd_intake)
    if response_baro.value is not None:
        boost = response_intake.value.magnitude - response_baro.value.magnitude
        boostGauge.value = boost
    
    # Update throttle position
    response_pedalPos = connection.query(cmd_pedalPos)
    if response_pedalPos.value is not None:
        pedalPos = response_pedalPos.value.magnitude
        throttleGauge.value = pedalPos

    

def update_gaugesSLOW():
    # Update Oil temp
    response_oil = connection.query(cmd_oil)
    if response_oil.value is not None:
        oil = response_oil.value.magnitude
        oilGauge.value = (oil * 9/5) + 32
    
    # Update Coolant temp
    response_coolant = connection.query(cmd_coolant)
    if response_coolant.value is not None:
        coolant = response_coolant.value.magnitude
        coolantGauge.value = (coolant * 9/5) + 32
    
    

# Update the gauges periodically
pn.state.add_periodic_callback(update_gaugesFAST, period=100)
pn.state.add_periodic_callback(update_gaugesSLOW, period=20000)

# Display the gauges
grid = pn.GridSpec(sizing_mode='scale_both')
grid[0,0] = speedGauge
grid[0,1] = rpmGauge
grid[0,2] = boostGauge
grid[1,0] = oilGauge
grid[1,1] = coolantGauge
grid[1,2] = throttleGauge

grid.show()
