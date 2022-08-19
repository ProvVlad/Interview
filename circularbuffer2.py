
class CircularBuffer():
    """Buffer FIFO. Buffer write element if not full or pass this element"""

    def __init__(self, maxsize: int = 5):
        
        self._buffer = {}
        self._writepoint = int(0)
        self._readpoint = int(0)
        self._size = maxsize -1
        

    def write(self, element):
        """Write element into buffer if buffer isn't full"""
        
        if self._writepoint > self._size:
            self._writepoint = 0

        if self._buffer.get(self._writepoint) == None:
            self._buffer[self._writepoint] = element
            self._writepoint = self._writepoint + 1
       
        return None

    def read(self):
        """Read and delete element"""

        if self._readpoint > self._size:
            self._readpoint = 0
        
        __result = self._buffer.pop(self._readpoint, None)
        if __result != None:
            self._readpoint = self._readpoint + 1
        
        return __result
    
    def buffer_print(self):
        """Print content of buffer"""
        
        print(self._buffer)



def test_circularbuffer():
    """Test class CircularBuffer"""

    test_list = range(10)
    buffer = CircularBuffer()

    for item in test_list:
        buffer.write(item)
        buffer.write(item)
        #print(buffer.read())
        print(buffer.read())
        buffer.buffer_print()


if __name__ == "__main__":
    test_circularbuffer()
