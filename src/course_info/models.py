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
        return "/courses/year-{0}/{1}".format(self.study_year, self.slug)
    
    class Meta:
        ordering = ['study_year', 'term']


class CourseSection(models.Model):
    topic = models.CharField(max_length = 255, help_text="The name of a sub section of the course")
    description = models.TextField(help_text = "Description about this section of the course.")
    tips = models.TextField(blank=True, help_text="Any tips for this section.")   
    lecturers = models.ManyToManyField(Lecturer, help_text = "Who teaches the course.")
    course = models.ForeignKey(Course)
    slug = models.SlugField(unique= True, help_text="Prepopulated from topic name. Must be unique")
    
    def __unicode__(self):
        return "{0} - {1}".format(self.course.name, self.topic) 
    
    def get_absolute_url(self):
        return "{0}/{1}".format(self.course.get_absolute_url(), self.slug)
    
    class Meta:
        verbose_name = "Course Section"
        verbose_name_plural = "Course Sections"
 
class CourseFile(models.Model):
    PAST_PAPER = 1
    IMAGE = 2
    LECTURE = 3
    NOTES = 4
    ESSAY = 5
    
    COURSE_FILE = (
                   (PAST_PAPER, 'Past Paper'),
                   (IMAGE, 'Image'),
                   (LECTURE, 'Lecture'),
                   (NOTES, 'Notes'),
                   (ESSAY, 'Essay'),
                   )
    
    name = models.CharField(max_length = 255, help_text="Course File Name.")
    year = models.DateField(blank = True, help_text="Examination Year or year the file was created")
    file = models.FileField(upload_to = "/uploads/course_file/")
    created_by = models.CharField(max_length = 255, blank = True, help_text="Files author")
    course_section = models.ForeignKey(CourseSection, blank = True, help_text="Course section have to be be added and saved above to be available")
    course = models.ForeignKey(Course)
    type = models.IntegerField(choices=COURSE_FILE)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Course File"
        verbose_name_plural = "Course Files"