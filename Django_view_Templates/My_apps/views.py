from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwagrs):
        context = super().get_context_data(** kwagrs)
        
        context['name'] = "Rakibul Islam" 
        context['country'] = "Bangladesh"

        list = [1,2,3,4,5,6]
        context['list'] = list 


        return context