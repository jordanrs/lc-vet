from django.db import models

# Create your models here.




class Lecturer(models.Model):
    VERY_BAD_TEACHING = 1
    BAD_TEACHING = 2
    AVERAGE_TEACHING = 3
    GOOD_TEACHING = 4
    VERY_GOOD_TEACHING = 5
    EXCELLENT_TEACHING = 6
    
    TEACHING_SCALE = (
              (VERY_BAD_TEACHING, 'Very Bad'),
              (BAD_TEACHING, 'Bad'),
              (AVERAGE_TEACHING, 'Average'),
              (GOOD_TEACHING, 'Good'),
              (VERY_GOOD_TEACHING, 'Very good'),
              (EXCELLENT_TEACHING, 'Excellent')
              )
    
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null = True)
    teaching = models.IntegerField(choices=TEACHING_SCALE, help_text = "How good or bad the teaching was")
    description = models.TextField(blank=True)
    slug = models.SlugField(unique = True, help_text = "Prepopulated from name, must be unique")
#    image = models.ImageField(upload_to="lecturer_images", blank=True)       
# needs pil installing 
        
    def __unicode__(self):
        return self.name    
    
    def get_absolute_url(self):
        return "/lecturer/{0}".format(self.name)
    
    class Meta:
        ordering = ['name']
        
        
class Course(models.Model):
    
    FIRST_TERM = 1
    SECOND_TERM = 2
    THIRD_TERM = 3
    ALL_YEAR = 4
    
    TERMS = (
         (ALL_YEAR,'All year'),
         (FIRST_TERM, '1st Term'),
         (SECOND_TERM, '2nd Term'),
         (THIRD_TERM, '3rd Term')         
         )

    FIRST_YEAR = 1
    SECOND_YEAR = 2
    THIRD_YEAR = 3
    FOURTH_YEAR = 4
    FIFTH_YEAR = 5
    YEARS = (
             (FIRST_YEAR, '1st Year'),
             (SECOND_YEAR, '2nd Year'),
             (THIRD_YEAR, '3rd Year'),
             (FOURTH_YEAR, '4th Year'),
             (FIFTH_YEAR, '5th Year'),
             )
    
    VERY_EASY = 1
    EASY = 2
    MEDIUM = 3
    HARD = 4
    VERY_HARD = 5
    EXTREME = 6
    
    DIFF_SCALE = (
                  (VERY_EASY, 'Very Easy'),
                  (EASY, 'Easy'),
                  (MEDIUM, 'Medium'),
                  (HARD, 'Hard'),
                  (VERY_HARD, 'Very Hard'),
                  (EXTREME, 'Extreme')
                  )

    name = models.CharField(max_length=255, help_text="The course name.")
    description = models.TextField(help_text="A overall description about the course.")
    study_year = models.IntegerField(choices=YEARS, help_text = "The year the course is taken.")
    term = models.IntegerField(choices=TERMS, help_text="The term the course is taken.")
    difficulty = models.IntegerField(choices = DIFF_SCALE, help_text = "How difficult the course is.")
    slug = models.SlugField(unique=True, help_text = "Prepopulated from course name. Must be unique.")
    
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/course/{0}".format(self.slug)
    
    class Meta:
        ordering = ['study_year', 'term']
        
class PastPaper(models.Model):
    name = models.CharField(max_length = 255, help_text="Past Paper Name.")
    year = models.DateField(blank = True, help_text="Examination Year.")
    file = models.FileField(upload_to = "/uploads/past-papers/")
    course = models.ForeignKey(Course)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Past Paper"
        verbose_name_plural = "Past Papers"
        
class CourseSection(models.Model):
    topic = models.CharField(max_length = 255)
    description = models.TextField(help_text = "Description about this section of the course.")
    tips = models.TextField(blank=True, help_text="Any tips for this section.")   
    lecturers = models.ManyToManyField(Lecturer, help_text = "Who teaches the course.")
    course = models.ForeignKey(Course)
    
    def __unicode__(self):
        return "{0} - {1}".format(self.course.name, self.topic) 
    
    class Meta:
        verbose_name = "Course Section"
        verbose_name_plural = "Course Sections"
        
class Note(models.Model):
    name = models.CharField(max_length = 255)
    created_by = models.CharField(max_length = 255)
    file = models.FileField(upload_to="/uploads/notes")
    course_section = models.ForeignKey(CourseSection)
    course = models.ForeignKey(Course)