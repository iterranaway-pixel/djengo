from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate the database with sample published posts for testing'

    def handle(self, *args, **options):
        # Get or create a superuser for author
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('admin')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created superuser: admin'))
        else:
            self.stdout.write(self.style.WARNING('Superuser admin already exists'))

        # Create sample posts
        sample_posts = [
            {
                'title': 'Welcome to My Blog',
                'slug': 'welcome-to-my-blog',
                'body': 'This is my first blog post. I am excited to share my thoughts and ideas with you!',
                'status': Post.Status.PUBLISHED,
            },
            {
                'title': 'Django Tips and Tricks',
                'slug': 'django-tips-and-tricks',
                'body': 'In this post, I will share some useful Django tips and tricks that I have learned over time.',
                'status': Post.Status.PUBLISHED,
            },
            {
                'title': 'Building Web Apps with Python',
                'slug': 'building-web-apps-with-python',
                'body': 'Python is a great language for building web applications. Learn how to get started with Django.',
                'status': Post.Status.PUBLISHED,
            },
        ]

        for post_data in sample_posts:
            post, created = Post.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    'title': post_data['title'],
                    'body': post_data['body'],
                    'status': post_data['status'],
                    'author': user,
                    'publish': timezone.now(),
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created post: {post.title} (id={post.id})')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'✗ Post already exists: {post.title} (id={post.id})')
                )

        self.stdout.write(self.style.SUCCESS('\nDone! Visit http://127.0.0.1:8000/blog/ to see the posts.'))
