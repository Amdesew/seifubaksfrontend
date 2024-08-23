from backendapp.models import Fuel, Oil

router = Router()

@router.get("/fuel")
def fuel_list_function(request):
    fuel_list = Fuel.objects.all()
    return fuel_list