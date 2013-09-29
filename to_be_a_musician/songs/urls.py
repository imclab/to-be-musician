from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from songs.views import InterpretationView, InterpretationCreateView, SongView

SONG_URL_PATTERN = '(?P<artist_slug>[\w_-]+)/(?P<song_slug>[\w_-]+)'

urlpatterns = patterns('',
    url(r"{0}/interpretation/add/$".format(SONG_URL_PATTERN),
        InterpretationCreateView.as_view(), name='songs_interpretation_add'),
    url(r"{0}/interpretation/(?P<id>\d+)/$".format(SONG_URL_PATTERN),
        InterpretationView.as_view(), name='songs_interpretation_detail'),
    url(r"{0}/$".format(SONG_URL_PATTERN), SongView.as_view(), name='songs_song'),
)
