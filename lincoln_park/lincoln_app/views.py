from django.shortcuts import render

from lincoln_app.models import AllLayers,Photos,PublicArt,Restaurants,Sports,Testing,WaterLeisure,Zoo
from django.core import serializers
# from django.core import serialize
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

from django.views.generic import TemplateView
from lincoln_app.models import Testing
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import NameForm,photoForms
# Create your views here.
from . import forms


# class HomeView(TemplateView):
#     template_name = 'park/index.html'
#     def index(self,request):
#     	all_L = AllLayers.objects.all()
#     	all_data = serializers.serialize('geojson', all_L, fields=('geoid','place_name','icon_name','latitude','longitude','geom'))
#     	#arts in park
#     	art = PublicArt.objects.all()
#     	art_data = serializers.serialize('geojson', art, fields=('geoid','park_name','park_number','place_name','artist_name','latitude','longitude','geom'))
#     	#food in park
#     	food = Restaurants.objects.all()
#     	food_data = serializers.serialize('geojson', food, fields=('geoid','activity_type','place_name','latitude','longitude','geom'))
#     	#all physical activites 
#     	photos = Photos.objects.all()
#     	photo_data = serializers.serialize('geojson', photos, fields=('caption','image','latitude','longitude','geom'))
#     	#all physical activites 
#     	sports = Sports.objects.all()
#     	sports_data = serializers.serialize('geojson', sports, fields=('geoid','place_name','latitude','longitude','geom'))
#     	#water based activites Beach, Harbor, Yatch
#     	water = WaterLeisure.objects.all()
#     	water_data = serializers.serialize('geojson', water, fields=('geoid','activity_type','place_name','longitude','latitude','geom'))
#     	#layer for Lincoln Park Zoo activites
#     	zoo = Zoo.objects.all()
#     	zoo_data = serializers.serialize('geojson', zoo,fields=('geoid','activity_type','place_name','longitude','latitude','geom'))
#     	form = NameForm()
#     	return render(request,self.template_name,{'all_data_layer':all_data,'art':art_data,'food':food_data,'pictures':photo_data,'sports':sports_data,'water':water_data,'zoo':zoo_data,'form':form})
#     	# return HttpResponse(request,self.template_name,{'all_data_layer':all_data,'art':art_data,'food':food_data,'pictures':photo_data,'sports':sports_data,'water':water_data,'zoo':zoo_data,'form':form})
#     def post(self, request):
#     	form = NameForm(request.POST)
#     	if form.is_valid():
#     		post = form.save(commit=False)
#     		post.user = request.user
#     		post.save()
#     		# text = form.cleaned_data['post']
#     	# 	form = NameForm()
#     	# 	return redirect('home:home')
#     	# args = {'form': form, 'text': text}
#     	# return render(request, self.template_name, args)


def index(request):
	if request.method == 'GET':
		all_L = AllLayers.objects.all()
		all_data = serializers.serialize('geojson', all_L, fields=('geoid','place_name','icon_name','latitude','longitude','geom'))
		#arts in park
		art = PublicArt.objects.all()
		art_data = serializers.serialize('geojson', art, fields=('geoid','park_name','park_number','place_name','artist_name','latitude','longitude','geom'))
		#food in park
		food = Restaurants.objects.all()
		food_data = serializers.serialize('geojson', food, fields=('geoid','activity_type','place_name','latitude','longitude','geom'))
		#all physical activites 
		photos = Photos.objects.all()
		photo_data = serializers.serialize('geojson', photos, fields=('ids','caption','image','latitude','longitude','geom'))
		#all physical activites 
		sports = Sports.objects.all()
		sports_data = serializers.serialize('geojson', sports, fields=('geoid','place_name','latitude','longitude','geom'))
		#water based activites Beach, Harbor, Yatch
		water = WaterLeisure.objects.all()
		water_data = serializers.serialize('geojson', water, fields=('geoid','activity_type','place_name','longitude','latitude','geom'))
		#layer for Lincoln Park Zoo activites
		zoo = Zoo.objects.all()
		zoo_data = serializers.serialize('geojson', zoo,fields=('geoid','activity_type','place_name','longitude','latitude','geom'))
		# form = NameForm()
		# return render(request,'park/index.html',{'all_data_layer':all_data,'art':art_data,'food':food_data,'pictures':photo_data,'sports':sports_data,'water':water_data,'zoo':zoo_data,'form':form})
		return render(request,'park/index.html',{'all_data_layer':all_data,'art':art_data,'food':food_data,'pictures':photo_data,'sports':sports_data,'water':water_data,'zoo':zoo_data})
	##this is for forms
	# elif request.method == 'POST':
	# 	form = NameForm(request.POST)
	# 	if form.is_valid():
	# 		post = form.save(commit=False)
	# 		post.user = request.user
	# 		post.save()
	# 		return HttpResponseRedirect("http://127.0.0.1:8000/")
	
	# elif request.method == 'POST':
	# 	form = NameForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return HttpResponseRedirect("http://127.0.0.1:8000/")
	# 	else:
	# 		return HttpResponseRedirect("http://127.0.0.1:8000/")
	##this is for testing
	# elif request.method == 'POST':
	# 	# form = NameForm(request.POST)
	# 	if request.POST.get('in_name'):
	# 		#database
	# 		post = Testing()
	# 		post.person_name= request.POST.get('in_name')
	# 		post.save()
	# 		return HttpResponseRedirect("http://127.0.0.1:8000/")
	# 	else:
	# 		return HttpResponseRedirect("http://127.0.0.1:8000/")


	elif request.method == 'POST':
		# if request.POST.get('in_name'):
		#database
		post = Photos()
		post.ids= request.POST.get('ids')
		post.caption= request.POST.get('caption')
		post.image= request.POST.get('fileupload')
		post.latitude= request.POST.get('latitude')
		post.longitude= request.POST.get('longitude')
		
		post.save()
		return HttpResponseRedirect("http://127.0.0.1:8000/")
		# else:
		# 	return HttpResponseRedirect("http://127.0.0.1:8000/")









#SAVE This
#http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php



# def createpost(request):
#         if request.method == 'POST':
#             if request.POST.get('in_name'):
#             	#database
#                 post=Post()
#                 )
#                 post.content= request.POST.get('content')
                
                
#                 return render(request, 'posts/create.html')  

#         else:
#                 return render(request,'posts/create.html')





	# else:
	# 	return render(request, 'park/index.html')
# def add(request):
#         if request.method == 'POST':
#                 form = RecipeForm(request.POST)
#                 if form.is_valid():

#                         form.save()
#                         #redirect
#                         return HttpResponse("Thank you")
#                 else:
#                         return HttpResponse("Form Not Valid")
	
# def post(self, request):
# 	form = NameForm(request.POST)
# 	if form.is_valid():
# 		post = form.save(commit=False)
# 		post.user = request.user
# 		post.save()
#     		# text = form.cleaned_data['post']
#     	# 	form = NameForm()
#     	# 	return redirect('home:home')
#     	# args = {'form': form, 'text': text}
#     	# return render(request, self.template_name, args)

# #DO NOT DELETE
# def index(request):
# 	#all layers
# 	all_L = AllLayers.objects.all()
# 	all_data = serializers.serialize('geojson', all_L,
#     	fields=('geoid','place_name','icon_name','latitude','longitude','geom')
#     	)
# 	#arts in park
# 	art = PublicArt.objects.all()
# 	art_data = serializers.serialize('geojson', art,
#     	fields=('geoid','park_name','park_number','place_name','artist_name','latitude','longitude','geom')
#     	)
# 	#food in park
# 	food = Restaurants.objects.all()
# 	food_data = serializers.serialize('geojson', food,
#     	fields=('geoid','activity_type','place_name','latitude','longitude','geom')
#     	)
# 	#all physical activites 
# 	photos = Photos.objects.all()
# 	photo_data = serializers.serialize('geojson', photos,
#     	fields=('caption','image','latitude','longitude','geom')
#     	)
# 	#all physical activites 
# 	sports = Sports.objects.all()
# 	sports_data = serializers.serialize('geojson', sports,
#     	fields=('geoid','place_name','latitude','longitude','geom')
#     	)
# 	#water based activites Beach, Harbor, Yatch
# 	water = WaterLeisure.objects.all()
# 	water_data = serializers.serialize('geojson', water,
#     	fields=('geoid','activity_type','place_name','longitude','latitude','geom')
#     	)
# 	#layer for Lincoln Park Zoo activites
# 	zoo = Zoo.objects.all()
# 	zoo_data = serializers.serialize('geojson', zoo,
#     	fields=('geoid','activity_type','place_name','longitude','latitude','geom')
#     	)
# 	form = NameForm()
# 	return render(request,'park/index.html',{'all_data_layer':all_data,'art':art_data,'food':food_data,'pictures':photo_data,'sports':sports_data,'water':water_data,'zoo':zoo_data,'form':form})



# def post(request):
# 	# if this is a POST request we need to process the form data
# 	if request.method == 'POST':
# 	    form = NameForm(request.POST)
# 	    if form.is_valid():
# 	    	name = form.cleaned_data.get('person_name')
# 	    	p = Testing(person_name=name)
# 	    	p.save()
# 	    	print(p)
# 	    	return render(request,'park/index.html')


        # post = form.save(commit=False)
        # post.user = request.user
        # post.save()

        # text = form.cleaned_data['in_name']
        # form = HomeForm()
        # return render(request,'park/index.html')
# def post(request):
# 	form = forms.NameForm()
# 	# form = NameForm()
# 	if request.method == 'POST':
# 	    form = forms.NameForm(request.POST)
# 	    # if form.is_valid():
	    	
#     	form.save()
#     	return render(request,'park/index.html')
	        # post = form.save(commit=False)
	        # post.user = request.user
	        # Contact.objects.create(person_name = form_email )
	        # post.save()

	        # text = form.cleaned_data['in_name']
	        # form = HomeForm()
	        # return render(request,'park/index.html')


