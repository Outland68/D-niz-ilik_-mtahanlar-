import copy
from django.template.context import Context

def patch_context_copy():
    def custom_copy(self):
        duplicate = copy.copy(super(Context, self))
        if hasattr(self, 'dicts'):
            duplicate.dicts = self.dicts[:]
        else:
            duplicate.dicts = []
        return duplicate
    Context.__copy__ = custom_copy

patch_context_copy()
