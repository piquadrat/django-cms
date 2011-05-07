from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from models import Link

class LinkPlugin(CMSPluginBase):
    model = Link
    name = _("Link")
    render_template = "cms/plugins/link.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        if instance.mailto:
            link = u"mailto:%s" % settings.dbgettext(instance.mailto)
        elif instance.url:
            link = settings.dbgettext(instance.url)
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'name':settings.dbgettext(instance.name),
            'link':link, 
            'placeholder':placeholder,
            'object':instance
        })
        return context
        
    def icon_src(self, instance):
        return settings.CMS_MEDIA_URL + u"images/plugins/link.png"
    
plugin_pool.register_plugin(LinkPlugin)
