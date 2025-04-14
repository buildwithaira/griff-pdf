from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'editor/home.html')

def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf = request.FILES['pdf_file']
        fs = FileSystemStorage(location='media/uploaded_pdfs/')
        filename = fs.save(pdf.name, pdf)
        file_url = fs.url(f"uploaded_pdfs/{filename}")
        return redirect(f'/edit/?file={file_url}')
    return redirect('home')

def edit_page(request):
    file_url = request.GET.get('file')
    return render(request, 'editor/editpage.html', {'file_url': file_url})
