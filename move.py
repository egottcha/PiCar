from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.output_devices import OutputDevice
from config import move_pins
from getkeys import key_check


factory = PiGPIOFactory(host='192.168.1.5')

move = OutputDevice(pin=move_pins.PIN_MOVE, active_high=False, pin_factory=factory)
fwd = OutputDevice(pin=move_pins.PIN_FWD, active_high=False, pin_factory=factory)
turn = OutputDevice(pin=move_pins.PIN_TURN, active_high=False, pin_factory=factory)
left = OutputDevice(pin=move_pins.PIN_LEFT, active_high=False, pin_factory=factory)

# turn.on()


#
# def __init__():
#     factory = PiGPIOFactory(host='192.168.1.5')
#
#     move = OutputDevice(move_pins.PIN_MOVE, pin_factory=factory)
#     fwd = OutputDevice(move_pins.PIN_FWD, pin_factory=factory)
#     turn = OutputDevice(move_pins.PIN_TURN, pin_factory=factory)
#     left = OutputDevice(move_pins.PIN_LEFT, pin_factory=factory)
#

