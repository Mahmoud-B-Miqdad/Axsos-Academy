from django.db import models

class CourseManager(models.Manager):
    def validate_course(self, post_data):
        """Validates course name and description length requirements."""
        errors = {}
        name = post_data.get('name', '').strip()
        desc = post_data.get('description', '').strip()

        if len(name) <= 5:
            errors['name'] = "Course name must be more than 5 characters long."
        
        if len(desc) <= 15:
            errors['description'] = "Description must be more than 15 characters long."
            
        return errors

    def create_course_with_desc(self, post_data):
        """Creates a Course instance and its related Description (One-to-One)."""
        new_course = self.create(name=post_data.get('name'))
        Description.objects.create(
            content=post_data.get('description'),
            course=new_course
        )
        return new_course


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CourseManager()


class Description(models.Model):
    # Ninja Bonus: One-to-one relationship with Course
    content = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='desc_info')


class Comment(models.Model):
    # Ninja Bonus: Comments section for each course
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)