from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

# Initialise I2C for LCD
lcd_i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
lcd = I2cLcd(lcd_i2c, 0x27, 2, 16)

# Initialize buttons
rotor_1_button = Pin(15, Pin.IN, Pin.PULL_UP)
rotor_2_button = Pin(14, Pin.IN, Pin.PULL_UP)
rotor_3_button = Pin(13, Pin.IN, Pin.PULL_UP)
select_button = Pin(12, Pin.IN, Pin.PULL_UP)
buttons = [rotor_1_button, rotor_2_button, rotor_3_button]

def rotor_selection():
    rotor_allocation = [0, 0, 0]
 
    # Clear LCD and display values
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(" R O T O R E N ")
    lcd.move_to(0, 1)
    lcd.putstr(f"   {rotor_allocation[0]:02}  {rotor_allocation[1]:02}  {rotor_allocation[2]:02}   ")
    
    while True:
        # Change rotor allocation on keypress, only change to rotor not already in use
        for button in buttons:
            if button.value() == 0:
                
             if (rotor_allocation[buttons.index(button)] + 1) not in rotor_allocation:
                rotor_allocation[buttons.index(button)] += 1
                
                if rotor_allocation[buttons.index(button)] > 5:
                 rotor_allocation[buttons.index(button)] = 0
                 
                while rotor_allocation.count(rotor_allocation[buttons.index(button)]) > 1:
                 rotor_allocation[buttons.index(button)] += 1
                 
                 if rotor_allocation[buttons.index(button)] > 5:
                     rotor_allocation[buttons.index(button)] = 0
                     
                 if rotor_allocation.count(rotor_allocation[buttons.index(button)]) == 1:
                     break
                      
             else:
                rotor_allocation[buttons.index(button)] += 1
                while rotor_allocation.count(rotor_allocation[buttons.index(button)]) > 1:             
                     rotor_allocation[buttons.index(button)] += 1
                     
                     if rotor_allocation[buttons.index(button)] > 5:
                         rotor_allocation[buttons.index(button)] = 0
                         break
                        
                     if rotor_allocation.count(rotor_allocation[buttons.index(button)]) == 1:
                         break
    
                                             
        lcd.move_to(0, 1)
        lcd.putstr(f"   {rotor_allocation[0]:02}  {rotor_allocation[1]:02}  {rotor_allocation[2]:02}   ")
        
        if select_button.value() == 0:
            lcd.clear()
            return rotor_allocation
            break
        

        
    

def rotor_config():
    rotor_positions = [0, 0, 0]
    lcd.clear()
    
    # Get rotor allocation 
    rotors_used = rotor_selection()
    
    while True:
        # Detect button press and adjust rotor position according to amount of button presses
        for button in buttons:
            if button.value() == 0:
                rotor_positions[buttons.index(button)] += 1
                if rotor_positions[buttons.index(button)] == 27:
                    rotor_positions[buttons.index(button)] = 1
                
        # Detect reset button press
        if select_button.value() == 0:
            for i in range(0, len(rotor_positions)):
                rotor_positions[i-1] = 0

            
        # Display rotor positions on display               
        lcd.move_to(0, 0)
        lcd.putstr(f"   {rotor_positions[0]:02}  {rotor_positions[1]:02}  {rotor_positions[2]:02}   ")
    
    
    
main()

