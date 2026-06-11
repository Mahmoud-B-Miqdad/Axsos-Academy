from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validate_show(self, post_data, is_update=False, show_id=None):
        """
        Handles all core validations, ninja bonuses, and sensei bonuses.
        """
        errors = {}
        
        title = post_data.get('title', '').strip()
        network = post_data.get('network', '').strip()
        description = post_data.get('description', '').strip()
        release_date_str = post_data.get('release_date', '')

        # 1. Core validations (Character length)
        if len(title) < 2:
            errors['title'] = "Title should be at least 2 characters."
        
        if len(network) < 3:
            errors['network'] = "Network should be at least 3 characters."

        # 2. Ninja Bonus: Description is optional, but must be at least 10 chars if provided
        if description and len(description) < 10:
            errors['description'] = "Description should be at least 10 characters if provided."

        # 3. Ninja Bonus: Release Date must be in the past
        if not release_date_str:
            errors['release_date'] = "Release date is required."
        else:
            try:
                release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
                if release_date >= datetime.today().date():
                    errors['release_date'] = "Release Date must be in the past."
            except ValueError:
                errors['release_date'] = "Invalid date format."

        # 4. Sensei Bonus: Unique validation for Title
        if title:
            existing_shows = Show.objects.filter(title__iexact=title)
            if is_update and show_id:
                existing_shows = existing_shows.exclude(id=show_id)
            
            if existing_shows.exists():
                errors['unique_title'] = "A TV show with this title already exists in the database."

        return errors

    def create_show(self, post_data):
        """Fat Model method to handle data creation"""
        return self.create(
            title=post_data.get('title'),
            network=post_data.get('network'),
            release_date=post_data.get('release_date'),
            description=post_data.get('description')
        )

    def update_show(self, show_id, post_data):
        """Fat Model method to handle data updates"""
        show = Show.objects.get(id=show_id)
        show.title = post_data.get('title')
        show.network = post_data.get('network')
        show.release_date = post_data.get('release_date')
        show.description = post_data.get('description')
        show.save()
        return show


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()