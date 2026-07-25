from django.template.context import Context

def patch_context_copy():
    def custom_copy(self):
        duplicate = Context()
        duplicate._processors = getattr(self, '_processors', None)
        duplicate._processors_index = getattr(self, '_processors_index', None)
        duplicate.autoescape = getattr(self, 'autoescape', True)
        duplicate.use_l10n = getattr(self, 'use_l10n', None)
        duplicate.use_tz = getattr(self, 'use_tz', None)
        duplicate.template_name = getattr(self, 'template_name', None)
        duplicate.template = getattr(self, 'template', None)
        duplicate.render_context = getattr(self, 'render_context', None)
        duplicate.dicts = [d.copy() for d in getattr(self, 'dicts', [])]
        return duplicate

    Context.__copy__ = custom_copy

patch_context_copy()
