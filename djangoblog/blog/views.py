from django.views.generic import View, DetailView, ListView, TemplateView

from blog.models import Post


class HomePageView(ListView):
	template_name = "homepage.html"

homepage_view = HomePageView.as_view()


class PostView(DetailView):
	template_name = "post.html"

post_view = PostView.as_view()

class ArchiveView(ListView):
	template_name = "archive.html"

archive_view = ArchiveView.as_view()

class AboutView(TemplateView):
    template_name = "about.html"

about_view = AboutView.as_view()