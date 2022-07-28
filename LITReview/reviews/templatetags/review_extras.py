from django import template
from reviews import models

register = template.Library()


@register.filter
def model_type(instance):
    return type(instance).__name__


@register.filter
def existing_review(instance):
        reviews = models.Review.objects.filter(ticket=instance)
        if len(reviews) == 0:
            return True


@register.simple_tag(takes_context=True)
def get_poster_display(context, user, instance):
    action = "demandé"
    if instance == "review":
        action = "publié"
    if user == context['user']:
        return f"vous avez {action} une critique"
    return f"{user.username} a {action} une critique"


@register.simple_tag(takes_context=True)
def get_rating_stars(context, rate):
    rating = ""
    for x in range(rate):
        rating += "★"
    for x in range(5-rate):
        rating += "☆"
    return rating
