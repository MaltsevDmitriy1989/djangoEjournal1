class TitleMixin:
    title = None
    greeting = None
    name = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['greeting'] = self.greeting
        context['name'] = self.name
        return context