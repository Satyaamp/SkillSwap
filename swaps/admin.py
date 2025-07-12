from django.contrib import admin
from .models import SwapRequest, Feedback

@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'offered_skill', 'requested_skill', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['sender__username', 'receiver__username']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['swap', 'rating', 'comment']
