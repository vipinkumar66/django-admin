from django.contrib import admin
from django.urls.resolvers import URLPattern
from .models import CrashData
from django.urls import path
from django.shortcuts import render
from django import forms


class InputCsvForm(forms.Form):
    select_file = forms.FileField()

class VinAdmin(admin.ModelAdmin):
    list_display = ("vin", "county")

    def get_urls(self) -> list[URLPattern]:
        urls =  super().get_urls()
        new_urls = [
            path("upload-csv/",self.upload_csv )
        ]
        return new_urls+urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["select_file"]
            file_data = csv_file.read().decode("utf-8")
            file_data = file_data.split("\n")
            for x in file_data[1:]:
                data = x.split(",")[:5]
                create = CrashData.objects.update_or_create(
                    vin = data[0],
                    crash_date = data[1],
                    county = data[2],
                    report_time = data[3]
                )
                print("created")


        form = InputCsvForm()
        return render(request, "admin/csv_upload.html", {"form":form})


admin.site.register(CrashData, VinAdmin)