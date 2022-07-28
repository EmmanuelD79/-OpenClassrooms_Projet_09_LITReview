from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from authentication.models import User
from . import forms, models
from django.conf import settings

REDIRECT_URL = settings.REDIRECT_URL


@login_required
def feed(request):
    all_reviews = models.Review.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user__in=request.user.follows.all())
    all_tickets = models.Ticket.objects.filter(user=request.user)
    tickets = models.Ticket.objects.filter(user__in=request.user.follows.all()).exclude(
        review__in=reviews
    )
    reviews_and_tickets = sorted(
        chain(reviews, tickets, all_reviews, all_tickets),
        key=lambda instance: instance.time_created, reverse=True
    )

    paginator = Paginator(reviews_and_tickets, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'reviews/feed.html', context=context)


@login_required
def own_feed(request):

    reviews = models.Review.objects.filter(user=request.user)
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews_and_tickets = sorted(
        chain(reviews, tickets),
        key=lambda instance: instance.time_created, reverse=True
    )

    paginator = Paginator(reviews_and_tickets, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'reviews/posts.html', context=context)


@login_required
def create_ticket(request):

    form = forms.TicketForm()

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect(REDIRECT_URL)
    return render(request, 'reviews/create_ticket.html', context={'form': form})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'reviews/view_ticket.html', {'ticket': ticket})


@login_required
def create_review(request):

    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if any([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect(REDIRECT_URL)

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }

    return render(request, 'reviews/create_review.html', context=context)

@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'reviews/view_review.html', {'review': review})


@login_required
def edit_review(request, review_id):

    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()

    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect(REDIRECT_URL)

        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect(REDIRECT_URL)

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }

    return render(request, 'reviews/edit_review.html', context=context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    review.delete()

    return redirect(REDIRECT_URL)


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    ticket.delete()

    return redirect(REDIRECT_URL)


@login_required
def delete_sub_user(request, sub_pk):
    sub = get_object_or_404(models.UserFollows, pk=sub_pk)
    sub.delete()

    return redirect('follow_users')


@login_required
def edit_ticket(request, ticket_id):

    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()

    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect(REDIRECT_URL)

        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect(REDIRECT_URL)

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }

    return render(request, 'reviews/edit_ticket.html', context=context)


@login_required
def follow_users(request):

    followed_by = models.UserFollows.objects.filter(user=request.user)
    followed_by_id =[followed.followed_user_id for followed in models.UserFollows.objects.filter(user=request.user)]
    follow = models.UserFollows.objects.filter(followed_user=request.user)
    choices = User.objects.exclude(id=request.user.id).exclude(id__in=followed_by_id).values_list("id", "username")

    form = forms.FollowUsersForm(request.POST, choices=choices)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, choices=choices)
        followed_id = request.POST.get('followed_id')
        followed_user = User.objects.get(id=followed_id)

        if form.is_valid():
            follow = models.UserFollows.objects.create(user=request.user, followed_user=followed_user)
            follow.save()
            return redirect('follow_users')

    context = {
        'followed_by': followed_by,
        'follow': follow,
        'form': form
    }

    return render(request, 'reviews/follow_users_form.html', context=context)


@login_required
def respond_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect(REDIRECT_URL)

    context = {
        'ticket': ticket,
        'review_form': review_form,
    }

    return render(request, 'reviews/respond.html', context=context)
