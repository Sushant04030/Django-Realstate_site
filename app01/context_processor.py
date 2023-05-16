from .models import *

def menu_links(request):
    try:
        locations = City.objects.all()
    except:
        locations = None

    try:
        types = PropertyType.objects.all()
    except:
        types = None

    try:
        c_agents = Agent.objects.all()
    except:
        c_agents = None
    
    try:
        c_agents=c_agents[:4]
    except:
        pass

    try:

        c_testimonials = Testimonial.objects.all()[:3] 
    except:
        c_testimonials = Testimonial.objects.all()


    return dict( locations = locations , types = types , c_agents = c_agents , c_testimonials = c_testimonials)