class download_csv_function:
    def download_csv(self,request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        # Using IO for creating the file in memory
        f = StringIO()
        writer = csv.writer(f)

        #Getting the heaader
        writer.writerow(['name', 'price', 'description'])

        # Getting the selected rows
        for i in queryset:
            writer.writerow([i.name, i.price, i.description])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=coffee_db.csv'
        return response
