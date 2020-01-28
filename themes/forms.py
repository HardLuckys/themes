from django import forms
from .models import Exercises, Categories
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class ExerciseCreateForm(forms.ModelForm):
    body = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 15},
            mce_attrs=({'menubar': False,
                                    'plugins': ['advlist autolink lists link image imagetools charmap print preview anchor',
                                                'textcolor searchreplace code insertdatetime media',
                                                'table contextmenu paste code help wordcount autoresize'],
                                    'autoresize_min_height': 250,
                                    'autoresize_on_init': False,
                                    'toolbar': '''
                                            insert | undo redo |  formatselect | bold italic backcolor  |
                                            alignjustify | bullist numlist outdent indent |
                                            removeformat | help',
                                            ''',
                                    'toolbar2': '''''',
                                    'content_css': ['//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
                                                    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'],
                                    'content_css_cors': 'true',
                                    'branding': False,
                                    'content_style': 'img {max-width: 100%; height:auto;}',
                                    'imagetools_toolbar': "rotateleft rotateright | flipv fliph | editimage imageoptions",
                                    })
        )
    )
    class Meta:
        model = Exercises
        fields =('categories', 'name', 'description', 'image', 'body')

class CategoriesCreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields =('name', 'description', 'image',)
