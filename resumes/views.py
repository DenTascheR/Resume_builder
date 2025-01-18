from django.http import HttpResponse
from reportlab.pdfgen import canvas

def export_pdf(request, pk):
    resume = Resume.objects.get(pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.title}.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 800, resume.title)
    p.drawString(100, 780, resume.content)
    p.showPage()
    p.save()
    return response
