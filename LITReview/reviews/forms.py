from django import forms
from . import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    title = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': "field-width"})
    )
    description = forms.CharField(
        max_length=2048,
        widget= forms.Textarea(attrs={'class': "field-width"})
    )

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    CHOICES = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)]

    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    headline = forms.CharField(
        max_length=128,
        label='Titre',
        widget=forms.TextInput(attrs={'class': "field-width"})
    )
    body = forms.CharField(
        max_length=8192,
        label='Commentaire',
        widget= forms.Textarea(attrs={'class': "field-width"})
    )

    rating = forms.CharField(label='Note', widget=forms.RadioSelect(choices=CHOICES, attrs={'class':'radio-block'}))

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.Form):

    class Meta:
        fields = ['followed_id']

    def __init__(self, *args, choices, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['followed_id'] = forms.ChoiceField(label='Nom utilisateur', choices=choices)
        self.fields['followed_id'].widget.attrs.update({'class': 'form-user-add'})
