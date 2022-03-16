from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'home/index.html'
  
class StoryView(TemplateView):
  template_name = 'home/story.html'
