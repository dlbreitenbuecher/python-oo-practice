class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start=100):
        """Creates serial number and original number. Original number used to reset serial number"""
        self.original_start = start
        self.serial_number = start
    
    def __repr__(self):
        return f"<Serial Generator start={self.original_start}>"

    
    def generate(self):
        """Generates a serial number, starting with the value for the start argument or the default start value of 100"""
        self.serial_number += 1
        return self.serial_number - 1

    def reset(self):
        """Resets the serial number to the original starting number"""
        self.serial_number = self.original_start