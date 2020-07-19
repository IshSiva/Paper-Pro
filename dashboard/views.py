from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from account.models import Author, Reviewer, Editor, User
from .models import Paper

from .forms import PaperUploadForm, DocumentUpdateForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required


from django.db import transaction
from .forms import PaperUploadForm,CommentsUploadForm,AuthorEditForm, StatusUploadForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required




# Create your views here.

def author_dboard(request):

	auth_a = Author.objects.filter(user_id = request.user.author)
	papers = Paper.objects.filter(author = request.user.author)
	print(papers)
	template = loader.get_template('dashboard/authordashboard.html')
	
	return HttpResponse(template.render({'author': auth_a, 'papers': papers}, request))

def reviewer_dboard(request):

	r_prof = Reviewer.objects.filter(user_id=request.user.reviewer)
	paper = Paper.objects.filter(reviewer=request.user.reviewer)
	template = loader.get_template('dashboard/reviewerdashboard.html')

	return HttpResponse(template.render({'reviewer': r_prof, 'papers':paper}, request))	

def editor_dboard(request):

	e_prof = User.objects.filter(id=request.user.id)
	template = loader.get_template('dashboard/editordashboard.html')
	papers = Paper.objects.all()

	return HttpResponse(template.render({'editor': e_prof, 'paper': papers}, request))	

	

def upload_paper(request):
	if request.method == 'POST':
		form = PaperUploadForm(request.POST, request.FILES)
		author = request.user.author

		upload_file = request.FILES['upload_paper']
		print(upload_file.size)
		fs = FileSystemStorage()
		name = fs.save(upload_file.name, upload_file)
		

		
		p = Paper()
		p.paper = name
		p.author = request.user.author
		p.title = request.POST['title']
		p.description = request.POST['description']
		p.field = request.POST['field']
		p.status = "waiting for review"
		p.comments = None
		p.save()
		
		url ='/db/authordboard/' 
		return redirect(url)


		
	else:
		form = PaperUploadForm()
		template = loader.get_template('dashboard/paper_upload.html')

		return HttpResponse(template.render({'upload_form': form}, request))


def view_paper(request, pid):
	p = Paper.objects.filter(id=pid)
	try:
		return(FileResponse(open(p.paper, 'rb'), content_type='application/pdf'))
	except FileNotFoundError:
		raise Http404()



@login_required


def update_paper(request, p_id):
	p = Paper.objects.filter(id = p_id)
	pap = p[0]
	if request.method == "POST":
		doc_form = DocumentUpdateForm(request.POST, request.FILES, instance = request.user.author)
		upload_file = request.FILES['doc']
		#print()
		author = request.user.author
		#print(upload_file.size)

		print(pap.paper)

		fs = FileSystemStorage()
		name = fs.save(upload_file.name, upload_file)

		pap.paper = name
		pap.save()
		#print(name)


		if doc_form.is_valid():
			doc = doc_form.save()
			
			doc.save()

			return redirect("/db/authordboard")

		else:
			print("error")
			print(doc_form.errors)
			return HttpResponse(template.render({'upload_form': doc_form, 'paper': pap}, request))


	else:
		doc_form = DocumentUpdateForm(request.POST, request.FILES, instance = request.user.author)
		template = loader.get_template('dashboard/paper_update.html')
		
		return HttpResponse(template.render({'upload_form': doc_form, 'paper': pap}, request))


def add_comments(request, p_id):
    if request.method == 'POST':
        comments_form = CommentsUploadForm(request.POST)
        if comments_form.is_valid:
            paper_obj = Paper.objects.get(id=p_id)
           # paper_obj = Paper.objects.create()
            print("object created")
          
            comment_data = comments_form.data.get('comments')
            print(comment_data)
            if len(comment_data):
                paper_obj.comments = comment_data
                paper_obj.save()
                #return render(request,'dashboard/reviewerdashboard.html')   
                return redirect("/db/reviewdboard")
            else:
                return redirect("/db/reviewdboard")

        else:
            print(comments_form.errors)
            return render(request,'dashboard/reviewerdashboard.html')

    else:
        comments_form = CommentsUploadForm()
        return render(request,'dashboard/reviewerdashboard.html')



@login_required
@transaction.atomic
def editAuthor(request):
	
	
	if request.method == 'POST':
		auth_form = AuthorEditForm(request.POST,request.FILES, instance = request.user.author)

		author = request.user.author

		
		
		if auth_form.is_valid():


			au = auth_form.save()
			au.save()
			return render(request,'dashboard/authordashboard.html')
		else:
			print(pgr_form.errors)
			return render(request,'dashboard/editauth.html', {'auth_form':auth_form})


	else:
		

		auth_form = AuthorEditForm(instance = request.user.author)
		
		context = {
		 "form":auth_form
					}
		
		return render(request, 'dashboard/editauth.html', context)


def get_reviewer(request, p_id):
	reviewers = Reviewer.objects.all()
	p = Paper.objects.get(id = p_id)
	print(p.title)
	return render(request, 'dashboard/reviewer_list.html', {'paper_details': p, 'reviewers': reviewers})

def assign_reviewer(request, p_id, r_id):
	reviewer = Reviewer.objects.get(user_id = r_id)
	pap = Paper.objects.get(id = p_id)
	pap.reviewer = reviewer
	pap.save()

	return redirect('/db/editordboard')


def add_status(request, p_id):
    if request.method == 'POST':
        status_form = StatusUploadForm(request.POST)
        if status_form.is_valid:
            paper = Paper.objects.get(id=p_id)
            status = status_form.data.get('status')
            if len(status):
                paper.status = status
                paper.save()
                return redirect('/db/editordboard')
            
        else:

            return render(request, 'dashboard/editordashboard.html')
    else:
        
        print(status_form.errors)
        return render(request, 'dashboard/editordashboard.html')


def add_comments(request, p_id):
    if request.method == 'POST':
        comments_form = CommentsUploadForm(request.POST)

        if comments_form.is_valid:
            paper_obj = Paper.objects.get(id=p_id)
           # paper_obj = Paper.objects.create()
            print("object created")
            #comment_data2 = comments_form.data.get('commentstoedit')

            comment_data1 = comments_form.data.get('commentstoauth')

            comment_data2 = comments_form.data.get('commentstoedit')
           #print(comment_data)
            if len(comment_data1):
                paper_obj.commentstoauth = comment_data1
                paper_obj.commentstoedit = comment_data2

                paper_obj.save()
                return redirect('/db/reviewdboard')

            
            
        else:
            print(comments_form.errors)
            return render(request, 'dashboard/reviewerdashboard.html')




