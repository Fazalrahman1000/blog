from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import JsonResponse
from .models import Post, Category, Tag, Comment, Like


def base_context():
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    }


# ── POSTS LIST ───────────────────────────────────────────────────
class PostsList(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.select_related('author', 'category') \
                           .prefetch_related('tag') \
                           .order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(base_context())
        return context


# ── CATEGORY FILTER ──────────────────────────────────────────────
class CategoryPosts(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category) \
                           .select_related('author', 'category') \
                           .prefetch_related('tag') \
                           .order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(base_context())
        context['active_category'] = self.kwargs['slug']
        return context


# ── TAG FILTER ───────────────────────────────────────────────────
class TagPosts(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tag=self.tag) \
                           .select_related('author', 'category') \
                           .prefetch_related('tag') \
                           .order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(base_context())
        context['active_tag'] = self.kwargs['slug']
        return context


# ── POST DETAIL ──────────────────────────────────────────────────
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(base_context())

        # Like info
        if self.request.user.is_authenticated:
            context['user_liked'] = self.object.likes.filter(
                user=self.request.user
            ).exists()
        else:
            context['user_liked'] = False
        context['like_count'] = self.object.likes.count()

        # Show "Last updated" only if the post was edited on a different day
        context['show_updated'] = (
            self.object.updated_at.strftime('%Y-%m-%d') !=
            self.object.created_at.strftime('%Y-%m-%d')
        )
        return context


# ── CREATE POST ──────────────────────────────────────────────────
@method_decorator(login_required, name='dispatch')
class CreatePost(View):

    def get(self, request):
        return render(request, 'blog/create_post.html', base_context())

    def post(self, request):
        title       = request.POST.get('title', '').strip()
        slug        = request.POST.get('slug', '').strip()
        content     = request.POST.get('content', '').strip()
        category_id = request.POST.get('category')
        tag_ids     = request.POST.getlist('tag')
        img         = request.FILES.get('featured_img')

        if not title or not slug or not content:
            messages.error(request, 'Title, slug and content are required.')
            return render(request, 'blog/create_post.html', base_context())

        category = None
        if category_id:
            category = get_object_or_404(Category, id=category_id)

        post = Post.objects.create(
            title=title,
            slug=slug,
            content=content,
            author=request.user,
            category=category,
            featured_img=img,
        )

        if tag_ids:
            post.tag.set(Tag.objects.filter(id__in=tag_ids))

        messages.success(request, 'Post published!')
        return redirect('post_detail', slug=post.slug)


# ── EDIT POST ────────────────────────────────────────────────────
@method_decorator(login_required, name='dispatch')
class EditPost(View):

    def get_post(self, slug, user):
        post = get_object_or_404(Post, slug=slug)
        if post.author != user and not user.is_staff:
            return None
        return post

    def get(self, request, slug):
        post = self.get_post(slug, request.user)
        if not post:
            messages.error(request, 'You are not allowed to edit this post.')
            return redirect('posts')
        context = base_context()
        context['post'] = post
        return render(request, 'blog/edit_post.html', context)

    def post(self, request, slug):
        post = self.get_post(slug, request.user)
        if not post:
            messages.error(request, 'You are not allowed to edit this post.')
            return redirect('posts')

        post.title   = request.POST.get('title', post.title).strip()
        post.slug    = request.POST.get('slug', post.slug).strip()
        post.content = request.POST.get('content', post.content).strip()

        category_id  = request.POST.get('category')
        post.category = get_object_or_404(Category, id=category_id) if category_id else None

        tag_ids = request.POST.getlist('tag')
        post.tag.set(Tag.objects.filter(id__in=tag_ids))

        if request.FILES.get('featured_img'):
            post.featured_img = request.FILES['featured_img']

        post.save()
        messages.success(request, 'Post updated!')
        return redirect('post_detail', slug=post.slug)


# ── DELETE POST ──────────────────────────────────────────────────
@method_decorator(login_required, name='dispatch')
class DeletePost(View):

    def get_post(self, slug, user):
        post = get_object_or_404(Post, slug=slug)
        if post.author != user and not user.is_staff:
            return None
        return post

    def get(self, request, slug):
        post = self.get_post(slug, request.user)
        if not post:
            messages.error(request, 'You are not allowed to delete this post.')
            return redirect('posts')
        context = base_context()
        context['post'] = post
        return render(request, 'blog/delete_post.html', context)

    def post(self, request, slug):
        post = self.get_post(slug, request.user)
        if not post:
            return redirect('posts')
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('posts')


# ── ADD COMMENT ──────────────────────────────────────────────────
@method_decorator(login_required, name='dispatch')
class AddComment(View):

    def post(self, request, slug):
        post    = get_object_or_404(Post, slug=slug)
        content = request.POST.get('content', '').strip()
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
        return redirect('post_detail', slug=slug)


# ── DELETE COMMENT ───────────────────────────────────────────────
@method_decorator(login_required, name='dispatch')
class DeleteComment(View):

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if request.user == comment.user or request.user.is_staff:
            post_slug = comment.post.slug
            comment.delete()
            return redirect('post_detail', slug=post_slug)
        return redirect('posts')


# ── LIKE POST ────────────────────────────────────────────────────
@method_decorator(login_required, name='dispatch')
class LikePost(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            like.delete()  # already liked → unlike

        return JsonResponse({
            'liked': created,
            'count': post.likes.count(),
        })