from rest_framework.permissions import BasePermission
from datetime import date, timedelta

class IsOwner(BasePermission):
    message = "You must be the owner of this booking to access it"
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
    

class UpdateOrCancel(BasePermission):
    message = "You cannot update/cancel a booking unless it is 3 days away"
    
    def has_object_permission(self, request, view, obj):
        obj_date = obj.date
        today = date.today()
        diff = timedelta(days=3)
        return obj_date > (today + diff)