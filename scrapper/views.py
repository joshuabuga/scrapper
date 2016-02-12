from django.shortcuts import (render_to_response, 
                              get_object_or_404, render)
from django.http import *
from scrapper.forms import *
from scrapper.models import MasterCsv
from scrapper.settings import *
from scraper.go import go
from django.core import serializers
import json
import glob
import os,sys
from django.views.generic import View
from scrapper.companiesFactory_one import companiesFactoryOne
from scrapper.companiesFactory import companiesFactory
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
@login_required(login_url='/login/')
def properties_list(request):
	properties_list_data= MasterCsv.objects.all()
	
	properties_list_json=serializers.serialize("json",properties_list_data)
	return render(request,'html/grid.html',{'data':properties_list_json})
def dashboard(request):
	
	return render(request,'html/dashboard.html')


class Upload(View):
	form=UploadForm()
	company_factory=companiesFactory()
	
	def post(self,request):

		form=UploadForm(request.POST,request.FILES)
		if form.is_valid():
			uploaded_file = form.save()
			company=request.POST['company']
			company_file=request.FILES['file'].name
			self.company_factory.set_file(company, uploaded_file.file)
			
			self.company_factory.save_company_data(company)
			return render(request,'html/success.html')
	def get(self,request):
		
		return render(request,'html/uploader.html',{'form':self.form})
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, *args, **kwargs):
		return super(Upload, self).dispatch(*args, **kwargs)
class UpdateList(View):
	form=UploadForm()
	company_factory=companiesFactoryOne()
	
	def post(self,request):

		form=UploadForm(request.POST,request.FILES)
		if form.is_valid():
			uploaded_file = form.save()
			company='master-list'
			company_file=request.FILES['file'].name
			
			self.company_factory.set_file(company, uploaded_file.file)
			
			self.company_factory.save_company_data(company)
			return render(request,'html/success.html')

	def get(self,request):
		# files_folder=MEDIA_ROOT + '/' + 'files/'
		# fileList = os.listdir(files_folder)
		# for fileName in fileList:
		# 	os.remove(files_folder+"/"+fileName)
	
		return render(request,'html/update.html',{'form':self.form})
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, *args, **kwargs):
		return super(UpdateList, self).dispatch(*args, **kwargs)
class Search(View):
	form=UploadForm()
	company_factory=companiesFactoryOne()
	
	def post(self,request):

		form=UploadForm(request.POST)
		if form.is_valid():
			search_code = request.POST['search_text']
			
			return render(request,'html/success.html')




		return render(request,'html/500.html')
	def get(self,request):
		
		return render(request,'html/search.html',{'form':self.form})
	@method_decorator(login_required(login_url='/login/'))
	def dispatch(self, *args, **kwargs):
		return super(Search, self).dispatch(*args, **kwargs)

