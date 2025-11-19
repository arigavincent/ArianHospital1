from django.db import models


# Department model for 'Our Departments' section
class Department(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	head = models.CharField(max_length=200, blank=True)
	contact = models.CharField(max_length=50, blank=True)
	order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

	class Meta:
		ordering = ["order", "name"]

	def __str__(self):
		return self.name


# Doctor model for 'Our Doctors' section
class Doctor(models.Model):
	full_name = models.CharField(max_length=200)
	title = models.CharField(max_length=200, blank=True, help_text="Short role or specialty, e.g. 'Head of Emergency Care'")
	qualifications = models.CharField(max_length=200, blank=True, help_text="Qualifications, e.g. 'MBChB, MMed'")
	phone = models.CharField(max_length=50, blank=True)
	email = models.EmailField(blank=True)
	image = models.CharField(max_length=300, blank=True, help_text="Static path or URL to a headshot (optional)")
	order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

	class Meta:
		ordering = ["order", "full_name"]

	def __str__(self):
		return self.full_name


# ContactInfo model for site-wide contact details used in footers and contact pages
class ContactInfo(models.Model):
	site_name = models.CharField(max_length=200, blank=True, help_text="Optional site/hospital name")
	address = models.TextField(blank=True)
	phone = models.CharField(max_length=50, blank=True)
	email = models.EmailField(blank=True)
	opening_hours = models.CharField(max_length=200, blank=True, help_text="Human readable opening hours")
	extra = models.TextField(blank=True, help_text="Any extra contact or directions (HTML allowed)")
	order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

	class Meta:
		ordering = ["order"]
		verbose_name = "Contact Info"
		verbose_name_plural = "Contact Info"

	def __str__(self):
		return self.site_name or f"ContactInfo #{self.pk}"
