from django.db import models
from django.contrib.auth.models import User
import Image

# Create your models here.
DR = 0
PROF = 1
MR = 2
MISS = 3
MRS = 4
MS = 5

TITLES = (
          (DR, "Dr."),
          (PROF, "Prof."),
          (MR, "Mr"),
          (MISS, "Miss"),
          (MRS, "Mrs"),
          (MS, "Ms")
          )
    
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
    
    AGE = (
           (0, "20-30"),
           (1, "30-40"),
           (2, "40-50"),
           (3, "50-60"),
           (4, "60-70"),
           (5, "70+")
           )
    
    MALE = 0
    FEMALE = 1
    
    GENDER = (
              (MALE, "Male"),
              (FEMALE, "Female"),
              )
    
    title = models.IntegerField(choices = TITLES)
    gender = models.IntegerField(choices = GENDER)
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(choices = AGE, blank=True, null = True)
    teaching = models.IntegerField(choices=TEACHING_SCALE, help_text = "How good or bad the teaching was")
    description = models.TextField(blank=True)
    slug = models.SlugField(unique = True, help_text = "Prepopulated from name, must be unique")
    image = models.ImageField(upload_to="uploads/lecturer_images/", blank=True, help_text="Please upload square images of at least 175px x 175px otherwise they will just look bad")       
        
    def __unicode__(self):
        return "{0} {1} {2}".format(TITLES[self.title][1], self.first_name, self.surname)    
    
    def get_absolute_url(self):
        return "/lecturers/{0}/".format(self.slug)
    
    def save(self, *args, **kwargs):
        if self.image == "":
            if self.gender == self.MALE:
                self.image = "uploads/lecturer_images/male_silhouette.png"
            elif self.gender == self.FEMALE:
                self.image = "uploads/lecturer_images/female_silhouette.png"

        super(Lecturer, self).save()
    
    class Meta:
        ordering = ['surname']
        
FIRST_YEAR = 1
SECOND_YEAR = 2
THIRD_YEAR = 3
FOURTH_YEAR = 4
FIFTH_YEAR = 5
SIXTH_YEAR = 6

YEARS = (
         (FIRST_YEAR, '1st Year'),
         (SECOND_YEAR, '2nd Year'),
         (THIRD_YEAR, '3rd Year'),
         (FOURTH_YEAR, '4th Year'),
         (FIFTH_YEAR, '5th Year'),
         (SIXTH_YEAR, '6th Year')
         )
        
class Course(models.Model):
    
    BOTH = 1
    VET_SCHOOL = 2
    MED_SCHOOL = 3
        
    SCHOOLS = (
               (BOTH, 'Both'),
               (VET_SCHOOL, 'Vets Only Course'),
               (MED_SCHOOL, 'Medics Only Course')
               )    
        
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
    school = models.IntegerField(choices=SCHOOLS, help_text = "Select who takes this course")
    study_year = models.IntegerField(choices=YEARS, help_text = "The year the course is taken.")
    term = models.IntegerField(choices=TERMS, help_text="The term the course is taken.")
    difficulty = models.IntegerField(choices = DIFF_SCALE, help_text = "How difficult the course is.")
    slug = models.SlugField(unique=True, help_text = "Prepopulated from course name. Must be unique.")    
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/courses/year-{0}/{1}/".format(self.study_year, self.slug)
    
    def get_school_based_name(self):
        return "{0} ({1})".format(self.name, self.SCHOOLS[self.school - 1][1][0])
    
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
        return "{0}".format(self.topic) 
    
    def get_absolute_url(self):
        #seperating slash is not needed as its brought in from the course URL
        return "{0}{1}/".format(self.course.get_absolute_url(), self.slug)
    
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
    year = models.DateField(blank = True, null = True, help_text="Examination Year or year the file was created")
    file = models.FileField(upload_to = "uploads/course_file/")
    created_by = models.CharField(max_length = 255, blank = True, help_text="Files author")
    course_section = models.ForeignKey(CourseSection, blank = True, help_text="Course section have to be be added and saved above to be available")
    course = models.ForeignKey(Course)
    type = models.IntegerField(choices=COURSE_FILE)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Course File"
        verbose_name_plural = "Course Files"
        
class InfoSetting(models.Model):
    key = models.CharField(max_length = 255, help_text="DO NOT CHANGE THIS VALUE")
    value = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return "{0} settings".format("key")
    
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

## Write vet reps model     

VET_SCHOOL = 1
MED_SCHOOL = 2

SCHOOL_TYPES = (
           (VET_SCHOOL, "Vet School"),
           (MED_SCHOOL, "Med School"),       
           )

class ClassRep(models.Model):   
    name = models.CharField(max_length = 255)
    school = models.IntegerField(choices = SCHOOL_TYPES)
    email = models.EmailField()
    year = models.IntegerField(choices=YEARS)
    
    def __unicode__(self):
        return self.name

class CollegeContact(models.Model):
    title = models.IntegerField(choices = TITLES)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    position = models.CharField(max_length = 255, blank = True)
    email = models.EmailField()
    tel = models.IntegerField()
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()

class DontPanicSection(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()   
    position = models.IntegerField(blank = True) 
