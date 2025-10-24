# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Child, Milestone, ChildMilestone, Notification

@receiver(post_save, sender=Child)
def create_child_milestones(sender, instance, created, **kwargs):
    if created:
        milestones = Milestone.objects.all()
        for milestone in milestones:
            ChildMilestone.objects.create(
                child=instance,
                milestone=milestone,
                status='pending'
            )
# signals.py





@receiver(post_save, sender=ChildMilestone)
def handle_milestone_notifications(sender, instance, **kwargs):
    child = instance.child
    parent_user = child.parent.profile.user
    daycare_user = child.daycare.profile.user
    message = f"The milestone '{instance.milestone.description}' for {child.child_name} is delayed."

    if instance.status == 'delayed':
        # Create notifications if they don't already exist
        Notification.objects.get_or_create(
            recipient=parent_user,
            title="Milestone Delayed",
            message=message
        )
        Notification.objects.get_or_create(
            recipient=daycare_user,
            title="Milestone Delayed",
            message=message
        )

    elif instance.status == 'completed':
        # Delete any existing "Milestone Delayed" notifications for this milestone
        Notification.objects.filter(
            title="Milestone Delayed",
            message=message,
            recipient__in=[parent_user, daycare_user]
        ).delete()

