from django.shortcuts import render
from .models import UserTweet
from .forms import UserTweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def  index(request):
    return render(request, 'index.html')

@login_required
def add_tweet(request):
    if request.method == "POST":
        form  = UserTweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('get_list_of_tweets')
    else:
        form = UserTweetForm()
    return render(request,'tweet_form.html',{'form':form})   


@login_required
def edit_tweet(request,id):
    tweet = get_object_or_404(UserTweet,pk = id,user = request.user)
    if request.method == "POST":
        form = UserTweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('get_list_of_tweets')
    else:
        form = UserTweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})  



def delete_tweet(request,id):
    tweet = get_object_or_404(UserTweet,pk=id,user=request.user)
    if request.method  == "POST":
        tweet.delete()
        return redirect('get_list_of_tweets')
    return render(request,'tweet_delete.html',{'tweet':tweet})  



def get_all_tweets(request):
    user_tweets = UserTweet.objects.all().order_by("-created_at")
    return render(request,'tweet_list.html',{'tweets':user_tweets})




def register(request):
    if request.method == "POST":
        form  = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('get_list_of_tweets')


    else:
        form  = UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})