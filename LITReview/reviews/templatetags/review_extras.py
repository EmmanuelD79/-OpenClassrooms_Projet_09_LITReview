from django import template


register = template.Library()


@register.filter
def model_type(instance):
    return type(instance).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user, instance):
    action = "demandé"
    if instance == "review":
        action = "publié"
    if user == context['user']:
        return f"Vous avez {action} une critique"
    return f"{user.username} a {action} une critique"


@register.simple_tag(takes_context=True)
def get_rating_stars(context, rate):
    rating = ""
    for x in range(rate):
        rating += "★"
    for x in range(5-rate):
        rating += "☆"
    return rating
