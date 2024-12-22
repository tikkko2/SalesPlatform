from registration.models import AddToCart

def get_number(request):
    if request.user.is_authenticated:
        number = AddToCart.objects.filter(user=request.user).count()
    else:
        number = 0
    return {
        "number" : number
    }