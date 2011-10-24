class Dencoder():
    BASE64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")
    SAFE_BASE64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    URL_SAFE = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_;:.+=$")
    HEX = list("0123456789ABCDEF")
    alphabet = BASE64
    
    def __init__(self, alphabet=None):
        """
        Set up the decoder/encoder alphabet.
        """
        if alphabet:
            self.alphabet = alphabet
        self.base = len(self.alphabet)
        
    def encode(self, number):
        """
        Turns a number in to a string that represents it.
        """
        if number == 0:
            return self.alphabet[0]
        s = ''
        while number > 0:
            s += self.alphabet[number % self.base]
            number /= self.base
        return s[::-1] # reverse string
        
    def decode(self, s):
        """
        Turns string encoding back in to a number.
        """
        i = 0
        for char in s:
            i = i * self.base + self.alphabet.index(char)
        return i
        
    def in_alphabet(self, s):
        """
        Takes a string and checks the values are in the alphabet used.
        """
        for char in s:
            if char not in self.alphabet:
                return False
        return True
