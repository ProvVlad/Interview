
class CircularBuffer():
    """Buffer FIFO. If buffer is full, when we write elements -> rewrites elements"""

    def __init__(self, maxsize = 5):
        self._buffer = {}
        self._writepoint = 0
        self._readpoint = 0
        self._size = maxsize -1
        

    def write(self, element):
        """Write element into buffer. If buffer is full, rewrite element"""
        
        if self._writepoint > self._size:
            self._writepoint = 0
        # If we rewrite element we have to change readpoint
        if self._buffer.get(self._writepoint) != None:
            if self._readpoint > self._size:
                self._readpoint = 0
            self._readpoint = self._readpoint + 1
        
        self._buffer[self._writepoint] = element
        self._writepoint = self._writepoint + 1
        
       

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
        buffer.buffer_print()
        print(buffer.read())
        #print(buffer.read())
        buffer.buffer_print()


if __name__ == "__main__":
    test_circularbuffer()
