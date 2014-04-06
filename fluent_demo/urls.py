from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fluent_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

### fluent-blogs ##############################################################

from fluent_blogs.sitemaps import \
	EntrySitemap, CategoryArchiveSitemap, AuthorArchiveSitemap, \
	TagArchiveSitemap

sitemaps = {
    'blog_entries': EntrySitemap,
    'blog_categories': CategoryArchiveSitemap,
    'blog_authors': AuthorArchiveSitemap,
    'blog_tags': TagArchiveSitemap,
}

urlpatterns += patterns('',
    url(r'^admin/util/taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),
    # url(r'^blog/comments/', include('django.contrib.comments.urls')),
    # url(r'^blog/', include('fluent_blogs.urls')), # Not needed if using `fluent_blogs.pagetypes.blogpage`.
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

### fluent-dashboard ##########################################################

urlpatterns += patterns('',
    url(r'^admintools/', include('admin_tools.urls')),
)

### form-designer #############################################################

urlpatterns += patterns('',
    (r'^forms/', include('form_designer.urls')),
)

### fluent-pages ##############################################################

urlpatterns += patterns('',
    url(r'^', include('fluent_pages.urls')) # Must come last, to catch all.
)
