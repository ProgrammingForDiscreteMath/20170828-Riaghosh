from math import sqrt
class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def sum(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def product(self,other):
        """
        Return the product of ``self`` and ``other``.
        """
        return ComplexNumber(self.real*other.real - self.imaginary*other.imaginary, 
                             self.imaginary*other.real + self.real*other.imaginary)
    
    def complex_conjugate(self):
        """
        Return the complex conjugate of ``self``.
        The complex conjugate of a complex number is a complex number with real and imaginary parts
        equal in magnitude to the original number but with a opposite sign in the imaginary part.
        """
        return ComplexNumber.__init__(self, self.real, - self.imaginary)
        
        
        

class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
    
    def polar_coordinates(self):
        """
        Return the polar coordinates of the complex number ``self``.
        """
        return (ComplexNumber.modulus(self),atan(self.imaginary/self.real))
        
    def logarithm(self):
        """
        Return the principal branch of a logarithm of a complex number. 
        The logarithm of a complex number  ``z`` is defined as log(z) = log(mod(z)) + i*arg(z).
        """
        temp=self.polar_coordinates()
        return ComplexNumber(log(temp[0]),temp[1])
    
    
