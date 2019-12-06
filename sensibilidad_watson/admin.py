from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Summary, Pillar, Category, SubCategory, CategoryResult, SubCategoryResult


# Register your models here.
@admin.register(Summary)
class AdminSummary(admin.ModelAdmin):
	pass


@admin.register(Pillar)
class AdminPillar(admin.ModelAdmin):
	pass


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ("name", "category", "trait_id")
	list_filter = ("category",)


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
	list_display = ("name", "category", "trait_id")
	list_filter = ("category",)


@admin.register(CategoryResult)
class AdminCategoryResult(admin.ModelAdmin):
	pass


@admin.register(SubCategoryResult)
class AdminSubCategoryResult(admin.ModelAdmin):
	pass
