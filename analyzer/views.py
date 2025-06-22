from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import LegalDocument
from .ai import build_vector_store, get_answer_from_store
import os
from django.contrib.auth.decorators import login_required

# Dummy implementations; replace with actual logic or import from the correct module
def extract_text_from_pdf(pdf_path):
    # TODO: Implement PDF text extraction
    return "Extracted text from PDF"

def analyze_document(text):
    # TODO: Implement document analysis/summary
    return "Summary of the document"

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            text = extract_text_from_pdf(doc.file.path)
            summary = analyze_document(text)
            doc.summary = summary
            doc.save()
            return render(request, 'summary.html', {'doc': doc})
    else:
        form = UploadForm()
    return render(request, 'analyzer/upload.html', {'form': form})


def document_chat(request, doc_id):
    doc = LegalDocument.objects.get(pk=doc_id)
    answer = None

    if request.method == 'POST':
        question = request.POST.get('question')
        index_path = f'vectorstores/{doc.id}'
        answer = get_answer_from_store(index_path, question)

    return render(request, 'analyzer/chat.html', {'doc': doc, 'answer': answer})
