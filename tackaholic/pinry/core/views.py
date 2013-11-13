from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django_images.models import Image
from django.contrib.auth.decorators import login_required

from braces.views import JSONResponseMixin, LoginRequiredMixin
from django_images.models import Thumbnail

from .forms import ImageForm#, BoardForm
from pinry.core.models import Board


class CreateImage(JSONResponseMixin, LoginRequiredMixin, CreateView):
    template_name = None  # JavaScript-only view
    model = Image
    form_class = ImageForm

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseRedirect(reverse('core:recent-tacks'))
        return super(CreateImage, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        image = form.save()
        for size in settings.IMAGE_SIZES.keys():
            Thumbnail.objects.get_or_create_at_size(image.pk, size)
        return self.render_json_response({
            'success': {
                'id': image.id
            }
        })

    def form_invalid(self, form):
        return self.render_json_response({'error': form.errors})

class CreateBoard(CreateView):
    template_name = None  # JavaScript-only view
    model = Board
    #form_class = BoardForm

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseRedirect(reverse('core:board'))
        return super(CreateBoard, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        board = form.save()
        return self.render_json_response({
            'success': {
                'id': board.id
            }
        })

    def form_invalid(self, form):
        return self.render_json_response({'error': form.errors})
