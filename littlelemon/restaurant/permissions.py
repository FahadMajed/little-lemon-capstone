from rest_framework.permissions import BasePermission ,SAFE_METHODS

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class MenuItemsPermission(BasePermission):
    
    

    def has_permission(self, request, view):
         if (request.user.groups.filter(name="Manager").exists()):
              return True
         elif (request.method in SAFE_METHODS and request.user.is_authenticated):
            return True
         else:
            return False
         

class CatagoryPermission(BasePermission):
    
    

    def has_permission(self, request, view):
         if (request.user.groups.filter(name="Manager").exists()):
              return True
         else:
            return False  


class CartPermission(BasePermission):
    

    def has_permission(self, request, view):
         if (request.user.groups.filter(name="Manager").exists() or request.user.groups.filter(name="Delivery Crew").exists()):
              return False
         else:
            return True                     

       
      
    

        
       
