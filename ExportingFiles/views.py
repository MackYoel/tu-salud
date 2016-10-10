#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import date
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Town, Weather, Clientes, Triaje
from .excel_utils import *
from .pdf_utils import PdfPrint
import datetime
import pandas as pd
from . import define_reports
from helpers import (
    CSV_SERIE,
    get_attribute,
    get_all_related_records,
    get_reduced_q_objects
)
from . import models


def all_clientes(request):

    clientes = Clientes.objects.all()[:20]

    template_name = "exportingfiles/all_clientes.html"
    context = {
        'clientes': clientes,
    }

    if 'excel' in request.POST:
        from_date = datetime.datetime.strptime(request.POST.get('from_date'), "%Y-%m-%d")
        to_date = datetime.datetime.strptime(request.POST.get('to_date'), "%Y-%m-%d") + datetime.timedelta(hours=23, minutes=59)
        business = request.POST.get('business', '')

        report = getattr(define_reports, request.POST.get('report'))
        Model = getattr(models, report['model'])

        date_filter = {
            'tfecha__gte': from_date,
            'tfecha__lte': to_date,
        }

        result = None
        queryset = get_all_related_records(Model, date_filter)
        if queryset:
            q_objects = get_reduced_q_objects(date_filter, business)
            if q_objects:
                result = queryset.filter(q_objects)

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=robin.xlsx'
        # xlsx_data = WriteToExcel(weather_period, town)

        # Create a Pandas dataframe from the data.

        df = pd.DataFrame({})

        output = StringIO.StringIO()

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(output, engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet1')

        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']

        report_rows = report['rows']

        # Write Headers
        indx = 0
        for header_name, _ in report_rows:
            worksheet.write(CSV_SERIE[indx] + '1', header_name)
            indx += 1

        # Write rows
        if result:
            i = 2
            for _obj in result:
                csv_i = 0
                for header_name, attr in report_rows:
                    worksheet.write(CSV_SERIE[csv_i] + str(i), get_attribute(_obj, attr))
                    csv_i += 1
                i += 1

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        response.write(output.getvalue())
        return response


    return render(request, template_name, context)


def all_towns(request):
    towns = Town.objects.all()
    template_name = "exportingfiles/all_towns.html"
    context = {
        'towns': towns,
    }
    return render(request, template_name, context)


def today_weather(request):
    today = date.today()
    today_w = Weather.objects.filter(date=today)
    template_name = "exportingfiles/today_weather.html"
    context = {
        'today_weather': today_w
    }
    return render(request, template_name, context)


def weather_history(request):
    weather_period = Weather.objects.all()
    town = None
    if request.method == 'POST':
        form = WeatherForm(data=request.POST)
        if form.is_valid():
            town_id = form.data['town']
            town = Town.objects.get(pk=town_id)
            weather_period = Weather.objects.filter(town=town_id)
        if 'excel' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
            # xlsx_data = WriteToExcel(weather_period, town)

            # Create a Pandas dataframe from the data.
            df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

            # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet1')

            # Close the Pandas Excel writer and output the Excel file.
            writer.save()

            #response.write(writer.)
            return response

        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfPrint(buffer, 'A4')
            pdf = report.report(weather_period, 'Weather statistics data')
            response.write(pdf)
            return response
    else:
        form = WeatherForm()

    template_name = "exportingfiles/weather_history.html"
    context = {
        'form': form,
        'town': town,
        'weather_period': weather_period,
    }
    return render(request, template_name, context)

def triaje_history(request):
    triaje_period = Triaje.objects.all()
    chistoria = None
    form = None
    if request.method == 'POST':
        form = TriajeForm(data=request.POST)
        if form.is_valid():
            chistoria = form.data['Clientes']
            clientes = Clientes.objects.get(pk=chistoria)
            triaje_period = Triaje.objects.filter(chistoria=chistoria)
        if 'excel' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
            xlsx_data = WriteToExcel(triaje_period, clientes)
            response.write(xlsx_data)
            return response
        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfPrint(buffer, 'A4')
            pdf = report.report(triaje_period, 'Weather statistics data')
            response.write(pdf)
            return response
    else:
        form = TriajeForm()

    template_name = "exportingfiles/triaje_history.html"
    context = {
        'form': form,
        'clientes': chistoria,
        'triaje_period': triaje_period,
    }
    return render(request, template_name, context)


def details(request, weather_id):
    weather = Weather.objects.get(pk=weather_id)
    template_name = "exportingfiles/details.html"
    context = {
        'weather': weather,
    }
    return render(request, template_name, context)
