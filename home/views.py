from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post,ContactUs
from django.contrib.auth.models import User
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'home/about.html', context)


def home_view(request):
    context = {
        'title': 'Skaetch'
    }
    return render(request, 'home/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'home/user-post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        filled_form = PostForm(request.POST)
        if filled_form.is_valid():
            title = filled_form.cleaned_data['title']
            content = filled_form.cleaned_data['content']
            description = filled_form.cleaned_data['description']
            user = User.objects.get(id=request.user.id)
            author = user
            post = Post(title=title, content=content,
                        author=author, description=description)
            post.save()
            messages.success(request, f'your post {title} has been submitted')

            context = {
                'title': 'Create Post',
                'form': form,
            }
            return redirect('post-details', pk=post.pk)
        else:
            message = 'The for you submitted is not valid!'
            form = PostForm()
            context = {
                'title': 'Create Post',
                'form': form,
                'message': message,
            }
            return render(request, 'home/create-post.html', context)
    else:
        context = {
            'title': 'Create Post',
            'form': form
        }
        return render(request, 'home/create-post.html', context)


class PostsDetailView(DetailView):
    model = Post
    #template_name = 'home/post-details.html'


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return render(request, 'home/post_update.html', {'form': form})
        else:
            form = PostForm(instance=post)
            messages.error(request, 'Something went wrong try again')
            return render(request, 'home/post_update.html', {'form': form})
    else:
        form = PostForm(instance=post)
        return render(request, 'home/post_update.html', {'form': form})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def isValid(values):
    valid = True
    for value in values:
        if value == '':
            valid = False
    return valid

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if isValid([name, email, subject,message]):
            contact = ContactUs(name=name,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request, 'Your message was sent successfully')
            context = {'title':'Skaetch And Build'}
            return render(request, 'home/index.html',context)
        else:
            context = {'title':'Contact Us'}
            messages.error(request, 'Something went wrong try again')
            return render(request, 'home/contact.html', context)

    context = {'title':'Contact Us'}

    return render(request, 'home/contact.html', context)

def speakers(request):
    context = {'title':'Speakers'}

    return render(request, 'home/speakers.html', context)

def schedule(request):
    context = {'title':'Schedule'}

    return render(request, 'home/schedule.html', context)