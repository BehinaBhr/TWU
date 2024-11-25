# class that models a point on a 2-d plot
class Point:
   """Represents a point in 2-D space.
   
   class variable: orgX, orgY; represents point of reference
   
   instance variable: x, y; representing the x/y coordinate of the point RELATIVE
                            to the reference

   Note: by convention, Python class file starts with captial letter and uses 
   the camel case convention

   e.g. BankAccount.py NOT bank_account.py
   """

   # class variable indicating a point representing a reference origin 
   _orgX = 0
   _orgY = 0

   # class method to update value of _orgX
   @classmethod
   def setOrgX(cls,x):
      """
      update the reference point x coordinate

      Args:
      x (int): x coordinate
      """
      cls._orgX = x

   # class method to update value of _orgY   
   @classmethod
   def setOrgY(cls,y):
      """
      update the reference point y coordinate
      
      Args:
      y (int): y coordinate
      """
      cls._orgY = y

   # constructor
   def __init__(self,x,y):
      """
      constructor (initialization funciton)
      - set initial values for x,y

      Args:
      x (int): x coordimate
      y (int): y coordinate
      """
      # whenever we prepend "self.", we indicate that this is an instance 
      # variable and not a local variable
      self._x = x # instance variable
      self._y = y # "_" to indicate its private

   # instance method
   def getAbsoluteX(self):
      """
      return the absolute value of the x-coordinate

      Returns:
      int: absolute x coordinate
      """
      return self._orgX + self._x
   
   # instance method
   def getAbsoluteY(self):
      """
      return the absolute value of the y-coordinate

      Returns:
      int: absolute y coordinate
      """
      return self._orgY + self._y

   # instance method
   def __str__(self):
      """
      return a string representation of this object
      
      This function is useful if we want to print information about this object 
      that is human-readable

      when we do print(x) where x = instance of Point class, this method gets
      called

      Returns:
         str: string representation of this object
      """
      # to access the attributes, you need to prepend the variable
      # name with "self."
      return "x="+str(self._x)+", y="+str(self._y)+" relative to (x="+str(self._orgX)+"/y="+str(self._orgY)+")"

   # instance method
   def distFromOrigin(self, p):
      """
      a function that calculates the distance between this Point and the input Point object

      Args:
         p (Point): input point object
      
      Returns:
         float: distance between this 
      """
      return ((self.getAbsoluteX() - p.getAbsoluteX())**2 + (self.getAbsoluteY() - p.getAbsoluteX())**2)**0.5