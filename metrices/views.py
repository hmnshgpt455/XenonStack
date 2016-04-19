from django.shortcuts import render,render_to_response
import json,requests,urllib3
from elasticsearch import Elasticsearch
from django.http import HttpResponse,JsonResponse

def SystemMetricesView(request):
	data = {
		"query" : {
			"query_string" : {"query" : "type: system"}
		}

	}
	response = requests.post('http://localhost:9200/topbeat-*/_search?',data = json.dumps(data))
	
	return HttpResponse(response,content_type = 'application/json')


def PerProcessMetricesView(request,pretty = True):
	data = {
		"query" : {
			"query_string" : {"query" : "type: process"}
		}

	}

	response = requests.post('http://localhost:9200/topbeat-*/_search?pretty',data = json.dumps(data))
	context = {
		'PerProcess_Metrices' : response.json()
	}

	return HttpResponse(response,content_type = 'application/json')

def FileSystemMetricesView(request):
	data = {
		"query" : {
			"query_string" : {"query" : "type: filesystem"}
		}

	}

	response = requests.post('http://localhost:9200/topbeat-*/_search?pretty',data = json.dumps(data))
	return HttpResponse(response,content_type = 'application/json')
