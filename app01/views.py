from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator

# mail verification import
from django.core.mail import send_mass_mail

# Create your views here.
def index_view(request):
    try:
        properties  = Property.objects.all().order_by('-id').filter(featured=True,available=True)[:6]
    except:
        properties  = Property.objects.all().order_by('-id').filter(featured=True,available=True)
    try:
        agents      = Agent.objects.all().order_by('-id')[:4]
    except:
        agents      = Agent.objects.all().order_by('-id')
    try:
        testimonial = Testimonial.objects.all().order_by('-id')[:4]
    except:
        testimonial = Testimonial.objects.all().order_by('-id')

    context = {
        'properties'    : properties,
        'agents'        : agents,
        'testimonial'   : testimonial,
    }
    return render(request, 'app01/index.html', context)


# # # # # property views # # # # #
def property_view(request):
    properties          = Property.objects.all().filter(available=True)
    paginator           = Paginator(properties, 15)
    page                = request.GET.get("page")
    paged_properties    = paginator.get_page(page)

    context = {
        'properties'    : paged_properties
    }
    return render(request, 'app01/property.html', context)


def property_detail_view(request, id):
    property            = Property.objects.get(id=id)
    photos              = Gallery.objects.filter(property=property)
    similar_properties  = Property.objects.all().filter(type=property.type,city=property.city,sale=property.sale,available=True).exclude(id=property.id)

    context = {
        'property'              : property,
        'photos'                : photos,
        'similar_properties'    : similar_properties,
    }
    return render(request, 'app01/property_detail.html', context)


# # # # # search views # # # # #
def search_price_view(request,price,types,city,status,keyword):
        
    if keyword == 'N' :
        properties = Property.objects.all().filter(type=types,city=city,rent=True)
        
    else:
        properties = Property.objects.order_by('-created_at').filter(Q(description__icontains=keyword) | Q(title__icontains=keyword))


    if int(status) == 0:
        properties = properties.filter(type=types,city=city,sale=True,available=True)
    else:
        properties = properties.filter(type=types,city=city,rent=True,available=True) 

    if price == 0:
        properties=properties.order_by("-price")
        price = 1
    else :
        properties=properties.order_by("price")
        price = 0

    try:                    
        properties_count   = properties.count()
        paginator = Paginator(properties, 15)
        page = request.GET.get("page")
        properties = paginator.get_page(page)

    except:
        properties_count = 0

    type_name = PropertyType.objects.get(id=types)
    city_name = City.objects.get(id=city)


    context = {
        "properties"        :   properties,
        "properties_count"  :   properties_count,
        "keyword"           :   keyword,
        "type"              :   types,
        "city"              :   city,
        "status"            :   status,
        "price"             :   price,
        "type_name"         :   type_name,
        "city_name"         :   city_name,
    }
    return render(request, 'app01/property.html', context)


def search_view(request):
    properties      = None
    keyword         = None
    type            = request.GET["types"]
    city            = request.GET["city"]
    status          = request.GET["status"]

    if 'keyword' in request.GET and request.GET["keyword"] !="":  
        keyword     = request.GET["keyword"]
        properties              = Property.objects.order_by('-created_at').filter(Q(description__icontains=keyword) | Q(title__icontains=keyword))
    else:
        properties = Property.objects.all()
        
    if int(status) == 0:
        properties = properties.filter(type=type,city=city,sale=True,available=True)
    else:
        properties = properties.filter(type=type,city=city,rent=True,available=True)

    try:                    
        properties_count    = properties.count()
        paginator           = Paginator(properties, 15)
        page                = request.GET.get("page")
        properties          = paginator.get_page(page)

    except:
        properties_count = 0
    
    type_name   = PropertyType.objects.get(id=type)
    city_name   = City.objects.get(id=city)

    context = {
        "properties"            :   properties,
        "properties_count"      :   properties_count,
        "keyword"               :   keyword,
        "type"                  :   type,
        "city"                  :   city,
        "status"                :   status,
        "type_name"             :   type_name,
        "city_name"             :   city_name,
    }
    return render(request, 'app01/property.html', context)


def category_view(request,id):

    category        = PropertyType.objects.get(id = id)
    properties      = Property.objects.all().filter(type=category,available=True)
    paginator       = Paginator(properties, 16)
    page            = request.GET.get("page")
    properties      = paginator.get_page(page)

    context = {
        'properties'    : properties,
        'type'          : category
    }
    return render(request, 'app01/property.html', context)


# # # # # Agents views # # # # #
def agents_view(request):
    agents  = Agent.objects.all()

    context = {
        'agents':agents
    }
    return render(request, 'app01/agent.html', context)


# # # # # about Us views # # # # #
def testimonial_view(request):
    testimonials    = Testimonial.objects.all().order_by('-updated_at')
    paginator       = Paginator(testimonials, 16)
    page            = request.GET.get("page")
    testimonials    = paginator.get_page(page)
    context = {
        'testimonials' : testimonials
    }
    return render(request, 'app01/testimonials.html', context)


# # # # # about Us views # # # # #
def aboutUs_view(request):
    return render(request, 'app01/about.html')


# # # # # Contact Us views # # # # #
def contactUs_view(request):
    return render(request, 'app01/contactUs.html')


def contact_view(request):
    contact = None

    try:
        if request.method == 'POST':
            fullname        = request.POST['fullname']
            email           = request.POST['email'] 
            subject         = request.POST['subject'] 
            message         = request.POST['message'] 
        

            contact    = Contact.objects.create(
                fullname    = fullname, 
                email       = email, 
                subject     = subject,
                message     = message,
            )
            contact.save()

            # email to the customer
            mail_subject    = 'You contacted Easy Realtors successfully'
            message         = (f'Thank you, We will get in touch within 2 working days. \nPlease check your information:\n\tName: {fullname},\n\tEmail: {email},\n\tSubject: {subject},\n\tMessage: {message}')


            # email to yourself
            mail_subject1   = 'Your received a message from your website Easy Realtors'
            message1        = f"\nContacted information :\n\tName: {fullname},\n\tEmail: {email},\n\tSubject: {subject},\n\tMessage: {message}"


            email1 = (mail_subject, message, 'easyspacerealtors.esr@gmail.com', [email])
            email2 = (mail_subject1, message1, 'easyspacerealtors.esr@gmail.com', ['easyspacerealtors.esr@gmail.com'])
            send_mass_mail((email1, email2), fail_silently=False)
            
            messages.success(request,"You contacted us successfully. we have send you a confirmation email")

    except:
        messages.success(request,"Contacting error please check your email correctly and try again")

    return redirect('contactUs_view')   