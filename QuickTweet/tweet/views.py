from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    # Show public tweets OR user's own private tweets
    if request.user.is_authenticated:
        tweets = Tweet.objects.filter(
            Q(visibility='public') | Q(user=request.user)
        ).order_by('-created_at')
    else:
        tweets = Tweet.objects.filter(visibility='public').order_by('-created_at')

    # SEARCH FILTER
    query = request.GET.get('q')
    if query:
        if request.user.is_authenticated:
            tweets = tweets.filter(text__icontains=query)
        else:
            tweets = Tweet.objects.filter(text__icontains=query, visibility='public')

    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')

    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def toggle_privacy(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)

    # Toggle visibility
    if tweet.visibility == 'public':
        tweet.visibility = 'private'
    else:
        tweet.visibility = 'public'

    tweet.save()
    return redirect('tweet_list')
