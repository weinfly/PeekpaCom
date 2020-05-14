from django.views.generic import View
from .forms import TagForm, TagEditForm
from apps.poster.models import Tag
from django.shortcuts import render, redirect, reverse
from utils import restful


class TagView(View):
    def post(self, request):
        # 新建提交
        if 'submit' in request.POST:
            form = TagForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                Tag.objects.create(name=name)
                return redirect(reverse("cms:tag_publish_view"))
            else:
                return restful.method_error("Form is error", form.get_errors())
        # 修改Tag
        elif 'modify' in request.POST:
            form = TagEditForm(request.POST)
            if form.is_valid():
                pk = form.cleaned_data.get('pk')
                name = form.cleaned_data.get('name')
                Tag.objects.filter(id=pk).update(name=name)
                return redirect(reverse("cms:tag_manage_view"))
            else:
                return restful.method_error("Form is error", form.get_errors())
        # 修改状态返回
        elif 'back':
            return redirect(reverse("cms:tag_manage_view"))
        # 新建状态的取消
        else:
            return redirect(reverse("cms:tag_publish_view"))


class TagEditView(View):
    def get(self,request):
        tag_id = request.GET.get('tag_id')
        tag = Tag.objects.get(pk=tag_id)
        context = {
            'item_data': tag,
        }
        return render(request, 'cms/tag/publish.html', context=context)


class TagDeleteView(View):
    def post(self,request):
        tag_id = request.POST.get('tag_id')
        Tag.objects.filter(id=tag_id).delete()
        return restful.ok()